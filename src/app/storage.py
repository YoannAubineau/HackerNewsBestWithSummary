import hashlib
import shutil
from collections.abc import Iterator
from datetime import date, datetime
from pathlib import Path

import frontmatter

from app.config import get_settings
from app.models import Article, Status


def short_hash(guid: str) -> str:
    return hashlib.sha256(guid.encode("utf-8")).hexdigest()[:8]


def _partition_path(articles_dir: Path, when: datetime) -> Path:
    return articles_dir / f"{when.year:04d}" / f"{when.month:02d}" / f"{when.day:02d}"


def path_for(guid: str, our_published_at: datetime, *, failed: bool = False) -> Path:
    settings = get_settings()
    base = settings.failed_dir if failed else settings.articles_dir
    return _partition_path(base, our_published_at) / f"{short_hash(guid)}.md"


def find_existing(guid: str) -> Path | None:
    """Return the on-disk path of an article matching ``guid`` if one exists.

    Searches the whole ``articles_dir`` tree (active + ``_failed``), because
    the partition is now based on ``our_published_at`` — which is the
    timestamp *we recorded the first time we saw the item*, not a value we
    can recompute from a fresh feed entry (hnrss's ``lastBuildDate`` drifts
    between polls). The filename is deterministic (``short_hash(guid)``),
    so a ``rglob`` unambiguously finds the file wherever it sits.
    """
    settings = get_settings()
    if not settings.articles_dir.exists():
        return None
    target = f"{short_hash(guid)}.md"
    for match in settings.articles_dir.rglob(target):
        return match
    return None


def sidecar_path(article_path: Path, kind: str) -> Path:
    """Path of a transient file (raw article text, raw discussion text).

    Suffix `.raw.{kind}.txt` — gitignored, never committed.
    """
    return article_path.with_suffix(f".raw.{kind}.txt")


def write_sidecar(article_path: Path, kind: str, content: str) -> Path:
    path = sidecar_path(article_path, kind)
    path.write_text(content, encoding="utf-8")
    return path


def read_sidecar(article_path: Path, kind: str) -> str | None:
    path = sidecar_path(article_path, kind)
    if not path.exists():
        return None
    return path.read_text(encoding="utf-8")


def clear_sidecars(article_path: Path) -> None:
    for sibling in article_path.parent.glob(f"{article_path.stem}.raw.*.txt"):
        sibling.unlink(missing_ok=True)


def save(article: Article, body: str = "") -> Path:
    path = path_for(article.guid, article.our_published_at)
    path.parent.mkdir(parents=True, exist_ok=True)
    post = frontmatter.Post(body, **_serialize_metadata(article))
    path.write_text(frontmatter.dumps(post) + "\n", encoding="utf-8")
    return path


def load(path: Path) -> tuple[Article, str]:
    post = frontmatter.loads(path.read_text(encoding="utf-8"))
    article = Article.model_validate(post.metadata)
    return article, post.content


def iter_by_status(status: Status) -> Iterator[tuple[Path, Article, str]]:
    settings = get_settings()
    if not settings.articles_dir.exists():
        return
    for path in sorted(settings.articles_dir.rglob("*.md")):
        if path.is_relative_to(settings.failed_dir):
            continue
        article, body = load(path)
        if article.status == status:
            yield path, article, body


def move_to_failed(path: Path, article: Article, body: str) -> Path:
    article.status = Status.FAILED
    dest = path_for(article.guid, article.our_published_at, failed=True)
    dest.parent.mkdir(parents=True, exist_ok=True)
    post = frontmatter.Post(body, **_serialize_metadata(article))
    dest.write_text(frontmatter.dumps(post) + "\n", encoding="utf-8")
    path.unlink(missing_ok=True)
    return dest


def dates_in_feed(entries_dates: list[datetime]) -> set[date]:
    return {d.date() for d in entries_dates}


def iter_summarized() -> Iterator[tuple[Path, Article, str]]:
    """Yield summarized articles in descending order of ``our_published_at``.

    Walks the YYYY/MM/DD partition newest-first and sorts within each day
    folder by ``our_published_at`` desc. Since the partition itself is keyed
    on ``our_published_at`` (the timestamp we recorded the first time we
    saw the item in our feed), no article in an earlier day can outrank an
    article in a later day — callers can break out of the loop as soon as
    they have enough items without scanning the rest of the repository.
    """
    settings = get_settings()
    root = settings.articles_dir
    if not root.exists():
        return
    for day_dir in _walk_day_dirs_desc(root):
        batch: list[tuple[Path, Article, str]] = []
        for path in day_dir.glob("*.md"):
            article, body = load(path)
            if article.status == Status.SUMMARIZED:
                batch.append((path, article, body))
        batch.sort(key=lambda t: t[1].our_published_at, reverse=True)
        yield from batch


def _walk_day_dirs_desc(root: Path) -> Iterator[Path]:
    """Yield every YYYY/MM/DD directory under ``root``, newest-first.

    Non-numeric children (such as ``_failed``) are skipped at every level,
    which also excludes the failed tree even when it lives beneath the
    articles directory.
    """
    for year in _numeric_subdirs_desc(root):
        for month in _numeric_subdirs_desc(year):
            yield from _numeric_subdirs_desc(month)


def _numeric_subdirs_desc(parent: Path) -> Iterator[Path]:
    subdirs = [d for d in parent.iterdir() if d.is_dir() and d.name.isdigit()]
    subdirs.sort(key=lambda d: d.name, reverse=True)
    yield from subdirs


def _serialize_metadata(article: Article) -> dict:
    data = article.model_dump(mode="json", exclude_none=False)
    return {k: v for k, v in data.items() if v is not None or k in {"error"}}


def ensure_articles_dir() -> None:
    settings = get_settings()
    settings.articles_dir.mkdir(parents=True, exist_ok=True)


def purge_tree(root: Path) -> None:
    if root.exists():
        shutil.rmtree(root)


def migrate_partitions() -> int:
    """Move every article file to the partition matching its ``our_published_at``.

    One-shot helper for the switch from ``source_published_at``-based
    partitioning to ``our_published_at``-based partitioning. Idempotent —
    files already in the right place are left alone, and a second run is
    a no-op. Sidecars (``<stem>.raw.*.txt``) travel with the ``.md`` they
    belong to. Source directories that become empty after the move are
    removed (up to the articles root).
    """
    settings = get_settings()
    if not settings.articles_dir.exists():
        return 0
    moved = 0
    source_dirs: set[Path] = set()
    for path in list(settings.articles_dir.rglob("*.md")):
        article, _body = load(path)
        failed = path.is_relative_to(settings.failed_dir)
        target = path_for(article.guid, article.our_published_at, failed=failed)
        if target == path:
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        sidecars = list(path.parent.glob(f"{path.stem}.raw.*.txt"))
        path.rename(target)
        for sidecar in sidecars:
            sidecar.rename(target.parent / sidecar.name)
        source_dirs.add(path.parent)
        moved += 1
    for directory in sorted(source_dirs, key=lambda d: len(d.parts), reverse=True):
        _prune_empty_dirs(directory, stop_at=settings.articles_dir)
    return moved


def _prune_empty_dirs(start: Path, *, stop_at: Path) -> None:
    current = start
    while current != stop_at and current.is_relative_to(stop_at):
        if not current.exists() or any(current.iterdir()):
            return
        current.rmdir()
        current = current.parent

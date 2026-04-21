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


def path_for(guid: str, source_published_at: datetime, *, failed: bool = False) -> Path:
    settings = get_settings()
    base = settings.failed_dir if failed else settings.articles_dir
    return _partition_path(base, source_published_at) / f"{short_hash(guid)}.md"


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
    path = path_for(article.guid, article.source_published_at)
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
    dest = path_for(article.guid, article.source_published_at, failed=True)
    dest.parent.mkdir(parents=True, exist_ok=True)
    post = frontmatter.Post(body, **_serialize_metadata(article))
    dest.write_text(frontmatter.dumps(post) + "\n", encoding="utf-8")
    path.unlink(missing_ok=True)
    return dest


def dates_in_feed(entries_dates: list[datetime]) -> set[date]:
    return {d.date() for d in entries_dates}


def iter_summarized() -> Iterator[tuple[Path, Article, str]]:
    yield from iter_by_status(Status.SUMMARIZED)


def _serialize_metadata(article: Article) -> dict:
    data = article.model_dump(mode="json", exclude_none=False)
    return {k: v for k, v in data.items() if v is not None or k in {"error"}}


def ensure_articles_dir() -> None:
    settings = get_settings()
    settings.articles_dir.mkdir(parents=True, exist_ok=True)


def purge_tree(root: Path) -> None:
    if root.exists():
        shutil.rmtree(root)

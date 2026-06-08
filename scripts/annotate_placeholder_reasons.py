"""Backfill the failure reason onto already-summarized "(unable to load
content)" placeholders, so historical entries match what the live pipeline
now records (``content_failure_reason`` + an annotated body line).

This is the read-mostly cousin of ``scripts/regen_article_summaries.py``:
that script spends LLM tokens to turn a placeholder into a real article
summary when ``fetch_article`` can now extract the page; this one spends no
tokens and only annotates the *intrinsic* obstacle of pages that still cannot
be loaded.

To surface that intrinsic obstacle rather than let a fallback mask it, the
Wayback and reader stages are disabled here (the direct + Webshare proxy path
is kept, mirroring the live first attempt). For each entry whose body is still
the bare ``(unable to load content)``:

- if the direct fetch still fails, its ``failure_reason`` (e.g. "access
  denied" for a paywall/anti-bot 403, "extraction failed", "connection
  failed") is written into both the frontmatter and the body line;
- if the direct fetch now SUCCEEDS, the placeholder is stale (a since-fixed
  extractor recovers it): it is left untouched and reported as a candidate for
  ``scripts/regen_article_summaries.py`` / ``app reprocess-placeholders``,
  rather than given a fabricated reason.

Already-annotated entries are skipped, so the script is idempotent.

Run from the repository root (so ``articles/`` resolves):

    uv run python scripts/annotate_placeholder_reasons.py            # annotate
    DRY_RUN=1 uv run python scripts/annotate_placeholder_reasons.py  # report only

No ``OPENROUTER_API_KEY`` is needed (no LLM call). ``WEBSHARE_PROXY_*`` from
``.env`` are used for the proxy retry when present, exactly as in CI.
"""

import os

# Force the page's own obstacle to surface: a recovered Wayback snapshot or a
# reader render would otherwise hide why the original load failed.
os.environ["WAYBACK_ENABLED"] = "false"
os.environ["READER_ENABLED"] = "false"

import re  # noqa: E402

from app.fetch_article import fetch_article  # noqa: E402
from app.storage import iter_summarized, save  # noqa: E402

DRY_RUN = os.environ.get("DRY_RUN") == "1"

# Only the bare placeholder; an already-annotated body carries its reason.
BARE_RE = re.compile(r"(## Résumé de l'article\s*\n+)\(unable to load content\)")


def main() -> None:
    targets = [
        (path, article, body)
        for path, article, body in list(iter_summarized())
        if BARE_RE.search(body)
    ]
    print(f"bare placeholders found: {len(targets)} (DRY_RUN={DRY_RUN})\n")

    annotated = loads_fine = errors = 0
    for _path, article, body in targets:
        try:
            content = fetch_article(article.url)
        except Exception as exc:  # noqa: BLE001
            errors += 1
            print(f"  ERROR  {article.url[:70]}  {type(exc).__name__}: {exc}")
            continue

        if (content.text or "").strip():
            loads_fine += 1
            print(f"  skip   loads-now [{content.source.value}]  {article.url[:60]}")
            continue

        reason = content.failure_reason or "connection failed"
        annotated += 1
        if DRY_RUN:
            print(f"  CAND   [{reason}]  {article.url[:62]}")
            continue
        article.content_failure_reason = reason
        new_body = BARE_RE.sub(rf"\1(unable to load content: {reason})", body, count=1)
        save(article, new_body)
        print(f"  OK     [{reason}]  {article.url[:62]}")

    label = "would annotate" if DRY_RUN else "annotated"
    print(
        f"\n{label}={annotated}  loads-now={loads_fine}  errors={errors}  "
        f"total={len(targets)}"
    )


if __name__ == "__main__":
    main()

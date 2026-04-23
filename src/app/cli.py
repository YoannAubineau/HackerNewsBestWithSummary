import json
import os
from pathlib import Path

import structlog
import typer

from app.logging_setup import setup_logging
from app.pipeline import (
    CycleResult,
    backfill_images,
    run_cycle,
    step_fetch_articles,
    step_fetch_discussions,
    step_fetch_feed,
    step_publish,
    step_summarize,
)
from app.usage import generate_chart, record_usage

log = structlog.get_logger()

app = typer.Typer(
    add_completion=False,
    help="HN Best → LLM summaries → enriched RSS feed",
)


@app.callback()
def _main() -> None:
    setup_logging()


@app.command()
def cycle() -> None:
    """Run the full pipeline: fetch → summarize → publish."""
    result = run_cycle()
    _emit_failures(result)


def _emit_failures(result: CycleResult) -> None:
    count = len(result.failures)
    if count:
        log.warning("cycle_article_failures", count=count, failures=result.failures)
    github_output = os.environ.get("GITHUB_OUTPUT")
    if not github_output:
        return
    failures_data = [{"guid": guid, "error": error} for guid, error in result.failures]
    # json.dumps with these separators is guaranteed single-line, so a plain
    # key=value entry in $GITHUB_OUTPUT is safe (no heredoc needed).
    payload = json.dumps(failures_data, separators=(",", ":"))
    with Path(github_output).open("a", encoding="utf-8") as handle:
        handle.write(f"failures_count={count}\n")
        handle.write(f"failures_json={payload}\n")


@app.command("fetch-feed")
def fetch_feed_cmd() -> None:
    """Step 1: fetch the source feed and create pending article files."""
    step_fetch_feed()


@app.command("fetch-articles")
def fetch_articles_cmd() -> None:
    """Step 2: download and extract article content."""
    step_fetch_articles()


@app.command("fetch-discussions")
def fetch_discussions_cmd() -> None:
    """Step 3: fetch HN comments via the Algolia API."""
    step_fetch_discussions()


@app.command()
def summarize() -> None:
    """Step 4: generate title rewrite, article summary, and discussion synthesis via LLM."""
    step_summarize()


@app.command()
def publish() -> None:
    """Step 5: generate the feed XML."""
    step_publish()


@app.command("backfill-images")
def backfill_images_cmd() -> None:
    """Fill missing image_url on past summarized articles (no LLM calls)."""
    backfill_images()


@app.command("update-usage")
def update_usage_cmd() -> None:
    """Record today's OpenRouter spend and regenerate the 30-day bar chart."""
    record_usage()
    generate_chart()

import typer

from app.logging_setup import setup_logging
from app.pipeline import (
    backfill_images,
    run_cycle,
    step_fetch_articles,
    step_fetch_discussions,
    step_fetch_feed,
    step_publish,
    step_summarize,
)

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
    run_cycle()


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
    """Step 5: generate feed.xml."""
    step_publish()


@app.command("backfill-images")
def backfill_images_cmd() -> None:
    """Fill missing image_url on past summarized articles (no LLM calls)."""
    backfill_images()

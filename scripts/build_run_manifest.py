"""
Build a run manifest for a Value Vacation Finder search run.

Section 12 of references/project_full_instructions.md requires every real
manual search run to eventually have a manifest recording which files were
involved, their hashes, and the environment the run was produced in.

This script does not call any connectors and does not calculate scores.
It only inventories files that already exist on disk for a given
search_run_id and records file metadata (path, exists, size_bytes, sha256)
plus environment metadata (python_version, conda_environment, git_branch,
git_commit, run_timestamp).

Usage:
    python scripts\\build_run_manifest.py --run-id run_20260625_lisbon_20261005_20261016
"""

from __future__ import annotations

import argparse
import hashlib
import platform
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml


PROJECT_ROOT = Path(__file__).resolve().parents[1]

DEFAULT_RUN_ID = "run_20260625_lisbon_20261005_20261016"

RAW_SOURCES = ["travel_advisory", "skyscanner", "expedia", "tripadvisor", "viator"]


def sha256_of_file(path: Path) -> str | None:
    """Return the sha256 hex digest of a file, or None if it doesn't exist."""
    if not path.exists() or not path.is_file():
        return None

    digest = hashlib.sha256()
    with path.open("rb") as file:
        for chunk in iter(lambda: file.read(65536), b""):
            digest.update(chunk)

    return digest.hexdigest()


def file_record(path: Path) -> dict[str, Any]:
    """Build a file_record_fields entry (path, exists, size_bytes, sha256)."""
    exists = path.exists() and path.is_file()

    return {
        "path": str(path.relative_to(PROJECT_ROOT)).replace("\\", "/"),
        "exists": exists,
        "size_bytes": path.stat().st_size if exists else None,
        "sha256": sha256_of_file(path) if exists else None,
    }


def run_git_command(args: list[str]) -> str | None:
    """Run a git command from the project root and return stripped stdout, or None on failure."""
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=PROJECT_ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None


def collect_environment_metadata() -> dict[str, Any]:
    """Collect environment_metadata fields."""
    import os

    return {
        "python_version": platform.python_version(),
        "conda_environment": os.environ.get("CONDA_DEFAULT_ENV"),
        "git_branch": run_git_command(["rev-parse", "--abbrev-ref", "HEAD"]),
        "git_commit": run_git_command(["rev-parse", "HEAD"]),
        "run_timestamp": datetime.now(timezone.utc).isoformat(),
    }


def collect_raw_inputs(run_id: str, destination_slug: str) -> dict[str, Any]:
    """Collect file_records for each raw connector capture folder."""
    raw_inputs = {}

    for source in RAW_SOURCES:
        candidate_path = (
            PROJECT_ROOT
            / "data"
            / "raw"
            / source
            / f"{run_id}_{source}_{destination_slug}.md"
        )
        raw_inputs[source] = file_record(candidate_path)

    return raw_inputs


def collect_transformed_inputs(destination_slug: str) -> dict[str, Any]:
    """Collect file_records for manual/interim candidate files."""
    manual_candidates_dir = PROJECT_ROOT / "data" / "interim" / "manual_candidates"

    records = []
    if manual_candidates_dir.exists():
        for path in sorted(manual_candidates_dir.glob(f"{destination_slug}_candidate*.yaml")):
            records.append(file_record(path))

    return {
        "manual_candidates": records,
        "sample_candidate": file_record(
            PROJECT_ROOT
            / "references"
            / "sample_candidates"
            / "sample_lisbon_candidate.yaml"
        ),
    }


def collect_processed_outputs() -> dict[str, Any]:
    """Collect file_records for processed candidate CSV outputs."""
    return {
        "sample_processed_csv": file_record(
            PROJECT_ROOT
            / "references"
            / "sample_processed"
            / "vacation_candidates_sample.csv"
        ),
        "real_processed_csv": file_record(
            PROJECT_ROOT
            / "data"
            / "processed"
            / "vacation_candidates"
            / "vacation_candidates.csv"
        ),
    }


def collect_scoring_outputs() -> dict[str, Any]:
    """Collect file_records for scoring configuration."""
    return {
        "scoring_weights_config": file_record(
            PROJECT_ROOT / "config" / "scoring_weights.yaml"
        ),
    }


def build_manifest(run_id: str, destination_slug: str) -> dict[str, Any]:
    """Build the full run manifest dict, following manifest_required_sections."""
    search_run_config_path = PROJECT_ROOT / "config" / "search_runs" / f"{run_id}.yaml"

    return {
        "run_id": run_id,
        "run_date": datetime.now(timezone.utc).date().isoformat(),
        "run_mode": "sample",
        "workflow": "value_vacation_finder_mvp",
        "environment": collect_environment_metadata(),
        "connector_capture": {
            "search_run_config": file_record(search_run_config_path),
        },
        "raw_inputs": collect_raw_inputs(run_id, destination_slug),
        "transformed_inputs": collect_transformed_inputs(destination_slug),
        "processed_outputs": collect_processed_outputs(),
        "scoring_outputs": collect_scoring_outputs(),
        "benchmark_outputs": {
            "fair_value_estimate_usd": None,
            "benchmark_method": "not_yet_built",
        },
        "reports": {
            "final_shortlist_report": None,
        },
        "parameters": {
            "destination_slug": destination_slug,
        },
        "known_limitations": [
            "Benchmark/fair-value logic is not implemented.",
            "Canadian travel advisory integration is not implemented.",
            "Passport/visa rules are not implemented.",
            "Viator activity source validation is unavailable for this run.",
        ],
    }


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Build a run manifest for a Value Vacation Finder search run."
    )

    parser.add_argument(
        "--run-id",
        type=str,
        default=DEFAULT_RUN_ID,
        help="search_run_id to build a manifest for.",
    )

    parser.add_argument(
        "--destination-slug",
        type=str,
        default="lisbon",
        help="Destination slug used in raw connector file names.",
    )

    return parser.parse_args()


def main() -> None:
    """Build and write a run manifest."""
    args = parse_args()

    manifest = build_manifest(args.run_id, args.destination_slug)

    output_dir = PROJECT_ROOT / "data" / "run_manifests"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / f"{args.run_id}_manifest.yaml"

    with output_path.open("w", encoding="utf-8") as file:
        yaml.safe_dump(manifest, file, sort_keys=False)

    print(f"Wrote run manifest: {output_path}")


if __name__ == "__main__":
    main()

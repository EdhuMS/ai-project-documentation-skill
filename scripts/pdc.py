#!/usr/bin/env python3
"""AI Project Documentation Skill — local project bootstrap and state validator."""
import argparse
import json
from pathlib import Path
import re
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]
PROFILES = {"light", "professional", "critical"}
STATUSES = {"planned", "in_progress", "blocked", "completed", "archived", "unknown"}


def validate(path):
    errors = []
    try:
        state = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        return [f"Cannot read valid JSON: {exc}"]
    if not isinstance(state, dict):
        return ["Root must be an object"]
    if state.get("schema_version") != "1.0":
        errors.append("schema_version must be 1.0")
    project_id = state.get("project_id")
    if not isinstance(project_id, str) or re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]{1,79}", project_id) is None:
        errors.append("project_id must contain 2-80 safe characters")
    if state.get("profile") not in PROFILES:
        errors.append("invalid profile")
    if state.get("status") not in STATUSES:
        errors.append("invalid status")
    storage = state.get("canonical_storage")
    if (not isinstance(storage, dict)
            or not isinstance(storage.get("provider"), str)
            or not storage.get("provider", "").strip()
            or not isinstance(storage.get("path"), str)
            or not storage.get("path", "").strip()):
        errors.append("canonical_storage requires provider and path")
    for name in ("evidence", "test_results", "blockers"):
        if not isinstance(state.get(name), list):
            errors.append(f"{name} must be an array")
    if not isinstance(state.get("next_action"), str) or not state.get("next_action", "").strip():
        errors.append("next_action must be nonempty")
    if state.get("verification_status") not in {"verified", "reported", "inferred", "unknown"}:
        errors.append("invalid verification_status")
    return errors


def init_project(project_dir, project_id):
    if re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]{1,79}", project_id) is None:
        raise ValueError("project ID must have 2-80 safe characters")
    output = Path(project_dir).resolve() / "docs" / "continuity"
    if output.exists() and any(output.iterdir()):
        raise FileExistsError(f"Refusing to overwrite existing documents: {output}")
    output.mkdir(parents=True, exist_ok=True)
    state = json.loads((ROOT / "templates" / "PROJECT-STATE.json").read_text(encoding="utf-8"))
    state["project_id"] = project_id
    (output / "PROJECT-STATE.json").write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
    shutil.copy2(ROOT / "templates" / "HANDOFF.md", output / "HANDOFF.md")
    (output / "README.md").write_text(
        f"# Documentation continuity — {project_id}\n\nCanonical local documentation. Verify primary sources before updating.\n",
        encoding="utf-8",
    )
    return output


def main(argv=None):
    parser = argparse.ArgumentParser(description="Local documentation tools")
    commands = parser.add_subparsers(dest="action", required=True)
    init = commands.add_parser("init", help="create local light-profile docs without overwrite")
    init.add_argument("project_dir")
    init.add_argument("--project-id", required=True)
    check = commands.add_parser("validate", help="check structured PROJECT-STATE.json")
    check.add_argument("state_file")
    args = parser.parse_args(argv)
    try:
        if args.action == "init":
            print(f"Created: {init_project(args.project_dir, args.project_id)}")
        else:
            errors = validate(args.state_file)
            if errors:
                print("\n".join(f"ERROR: {error}" for error in errors), file=sys.stderr)
                return 1
            print("VALID: project state v1.0")
        return 0
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

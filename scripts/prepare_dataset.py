"""Convert a simple source JSONL into Ada-MSS repair task JSONL format.

Input row example:
{"id":"x","buggy_code":"...","tests":"..."}
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True, help="source jsonl path")
    ap.add_argument("--output", required=True, help="target repair_tasks jsonl path")
    args = ap.parse_args()

    src = Path(args.input)
    dst = Path(args.output)
    dst.parent.mkdir(parents=True, exist_ok=True)

    lines_out: list[str] = []
    for i, line in enumerate(src.read_text(encoding="utf-8").splitlines()):
        if not line.strip():
            continue
        item = json.loads(line)
        task_id = item.get("task_id") or item.get("id") or f"task_{i}"
        out = {
            "task_id": task_id,
            "buggy_code": item["buggy_code"],
            "tests": item["tests"],
        }
        lines_out.append(json.dumps(out, ensure_ascii=False))

    dst.write_text("\n".join(lines_out) + "\n", encoding="utf-8")
    print(f"converted {len(lines_out)} tasks -> {dst}")


if __name__ == "__main__":
    main()

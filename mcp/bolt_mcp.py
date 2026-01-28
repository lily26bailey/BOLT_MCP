from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path

from fastmcp import FastMCP

mcp = FastMCP("bolt_mcp")

REPO_ROOT = Path(__file__).resolve().parents[1]


def _run(cmd: list[str], cwd: Path = REPO_ROOT) -> str:
    p = subprocess.run(cmd, cwd=str(cwd), capture_output=True, text=True)
    out = (p.stdout or "") + ("\n" + p.stderr if p.stderr else "")
    if p.returncode != 0:
        raise RuntimeError(f"Command failed: {' '.join(cmd)}\n{out}")
    return out.strip()


@mcp.tool()
def repo_quickstart() -> str:
    return "\n".join([
        "Therapist inference (sample):",
        "  python therapist_behavior_inference.py --method multi_label_w_def_and_ex "
        "--input_path sample_dataset/sample_therapist_input.jsonl "
        "--output_path sample_dataset/sample_therapist_output.jsonl",
        "",
        "Client inference (sample):",
        "  python client_behavior_inference.py --method multi_label_w_def_and_ex "
        "--input_path sample_dataset/sample_client_input.jsonl "
        "--output_path sample_dataset/sample_client_output.jsonl",
    ])


@mcp.tool()
def reproduce_intro_figure(output_path: str = "mcp/reproduced_intro_figure.png") -> str:
    src = REPO_ROOT / "Intro-Figure.png"
    if not src.exists():
        raise FileNotFoundError("Intro-Figure.png not found in repo root.")
    dst = REPO_ROOT / output_path
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dst)
    return f"Saved: {dst}"


@mcp.tool()
def run_therapist_inference(
    method: str = "multi_label_w_def_and_ex",
    input_path: str = "sample_dataset/sample_therapist_input.jsonl",
    output_path: str = "sample_dataset/sample_therapist_output.jsonl",
) -> str:
    cmd = [
        "python", "therapist_behavior_inference.py",
        "--method", method,
        "--input_path", input_path,
        "--output_path", output_path,
    ]
    return _run(cmd)


@mcp.tool()
def run_client_inference(
    method: str = "multi_label_w_def_and_ex",
    input_path: str = "sample_dataset/sample_client_input.jsonl",
    output_path: str = "sample_dataset/sample_client_output.jsonl",
) -> str:
    cmd = [
        "python", "client_behavior_inference.py",
        "--method", method,
        "--input_path", input_path,
        "--output_path", output_path,
    ]
    return _run(cmd)


@mcp.tool()
def make_behavior_histogram(
    jsonl_path: str,
    field: str,
    output_path: str = "mcp/behavior_hist.png",
    top_k: int = 15,
) -> str:
    import pandas as pd
    import matplotlib.pyplot as plt

    p = REPO_ROOT / jsonl_path
    if not p.exists():
        raise FileNotFoundError(f"Missing file: {p}")

    counts = {}
    with p.open("r", encoding="utf-8") as f:
        for line in f:
            obj = json.loads(line)
            labels = obj.get(field, [])
            if isinstance(labels, str):
                labels = [labels]
            for lab in labels:
                counts[lab] = counts.get(lab, 0) + 1

    if not counts:
        raise ValueError(f"No labels found for field '{field}' in {jsonl_path}")

    s = pd.Series(counts).sort_values(ascending=False).head(top_k)

    out = REPO_ROOT / output_path
    out.parent.mkdir(parents=True, exist_ok=True)

    plt.figure()
    s.sort_values().plot(kind="barh")
    plt.xlabel("Count")
    plt.title(f"Top {len(s)} labels in {field}")
    plt.tight_layout()
    plt.savefig(out, dpi=200)
    plt.close()

    return f"Saved: {out}"


if __name__ == "__main__":
    mcp.run()

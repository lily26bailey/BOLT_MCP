# BOLT PaperAgent MCP Server

This repository provides a **Model Context Protocol (MCP) server** for the paper:

> **A Computational Framework for Behavioral Assessment of LLM Therapists**  
> https://arxiv.org/pdf/2401.00820

It is designed to be used as a “PaperAgent” via an MCP-compatible client, **Gemini CLI**.

---

## What’s in this repo?

- `mcp/bolt_mcp.py`: MCP server exposing PaperAgent tools
- `mcp/requirements.txt`: Python deps for the MCP server
- `README.md`: setup + usage instructions

---

## Prerequisites

- macOS / Linux
- Python **>= 3.10**
- `git`
- Node.js **>= 18** (for Gemini CLI)

Check versions:

```bash
python3 --version
node -v
npm -v


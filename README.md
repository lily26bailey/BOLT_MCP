# BOLT PaperAgent MCP Server

This repository provides a **Model Context Protocol (MCP) server** for the paper:

> **A Computational Framework for Behavioral Assessment of LLM Therapists**  
> https://arxiv.org/pdf/2401.00820

The MCP server exposes tools for:
- Reproducing figures from the paper
- Running therapist and client behavior inference
- Analyzing behavioral distributions

It is implemented using **FastMCP** and is designed to be used with the **Gemini CLI** as a PaperAgent.

---

## Setup

### 1. Create and activate a Python environment (Python ≥ 3.10)
```bash
python3.11 -m venv .venv
source .venv/bin/activate



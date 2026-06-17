#!/usr/bin/env python3
"""
notes_server.py  --  your first MCP server (Demo 3).

A small, practical MCP server that gives a local model something it cannot do on
its own: a private, persistent notes and knowledge base. Run it behind Ollama and
Open WebUI and the model can save notes during a chat and search them later, all
offline and on your machine.
"""
import datetime
import json
import pathlib
import sys

from mcp.server.fastmcp import FastMCP

# Notes are stored as one JSON object per line in a local file.
DB = pathlib.Path(__file__).with_name("notes_db.jsonl")

mcp = FastMCP("my-notes")


def _load() -> list[dict]:
    if not DB.exists():
        return []
    out = []
    for line in DB.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line:
            out.append(json.loads(line))
    return out


@mcp.tool()
def save_note(text: str, tags: list[str] | None = None) -> str:
    """Save a note with optional tags."""
    if tags is None:
        tags = []
    note = {
        "text": text,
        "tags": [t.strip() for t in tags if t.strip()],
        "saved_at": datetime.datetime.now().isoformat(timespec="seconds"),
    }
    with DB.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(note) + "\n")
    print(f"[notes] saved note ({len(note['text'])} chars)", file=sys.stderr, flush=True)
    return f"Saved. You now have {len(_load())} notes."


@mcp.tool()
def search_notes(query: str = "") -> str:
    """Search your saved notes for a word or phrase and return the matches."""
    if not query.strip():
        return "Please provide a word or phrase to search for."
    q = query.lower()
    hits = [n for n in _load() if q in n["text"].lower() or any(q in t.lower() for t in n["tags"])]
    if not hits:
        return f"No notes match '{query}'."
    lines = [f"- {n['text']}  (saved {n['saved_at']})" for n in hits]
    return f"Found {len(hits)} note(s) matching '{query}':\n" + "\n".join(lines)


@mcp.tool()
def list_notes() -> str:
    """List every saved note."""
    notes = _load()
    if not notes:
        return "You have no notes yet. Use save_note to save one."
    return f"You have {len(notes)} note(s):\n" + "\n".join(f"- {n['text']}" for n in notes)


if __name__ == "__main__":
    print(f"[notes] starting my-notes MCP server; db={DB}", file=sys.stderr, flush=True)
    mcp.run()

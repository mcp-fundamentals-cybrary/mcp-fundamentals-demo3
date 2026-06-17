# Demo 3: Build and Run Your First MCP Server

Run a small notes server (an MCP server written in Python) and connect it to
Open WebUI, so a local model can save notes during a chat and find them later.
You do not edit the server. Two short scripts handle setup and launching.

## What is in here

- `notes_server.py` -- the MCP server. Three tools: save a note, search notes, list notes. Stores notes in a plain text file (`notes_db.jsonl`).
- `setup.sh` -- run once. Builds a local Python environment and installs what the demo needs.
- `start_demo3.sh` -- run each time you want the demo. Starts the server so Open WebUI can reach it.

## What you need first

- Python 3 installed (check with `python3 --version`).
- Open WebUI with a local model already running (for example through Ollama).
- A couple of gigabytes of free disk space for the install.

## Step 1: One-time setup

From the project folder, run:

```
bash setup.sh
```

This creates a `.venv` folder (an isolated Python environment) and installs two things: the MCP Python SDK, which runs the server, and mcpo, the small bridge that lets Open WebUI talk to the server. You only do this once. Do not use `sudo`.

## Step 2: Start the demo

```
bash start_demo3.sh
```

This starts the server on `http://localhost:8000` and leaves it running. Keep this terminal open while you use the demo. Press `Ctrl-C` to stop it when you are done. To use a different port, pass it as an argument: `bash start_demo3.sh 9000`.

## Step 3: Connect it in Open WebUI

1. In Open WebUI, open **Settings**, then **Tools**.
2. Add a new connection of type **OpenAPI**.
3. Set the URL to `http://localhost:8000`.

To see the three tools laid out as a live reference, open `http://localhost:8000/docs` in your browser.

## Step 4: Try it

In a chat with your local model, ask it to save a note, for example:

> Save a note: the project review is Friday at 2pm. Tag it project and meeting.

Then, in a brand new chat, ask it to find that note:

> Search my notes for the project review.

The note comes back, because it lives in the small server you are running, not in the model. That is the whole point of the demo: the server gave the model an ability it did not have on its own.

## Troubleshooting

- **`bash: setup.sh: No such file or directory`** -- you are not in the project folder. `cd` into it first.
- **`start_demo3.sh` says the environment is not set up** -- run `bash setup.sh` first.
- **Out of disk space during setup** -- the install needs room to unpack; free up space and rerun.
- **Open WebUI cannot connect** -- make sure the `start_demo3.sh` terminal is still running, and that the URL is exactly `http://localhost:8000` (or the port you chose).
- **Do not run the scripts with `sudo`** -- the demo runs as your normal user.

## License

Released under the MIT License. See `LICENSE`.

## Disclaimer

These lab files are provided for educational use as part of the MCP Fundamentals course. They are offered as-is, without warranty of any kind. The scripts create a local Python environment, install third-party packages from the internet, and run a local web service on your machine. Review the scripts before running them, and run them only in an environment you are comfortable using for learning. You are responsible for how you use these materials. Cybrary and the course author are not responsible for any damage, data loss, or other consequences arising from their use.

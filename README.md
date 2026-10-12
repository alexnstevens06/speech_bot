# speech_bot

A terminal choose-your-own-adventure chat. `basic_CYOA.py` uses the xAI SDK to stream a reply, then waits for one key (0 to quit, or 1, 2, or 3) and writes a transcript.

The other Python files are short examples: listing model names, a one-shot chat, a streaming chat, and reading keys with `readchar`. Settings come from a local `config.json`, which is gitignored.

## Tech

- Python
- `xai-sdk` for chat and streaming
- `readchar` for single-key input

## Setup

```sh
python3 -m venv .venv
. .venv/bin/activate
pip install xai-sdk readchar
```

Create `config.json` in the directory you run from. `access_config.py` reads these keys:

```json
{
  "model": "<model name>",
  "api_key_environment_name": "<name of the env var that holds your API key>",
  "system_prompt": "...",
  "transcript_path": "transcripts",
  "temp_file_write": "...",
  "base_AI_persona": "...",
  "base_user_persona": "...",
  "base_scenario_prompt": "..."
}
```

Then export your xAI API key under the variable named in `api_key_environment_name`. `list_model_names.py` reads `GROK_API_KEY` directly.

## Running

```sh
python basic_CYOA.py
```

The script asks for your persona, the AI's persona, and the scenario; leave any of them empty to use the defaults from `config.json`. Press `y` to start (or `0` to quit), then `1`, `2`, or `3` to pick an option and `0` to stop. Each run writes a timestamped transcript into `transcript_path`, which must already exist.

## CI

There are no tests, so CI byte-compiles every Python file as a syntax smoke check.

## License

MIT, see `LICENSE`.

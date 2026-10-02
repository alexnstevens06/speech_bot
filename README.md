# speech_bot

A terminal choose-your-own-adventure chat. `basic_CYOA.py` uses the xAI SDK to stream a reply, then waits for one key (0 to quit, or 1, 2, or 3) and writes a transcript.

The other Python files are short examples: listing model names, a one-shot chat, a streaming chat, and reading keys with `readchar`. Settings come from a local `config.json`, which is gitignored.

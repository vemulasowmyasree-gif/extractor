import json
from pathlib import Path

CONFIG_PATH = Path(__file__).resolve().parent / "config.json"

try:
    with CONFIG_PATH.open(encoding="utf-8") as config_file:
        config = json.load(config_file)
except FileNotFoundError as exc:
    raise RuntimeError(
        "Missing config.json. Copy config.example.json to config.json "
        "and set OPENAI_API_KEY."
    ) from exc
except json.JSONDecodeError as exc:
    raise RuntimeError("config.json must contain valid JSON.") from exc

OPENAI_API_KEY = config.get("OPENAI_API_KEY") if isinstance(config, dict) else None
if not isinstance(OPENAI_API_KEY, str) or not OPENAI_API_KEY.strip():
    raise RuntimeError("Set a non-empty OPENAI_API_KEY string in config.json.")

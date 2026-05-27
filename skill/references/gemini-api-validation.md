# Gemini API Key Validation

Quick check to see if a `GOOGLE_API_KEY` is valid before relying on it.

## REST API Test (no Hermes dependency)

```python
import urllib.request, json, os

# Read key from .env
env_path = os.path.expanduser("~/.hermes/.env")
api_key = None
with open(env_path) as f:
    for line in f:
        line = line.strip()
        if line.startswith("GOOGLE_API_KEY="):
            api_key = line.split("=", 1)[1]
            break

url = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}"
req = urllib.request.Request(url)
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        data = json.loads(resp.read())
        models = [m["name"].split("/")[-1] for m in data.get("models", [])]
        gemini = [m for m in models if "gemini" in m.lower()]
        print(f"✅ Valid — {len(gemini)} Gemini models")
except urllib.error.HTTPError as e:
    print(f"❌ HTTP {e.code}: {e.read().decode()[:200]}")
```

## Key Types

| Source | Requires | Behavior |
|--------|----------|----------|
| AI Studio (aistudio.google.com) | Just create key | Works immediately |
| GCP (console.cloud.google.com) | Billing + Generative Language API enabled | `API_KEY_INVALID` if not set up |

## Validation Codes

- `200` → Valid. Returns JSON model list.
- `400` → Invalid request (malformed URL).
- `403` → Key invalid or API not enabled.
- `429` → Rate limited.

## Date Validated

2026-05-27 — Key currently valid, 31 Gemini models available including gemini-2.5-pro.

import json
import os
import sys
import urllib.request
import uuid
from pathlib import Path

URL = "https://api.openai.com/v1/audio/transcriptions"
MAX_BYTES = 25 * 1024 * 1024


def vocab_prompt():
    brand = Path("brand.json")
    if not brand.exists():
        return ""
    words = json.loads(brand.read_text(encoding="utf-8")).get("vocab", [])
    return ", ".join(words)


def multipart(fields, file_field, file_path):
    boundary = uuid.uuid4().hex
    body = bytearray()
    for name, value in fields:
        body += f'--{boundary}\r\nContent-Disposition: form-data; name="{name}"\r\n\r\n{value}\r\n'.encode()
    body += f'--{boundary}\r\nContent-Disposition: form-data; name="{file_field}"; filename="{file_path.name}"\r\nContent-Type: audio/wav\r\n\r\n'.encode()
    body += file_path.read_bytes() + b"\r\n"
    body += f"--{boundary}--\r\n".encode()
    return bytes(body), boundary


def main():
    key = os.environ.get("OPENAI_API_KEY")
    if not key:
        sys.exit("Falta OPENAI_API_KEY en el entorno. No se lee de ningún archivo.")
    audio = Path(sys.argv[1])
    out = Path(sys.argv[2])
    lang = sys.argv[3] if len(sys.argv) > 3 else "es"
    if audio.stat().st_size > MAX_BYTES:
        sys.exit(f"{audio.name} pesa más de 25 MB. Divídelo antes de enviarlo.")
    fields = [("model", "whisper-1"), ("language", lang), ("response_format", "verbose_json"), ("timestamp_granularities[]", "word"), ("timestamp_granularities[]", "segment")]
    prompt = vocab_prompt()
    if prompt:
        fields.append(("prompt", prompt))
    body, boundary = multipart(fields, "file", audio)
    request = urllib.request.Request(URL, data=body, headers={"Authorization": f"Bearer {key}", "Content-Type": f"multipart/form-data; boundary={boundary}"})
    with urllib.request.urlopen(request, timeout=600) as response:
        data = json.loads(response.read().decode("utf-8"))
    words = [{"w": w["word"].strip(), "s": round(w["start"], 3), "e": round(w["end"], 3)} for w in data.get("words", [])]
    out.write_text(json.dumps(words, ensure_ascii=False, indent=1), encoding="utf-8")
    segments = [{"s": round(s["start"], 2), "e": round(s["end"], 2), "text": s["text"].strip()} for s in data.get("segments", [])]
    out.with_suffix(".segments.json").write_text(json.dumps(segments, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{len(words)} palabras, {len(segments)} frases -> {out}")


main()

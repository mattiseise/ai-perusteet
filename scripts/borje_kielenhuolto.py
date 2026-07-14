#!/usr/bin/env python3
"""
Börje — kielenhuoltoagentti (GPT-5.4 via OpenRouter)

Käsittelee markdown-tiedostoja ja korjaa suomen kielen, rakenteen
ja pedagogisen selkeyden GPT-5.4:llä. Ei muuta asiasisältöä.

Käyttö:
  python3 borje_kielenhuolto.py <tiedosto_tai_kansio> [--course-id ID] [--lesson-id ID] [--dry-run]
  python3 borje_kielenhuolto.py student/lesson-19/self-study.md
  python3 borje_kielenhuolto.py student/lesson-19/        # kaikki .md-tiedostot kansiossa
  python3 borje_kielenhuolto.py --course-id ai-perusteet-1ov --lesson-id lesson-19  # pipeline-mode

Ympäristömuuttuja:
  OPENROUTER_API_KEY  (luetaan myös ~/.openclaw/.env)

Riippuvuudet:
  pip install httpx
"""

from __future__ import annotations

import argparse
import asyncio
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

try:
    import httpx
except ImportError:
    print("ERROR: httpx ei ole asennettu. Asenna: pip install httpx", file=sys.stderr)
    sys.exit(1)

# ── Config ──────────────────────────────────────────────────────────────────

MODEL = "openai/gpt-5.4"
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
MAX_TOKENS = 16384
TEMPERATURE = 0.1          # konservatiivinen — kielenhuolto, ei luovuus
TIMEOUT = 180              # sekuntia per API-kutsu
CONCURRENCY = 6            # rinnakkaisten API-kutsujen max-määrä

WORKSPACE = Path(__file__).resolve().parents[1]  # .openclaw/workspace
LOG_DIR = WORKSPACE / "logs"

SYSTEM_PROMPT = """\
Olet suomenkielinen kielenhuoltaja ja pedagoginen editori.
Tehtäväsi on parantaa markdown-muotoista opetusmateriaalia.

KIELENHUOLTO
- Korjaa kielioppi, yhdyssanat, välimerkit ja sanavalinnat
- Tee tekstistä sujuvaa ja luonnollista suomea
- Älä muuta asiasisältöä

RAKENNE JA PEDAGOGIIKKA (rajoitettu)
- Voit selkeyttää otsikoita (mutta säilytä niiden merkitys)
- Voit jakaa liian pitkiä kappaleita
- Voit muuttaa listoja selkeämmiksi
- Voit lisätä lyhyitä väliotsikoita, jos ne parantavat luettavuutta
- Voit selkeyttää ohjeita vaiheittaisiksi

MARKDOWN-SÄÄNNÖT
- Säilytä kaikki markdown-rakenteet: otsikkotasot (#, ##, ###), koodilohkot, listat, linkit
- Älä muuta koodilohkojen sisältöä — ne ovat koskemattomia
- Säilytä YAML-frontmatter sellaisenaan
- Älä poista tai lisää markdown-elementtejä (kuvia, linkkejä, taulukoita) ellei se ole välttämätöntä selkeyden vuoksi

TURVAEHTO
- Jos et ole varma muutoksesta, jätä alkuperäinen teksti ennalleen
- Mieluummin liian vähän muutoksia kuin liikaa

ÄLÄ TEE NÄITÄ
- Älä lisää uusia asioita tai sisältöä
- Älä keksi esimerkkejä
- Älä poista olennaista sisältöä
- Älä muuta tehtävän tavoitetta tai vaatimuksia
- Älä muuta koodia koodilohkojen sisällä

Palauta VAIN korjattu markdown-teksti. Ei selityksiä, ei kommentteja, \
ei "tässä korjattu versio" -alustuksia. Pelkkä korjattu teksti."""


# ── API helpers ─────────────────────────────────────────────────────────────

def load_api_key() -> str:
    """Load OpenRouter API key from env or .env file."""
    key = os.environ.get("OPENROUTER_API_KEY")
    if key:
        return key

    env_path = Path.home() / ".openclaw" / ".env"
    if env_path.exists():
        for line in env_path.read_text(encoding="utf-8").splitlines():
            if line.startswith("OPENROUTER_API_KEY="):
                return line.split("=", 1)[1].strip()

    print("ERROR: OPENROUTER_API_KEY not found in environment or ~/.openclaw/.env", file=sys.stderr)
    sys.exit(1)


def build_user_prompt(content: str) -> str:
    """Wrap markdown content in clear delimiters for the LLM."""
    return f"--- BEGIN MARKDOWN ---\n{content}\n--- END MARKDOWN ---"


def strip_markdown_fence(text: str) -> str:
    """Remove markdown code fences if GPT wraps the output."""
    text = text.strip()
    if text.startswith("```markdown"):
        text = text[len("```markdown"):].strip()
    elif text.startswith("```md"):
        text = text[len("```md"):].strip()
    elif text.startswith("```"):
        text = text[3:].strip()
    if text.endswith("```"):
        text = text[:-3].strip()
    return text


async def call_gpt54(
    content: str,
    api_key: str,
    client: httpx.AsyncClient,
    semaphore: asyncio.Semaphore,
) -> tuple[str, dict]:
    """Send content to GPT-5.4 via OpenRouter. Returns (corrected_text, usage_dict)."""
    payload = {
        "model": MODEL,
        "temperature": TEMPERATURE,
        "max_tokens": MAX_TOKENS,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": build_user_prompt(content)},
        ],
    }

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json; charset=utf-8",
        "HTTP-Referer": "https://openclaw.fi",
        "X-Title": "Borje kielenhuolto",
    }

    # Encode JSON body explicitly as UTF-8 to handle Finnish characters
    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")

    async with semaphore:
        for attempt in range(3):
            try:
                resp = await client.post(
                    OPENROUTER_URL,
                    content=body,
                    headers=headers,
                    timeout=TIMEOUT,
                )
                resp.raise_for_status()
                data = resp.json()
                text = data["choices"][0]["message"]["content"]
                usage = data.get("usage", {})
                return strip_markdown_fence(text), usage
            except Exception as e:
                if attempt < 2:
                    wait = 3 * (attempt + 1)
                    print(f"  ⚠ Yritys {attempt + 1}/3 epäonnistui: {e}. Odotetaan {wait}s...", file=sys.stderr)
                    await asyncio.sleep(wait)
                else:
                    raise


# ── JSONL logging ──────────────────────────────────────────────────────────

def append_log(entry: dict):
    """Append a result entry to JSONL log."""
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    log_path = LOG_DIR / "borje_run_log.jsonl"
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


# ── File processing ─────────────────────────────────────────────────────────

async def process_file(
    filepath: Path,
    api_key: str,
    client: httpx.AsyncClient,
    semaphore: asyncio.Semaphore,
    output_dir: Path | None = None,
    dry_run: bool = False,
) -> dict:
    """Process a single markdown file. Returns result dict."""
    print(f"📄 {filepath.name}", end="", flush=True)

    original = filepath.read_text(encoding="utf-8")

    if len(original.strip()) < 50:
        print(" — ohitettu (liian lyhyt)")
        return {"file": str(filepath), "status": "skipped", "reason": "too_short"}

    t0 = time.monotonic()
    corrected, usage = await call_gpt54(original, api_key, client, semaphore)
    elapsed = time.monotonic() - t0

    # Count approximate changes (simple diff)
    orig_lines = original.splitlines()
    corr_lines = corrected.splitlines()
    changed_lines = sum(1 for a, b in zip(orig_lines, corr_lines) if a != b)
    changed_lines += abs(len(orig_lines) - len(corr_lines))

    # Determine output path
    if output_dir:
        out_path = output_dir / filepath.name
    else:
        out_path = filepath  # in-place

    if not dry_run:
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(corrected, encoding="utf-8")
        status_mark = "✓"
    else:
        status_mark = "🔍 (dry-run)"

    print(f" — {changed_lines} muutettua riviä, {elapsed:.1f}s {status_mark}")

    result = {
        "file": str(filepath),
        "output": str(out_path),
        "status": "corrected",
        "changed_lines": changed_lines,
        "elapsed_s": round(elapsed, 1),
        "tokens": usage,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }

    # Log to JSONL
    append_log(result)

    return result


def collect_files(target: Path) -> list[Path]:
    """Collect .md files from path (single file or directory)."""
    if target.is_file() and target.suffix == ".md":
        return [target]
    elif target.is_dir():
        files = sorted(target.glob("**/*.md"))
        return [f for f in files if not f.name.startswith(".")]
    else:
        print(f"ERROR: {target} ei ole .md-tiedosto eikä kansio", file=sys.stderr)
        sys.exit(1)


# ── Pipeline event output ───────────────────────────────────────────────────

def write_event(course_id: str, lesson_id: str, results: list[dict], total_tokens: dict):
    """Write pipeline event JSON."""
    event_dir = WORKSPACE / "events" / "borje" / course_id
    event_dir.mkdir(parents=True, exist_ok=True)

    event = {
        "schema_version": "1.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "agent": "borje",
        "model": MODEL,
        "status": "pass",
        "course_id": course_id,
        "lesson_id": lesson_id,
        "files_checked": [r["file"] for r in results],
        "fixes_applied": sum(r.get("changed_lines", 0) for r in results),
        "tokens_used": total_tokens,
        "fix_examples": [],  # TODO: voisi kerätä diffejä
        "results": results,
    }

    event_path = event_dir / f"{lesson_id}.json"
    event_path.write_text(json.dumps(event, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\n📋 Event kirjoitettu: {event_path}")


# ── Main ───────────────────────────────────────────────────────────────────

async def run(args: argparse.Namespace):
    """Async main runner."""
    # Resolve files
    if args.course_id and args.lesson_id and not args.target:
        # Pipeline mode: use standard paths
        targets = []
        base = WORKSPACE.parent.parent / "workspace" / "ai-perusteet"
        content_file = base / "content" / "lessons" / f"{args.lesson_id}.md"
        student_dir = base / "student" / args.lesson_id
        teacher_dir = base / "teacher" / args.lesson_id

        for t in [content_file]:
            if t.exists():
                targets.append(t)
        for d in [student_dir, teacher_dir]:
            if d.exists():
                targets.extend(sorted(d.glob("*.md")))

        if not targets:
            print(f"Ei löytynyt tiedostoja lesson_id:lle {args.lesson_id}", file=sys.stderr)
            sys.exit(1)
        files = targets
    elif args.target:
        files = collect_files(Path(args.target))
    else:
        print("Anna tiedosto/kansio tai --course-id + --lesson-id", file=sys.stderr)
        sys.exit(1)

    api_key = load_api_key()

    # Output directory (optional)
    output_dir = Path(args.output_dir) if args.output_dir else None
    if output_dir:
        output_dir.mkdir(parents=True, exist_ok=True)

    print(f"\n🔧 Börje kielenhuolto — {MODEL}")
    print(f"   Tiedostoja: {len(files)}")
    print(f"   Rinnakkaisuus: {CONCURRENCY}")
    if args.dry_run:
        print("   ⚠ DRY-RUN: muutoksia ei kirjoiteta")
    if output_dir:
        print(f"   Output: {output_dir}")
    print()

    semaphore = asyncio.Semaphore(CONCURRENCY)

    async with httpx.AsyncClient() as client:
        tasks = [
            process_file(f, api_key, client, semaphore, output_dir, args.dry_run)
            for f in files
        ]
        results = await asyncio.gather(*tasks, return_exceptions=True)

    # Handle exceptions
    clean_results = []
    for i, r in enumerate(results):
        if isinstance(r, Exception):
            print(f"  ✗ {files[i].name}: {r}", file=sys.stderr)
            clean_results.append({
                "file": str(files[i]),
                "status": "error",
                "error": str(r),
            })
        else:
            clean_results.append(r)

    # Summary
    corrected = sum(1 for r in clean_results if r.get("status") == "corrected")
    skipped = sum(1 for r in clean_results if r.get("status") == "skipped")
    errors = sum(1 for r in clean_results if r.get("status") == "error")
    total_changes = sum(r.get("changed_lines", 0) for r in clean_results)

    total_tokens = {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0}
    for r in clean_results:
        if "tokens" in r and isinstance(r["tokens"], dict):
            for k in total_tokens:
                total_tokens[k] += r["tokens"].get(k, 0)

    print(f"\n{'='*50}")
    print(f"Börje valmis: {corrected} korjattu, {skipped} ohitettu, {errors} virhe(ttä)")
    print(f"Muutettuja rivejä yhteensä: {total_changes}")
    print(f"Tokeneita käytetty: {total_tokens.get('total_tokens', '?')}")

    # Write pipeline event if course/lesson IDs given
    if args.course_id and args.lesson_id:
        write_event(args.course_id, args.lesson_id, clean_results, total_tokens)


def main():
    parser = argparse.ArgumentParser(
        description="Börje — kielenhuoltoagentti (GPT-5.4 via OpenRouter)"
    )
    parser.add_argument(
        "target",
        nargs="?",
        help="Tiedosto tai kansio käsiteltäväksi (.md)",
    )
    parser.add_argument("--course-id", help="Kurssin ID (pipeline-tilaan)")
    parser.add_argument("--lesson-id", help="Oppitunnin ID (pipeline-tilaan)")
    parser.add_argument("--output-dir", help="Erillinen tuloskansio (oletus: ylikirjoita in-place)")
    parser.add_argument("--dry-run", action="store_true", help="Älä kirjoita muutoksia")
    args = parser.parse_args()

    asyncio.run(run(args))


if __name__ == "__main__":
    main()

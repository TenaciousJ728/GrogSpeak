from flask import Flask, request, Response
import requests
import time

app = Flask(__name__)

XAI_KEY = "xai-xxXXxXXxXxXxXxXxxXXxXXxxxxxxXxXXXXXXXXxXXXxXXXxxxXXxXXXxxXxXXXXXXxXxxXxxxXXxXXxx"   # ← Your real API key here

# ============ OPTIONAL SETTINGS =============
EMBELLISH_TTS = True # Set to True to have Grok process your ST chat for more lively, expressive TTS
INTENSITY = "heavy" # "light", "medium", "heavy"
DEBUG_EMBELISHMENT = True # ← Set to True to see the exact processed ST chat being sent to TTS
# ============================================

VOICE_MAP = {
    # These rely on Available Voices set to "Eve,Ara,Rex,Sal,Leo" in SillyTavern TTS extension settings
    "eve": "eve",
    "ara": "ara",
    "rex": "rex",
    "sal": "sal",
    "leo": "leo",
    # Fallbacks in case someone still uses old OpenAI-compatible defaults: "alloy,echo,fable,onyx,nova,shimmer,coral,ash,sage,sky"
    "alloy": "eve",
    "fable": "ara",
    "echo": "rex",
    "nova": "sal",
    "onyx": "leo"
}

def smart_embellish(full_text: str) -> str:
    if not EMBELLISH_TTS or not full_text.strip():
        # print("🔄 Embellishment skipped")
        return full_text

    # Intensity-based instructions
    if INTENSITY == "light":
        intensity_desc = "Use very few tags. Keep it subtle and natural."
    elif INTENSITY == "medium":
        intensity_desc = "Use a moderate amount of tags where they naturally improve delivery."
    else:  # heavy
        intensity_desc = "Use tags more freely to make the speech expressive and emotional."

    print(f"🤖 Requesting embellished text from Grok ({INTENSITY} intensity)...")

    system_prompt = f"""You are an expert TTS expression director for xAI voices.

You can use two types of tags for dramatic effect and to make speech sound more alive and emotional:

**Inline tags** (place them where the sound should happen):
[pause], [long-pause], [laugh], [chuckle], [giggle], [cry], [sigh], [breath], [inhale], [exhale], [tsk], [tongue-click], [lip-smack], [hum-tune]

**Wrapping tags** (wrap words or phrases):
<soft>, <whisper>, <loud>, <emphasis>, <slow>, <fast>, <higher-pitch>, <lower-pitch>, 
<build-intensity>, <decrease-intensity>, <sing-song>, <singing>, <laugh-speak>

Rules:
- Use tags sparingly and only when they feel natural for the emotion and context.
- Match the character's personality and the tone of the line.
- Prioritize tags for quotes. Make quotes audibly distinguishable from narration.
- Do not overuse tags — too many will sound robotic or exaggerated.
- Intensity level: {INTENSITY} — {intensity_desc}

Return ONLY the text with the appropriate tags inserted. 
Do not add any explanations, notes, or extra text."""


    start_time = time.time()
    try:
        resp = requests.post(
            "https://api.x.ai/v1/chat/completions",
            headers={"Authorization": f"Bearer {XAI_KEY}", "Content-Type": "application/json"},
            json={
                "model": "grok-4-1-fast-non-reasoning",
                "temperature": 0.3,
                "max_tokens": 1000,
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"Add expression tags to this line for TTS:\n\n{full_text}"}
                ]
            },
            timeout=10
        )

        if resp.status_code == 200:
            enriched = resp.json()["choices"][0]["message"]["content"].strip()
            print(f"✅ Got embellished text in {time.time() - start_time:.2f}s ({len(enriched)} chars)")

            if DEBUG_EMBELISHMENT:
                print(f"-" * 60 + "\nℹ️ Text for TTS:")
                print(enriched)
                print(f"-" * 60)

            return enriched
        else:
            print(f"❌ Embellishment failed: {resp.status_code}")
    except Exception as e:
        print(f"❌ Embellishment error: {e}")

    # print("⚠️ Using original text for TTS")
    return full_text


@app.route("/v1/audio/speech", methods=["POST"])
@app.route("/v1", methods=["POST"])
def tts():
    data = request.get_json()
    original_text = data.get("input") or data.get("text", "")

    print(f"\n\nNew TTS Request ({len(original_text)} chars)")

    # Step 1: Embellish
    processed_text = smart_embellish(original_text)

    # Step 2: Send to TTS
    voice = data.get("voice", "eve").lower()
    xai_voice = VOICE_MAP.get(voice, "eve")

    print(f"🤖 Requesting xAI TTS (Voice: {xai_voice})...")

    start_time = time.time()
    payload = {
        "text": processed_text,
        "voice_id": xai_voice,
        "language": "en"
    }

    r = requests.post("https://api.x.ai/v1/tts",
                      json=payload,
                      headers={"Authorization": f"Bearer {XAI_KEY}", "Content-Type": "application/json"})

    elapsed = time.time() - start_time

    if r.status_code != 200:
        print(f"❌ xAI TTS Error ({r.status_code}): {r.text}")
        return "Error", 500

    print(f"✅ Received {len(r.content)/1024:.1f}KB stream in {elapsed:.2f}s")

    return Response(r.content, mimetype="audio/mpeg")


if __name__ == "__main__":
    print("=" * 60 + "\n" + " " * 21 + "🍺 GrogSpeak 🔊\n" + " " * 14 + "Grok TTS Proxy for SillyTavern\n" + "=" * 60)
    print("ver 2026.04.11\n")
    print(f"SETTINGS:\n✨ EMBELLISH_TTS = {EMBELLISH_TTS}\n💢 INTENSITY = {INTENSITY}\nℹ️ DEBUG_EMBELISHMENT = {DEBUG_EMBELISHMENT}\n")
    app.run(host="127.0.0.1", port=18790, debug=False)

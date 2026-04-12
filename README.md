# GrogSpeak
Grok TTS for SillyTavern, but with extra grog 🍺

<img width="835" height="525" alt="Screenshot 2026-04-11 220739" src="https://github.com/user-attachments/assets/19426757-8347-49df-a438-336bc5861441" />

## What is GrogSpeak?
A local-only proxy server run alongside SillyTavern, enabling it to use [xAI/Grok](https://docs.x.ai/developers/model-capabilities/audio/voice) for TTS. It takes ST's OpenAI-compatible calls and translates them for use with Grok's API, fetching audible dictation of your ST chat with some gusto and emotion.

No mods necessary! Just some dependencies. And then you just set, launch, and go.


## Setup
This will assume you're setting up for a Windows machine, but should also work for Linux with some minor adaptation.

### 1. Get xAI authorization
<!-- <img width="932" height="274" alt="Screenshot 2026-03-27 100148" src="https://github.com/user-attachments/assets/a754bb83-99b4-4790-958f-3143829006a3" /> -->

- Go to the [xAI API Console](https://console.x.ai/) and get logged in. Sign up if you haven't already.
- Proceed to create a new API key. Take note of the newly generated key for later. It looks something like `xai-xxXXxXXxXxXxXxXxxXXxXXxxxxxxXxXXXXXXXXxXXXxXXXxxxXXxXXXxxXxXXXXXXxXxxXxxxXXxXXxx`.
- Ensure you have a credits balance.

> [!WARNING]
> If your credit balance is empty, purchase some credits. Otherwise, you will not be able to use the API at all.
>
> You can only purchase a minimum of $5 in credits, but it'll be WAYYYYYYYY more than enough to test. Grok's API costs are **dirt-cheap**!

### 2. Setup python
- Access your PC/server in which you're running SillyTavern.
- You more than likely already have python installed. But if not, fetch the latest standalone installer [here](https://www.python.org/downloads/) and install it.
- Open the Terminal/Command Prompt and run this line: `pip install flask requests`

### 3. Fetch, edit, run GrogSpeak
- [Download GrogSpeak](https://github.com/TenaciousJ728/GrogSpeak/archive/refs/heads/main.zip). Extract `grogspeak.py` and `Start GrogSpeak.bat`, and place them somewhere memorable.
- Open `grogspeak.py.py` in a text editor like Notepad. Find "XAI_KEY" in line 7 and paste your Grok API key within the quotation marks. Save, and close.
- Open `Start GrogSpeak.bat` to run GrogSpeak. You should see the following output, meaning GrogSpeak is ready:
```
============================================================
                     🍺 GrogSpeak 🔊
              Grok TTS Proxy for SillyTavern
============================================================
ver 2026.04.11

SETTINGS:
✨ EMBELLISH_TTS = True
💢 INTENSITY = heavy
ℹ️ DEBUG_EMBELISHMENT = True

 * Serving Flask app 'grogSpeak'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:18790
Press CTRL+C to quit
```
...but we're not done yet!
### 4. Configure SillyTavern
<img width="400" height="759" alt="Screenshot_20260412-085224" src="https://github.com/user-attachments/assets/e13692c6-7136-49b7-be4d-db341498f2bd" />

- Access your SillyTavern server through your browser.
- Click on the Extensions icon (the three cubes), and then expand the "TTS" extension.
- Configure the TTS options as depicted in the screenshot. The outlined options are required.
- Click the "Reload" button to reveal some settings that may be hidden.

### 5. Test!
In the same TTS options menu, you can test by clicking the "Available voices" button. If you hear a voice, you're done! 🎉 Now you can tweak the other TTS options to taste.

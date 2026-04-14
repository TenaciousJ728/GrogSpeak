# GrogSpeak
xAI (Grok) TTS for SillyTavern, but with extra grog 🍺

<img width="835" height="509" alt="Screenshot 2026-04-13 190824" src="https://github.com/user-attachments/assets/4c790b20-ed40-4789-8a85-033b2d266b0f" />

A proxy that runs alongside your [SillyTavern](https://sillytavern.app/) instance, enabling its TTS feature to use [xAI (Grok)](https://docs.x.ai/developers/model-capabilities/audio/voice) proper.

No SillyTavern mods necessary! Just some dependencies.

## ✨ Features
- xAI TTS chat dictation by its full cast of voices: Eve, Ara, Rex, Sal, Leo
- Smart Embellishment - Use Grok to make TTS more naturally expressive
- Lightweight and quick to launch
- Fully local proxy - Your chat data and API key remains secure
- Supports Docker SillyTavern instances


## 🛠️ Quick Setup

### 1. Get xAI Access
<!-- <img width="932" height="274" alt="Screenshot 2026-03-27 100148" src="https://github.com/user-attachments/assets/a754bb83-99b4-4790-958f-3143829006a3" /> -->

- Log into [xAI API Console](https://console.x.ai/)
- Generate a new API key
- Ensure you have a credits balance

### 2. Install Dependencies
- Install python
    - **Windows:** Go [here](https://www.python.org/downloads/) and get the standalone installer. Enable `Add python.exe to PATH` and proceed to install.
- Install Flask
    - **Windows:** Run `pip install flask requests`
    - **Debian-based Linux:** `pip install flask` or `sudo apt install python3-flask -y`

### 3. Download & Configure
- [Download the repo](https://github.com/TenaciousJ728/GrogSpeak/archive/refs/heads/main.zip) and extract it
- Edit `GrogSpeak.py` and paste your API key on the `XAI_KEY` line
- Tweak [`OPTIONAL SETTINGS`](#%EF%B8%8F-settings) to taste
 
### 4. Run GrogSpeak
- **Windows:** Open `StartGrogSpeak.bat` or run `python GrogSpeak.py` in the same dir
- **Linux:** Run `python3 GrogSpeak.py` in the same dir

### 5. Configure in SillyTavern
Open `TTS` extension and set...

- **Select TTS Provider** → `OpenAI Compatible`
- [x] **Enabled**
- [x] **Pass Asterisks to TTS Engine**
- **Provider Endpoint** → `http://127.0.0.1:18790/v1`
    - **Docker users**: `http://host.docker.internal:18790/v1` 
- **Available Voices** → `Eve,Ara,Rex,Sal,Leo`
Then click the **Reload** button.

### 6. Test!
Click **Available Voices** to go testing!


## ⚙️ Settings

- `EMBELLISH_TTS` → `True` | `False`
Whether or not to include [inline and wrapping tags](https://docs.x.ai/developers/model-capabilities/audio/text-to-speech#inline-tags) to make TTS more expressive. Grok will perform the embellishment before it is sent to the TTS model.

- `INTENSITY` → `light` | `medium` | `heavy`
The amount of tags to insert at embellishment.

- `DEBUG_EMBELISHMENT` → `True` | `False`
Whether or not to print the embellished text in the GrogSpeak console.


## 📝 Notes
- For long messages, consider enabling **Narrate by paragraphs** in the TTS extension


## ⚖️ Legal

GrogSpeak is made by TenaciousJ728
- [MIT License](https://github.com/TenaciousJ728/GrogSpeak/blob/main/LICENSE)
- An unoffical tool for SillyTavern
- Runs independently of SillyTavern
- TenaciousJ728 is in no way affiliated with SillyTavern, xAI, nor 𝕏.

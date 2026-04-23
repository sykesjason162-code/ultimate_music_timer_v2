
# ComfyUI-Ultimate-Music-Timer

A precision timing and text-sanitization node for **ACE-Step Audio 1.5** and other AI music generation workflows in ComfyUI.

## 🌟 Overview
Setting the correct duration for AI music generation is often a "trial and error" nightmare. If the duration is too short, the AI cuts off the lyrics; if it's too long, the AI begins to hallucinate or repeat lines. 

The **Ultimate Music Timer** solves this by calculating the perfect duration based on **Lyric Density** (characters per second) and automatically fixing common punctuation bugs that cause the AI to skip words.

## ✨ Key Features
- **Genre-Based Multipliers:** Automatically switches between paces (e.g., Soul at 13.0 chars/sec, Rap at 22.0 chars/sec).
- **The "Comma-Fix":** Automatically converts commas to `--` internally to prevent ACE-Step 1.5 from skipping text after a pause.
- **Auto-Character Count:** No more external "Text Stats" nodes; it handles the string math internally.
- **Dual Buffers:** Independent sliders for `Intro` and `Outro` padding to allow for instrumental swells and fades.
- **User Guide Output:** Built-in instructions and session stats visible directly in the UI.

## 🛠️ Installation

1. Navigate to your ComfyUI custom nodes directory:
   ```bash
   cd ComfyUI/custom_nodes/
   ```
2. Create a new folder named `ComfyUI-Ultimate-Music-Timer`.
3. Save the `ultimate_music_timer_v2.py` file into that folder.
4. Restart ComfyUI.

## 🚀 How to Use

### 1. The Setup
Search for `🎵 Ultimate Music Timer (Genre Sync)` in the node menu.

### 2. Node Connections
* **`lyrics` (Input):** Connect your raw text or Psalm string here.
* **`duration_float` (Output):** Connect this to the `seconds` input of your **EmptyAceStepLatent** and the `duration` input of your **TextEncodeAceStepAudio1.5**.
* **`cleaned_lyrics` (Output):** **CRITICAL.** Connect this to the `text` input of your Text Encoder. This version of the text has been sanitized to prevent word-skipping.
* **`stats_panel` (Output):** Connect to a `Show Text` node to see a breakdown of character counts and final duration math.

### 3. Recommended Settings
* **1960s Soul/Psalms:** Use `Soul_Classic (13.0)`.
* **Emotional Ballads:** Use `Soul_Ballad (9.5)`.
* **Fast Praise/Pop:** Use `Motown_Upbeat (16.5)`.

## 🧮 The Formula
The node operates on a transparent logic to ensure your renders stay within VRAM limits (especially useful for 6GB/8GB cards like the ASUS Zephyrus G14):

`Total Seconds = (Character Count / Genre Pace) + Intro Buffer + Outro Buffer`

## 📝 License
MIT License - Feel free to use this in your own workflows or expand upon it!

***

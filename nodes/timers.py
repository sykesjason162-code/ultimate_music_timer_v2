import math

class UltimateMusicTimerV2:
    """
    DESCRIPTION = ### 🎵 Universal Music Timer (Genre Sync)
    Automates duration for ACE-Step Audio 1.5 and similar models.
    
    **Features:**
    - **Advanced Sanitization:** Automatically handles commas, semicolons, and parentheses to prevent AI skipping.
    - **Genre Pace:** Sets character density based on musical style.
    - **Automatic Buffers:** Adds silence for intros and outros.
    """
    
    DESCRIPTION = """
    ### 🎵 Universal Music Timer (Genre Sync)
    This node calculates the exact seconds needed for AI music generation.
    
    **How to use:**
    1. Connect 'lyrics' to your text input.
    2. Choose a 'genre' or set 'custom_pace'.
    3. Link 'duration_float' to your Latent and Encoder 'duration' slots.
    4. Link 'cleaned_lyrics' to your Text Encoder (CRITICAL for fixing skipping).
    """

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "lyrics": ("STRING", {"multiline": True}),
                "genre": ([
                    "Soul_Classic (13.0)", 
                    "Soul_Ballad (9.5)", 
                    "Motown_Upbeat (16.5)", 
                    "Gospel_Powerful (11.0)",
                    "Modern_R&B (14.0)",
                    "Country_Folk (10.5)",
                    "Pop_Rock (15.5)",
                    "Hip_Hop_Rap (22.0)",
                    "Ambient_Spoken (14.5)",
                    "Custom_Manual"
                ],),
                "custom_pace": ("FLOAT", {"default": 13.0, "min": 1.0, "max": 50.0, "step": 0.1}),
                "intro_buffer": ("FLOAT", {"default": 15.0, "min": 0.0, "max": 100.0, "step": 1.0}),
                "outro_buffer": ("FLOAT", {"default": 15.0, "min": 0.0, "max": 100.0, "step": 1.0}),
            },
        }

    RETURN_TYPES = ("FLOAT", "INT", "STRING", "STRING")
    RETURN_NAMES = ("duration_float", "duration_int", "stats_panel", "cleaned_lyrics")
    FUNCTION = "calculate_logic"
    CATEGORY = "AudioTools"

    def calculate_logic(self, lyrics, genre, custom_pace, intro_buffer, outro_buffer):
        # --- 1. ADVANCED SANITIZATION ---
        # Replace common "stop" punctuation with safe pauses (--)
        safe_lyrics = lyrics.replace(",", " --").replace(";", " --").replace(":", " --")
        
        # Remove parentheses but keep the words inside them
        # (This prevents the AI from thinking the text is 'metadata' and skipping it)
        safe_lyrics = safe_lyrics.replace("(", " ").replace(")", " ")
        
        # Collapse multiple spaces into single spaces for accurate char count
        safe_lyrics = " ".join(safe_lyrics.split())
        
        # --- 2. PACE MAPPING ---
        pace_map = {
            "Soul_Classic (13.0)": 13.0,
            "Soul_Ballad (9.5)": 9.5,
            "Motown_Upbeat (16.5)": 16.5,
            "Gospel_Powerful (11.0)": 11.0,
            "Modern_R&B (14.0)": 14.0,
            "Country_Folk (10.5)": 10.5,
            "Pop_Rock (15.5)": 15.5,
            "Hip_Hop_Rap (22.0)": 22.0,
            "Ambient_Spoken (14.5)": 14.5,
            "Custom_Manual": custom_pace
        }
        pace = pace_map.get(genre, 13.0)
        
        # --- 3. DURATION CALCULATION ---
        char_count = len(safe_lyrics)
        # Avoid division by zero
        base_time = char_count / max(pace, 0.1)
        total_time = base_time + intro_buffer + outro_buffer
        
        # Ceiling the value to ensure the AI has enough room to finish the last word
        final_val = float(math.ceil(total_time))
        
        # --- 4. STATS FOR UI FEEDBACK ---
        stats = (f"--- SESSION STATS ---\n"
                 f"Genre: {genre}\n"
                 f"Char Count: {char_count}\n"
                 f"Total Duration: {final_val}s")
        
        return (final_val, int(final_val), stats, safe_lyrics)

# Standard ComfyUI Mapping for the library
NODE_CLASS_MAPPINGS = {"UltimateMusicTimerV2": UltimateMusicTimerV2}
NODE_DISPLAY_NAME_MAPPINGS = {"UltimateMusicTimerV2": "🎵 Universal Music Timer (Genre Sync)"}
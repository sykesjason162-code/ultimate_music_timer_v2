import math

class UltimateMusicTimerV2:
    """
    ### Ultimate Music Timer (Genre Sync)
    Automates the timing for ACE-Step Audio 1.5. 
    
    **How to use:**
    1. Connect your lyric text to 'lyrics'.
    2. Choose a 'genre' or set a 'custom_pace'.
    3. Connect 'duration_float' to your Latent and Encoder 'seconds/duration' slots.
    4. Connect 'cleaned_lyrics' to your Text Encoder (this fixes comma-skipping).
    
    *Note: The node automatically converts commas to '--' to prevent word-skipping.*
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

    RETURN_TYPES = ("FLOAT", "INT", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("duration_float", "duration_int", "stats_panel", "cleaned_lyrics", "user_guide")
    FUNCTION = "calculate_logic"
    CATEGORY = "AudioTools"

    def calculate_logic(self, lyrics, genre, custom_pace, intro_buffer, outro_buffer):
        # 1. Comma Fix
        safe_lyrics = lyrics.replace(",", " --")
        
        # 2. Genre Mapping
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
        
        # 3. Math logic
        char_count = len(safe_lyrics)
        base_time = char_count / max(pace, 0.1)
        total_time = base_time + intro_buffer + outro_buffer
        final_val = float(math.ceil(total_time))
        
        # 4. Detailed Stats for the Power User
        stats = (f"--- SESSION STATS ---\n"
                 f"Genre: {genre}\n"
                 f"Chars: {char_count}\n"
                 f"Duration: {final_val}s")
        
        # 5. Quick Info for the Info Panel / UI
        guide = (
            "HELP: Connect 'cleaned_lyrics' to your Text Encoder to fix comma-skipping errors. "
            "Adjust 'intro/outro' to add room for instruments."
        )
        
        return (final_val, int(final_val), stats, safe_lyrics, guide)

NODE_CLASS_MAPPINGS = {"UltimateMusicTimerV2": UltimateMusicTimerV2}
NODE_DISPLAY_NAME_MAPPINGS = {"UltimateMusicTimerV2": "🎵 Ultimate Music Timer (Genre Sync)"}

# Import the class from the 'nodes' subfolder and 'timers.py' file
from .nodes.timers import UltimateMusicTimerV2

# Register the node with ComfyUI
NODE_CLASS_MAPPINGS = {
    "UltimateMusicTimerV2": UltimateMusicTimerV2
}

# The name that appears in the UI menu
NODE_DISPLAY_NAME_MAPPINGS = {
    "UltimateMusicTimerV2": "🎵 Universal Music Timer (Genre Sync)"
}

print("### [Audio-Logic] Version 1.0.0 Loaded Successfully")

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
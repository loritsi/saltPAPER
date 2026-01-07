
# input mapping service
# initialises with a mapping dict of
# key trigger -> "event" (arbitrary string)
# i.e. K_up
import sys
from pathlib import Path

# Add project root to path for standalone execution
if __name__ == "__main__":
    sys.path.insert(0, str(Path(__file__).parent.parent.parent))

import pygame
import pygame.locals as pl

KEY_VALUE_TO_NAME = {
    value: name
    for name, value in vars(pl).items()
    if name.startswith("K_")
}
BUTTON_EVENTS = [
    "CONTROLLER_BUTTON_A", "CONTROLLER_BUTTON_B",
    "CONTROLLER_BUTTON_X", "CONTROLLER_BUTTON_Y"
    "CONTROLLER_BUTTON_DPAD_UP", "CONTROLLER_BUTTON_DPAD_DOWN",
    "CONTROLLER_BUTTON_DPAD_LEFT", "CONTROLLER_BUTTON_DPAD_RIGHT",
    "CONTROLLER_BUTTON_LEFTSHOULDER", "CONTROLLER_BUTTON_RIGHTSHOULDER",
    "CONTROLLER_BUTTON_LEFTSTICK", "CONTROLLER_BUTTON_RIGHTSTICK",
    "CONTROLLER_BUTTON_BACK", "CONTROLLER_BUTTON_GUIDE",
    "CONTROLLER_BUTTON_START"
]

class EventMapper():
    def __init__(self):
        pass

    def process_events(events):
        events_combined = []
        for event in events:
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                    key = KEY_VALUE_TO_NAME.get(event.key, "unknown")
                    events_combined.append(key)


if __name__ == "__main__":
    from components.helper.textwindow import TextWindow

    tw = TextWindow()

    while tw.running:
        tw.tick()
        if tw.events != []:
            for event in tw.events:
                    


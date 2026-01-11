
# input mapping service
# initialises with a mapping dict of
# key trigger -> "event" (arbitrary string)
# i.e. K_up
import sys
from pathlib import Path

if __name__ == "__main__":
    sys.path.insert(0, str(Path(__file__).parent.parent.parent))

import pygame
import pygame.locals as pl
import pygame._sdl2.controller as ctrl

KEY_VALUE_TO_NAME = {
    value: name
    for name, value in vars(pl).items()
    if name.startswith("K_")
}
BUTTON_VALUE_TO_NAME = {
    value: name
    for name, value in vars(pl).items()
    if name.startswith("CONTROLLER_BUTTON_")
}

EVENT_TYPES_LISTENING = {
    pygame.KEYDOWN: "key",
    pygame.KEYUP: "key",
    pygame.CONTROLLERBUTTONDOWN: "button",
    pygame.CONTROLLERBUTTONUP: "button",
}

class EventMapper():
    def __init__(self):
        self.gamepad = None
        self.input_roster = {}
        for item in KEY_VALUE_TO_NAME.values():
            self.input_roster[item] = 0
        for item in BUTTON_VALUE_TO_NAME.values():
            self.input_roster[item] = 0
        

    def controllercheck(self):
        if ctrl.get_count() > 0 and self.gamepad is None:
            self.gamepad = ctrl.Controller(0)
        elif ctrl.get_count() == 0:
            self.gamepad = None

    def tick(self):
        for item in self.input_roster:
            if self.input_roster[item] > 0:     # positive / pressed
                self.input_roster[item] += 1
            elif self.input_roster[item] < 0:   # negative / unpressed after first press
                self.input_roster[item] -= 1
            else:                               # 0 / never pressed
                continue

    def process_events(self, events):
        self.tick()
        self.controllercheck()
        for event in events:
            event_type = event.type
            if event_type in EVENT_TYPES_LISTENING.keys():
                target = EVENT_TYPES_LISTENING[event.type]
                value = getattr(event, target, None)
                
                if target == "key":
                    name = KEY_VALUE_TO_NAME.get(value, "unknown")
                elif target == "button":
                    name = BUTTON_VALUE_TO_NAME.get(value, "unknown")
                else:
                    name = "unknown"

                updown = -1 if event_type in [pygame.KEYUP, pygame.CONTROLLERBUTTONUP] else 1
                print(f"{name} ({value}) set to {updown}")
                
                self.input_roster[name] = updown
            else:
                if event.type not in [pygame.JOYBUTTONDOWN, pygame.JOYBUTTONUP]:
                    pass
                    #events_combined.append(f"ignored event {event}")
        


if __name__ == "__main__":
    ctrl.init()
    from engine.helper.textwindow import TextWindow

    tw = TextWindow(width=60, height=25)
    em = EventMapper()

    while tw.running:
        tw.tick()
        em.process_events(tw.events)
        tw.blank()
        
        tw.write(2, 1, f"CONTROLLER BUTTON TEST")
        tw.write(2, 2, f"FPS: {tw.clock.get_fps():.2f}")
        
        y = 4
        tw.write(2, y, "CONTROLLER BUTTONS:")
        y += 1
        
        for name, value in em.input_roster.items():
            if name.startswith("CONTROLLER_BUTTON_"):
                button_name = name.replace("CONTROLLER_BUTTON_", "")
                tw.write(3, y, button_name)
                
                if value > 0:
                    tw.write(20, y, "[PRESSED]")
                    tw.write(40, y, f"{str(abs(value))} frames")
                elif value < 0:
                    tw.write(20, y, "[released]")
                    tw.write(40, y, f"{str(abs(value))} frames")
                else:
                    tw.write(20, y, "[neutral]")
                    tw.write(40, y, "0")
                
                y += 1
        tw.clock.tick(120)


from typing import Callable

class Event():
    def __init__(
            self,
            triggers: str | list,
            criteria: Callable,
            callback: Callable,
            args: list = None,
            priority: int = 0,
            eat_trigger: bool = False
    ):
        self.triggers = triggers if isinstance(triggers, list) else [triggers]
        self.criteria = criteria
        self.callback = callback
        self.args = args if args else []
        self.priority = priority
        self.eat_trigger = eat_trigger

class Criteria():
    @staticmethod
    def on_press(f):
        return True if f==1 else False
    
    @staticmethod
    def on_held(f):
        return True if f>0 else False
    
    @staticmethod
    def on_release(f):
        return True if f==-1 else False
    
    @staticmethod
    def make_on_held_interval(x):
        def on_held_interval(f):
            return True if f % x == 0 else False
        return on_held_interval
    
    @staticmethod
    def make_combined_criteria(func_a, func_b) -> bool:
        def combined_criteria(f):
            truth = func_a(f) and func_b(f)
            return truth
        return combined_criteria


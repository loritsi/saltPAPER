

class StateService:
    def __init__(self):
        ...

        # empty box for user to put shared variables without cluttering globals

    def __getattr__(self, name):
        try:
            return self.__getattribute__(name)
        except AttributeError:
            return None
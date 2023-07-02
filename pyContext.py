"""The Context class is the primary interface for interacting with state objects.
State changes are handled by the transition_to method.
All other methods get piped into the state class's matching methods"""

from abc import ABC,abstractmethod

class Context:
    _state = None

    def __init__(self, state):
        """Context transitions into a state on init by running the transition_to method"""

        self.transition_to(state)




    def transition_to(self, state):
        """give context on state change, update self state variable and assign self as the states context"""

        print(f"state change requested - {type(state).__name__}")
        self._state = state
        self._state.context = self




    def hello(self) -> None:
        """Print a hello message from the current state object"""
        self._state.hello()




    def say(self, msg: str):
        """have the state object accept a parameter and print the message"""
        self._state.say(msg)




    def get_integer_attribute(self) -> int:
        """Return a integer value from a state object"""
        return self._state.get_integer_attribute()







class State(ABC):
    """Class is used by context to implement behaviors"""
    _context = None

    #default property
    _value = 5

    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, context):
        self._context = context


    @abstractmethod
    def hello(self) -> None:
        pass

    @abstractmethod
    def say(self, msg) -> None:
        pass

    @abstractmethod
    def get_integer_attribute(self) -> int:
        pass

from run.file_context import State

class Concrete_State_A(State):
    """Example class A"""

    def hello(self) -> None:
        """say hello"""
        print(f"hello from {type(self).__name__}!")




    def say(self, msg: str) -> None:
        """message from this class"""
        print(f"{type(self).__name__}: {msg}")




    def get_integer_attribute(self) -> int:
        """stored integer attribute"""
        return self._value



class Concrete_State_B(State):
    """Example class B"""


    def __init__(self, value):
        """On init change the default value to the value parameter"""

        self._value = value




    def hello(self) -> None:
        """say hello"""
        print(f"hi, I am {type(self).__name__}!")




    def say(self, msg: str) -> None:
        """message from this class"""
        print(f"'{msg}' says {type(self).__name__}")




    def get_integer_attribute(self) -> int:
        """stored integer attribute"""
        return self._value

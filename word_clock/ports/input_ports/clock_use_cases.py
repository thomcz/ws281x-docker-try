from abc import ABC, abstractmethod


class ClockUseCases(ABC):
    """
    Input port interface defining the use cases for the word clock application.
    This interface defines how external systems interact with the application.
    """
    
    @abstractmethod
    def update_clock(self) -> None:
        """
        Update the clock display based on the current time.
        This is the main use case for the word clock application.
        """
        pass
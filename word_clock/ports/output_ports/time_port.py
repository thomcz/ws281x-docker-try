from abc import ABC, abstractmethod
from datetime import datetime


class TimePort(ABC):
    """
    Output port interface for retrieving the current time.
    This interface defines how the application gets time information.
    """
    
    @abstractmethod
    def get_current_time(self) -> datetime:
        """
        Get the current time.
        
        Returns:
            The current datetime
        """
        pass
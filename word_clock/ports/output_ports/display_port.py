from abc import ABC, abstractmethod
from typing import List


class DisplayPort(ABC):
    """
    Output port interface for displaying the word clock.
    This interface defines how the application interacts with display devices.
    """
    
    @abstractmethod
    def set_leds(self, led_list: List[int], color: int) -> None:
        """
        Set the specified LEDs to the given color.
        
        Args:
            led_list: List of LED indices to set
            color: Color value to set the LEDs to
        """
        pass
        
    @abstractmethod
    def reset_leds(self) -> None:
        """
        Turn off all LEDs.
        """
        pass
from datetime import datetime
from typing import List

from word_clock.domain.entities.clock_state import ClockState


class ClockService:
    """
    Domain service that contains the core business logic for the word clock.
    This service uses the ClockState entity but doesn't depend on any external systems.
    """
    
    def __init__(self, clock_state: ClockState = None):
        """
        Initialize the clock service with a clock state entity.
        
        Args:
            clock_state: The clock state entity to use. If None, a new one will be created.
        """
        self.clock_state = clock_state or ClockState()
    
    def get_active_leds(self, current_time: datetime) -> List[int]:
        """
        Get the list of LEDs that should be active based on the current time.
        
        Args:
            current_time: The current time
            
        Returns:
            A list of LED indices that should be lit
        """
        return self.clock_state.calculate_state(current_time)
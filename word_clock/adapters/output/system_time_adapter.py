from datetime import datetime

from pytz import timezone

from word_clock.ports.output_ports.time_port import TimePort


class SystemTimeAdapter(TimePort):
    """
    Adapter that implements the TimePort interface using the system time.
    This adapter handles timezone conversions.
    """
    
    def __init__(self, timezone_name: str = 'Europe/Berlin'):
        """
        Initialize the system time adapter.
        
        Args:
            timezone_name: The name of the timezone to use
        """
        self.timezone_name = timezone_name
    
    def get_current_time(self) -> datetime:
        """
        Get the current time in the configured timezone.
        
        Returns:
            The current datetime
        """
        return datetime.now(timezone(self.timezone_name))
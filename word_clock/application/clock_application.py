from rpi_ws281x import Color

from word_clock.domain.services.clock_service import ClockService
from word_clock.ports.input_ports.clock_use_cases import ClockUseCases
from word_clock.ports.output_ports.display_port import DisplayPort
from word_clock.ports.output_ports.time_port import TimePort


class ClockApplication(ClockUseCases):
    """
    Application service that implements the ClockUseCases interface.
    This class orchestrates the flow between domain services and ports.
    """
    
    def __init__(
        self,
        clock_service: ClockService,
        display_port: DisplayPort,
        time_port: TimePort,
        color: int = Color(255, 255, 255)
    ):
        """
        Initialize the clock application.
        
        Args:
            clock_service: The domain service for clock logic
            display_port: The port for displaying the clock
            time_port: The port for retrieving the current time
            color: The color to use for the LEDs
        """
        self.clock_service = clock_service
        self.display_port = display_port
        self.time_port = time_port
        self.color = color
    
    def update_clock(self) -> None:
        """
        Update the clock display based on the current time.
        This method implements the main use case for the word clock application.
        """
        # Get the current time from the time port
        current_time = self.time_port.get_current_time()
        
        # Get the active LEDs from the domain service
        active_leds = self.clock_service.get_active_leds(current_time)
        
        # Update the display through the display port
        self.display_port.set_leds(active_leds, self.color)
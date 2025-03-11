from time import sleep

from word_clock.ports.input_ports.clock_use_cases import ClockUseCases


class CliAdapter:
    """
    Command-line interface adapter that triggers the clock use cases.
    This adapter is responsible for the user interaction through the command line.
    """
    
    def __init__(self, clock_use_cases: ClockUseCases):
        """
        Initialize the CLI adapter.
        
        Args:
            clock_use_cases: The clock use cases to trigger
        """
        self.clock_use_cases = clock_use_cases
    
    def run(self, update_interval: int = 30):
        """
        Run the word clock application with periodic updates.
        
        Args:
            update_interval: The interval in seconds between updates
        """
        print(f"Word Clock started. Updating every {update_interval} seconds.")
        try:
            while True:
                self.clock_use_cases.update_clock()
                sleep(update_interval)
        except KeyboardInterrupt:
            print("Word Clock stopped.")
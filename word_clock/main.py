#!/usr/bin/env python3
"""
Main entry point for the Word Clock application.
This module configures dependency injection and starts the application.
"""

from word_clock.adapters.input.cli_adapter import CliAdapter
from word_clock.adapters.output.led_strip_adapter import LedStripAdapter
from word_clock.adapters.output.system_time_adapter import SystemTimeAdapter
from word_clock.application.clock_application import ClockApplication
from word_clock.domain.entities.clock_state import ClockState
from word_clock.domain.services.clock_service import ClockService


def main():
    """
    Configure and start the Word Clock application.
    """
    # Create domain layer components
    clock_state = ClockState()
    clock_service = ClockService(clock_state)
    
    # Create adapters
    display_adapter = LedStripAdapter()
    time_adapter = SystemTimeAdapter()
    
    # Create application layer
    clock_application = ClockApplication(
        clock_service=clock_service,
        display_port=display_adapter,
        time_port=time_adapter
    )
    
    # Create CLI adapter and run the application
    cli_adapter = CliAdapter(clock_application)
    cli_adapter.run()


if __name__ == "__main__":
    main()
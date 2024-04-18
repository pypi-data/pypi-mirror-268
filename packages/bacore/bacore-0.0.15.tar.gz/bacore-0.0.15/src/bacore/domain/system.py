"""Module for domain system."""
from shutil import which


class CommandLineProgram:
    """Program."""

    def __init__(self, name: str, verify_exists_func: callable = which):
        """Initialize."""
        self.name = name
        self.verify_exists_func = verify_exists_func

    def verify_exists(self) -> bool:
        """Verify command line program exists on path."""
        return self.verify_exists_func(self.name) is not None

"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        self.start = start
        self.current = start

    def generate(self):
        """Returns the next number in the sequence and increments current number.
        >>> serial = SerialGenerator(start=100)

        >>> serial.generate()
        100

        >>> serial.generate()
        101
        """
        num = self.current
        self.current += 1
        return num

    def reset(self):
        """Resets the current number to the original starting number.
        >>> serial = SerialGenerator(start=100)

        >>> serial.generate()
        100

        >>> serial.reset()

        >>> serial.generate()
        100
        """
        self.current = self.start
    
    def __repr__(self):
        """
        >>> serial = SerialGenerator(start=100)

        >>> serial.__repr__()
        '<SerialGenerator start=100 next=101>'
        """
        return f'<SerialGenerator start={self.start} next={self.current + 1}>'


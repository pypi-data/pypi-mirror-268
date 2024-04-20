class PriceRange:
    def __init__(self, timestamp, high, low, open, close):
        self._timestamp = timestamp
        self._high = high
        self._low = low
        self._open = open
        self._close = close
        self._volume = 
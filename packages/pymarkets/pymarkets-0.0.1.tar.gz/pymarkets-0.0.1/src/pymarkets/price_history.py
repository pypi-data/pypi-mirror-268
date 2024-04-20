class PriceHistory:
    def __init__(self, timestamps, highs, lows, opens, closes):
        self._timestamps = timestamps
        self._highs = highs
        self._lows = lows
        self._opens = opens
        self._closes = closes
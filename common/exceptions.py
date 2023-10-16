class InsufficientStockException(Exception):
    def __init__(self, message="Insufficient stock available"):
        self.message = message
        super().__init__(self.message)

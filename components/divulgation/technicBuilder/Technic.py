class Technic():
    """
    Using builder pattern to create artist configuration
    """

    def __init__(self) -> None:
        self.parts = []
    
    def add(self, part) -> None:
        self.parts.append(part)

    def get_parts(self) -> None:
        return self.parts
class Subject:
    def __init__(self, id: int = None, name: str = '', code: str = '', description: str = ''):
        if not name or not code:
            raise ValueError("Nombre y código son obligatorios.")

        self.id = id
        self.name = name
        self.code = code
        self.description = description

    def __str__(self):
        return f"Subject(id={self.id}, name={self.name}, code={self.code}, description={self.description})"
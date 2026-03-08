from Astandy.enums.events import Event

class Update:
    event: Event

    def __init__(self):
        pass

    def __str__(self):
        return f'{self.__class__.__name__}(event={self.event.name})'
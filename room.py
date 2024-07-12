from pathlib import Path
from ascii_magic import AsciiArt

class Room:

    def __init__(self, description, objects, pic=None):
        self.description = description
        self.objects = objects
        self.pic = pic
        self.exits = {}

    def add_exit(self, direction, room):
        self.exits[direction] = room

    def show(self):
        if self.pic:
            art = AsciiArt.from_image(Path('assets') / f"{self.pic}.jpg")
            art.to_terminal()
        print()
        print(self.description)

    def __str__(self):
        return self.description
    
    def __contains__(self, object):
        return object in self.objects
    
    def __remove__(self, object):
        self.objects.remove(object)

    
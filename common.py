import json
from PIL import ImageTk, Image
def loadImage(path, size=128):
    _image = Image.open(path)
    _image = _image.resize((size, size), Image.ANTIALIAS)
    _image = ImageTk.PhotoImage(_image)
    return _image


def from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb


class EnvironmentVariable():
    def __init__(self):
        with open('./data/config.json', encoding='utf-8') as fh:
            self.config = json.load(fh)

    def getConfig(self):
        return self.config


env_var = EnvironmentVariable()

def getConfig():
    return env_var.getConfig()


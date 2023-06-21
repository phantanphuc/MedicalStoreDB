from PIL import ImageTk, Image
def loadImage(path, size=128):
    _image = Image.open(path)
    _image = _image.resize((size, size), Image.ANTIALIAS)
    _image = ImageTk.PhotoImage(_image)
    return _image
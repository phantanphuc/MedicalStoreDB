from PIL import ImageTk, Image
def loadImage(path):
    _image = Image.open(path)
    _image = _image.resize((128, 128), Image.ANTIALIAS)
    _image = ImageTk.PhotoImage(_image)
    return _image
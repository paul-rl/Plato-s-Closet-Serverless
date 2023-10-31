from pathlib import Path


def getTextBody():
    path = Path().parent.absolute()
    f = open(path / 'src' / 'assets' / 'message.txt', 'r')
    textBody = f.read()
    f.close()

    return textBody


def setTextBody(newBody):
    path = Path().parent.absolute()
    f = open(path / 'src' / 'assets' / 'message.txt', 'w')
    f.write(newBody)
    f.close()

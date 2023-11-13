from pathlib import Path


def getTextBody():
    absPath = Path().parent.absolute()
    path = absPath / 'src' / 'assets/' / 'message.txt'
    with open(path, 'r') as f:
        textBody = f.read()
        return textBody
    print("Error, could not open file")
    return None


def setTextBody(newBody):
    absPath = Path().parent.absolute()
    path = absPath / 'src' / 'assets/' / 'message.txt'
    with open(path, 'w') as f:
        f.write(newBody)

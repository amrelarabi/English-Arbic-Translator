class Result:
    def __init__(self):
        self.Value = None
        self.Suggesions = []

    def Translated(self):
        return self.Value is not None

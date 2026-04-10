class One:
    def __init__(self, text: str) -> str:
        self.text = text
    def __str__(self) -> str:
        return self.text
    def addcat(self) -> str:
        return "cat added " + self.text
    def addotherthing(self,other):
        return other + self.text


def Upper(text:str) -> str:
    return text.upper()




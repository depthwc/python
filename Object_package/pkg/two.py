class Two:
    def __init__(self, text: str) -> str:
        self.text = text
    def __str__(self) -> str:
        return self.text
    def addcow(self) -> str:
        return "cow added " + self.text
    def whatever(self,other):
        return other + self.text
    
def Lower(text:str) -> str:
    return text.lower()
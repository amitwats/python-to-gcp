from AbstractDBInteracter import AbstractDBInteracter

class GCPInteracter(AbstractDBInteracter):
    
    def __init__(self):
        super().__init__()
     

    def InsertString(self,pString:str):
        AbstractDBInteracter.InsertString(self,pString)
        print("GCP Interacter:InsertString "+pString)

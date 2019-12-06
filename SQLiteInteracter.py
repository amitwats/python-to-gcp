from AbstractDBInteracter import AbstractDBInteracter

class SQLiteInteracter(AbstractDBInteracter):
    
    def __init__(self):
        super().__init__()


    def InsertString(self,pString:str):
        AbstractDBInteracter.InsertString(self,pString)
        print("SQLite Interacter:InsertString "+pString)


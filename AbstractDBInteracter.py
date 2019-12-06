from abc import ABC, abstractmethod



class AbstractDBInteracter(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def InsertString(self,pString:str):
        pass

from abc import ABC, abstractmethod
class Bangladesh(ABC): 
    @abstractmethod
    def print0to20(self):
        pass
    def print0toten(self):
        for i in range(11):
            print(i)

## Test

class Car:
    
    def __init__(self, manif: str, model: str, year: int):
        self.manif = manif
        self.model = model
        self.year = year
    
    def drive(self):
        print(f"I'm {self.model}, and I'M WALKING HEEEERRREEE")
    
    def __del__(self):
        print(f"I'm {self.model} and I'm GONE!!!")
        super().__del__()
        



class CheckName:
    def __init__(self,name):
        self.name=name
    def check(self):
        print(f'Same or Different name and it is {self.name}')
obj = CheckName("madhu")
obj.check()

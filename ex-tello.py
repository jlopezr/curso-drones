import tello

class Main(tello.App):
    
    def __init__(self):
        super().__init__()
        self.i = 0
    
    def draw(self):
        print("Hola", self.i)
        self.i = self.i + 1
        
app = Main()
app.run()
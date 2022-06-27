class Prueba:
    
    def run():
        print("Prueba::run()")
        
    def run2(self):
        print("Prueba::run2()")            


#p = Prueba()
#p.run2()


class Prueba2(Prueba):
    def run2(self):
        print("Prueba2::run2()")
        super().run2()

p2 = Prueba2()
Prueba2.run()
p2.run2()
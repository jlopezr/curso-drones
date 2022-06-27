import pygame

class App:
    
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()
        self.frames = 20
        self.screenSize = (800,600)
        
        self.BLACK = (  0,   0,   0)
        self.WHITE = (255, 255, 255)
        self.BLUE  = (  0,   0, 255)
        self.GREEN = (  0, 255,   0)
        self.RED   = (255,   0,   0)
        self.GREY  = (128, 128, 128)
    
    def initScreen(self):
        #print("SETUP()")
        pygame.init()
        self.screen = pygame.display.set_mode(self.screenSize)
        
    def setup(self):
        pass

    def draw(self):
        pass
    
    def run(self):
        
        self.initScreen()
        self.setup()
        
        while self.running:

            #print("RUN()")

            self.clock.tick(self.frames)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                        
            self.draw()
                                                
        pygame.quit()

import pygame
import sys
from fpsCounter import FpsCounter
from objects import Button
from game import Game
from tilemap import Tilemap

class Game(Game):
    def __init__(self) -> None:
        super().__init__()
        self.fps_counter = FpsCounter(window=self.screen, font_size= 36)
        self.buttons = {
            "1": Button(0,0,75,30,text="test1",window=self.screen),
            "2": Button(0,0,75,30,"test2",self.screen),
            "3": Button(0,0,75,30,"test3",self.screen),
            "4": Button(0,0,75,30,"test4",self.screen),
        }
        self.tilemap = Tilemap(self.screen,64)
        
        for key, value in self.buttons.items():
            value.center_of_screen_x()
            value.align_on_y_axis(int(key),4)
            
        self.offset = [0,0]
    
    def draw(self) -> None:
        self.screen.fill((255, 255, 255)) #fill with white
        self.fps_counter.draw()
        for _, value in self.buttons.items():
            value.draw()
        self.tilemap.draw(offset=tuple(self.offset))
            
            
    def logic(self) -> None:
        for _, value in self.buttons.items():
            value.check_click()
        #self.tilemap.logic(pygame.mouse.get_pos())
        self.tilemap.fill_screen()
         
    def run(self) -> None:
        while self.running:
            self.fps_counter.count_fps()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.offset[0] -= 1
                    # mouse_pressed = pygame.mouse.get_pressed()
                    # if mouse_pressed[0]:
                    #     self.offset += 1
                    # elif mouse_pressed[2]:
                    #     self.offset -= 1
                    
            self.draw()
            self.logic()
            
            # Update the display
            pygame.display.flip()
            self.clock.tick(60)



Game().run()
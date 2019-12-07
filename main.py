# "ArcuS"
# Frozen Jam by tgfcoder <https://twitter.com/tgfcoder> licensed under CC-BY-3 <http://creativecommons.org/licenses/by/3.0/>

import pygame
import constants
pygame.init()
displayInfoObject = pygame.display.Info()
constants.WIDTH = displayInfoObject.current_w - 20
constants.HEIGHT = displayInfoObject.current_h - 20
from game import *


#Function for opening screen
def main() :
    intro = True
    game = Game()
    game.loadMusic()
    game.readHighScore()
    while intro:
        pygame.mixer.music.play(loops=-1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = False
        game.screen.fill(SKY_BLUE)
        game.screen.blit(game.background, game.background_rect)
        game.draw.Button(200, 2*HEIGHT/3, "PLAY", BRIGHT_GREEN, GREEN, game.gameloop, 150, 100)
        game.draw.Button(WIDTH-450, 2*HEIGHT/3, "QUIT", BRIGHT_RED, RED, quit, 150, 100)
        game.draw.draw_text("__ArcuS__", WIDTH/2, HEIGHT/3, 200, BLUE)
        game.draw.draw_text("HIGH SCORE:%d" % (game.highscore), WIDTH-400, 50, 30, BLACK)
        pygame.display.flip()
        game.clock.tick(FPS)

main()

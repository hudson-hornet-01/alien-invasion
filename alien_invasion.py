import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
import game_functions as gf

def run_game():
    pygame.init()
    
    pygame.mixer.init()

    pygame.mixer.music.load("lightyear.ogg")
    pygame.mixer.music.set_volume(0.5)   
    pygame.mixer.music.play(-1)
    
    ai_settings=Settings()
    
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    stats=GameStats(ai_settings)
    sb=Scoreboard(ai_settings,screen,stats)
    
    ship=Ship(ai_settings,screen)

    play_button=Button(ai_settings,screen,"Play")

    bullets=Group()
    aliens=Group()

    gf.create_fleet(ai_settings,screen,ship,aliens)
    
    try:
        with open('highscore.txt') as f:
            stats.high_score = int(f.read())
    except:
        stats.high_score = 0  

    sb.prep_high_score()  

    while True:
        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            gf.update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets) 
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)
        
        
run_game()
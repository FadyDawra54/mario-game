import pygame
from enemy import Enemy
from coin import Coin

class Level:
    def __init__(self, level_num, screen_width, screen_height):
        self.level_num = level_num
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.platforms = []
        self.enemies = []
        self.coins = []
        
        self.generate_level()
    
    def generate_level(self):
        """Génère les platefmes de base"""
        # Plateforme de base (sol)
        self.platforms.append(pygame.Rect(0, self.screen_height - 50, 
                                         self.screen_width, 50))
        
        if self.level_num == 1:
            self.generate_level_1()
        elif self.level_num == 2:
            self.generate_level_2()
        elif self.level_num == 3:
            self.generate_level_3()
        else:
            self.generate_level_1()
    
    def generate_level_1(self):
        """Niveau 1 - Facile"""
        # Platefmes intermédiaires
        self.platforms.append(pygame.Rect(200, 450, 150, 20))
        self.platforms.append(pygame.Rect(500, 380, 150, 20))
        self.platforms.append(pygame.Rect(800, 320, 150, 20))
        self.platforms.append(pygame.Rect(1000, 250, 180, 20))
        
        # Ennemis
        self.enemies.append(Enemy(300, 400, 2))
        self.enemies.append(Enemy(600, 330, 2))
        
        # Pièces
        for i in range(3):
            self.coins.append(Coin(250 + i * 25, 420))
        
        for i in range(2):
            self.coins.append(Coin(550 + i * 25, 350))
        
        for i in range(3):
            self.coins.append(Coin(850 + i * 25, 290))
    
    def generate_level_2(self):
        """Niveau 2 - Moyen"""
        # Platefmes
        self.platforms.append(pygame.Rect(150, 480, 120, 20))
        self.platforms.append(pygame.Rect(350, 420, 120, 20))
        self.platforms.append(pygame.Rect(550, 360, 120, 20))
        self.platforms.append(pygame.Rect(750, 300, 120, 20))
        self.platforms.append(pygame.Rect(950, 240, 220, 20))
        
        # Ennemis (plus nombreux)
        self.enemies.append(Enemy(200, 430, 3))
        self.enemies.append(Enemy(400, 370, 3))
        self.enemies.append(Enemy(600, 310, 3))
        self.enemies.append(Enemy(800, 250, 3))
        
        # Pièces
        for i in range(8):
            self.coins.append(Coin(100 + i * 30, 450))
        
        for i in range(8):
            self.coins.append(Coin(300 + i * 30, 390))
        
        for i in range(10):
            self.coins.append(Coin(900 + i * 25, 210))
    
    def generate_level_3(self):
        """Niveau 3 - Difficile"""
        # Platefmes
        self.platforms.append(pygame.Rect(100, 480, 100, 20))
        self.platforms.append(pygame.Rect(300, 430, 100, 20))
        self.platforms.append(pygame.Rect(500, 380, 100, 20))
        self.platforms.append(pygame.Rect(700, 320, 100, 20))
        self.platforms.append(pygame.Rect(900, 260, 100, 20))
        self.platforms.append(pygame.Rect(1000, 150, 180, 20))
        
        # Ennemis (beaucoup plus)
        for i in range(5):
            self.enemies.append(Enemy(150 + i * 200, 430, 3 + i))
        
        # Pièces
        for x in range(100, self.screen_width - 100, 80):
            for y in range(200, 500, 100):
                self.coins.append(Coin(x, y))
    
    def get_platforms(self):
        return self.platforms
    
    def get_enemies(self):
        return self.enemies
    
    def get_coins(self):
        return self.coins

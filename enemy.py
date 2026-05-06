import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, speed=2):
        super().__init__()
        self.width = 32
        self.height = 32
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((100, 100, 0))  # Goomba jaune-brun
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        # Mouvement
        self.speed = speed
        self.direction = 1  # 1 pour droite, -1 pour gauche
        self.move_range = 150
        self.start_x = x
        
        # Physique
        self.vel_y = 0
        self.gravity = 0.5
        self.on_ground = False
        self.max_fall_speed = 10
    
    def update(self, platforms, screen_width, screen_height, player_rect=None):
        """Met à jour la position de l'ennemi"""
        # Mouvement horizontal
        self.rect.x += self.speed * self.direction
        
        # Inverser la direction si limite de portée atteinte
        if abs(self.rect.x - self.start_x) > self.move_range:
            self.direction *= -1
        
        # Appliquer la gravité
        if not self.on_ground:
            self.vel_y += self.gravity
            if self.vel_y > self.max_fall_speed:
                self.vel_y = self.max_fall_speed
        
        self.rect.y += self.vel_y
        
        # Collision avec les platefomes
        self.on_ground = False
        for platform in platforms:
            if self.rect.colliderect(platform):
                # Collision par le dessus
                if self.vel_y > 0 and self.rect.bottom <= platform.top + 10:
                    self.rect.bottom = platform.top
                    self.vel_y = 0
                    self.on_ground = True
                # Collision latérale
                elif self.vel_x > 0:
                    self.rect.right = platform.left
                    self.direction = -1
                elif self.vel_x < 0:
                    self.rect.left = platform.right
                    self.direction = 1
        
        # Limites de l'écran
        if self.rect.left < 0 or self.rect.right > screen_width:
            self.direction *= -1
        
        # Game Over si l'ennemi tombe
        if self.rect.top > screen_height:
            return False
        
        return True
    
    def draw(self, surface):
        """Dessine l'ennemi (Goomba)"""
        self.image.fill((100, 100, 0))
        
        # Tête
        pygame.draw.circle(self.image, (100, 100, 0), (self.width // 2, 12), 10)
        # Yeux
        pygame.draw.circle(self.image, (255, 255, 255), (self.width // 2 - 4, 10), 3)
        pygame.draw.circle(self.image, (255, 255, 255), (self.width // 2 + 4, 10), 3)
        pygame.draw.circle(self.image, (0, 0, 0), (self.width // 2 - 4, 10), 1)
        pygame.draw.circle(self.image, (0, 0, 0), (self.width // 2 + 4, 10), 1)
        # Corps
        pygame.draw.rect(self.image, (80, 80, 0), (4, 20, 24, 12))
        
        surface.blit(self.image, self.rect)
    
    def get_rect(self):
        """Retourne le rectangle de l'ennemi"""
        return self.rect
    
    def is_defeated(self, player_rect):
        """Vérifie si l'ennemi a été vaincu en sautant dessus"""
        if self.rect.colliderect(player_rect):
            # L'ennemi est vaincu si le joueur saute dessus (vient du dessus)
            return player_rect.centerx in range(self.rect.left, self.rect.right)
        return False

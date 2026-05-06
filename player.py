import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.width = 32
        self.height = 48
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((255, 0, 0))  # Rouge pour Mario
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        # Physique
        self.vel_x = 0
        self.vel_y = 0
        self.on_ground = False
        self.gravity = 0.5
        self.max_fall_speed = 15
        self.jump_power = -12
        self.max_speed = 5
        
        # Animation
        self.facing_right = True
        self.has_jumped = False
    
    def handle_input(self, keys):
        """Gère l'entrée du joueur"""
        # Mouvement horizontal
        if keys[pygame.K_LEFT]:
            self.vel_x = -self.max_speed
            self.facing_right = False
        elif keys[pygame.K_RIGHT]:
            self.vel_x = self.max_speed
            self.facing_right = True
        else:
            self.vel_x = 0
        
        # Saut
        if keys[pygame.K_SPACE] and self.on_ground and not self.has_jumped:
            self.vel_y = self.jump_power
            self.on_ground = False
            self.has_jumped = True
        
        # Relâchement de la touche saut
        if not keys[pygame.K_SPACE]:
            self.has_jumped = False
    
    def update(self, platforms, screen_width, screen_height):
        """Met à jour la position du joueur"""
        # Appliquer la gravité
        if not self.on_ground:
            self.vel_y += self.gravity
            if self.vel_y > self.max_fall_speed:
                self.vel_y = self.max_fall_speed
        
        # Appliquer la vélocité
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        
        # Collision avec les platefomes (horizontal)
        self.on_ground = False
        for platform in platforms:
            if self.rect.colliderect(platform):
                # Collision par le dessus (saut sur plateforme)
                if self.vel_y > 0 and self.rect.bottom <= platform.top + 15:
                    self.rect.bottom = platform.top
                    self.vel_y = 0
                    self.on_ground = True
                # Collision par le bas (tête contre plateforme)
                elif self.vel_y < 0:
                    self.rect.top = platform.bottom
                    self.vel_y = 0
                # Collision latérale
                elif self.vel_x > 0:
                    self.rect.right = platform.left
                elif self.vel_x < 0:
                    self.rect.left = platform.right
        
        # Limites de l'écran (horizontal)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen_width:
            self.rect.right = screen_width
        
        # Game Over si le joueur tombe
        if self.rect.top > screen_height:
            return False
        
        return True
    
    def draw(self, surface):
        """Dessine le joueur"""
        # Réinitialiser l'image
        self.image.fill((255, 0, 0))
        
        # Dessiner les détails de Mario
        # Tête
        pygame.draw.circle(self.image, (255, 200, 100), (self.width // 2, 12), 8)
        # Yeux
        pygame.draw.circle(self.image, (0, 0, 0), (self.width // 2 - 3, 10), 2)
        pygame.draw.circle(self.image, (0, 0, 0), (self.width // 2 + 3, 10), 2)
        # Corps
        pygame.draw.rect(self.image, (255, 0, 0), (6, 20, 20, 16))
        # Jambes
        pygame.draw.rect(self.image, (0, 0, 100), (8, 36, 6, 12))
        pygame.draw.rect(self.image, (0, 0, 100), (18, 36, 6, 12))
        
        # Flip l'image si nécessaire
        if not self.facing_right:
            self.image = pygame.transform.flip(self.image, True, False)
        
        surface.blit(self.image, self.rect)
    
    def get_rect(self):
        """Retourne le rectangle du joueur"""
        return self.rect

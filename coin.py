import pygame

class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.width = 16
        self.height = 16
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((255, 215, 0))  # Or
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        # Animation
        self.bob_offset = 0
        self.bob_speed = 0.15
        self.bob_range = 5
        self.original_y = y
        self.collected = False
    
    def update(self):
        """Met à jour la pièce (animation de flottaison)"""
        if not self.collected:
            self.bob_offset += self.bob_speed
            self.rect.y = self.original_y + self.bob_range * abs(__import__('math').sin(self.bob_offset))
    
    def draw(self, surface):
        """Dessine la pièce"""
        # Cercle doré
        pygame.draw.circle(self.image, (255, 215, 0), (self.width // 2, self.height // 2), 7)
        # Bordure
        pygame.draw.circle(self.image, (200, 170, 0), (self.width // 2, self.height // 2), 7, 2)
        # Détail
        pygame.draw.line(self.image, (200, 170, 0), (self.width // 2 - 2, self.height // 2 - 2), 
                        (self.width // 2 + 2, self.height // 2 + 2), 1)
        
        if not self.collected:
            surface.blit(self.image, self.rect)
    
    def collect(self):
        """Marque la pièce comme collectée"""
        self.collected = True
    
    def get_rect(self):
        """Retourne le rectangle de la pièce"""
        return self.rect

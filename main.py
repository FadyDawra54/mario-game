import pygame
import sys
from player import Player
from level import Level
from enemy import Enemy
from coin import Coin

# Initialisation de Pygame
pygame.init()

# Paramètres de l'écran
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
FPS = 60

# Couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (135, 206, 235)
GREEN = (34, 139, 34)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("🎮 Mario Game - Python Edition")
        self.clock = pygame.time.Clock()
        self.running = True
        self.paused = False
        
        # État du jeu
        self.current_level = 1
        self.score = 0
        self.game_over = False
        self.level_complete = False
        
        # Initialiser le jeu
        self.init_level()
    
    def init_level(self):
        """Initialise un nouveau niveau"""
        self.level = Level(self.current_level, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.player = Player(50, SCREEN_HEIGHT - 150)
        self.game_over = False
        self.level_complete = False
        self.paused = False
    
    def handle_events(self):
        """Gère les événements"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_p:
                    self.paused = not self.paused
                elif event.key == pygame.K_r and self.game_over:
                    self.current_level = 1
                    self.score = 0
                    self.init_level()
    
    def update(self):
        """Met à jour la logique du jeu"""
        if self.paused or self.game_over or self.level_complete:
            return
        
        # Entrée du joueur
        keys = pygame.key.get_pressed()
        self.player.handle_input(keys)
        
        # Mise à jour du joueur
        if not self.player.update(self.level.get_platforms(), SCREEN_WIDTH, SCREEN_HEIGHT):
            self.game_over = True
            return
        
        # Mise à jour des ennemis
        for enemy in self.level.get_enemies():
            enemy.update(self.level.get_platforms(), SCREEN_WIDTH, SCREEN_HEIGHT)
        
        # Mise à jour des pièces
        for coin in self.level.get_coins():
            coin.update()
        
        # Vérifier les collisions avec les pièces
        player_rect = self.player.get_rect()
        for coin in self.level.get_coins():
            if not coin.collected and player_rect.colliderect(coin.get_rect()):
                coin.collect()
                self.score += 10
        
        # Vérifier les collisions avec les ennemis
        coins_collected = sum(1 for coin in self.level.get_coins() if coin.collected)
        enemies_to_remove = []
        
        for i, enemy in enumerate(self.level.get_enemies()):
            enemy_rect = enemy.get_rect()
            # Vérifier si le joueur a sauté sur l'ennemi
            if (player_rect.colliderect(enemy_rect) and 
                self.player.vel_y > 0 and 
                player_rect.centerx in range(enemy_rect.left, enemy_rect.right)):
                enemies_to_remove.append(i)
                self.score += 50
            # Vérifier si le joueur a touché l'ennemi normalement (game over)
            elif player_rect.colliderect(enemy_rect):
                if player_rect.centerx not in range(enemy_rect.left, enemy_rect.right) or self.player.vel_y <= 0:
                    self.game_over = True
                    return
        
        # Retirer les ennemis vaincus
        for i in reversed(enemies_to_remove):
            self.level.enemies.pop(i)
        
        # Vérifier la fin du niveau
        if coins_collected == len(self.level.get_coins()) and len(self.level.get_enemies()) == 0:
            self.level_complete = True
    
    def draw(self):
        """Dessine tous les éléments du jeu"""
        # Fond bleu ciel
        self.screen.fill(BLUE)
        
        # Dessiner les platefmes
        for platform in self.level.get_platforms():
            pygame.draw.rect(self.screen, GREEN, platform)
            pygame.draw.rect(self.screen, (0, 100, 0), platform, 3)
        
        # Dessiner les ennemis
        for enemy in self.level.get_enemies():
            enemy.draw(self.screen)
        
        # Dessiner les pièces
        for coin in self.level.get_coins():
            coin.draw(self.screen)
        
        # Dessiner le joueur
        self.player.draw(self.screen)
        
        # Interface utilisateur
        self.draw_ui()
        
        # Écrans spéciaux
        if self.paused:
            self.draw_pause_screen()
        elif self.game_over:
            self.draw_game_over_screen()
        elif self.level_complete:
            self.draw_level_complete_screen()
        
        pygame.display.flip()
    
    def draw_ui(self):
        """Dessine l'interface utilisateur"""
        font = pygame.font.Font(None, 36)
        
        # Score
        score_text = font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))
        
        # Niveau
        level_text = font.render(f"Niveau: {self.current_level}", True, WHITE)
        self.screen.blit(level_text, (SCREEN_WIDTH - 250, 10))
        
        # Instructions
        small_font = pygame.font.Font(None, 24)
        instructions = small_font.render("P: Pause | ESC: Quitter", True, WHITE)
        self.screen.blit(instructions, (10, SCREEN_HEIGHT - 30))
    
    def draw_pause_screen(self):
        """Dessine l'écran de pause"""
        font = pygame.font.Font(None, 72)
        pause_text = font.render("PAUSE", True, RED)
        text_rect = pause_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        
        # Semi-transparent overlay
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(128)
        overlay.fill(BLACK)
        self.screen.blit(overlay, (0, 0))
        self.screen.blit(pause_text, text_rect)
    
    def draw_game_over_screen(self):
        """Dessine l'écran de game over"""
        font = pygame.font.Font(None, 72)
        game_over_text = font.render("GAME OVER", True, RED)
        text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        
        small_font = pygame.font.Font(None, 36)
        restart_text = small_font.render("Appuyez sur R pour recommencer", True, YELLOW)
        restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
        
        # Semi-transparent overlay
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(200)
        overlay.fill(BLACK)
        self.screen.blit(overlay, (0, 0))
        self.screen.blit(game_over_text, text_rect)
        self.screen.blit(restart_text, restart_rect)
    
    def draw_level_complete_screen(self):
        """Dessine l'écran de fin de niveau"""
        font = pygame.font.Font(None, 72)
        complete_text = font.render("NIVEAU COMPLÉTÉ!", True, YELLOW)
        text_rect = complete_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        
        small_font = pygame.font.Font(None, 36)
        if self.current_level < 3:
            next_text = small_font.render("Appuyez sur une touche pour continuer...", True, YELLOW)
        else:
            next_text = small_font.render("Vous avez gagné! Appuyez sur R pour recommencer", True, YELLOW)
        next_rect = next_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
        
        # Semi-transparent overlay
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(200)
        overlay.fill(BLACK)
        self.screen.blit(overlay, (0, 0))
        self.screen.blit(complete_text, text_rect)
        self.screen.blit(next_text, next_rect)
        
        # Attendre une touche pour continuer
        if self.current_level < 3:
            keys = pygame.key.get_pressed()
            if any(keys):
                self.current_level += 1
                self.init_level()
    
    def run(self):
        """Boucle principale du jeu"""
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()

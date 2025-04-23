import pygame
import random
import time

# Initialisation de Pygame
pygame.init()

# Paramètres de l'écran
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Couleurs
BACKGROUND_COLOR = (0, 0, 0)
CIRCLE_COLORS = [(255, 0, 0)]  
TEXT_COLOR = (250, 250, 250)

# Variables de suivi
click_times = []
successful_clicks = 0
total_clicks = 0
total_circles = 0
circle_spawn_time = None
circle_position = None
circle_radius = 15
min_time_between_circles = 0.5  
max_time_between_circles = 1.5  
game_duration = 60  

# Horloge pour contrôler les FPS
clock = pygame.time.Clock()

# Fonction pour afficher du texte au centre de l'écran
def display_centered_text(message, y_offset, font_size, color=TEXT_COLOR):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(message, True, color)
    text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + y_offset))
    screen.blit(text_surface, text_rect)

# Fonction pour afficher un écran de démarrage
def start_screen():
    screen.fill(BACKGROUND_COLOR)
    display_centered_text("Préparez-vous!", -50, 48)
    display_centered_text("Le jeu commence dans:", 0, 36)
    pygame.display.flip()
    time.sleep(1)
    for i in range(3, 0, -1):
        screen.fill(BACKGROUND_COLOR)
        display_centered_text(str(i), 0, 100)
        pygame.display.flip()
        time.sleep(1)
    screen.fill(BACKGROUND_COLOR)
    pygame.display.flip()

# Fonction pour afficher un écran de fin
def end_screen():
    screen.fill(BACKGROUND_COLOR)
    display_centered_text("Temps écoulé!", -50, 48)
    display_centered_text("Calcul des résultats...", 0, 36)
    pygame.display.flip()
    time.sleep(2)

# Fonction pour afficher un cercle aléatoire
def show_random_circle():
    global circle_position, circle_spawn_time, total_circles
    color = random.choice(CIRCLE_COLORS)
    circle_position = (random.randint(circle_radius, SCREEN_WIDTH - circle_radius),
                       random.randint(circle_radius, SCREEN_HEIGHT - circle_radius))
    pygame.draw.circle(screen, color, circle_position, circle_radius)
    circle_spawn_time = time.time()
    total_circles += 1

# Affichage de l'écran de démarrage
start_screen()

# Début du jeu
start_time = time.time()

# Boucle principale du jeu
running = True
time_to_next_circle = random.uniform(min_time_between_circles, max_time_between_circles)
last_circle_time = time.time()

while running and (time.time() - start_time) < game_duration:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            total_clicks += 1  
            if circle_position:
                mouse_pos = pygame.mouse.get_pos()
                distance = pygame.math.Vector2(circle_position).distance_to(mouse_pos)
                if distance <= circle_radius:
                    click_time = time.time() - circle_spawn_time
                    click_times.append(click_time)
                    successful_clicks += 1
                    circle_position = None 
                    screen.fill(BACKGROUND_COLOR) 

    # Afficher un nouveau cercle après un délai aléatoire
    if not circle_position and (time.time() - last_circle_time) > time_to_next_circle:
        show_random_circle()
        last_circle_time = time.time()
        time_to_next_circle = random.uniform(min_time_between_circles, max_time_between_circles)

    pygame.display.flip()
    clock.tick(60)

# Écran de fin
end_screen()

# Calcul de la moyenne des temps de réaction
average_time = sum(click_times) / len(click_times) if click_times else 0

# Affichage des résultats
screen.fill(BACKGROUND_COLOR)
display_centered_text(f"Temps de réaction moyen : {average_time:.3f} secondes", -25, 36)
display_centered_text(f"Clics réussis : {successful_clicks} / {total_clicks}", 25, 36)

pygame.display.flip()

# Attendre avant de quitter
time.sleep(10)

pygame.quit()

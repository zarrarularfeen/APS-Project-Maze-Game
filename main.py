import pygame
import sys
import time

pygame.init()

# Constants
BUTTON_WIDTH = 100
BUTTON_HEIGHT = 50
WIDTH, HEIGHT = 1142, 660
FPS = 120
CELL_SIZE = 20
BLACK = (0, 0, 0)
DARKGRAY = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)


maze_dict = {
    "easy_maze": [
        "S********************",
        "* *       *     * * *",
        "* ***** ***** *** * *",
        "*   *   *   *       *",
        "* ***** * ******* * *",
        "*               * * *",
        "* *** * ******* * ***",
        "*   * *     *     * *",
        "*** * * * * *** *** *",
        "*   * * * *   * *   *",
        "***** * *** * * *** *",
        "*     * * * * * * * *",
        "***** *** * *** * * *",
        "*   * *   * *       *",
        "* *** *** * * *** ***",
        "*     *       *     *",
        "* ******* * *********",
        "*   *   * * * * *   *",
        "***** *** *** * * ***",
        "*                  E*",
        "*********************"
    ],
    "medium_maze": [
        "***************************************************",
        "S     *   *     *   *     *   * *     * *     *   *",
        "* * *** ***** ***** * * *** * * *** *** * *** *** *",
        "* * * *   *         * *   * * *     * *     * *   *",
        "* *** * *** ******* * *** *** ***** * * ***** *** *",
        "* *   *     *   * * *   *     *             *     *",
        "* * *********** * * *** ********* * * * *** ***** *",
        "*         *                       * * *   *     * *",
        "* * ***** ***** ******* ********* *** *** ******* *",
        "* * * *   *   *       * *         * * *   * *     *",
        "* *** *** * * *** *** *********** * *** *** *** ***",
        "* *   * *   * * *   *     *   * * * *     *       *",
        "* *** * ***** * ***** ***** *** *** *     *       *",
        "*   *                 *       * * *       *   *   *",
        "***** *** *** ***** ******* *** * * * *** * *** * *",
        "* *     * *   *   *         * * * * * * * *     * *",
        "* *** *** * ***** * *** ***** * * ***** * *** * * *",
        "*     *   *     * * * * * *   *         *     * * *",
        "* *********** *** * * * * * * ***** * *********** *",
        "* *   *     *   *   *       * * *   *     *   *   *",
        "* * *** *** *********** ******* *** * * *** *** ***",
        "*   *   *           *       *       * *       *   *",
        "*** * *** ******* *** * * ***** *** * * ***** * ***",
        "* * *   *   *     * * * * *     *   * *   *     * *",
        "* * ************* * ******* *** * *** * *** * *** *",
        "*   *     * *   *     *   * *   * *     *   *     *",
        "* * *** * * * ***** *** * *** *** *** *** * * * * *",
        "* *     *   * * *     *     * *   * *   * * * * * *",
        "* ******* *** *** *** *** ***** * *** ******* *** *",
        "*       *         *   *   * *   * *   *       *   *",
        "*** * ********* * ******* * * * * * *********** * *",
        "*   *   * *   * *         * *   * *   *   *   * *E*",
        "***************************************************",
        "*       *   * * *     * *     *   * * *   *     * *",
        "* ******* ***** *** ******* *** * *** * *** * *** * *",
        "* *     *     *           * * * *           * *   *",
        "* *** *** ******* ******* *** * * *** * ***********",
        "*  *      *             *  *                     E*",
        "***************************************************"
    ],
    "hard_maze": [
        "*********************************************************",
        "S *   *   *                 *   *   *             * *   *",
        "* * * * * * *** * ***** * *** *** * * *** ***** * * *** *",
        "*   * * *     * * *     * * *     *     * * * * * *     *",
        "* * ********* ***** * * *** * *** * * * *** * ******* * *",
        "* *             * * * *         * * * * *             * *",
        "********* *** * * * * *** ***** *** ***************** ***",
        "* *       *   *   * * * * *   * *       *       * *   * *",
        "* *** ********* *** *** * * * *** * ********* * * *** * *",
        "*     *         *     * *   * * * * * *   *   *         *",
        "* *** *** *** *** ***** *** *** *** * * *** *********** *",
        "*   * *     *   *       *   * *     * *       * *     * *",
        "* * * *** ******* ***** ***** * *** * * *** *** *** *** *",
        "* * * * * * *   *     *     * * * *   *   * * *   *     *",
        "* ***** * * * *** ***** *** * *** *** * * * * * ***** * *",
        "*   *   * * * * *   * *   *   * * *   * * * * * *   * * *",
        "*** * ***** * * * *** * * *** * * * *** ***** * * ***** *",
        "*       *         * *   * *     *     *       *   * * * *",
        "*** * *** ***** * * * *** *** *** ******* *** *** * * * *",
        "*   *   * *     *   *   * * * *       *   * *     *     *",
        "******* ********* *** *** * *** * * ******* *** ******* *",
        "*   * *         *   * *   * * * * *     *   *   *       *",
        "* *** ******* ********* *** * *** * * * *** * ***** *** *",
        "* * *   *     *   * *       * *   * * *   *     * * *   *",
        "* * * ***** *** *** * ******* ***** ***** * * * * * *** *",
        "* * *         *       * *     * * *   * *   * * * * *   *",
        "* * * ******* ******* * * *** * * ***** ***** *** *** * *",
        "*       *     * * * * * * *     *         *     * *   * *",
        "* ***** *** * * * * * * * ********* * * * *** * * * * ***",
        "* *   * *   *   *       * * *     * * * *     *   * *   *",
        "* * *** *** ***** * *** * * *** * ***** *** ********* ***",
        "* *   * *     * * * *   *   *   * * *   *              E*",
        "*********************************************************",
    ]
}

# Initializing the maze to start at easy level
maze = maze_dict["easy_maze"]

# Player starting position [x, y]
player_pos = [1, 1]

# Loading fonts
font = pygame.font.Font(None, 36)

# Loading the player image for animation
object_image = pygame.image.load("player.png")
object_image = pygame.transform.scale(object_image, (50, 50))  # Resizing the image to 50 by 50.

# Loading player image
player_image = pygame.image.load("player 2.png")
player_image = pygame.transform.scale(player_image, (CELL_SIZE, CELL_SIZE))  # Resize the image to match the cell size

# Loading background image
background_image = pygame.image.load("test.jpg")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Load background sound effect
pygame.mixer.init()
background_sound = pygame.mixer.Sound("background music.mp3")
# Set the volume to 20%
background_sound.set_volume(0.2)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Runner")
clock = pygame.time.Clock()

def animate(x, y, frame):
    if frame > 0:

        # Clear the screen
        screen.fill(BLACK)

        # Display "Loading..." text
        text = font.render("Loading...", True, WHITE)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT - 50))
        screen.blit(text, text_rect)

        # Draw the object at the current position
        screen.blit(object_image, (x, y))

        # Refreshing display
        pygame.display.flip()

        # Frame rate
        pygame.time.delay(50)

        # Call the function recursively with updated parameters
        animate(x + 5, y, frame - 1)


def draw_maze():
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == "*":
                pygame.draw.rect(screen, DARKGRAY, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif cell == "S":
                pygame.draw.rect(screen, RED, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif cell == "E":
                pygame.draw.rect(screen, (0, 255, 0), (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))


def draw_player():
    screen.blit(player_image, (player_pos[0] * CELL_SIZE, player_pos[1] * CELL_SIZE))

# Create the welcome screen window
welcome_screen = pygame.display.set_mode((WIDTH, HEIGHT))

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

def draw_buttons():
    start_button = pygame.Rect(WIDTH // 2 - BUTTON_WIDTH // 2, HEIGHT // 2 - BUTTON_HEIGHT // 2, BUTTON_WIDTH, BUTTON_HEIGHT)
    quit_button = pygame.Rect(WIDTH // 2 - BUTTON_WIDTH // 2, HEIGHT // 2 - BUTTON_HEIGHT // 2 + 70, BUTTON_WIDTH, BUTTON_HEIGHT)

    pygame.draw.rect(welcome_screen, WHITE, start_button)
    pygame.draw.rect(welcome_screen, WHITE, quit_button)

    draw_text('Start', font, BLACK, welcome_screen, WIDTH // 2, HEIGHT // 2 - BUTTON_HEIGHT // 2 + 25)
    draw_text('Quit', font, BLACK, welcome_screen, WIDTH // 2, HEIGHT // 2 - BUTTON_HEIGHT // 2 + 95)

    return start_button, quit_button

animate(WIDTH//3, HEIGHT//2, 50) # Call the recursive animation function with parameters

# Game loop for the welcome screen
running = True
welcome_running = True
while welcome_running:
    welcome_screen.fill(BLACK)

    draw_text('Welcome to the Maze Runner!', font, WHITE, welcome_screen, WIDTH // 2, HEIGHT // 2 - BUTTON_HEIGHT // 2 - 70)

    start_button, quit_button = draw_buttons()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            welcome_running = False
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if start_button.collidepoint(mouse_pos):
                welcome_running = False
            elif quit_button.collidepoint(mouse_pos):
                welcome_running = False
                running = False

    pygame.display.flip()

# Game loop for the game
current_level = "easy"
completion_timer = 0  # Timer to control how long the completion message is displayed
completion_duration = 3  # Duration to display the completion message in seconds
while running:
    background_sound.play()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and maze[player_pos[1] - 1][player_pos[0]] != "*":
                player_pos[1] -= 1
            if event.key == pygame.K_s and maze[player_pos[1] + 1][player_pos[0]] != "*":
                player_pos[1] += 1
            if event.key == pygame.K_a and maze[player_pos[1]][player_pos[0] - 1] != "*":
                player_pos[0] -= 1
            if event.key == pygame.K_d and maze[player_pos[1]][player_pos[0] + 1] != "*":
                player_pos[0] += 1

    screen.blit(background_image, (0, 0))  # Draw the background image
    draw_maze()
    draw_player()

    # Check if the player reached the endpoint in the current maze
    if maze[player_pos[1]][player_pos[0]] == "E":
        # Display a message based on the current level
        if current_level == "easy":
            current_level = "medium"
            maze = maze_dict["medium_maze"]
            player_pos = [1, 1]  # Reset player position for the new level
            completion_timer = time.time()  # Start the completion message timer

        elif current_level == "medium":
            current_level = "hard"
            maze = maze_dict["hard_maze"]
            player_pos = [1, 1]  # Reset player position for the new level
            completion_timer = time.time()  # Start the completion message timer

        elif current_level == "hard":
            running = False  # End the game after completing the hard level
            completion_timer = time.time()  # Start the completion message timer

    # Display the congratulatory message when the timer is active
    if completion_timer > 0:
        rect_width, rect_height = 2000, 50
        rect = pygame.Rect((WIDTH - rect_width) // 2, (HEIGHT - rect_height) // 2, rect_width, rect_height)
        pygame.draw.rect(screen, (255, 255, 255), rect)

        if current_level == "medium":
            text = font.render("Congratulations! You completed the easy level.", True, (0, 0, 0))
        elif current_level == "hard":
            text = font.render("Congratulations! You completed the medium level.", True, (0, 0, 0))
        else:
            text = font.render("Congratulations! You completed the game.", True, (0, 0, 0))
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)

        # Check if the completion duration has elapsed
        if time.time() - completion_timer >= completion_duration:
            completion_timer = 0  # Reset the completion message timer

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()

import pygame
import sys
import subprocess
from button import Button
pygame.init()
pygame.mixer.init()
SCREEN = pygame.display.set_mode((900, 830))
pygame.display.set_caption("Menu")
BG = pygame.image.load("assets/tampilan awal/main menu.png")
PLAY_IMAGE = pygame.image.load("assets/tampilan awal/Play Rect.png")
CREDITS_IMAGE = pygame.image.load("assets/tampilan awal/play Rect.png")
QUIT_IMAGE = pygame.image.load("assets/tampilan awal/Quit Rect.png")
pygame.mixer.music.load("assets/sound/awal.mp3")
pygame.mixer.music.set_volume(0.4)  # volume suara
pygame.mixer.music.play(-1)  # 
def get_font(size):
    return pygame.font.Font("assets/tampilan awal/font.ttf", size)
def get_pac_font(size):
    return pygame.font.Font("assets/tampilan awal/PAC-font.ttf", size)
def play():
    pygame.mixer.music.pause()  # membuat backsound berhenti saat berpindah jendela
    try:
        process = subprocess.Popen(["python", "Pac-Animal.py"])  # pindah ke jendela pac animal.py
        process.wait()  # Wait for the process to complete
    except subprocess.CalledProcessError as e:
        print(f"Error running Pac-Animal.py: {e}")
    finally:
        pygame.mixer.music.unpause()  # 
        #pygame.quit()  # jendela menutup saat jendela pac animal di tutup
        #sys.exit()  

def credits():
    while True:
        CREDITS_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")

        CREDITS_TEXT = get_font(50).render("About", True, "white")
        CREDITS_RECT = CREDITS_TEXT.get_rect(center=(460, 100))
        SCREEN.blit(CREDITS_TEXT, CREDITS_RECT)
        CREDITS_TEXT1 = get_font(30).render("Game ini di buat sebagai ", True, "white")
        CREDITS_RECT1 = CREDITS_TEXT1.get_rect(center=(450, 250))
        SCREEN.blit(CREDITS_TEXT1, CREDITS_RECT1)
        CREDITS_TEXT2 = get_font(30).render("syarat untuk mengikuti ", True, "white")
        CREDITS_RECT2 = CREDITS_TEXT2.get_rect(center=(450, 300))
        SCREEN.blit(CREDITS_TEXT2, CREDITS_RECT2)
        CREDITS_TEXT3 = get_font(30).render(" Praktek kerja lapangan ", True, "white")
        CREDITS_RECT3 = CREDITS_TEXT3.get_rect(center=(450, 350))
        SCREEN.blit(CREDITS_TEXT3, CREDITS_RECT3)

        CREDITS_BACK = Button(image=None, pos=(450, 450), 
                            text_input="BACK", font=get_font(25), base_color="white", hovering_color="grey")

        CREDITS_BACK.changeColor(CREDITS_MOUSE_POS)
        CREDITS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CREDITS_BACK.checkForInput(CREDITS_MOUSE_POS):
                    return  # 

        pygame.display.update()

# Main menu
def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_pac_font(80).render("pAc AnImAl", True, "white")  
        MENU_RECT = MENU_TEXT.get_rect(center=(450, 100))

        PLAY_BUTTON = Button(image=PLAY_IMAGE, pos=(450, 250), 
                            text_input="PLAY", font=get_font(60), base_color="#ded4fc", hovering_color="White")
        CREDITS_BUTTON = Button(image=CREDITS_IMAGE, pos=(450, 400), 
                            text_input="ABOUT", font=get_font(60), base_color="#ded4fc", hovering_color="White")
        QUIT_BUTTON = Button(image=QUIT_IMAGE, pos=(450, 550), 
                            text_input="QUIT", font=get_font(60), base_color="#ded4fc", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, CREDITS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if CREDITS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    credits()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

if __name__ == "__main__":
    main_menu()

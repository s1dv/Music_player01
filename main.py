import os
#ignore pygame message annoying
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame

#main function
def main():

    try:
        pygame.mixer.init()
    except pygame.error as e:
        print("audio initialization error", e)

if __name__ == "__main__":
    main()

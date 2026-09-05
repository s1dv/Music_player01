import os
#ignore pygame message annoying
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame

def play_music(folder, song_name):

    file_path = os.path.join(folder, song_name)  #concatinating path

    if not os.path.exists(file_path):   #if not in dir
        print("file not found")
        return

    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    print(f"\nNow PLAYING : {song_name}")
    print("commands [P]ause, [R]esume, [S]top")

    while True:

        command = input("> ").upper()

        if command == "P":
            pygame.mixer.music.pause()
            print("PAUSED!")

        elif command == "R":
            pygame.mixer.music.unpause()
            print("RESUMED")

        elif command == "S":
            pygame.mixer.music.stop()
            print(f"stopped playing {song_name}")
            return
        else:
            print("invalid option")

#main function
def main():

    try:
        pygame.mixer.init()
    except pygame.error as e:
        print("audio initialization error", e)

    folder = "music"

    if not os.path.isdir(folder):   #checking if the music folder is inside the root dir or not.
        print(f"folder '{folder}' not found!")
        return

    #checking mp3 files
    mp3_files = [file for file in os.listdir(folder) if file.endswith(".mp3")]

    #if not mp3 files.
    if not mp3_files:
        print(" no mp3 files found")

    while True:
        print("***** MP3 PLAYER *****")
        print("my song list : ")

        for index, song in enumerate(mp3_files, start=1):
            print(f"{index}. {song}")

        choice_input = input("choose the song you wanna play by typing s. number {enter Q to quit} :")

        if choice_input.upper() == "Q":
            print("bye!")
            break

        if not choice_input.isdigit():
            print("please enter a digit !")
            continue


        choice = int(choice_input) -1 #typecasting string choice into integer, -1 for index

        if 0<= choice <len(mp3_files):
            play_music(folder, mp3_files[choice])
        else:
            print("pls ENTER A VALID SONG NUMBER")




if __name__ == "__main__":
    main()

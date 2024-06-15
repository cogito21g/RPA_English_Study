# main.py
import os

def main():
    print("Select the script to run:")
    print("1. Create Audio")
    print("2. Create Video")

    choice = input("Enter the number of the script you want to run: ")

    if choice == "1":
        os.system("python create_audio.py")
    elif choice == "2":
        os.system("python video_creator.py")
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()

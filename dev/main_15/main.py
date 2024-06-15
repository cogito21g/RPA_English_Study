# main.py
import os

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))

    while True:
        print("Select the script to run:")
        print("1. Create Audio")
        print("2. Create Video")
        print("Type 'exit' to quit.")

        choice = input("Enter the number of the script you want to run: ")

        if choice.lower() == 'exit':
            break

        if choice == "1":
            script_path = os.path.join(current_dir, "create_audio.py")
            os.system(f"python \"{script_path}\"")
        elif choice == "2":
            script_path = os.path.join(current_dir, "video_creator.py")
            os.system(f"python \"{script_path}\"")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

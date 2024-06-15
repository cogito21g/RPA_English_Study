import subprocess

def run_script(script_name):
    try:
        subprocess.run(["python", script_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running {script_name}: {e}")

def main():
    while True:
        print("\nSelect the script to run or type 'exit' to quit:")
        print("1. create_audio.py")
        print("2. create_video.py")
        choice = input("Enter 1, 2, or 'exit': ")

        if choice == '1':
            run_script("create_audio.py")
        elif choice == '2':
            run_script("create_video.py")
        elif choice.lower() == 'exit':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 'exit'.")

if __name__ == "__main__":
    main()

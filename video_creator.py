# video_creator.py
import os
from moviepy.editor import ImageClip, AudioFileClip
from datetime import datetime

def create_video_with_audio(image_path, audio_file, output_dir, log_file):
    # Load the image
    image_clip = ImageClip(image_path).set_duration(1)  # Default duration of 1 second

    # Load the audio file
    audio_clip = AudioFileClip(audio_file)

    # Set the duration of the image to match the audio
    img_clip_with_audio = image_clip.set_duration(audio_clip.duration).set_audio(audio_clip)

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Create the output file path
    audio_filename = os.path.splitext(os.path.basename(audio_file))[0]
    output_file_path = os.path.join(output_dir, f"{audio_filename}.mp4")

    # Check if the file already exists
    if not os.path.exists(output_file_path):
        # Write the result to a file
        img_clip_with_audio.write_videofile(output_file_path, codec='libx264', fps=24)
        log_message = f"Video created successfully: {output_file_path}"
    else:
        log_message = f"Video already exists: {output_file_path}"

    # Log the message
    with open(log_file, "a", encoding="utf-8") as log:
        log.write(f"{datetime.now()}: {log_message}\n")

    print(log_message)

def list_directories(path):
    return [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]

def main():
    image_path = "image1.png"  # Path to the image file
    base_dir = "output"  # Base directory containing the folders with audio files
    output_base_dir = "video_output"  # Base directory for video outputs
    log_dir = "logs"  # Directory for log files

    # Create log directory if it doesn't exist
    os.makedirs(log_dir, exist_ok=True)

    # Create log file path based on current date
    current_date = datetime.now().strftime("%Y-%m-%d")
    log_file = os.path.join(log_dir, f"log_{current_date}.log")

    while True:
        # List all directories in the base directory
        directories = list_directories(base_dir)
        if not directories:
            print("No directories found in the specified base directory.")
            return

        print("Available directories:")
        for idx, directory in enumerate(directories, start=1):
            print(f"{idx}. {directory}")

        selection = input("Enter the number of the directory to process (or 'exit' to quit): ")
        if selection.lower() == 'exit':
            return

        if not selection.isdigit() or int(selection) < 1 or int(selection) > len(directories):
            print("Invalid selection. Please try again.")
            continue

        selected_directory = directories[int(selection) - 1]
        audio_dir = os.path.join(base_dir, selected_directory)

        # List all audio files in the selected directory
        audio_files = []
        for root, _, files in os.walk(audio_dir):
            for file in files:
                if file.endswith(".mp3"):
                    audio_files.append(os.path.join(root, file))

        if not audio_files:
            print("No audio files found in the selected directory.")
        else:
            for audio_file in audio_files:
                # Determine the subdirectory within the output directory
                relative_dir = os.path.relpath(os.path.dirname(audio_file), audio_dir)
                output_dir = os.path.join(output_base_dir, relative_dir)

                create_video_with_audio(image_path, audio_file, output_dir, log_file)

if __name__ == "__main__":
    main()

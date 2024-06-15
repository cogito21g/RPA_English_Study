# video_creator.py
import os
from moviepy.editor import ImageClip, AudioFileClip

def create_video_with_audio(image_path, audio_file, output_dir):
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
        print(f"Video created successfully: {output_file_path}")
    else:
        print(f"Video already exists: {output_file_path}")

if __name__ == "__main__":
    image_path = "image1.png"  # Path to the image file
    audio_dir = "output"  # Directory containing the audio files
    output_base_dir = "video_output"  # Base directory for video outputs

    # List all audio files in the directory
    audio_files = []
    for root, _, files in os.walk(audio_dir):
        for file in files:
            if file.endswith(".mp3"):
                audio_files.append(os.path.join(root, file))

    if not audio_files:
        print("No audio files found in the specified directory.")
    else:
        for audio_file in audio_files:
            # Determine the subdirectory within the output directory
            relative_dir = os.path.relpath(os.path.dirname(audio_file), audio_dir)
            output_dir = os.path.join(output_base_dir, relative_dir)

            create_video_with_audio(image_path, audio_file, output_dir)

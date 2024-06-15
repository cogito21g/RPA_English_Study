# create_audio.py
import os
import shutil
from gtts import gTTS
from datetime import datetime
from pydub import AudioSegment

def log_message(log_file, message):
    with open(log_file, "a", encoding="utf-8") as log:
        log.write(f"{datetime.now()}: {message}\n")

def parse_input(text):
    articles = {}
    word_list = ""
    lines = text.strip().split("\n")
    current_topic_level = None
    current_title = None
    current_content = []
    for line in lines:
        if line.startswith("### "):
            if current_topic_level and current_title:
                articles[(current_topic_level, current_title)] = "\n".join(current_content).strip()
                current_content = []
            current_topic_level = line.replace("### ", "").strip()
        elif line.startswith("**Title: "):
            current_title = line.replace("**Title: ", "").replace("**", "").strip()
        elif line.startswith("```text"):
            continue
        elif line.startswith("```"):
            continue
        elif line.startswith("| 단어 ") or line.startswith("| ---"):
            continue
        elif line.startswith("| "):
            word_list += line + "\n"
        else:
            current_content.append(line)
    
    if current_topic_level and current_title:
        articles[(current_topic_level, current_title)] = "\n".join(current_content).strip()
    
    return articles, word_list.strip()

def save_articles(articles, word_list):
    current_date = datetime.now().strftime("%Y-%m-%d")
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, f"log_{current_date}.log")
    
    for idx, ((topic_level, title), text) in enumerate(articles.items(), start=1):
        split_topic_level = topic_level.split(": ")
        if len(split_topic_level) == 3:
            category, topic, level = split_topic_level
            base_dir = os.path.join("output", current_date, f"{category}_{topic}".replace(' ', '_').replace('-', '_'))
        else:
            error_message = f"Error: Unexpected format in topic_level: {topic_level}"
            print(error_message)
            log_message(log_file, error_message)
            continue

        os.makedirs(base_dir, exist_ok=True)
        
        file_name = f"{level}_{title.replace(' ', '_').replace('-', '_')}"
        
        text_file_path = os.path.join(base_dir, f"{file_name}.txt")
        with open(text_file_path, "a", encoding="utf-8") as file:
            file.write(text.strip() + "\n")
        log_message(log_file, f"Text file updated/created: {text_file_path}")
        
        audio_file_path = os.path.join(base_dir, f"{file_name}.mp3")
        if not os.path.exists(audio_file_path):
            tts = gTTS(text=text.strip(), lang='en')
            tts.save(audio_file_path)
            log_message(log_file, f"Audio file created: {audio_file_path}")
        else:
            log_message(log_file, f"Audio file already exists: {audio_file_path}")

        print(f"Processed {idx}/{len(articles)}: {topic_level} - {title}")

    if word_list:
        word_list_path = os.path.join(base_dir, f"word_list_{topic.replace(' ', '_').replace('-', '_')}.txt")
        with open(word_list_path, "a", encoding="utf-8") as file:
            file.write(word_list + "\n")
        log_message(log_file, f"Word list file updated/created: {word_list_path}")
        
        word_audio_path = os.path.join(base_dir, f"word_list_{topic.replace(' ', '_').replace('-', '_')}.mp3")
        if not os.path.exists(word_audio_path):
            word_lines = word_list.split("\n")
            combined_audio = AudioSegment.silent(duration=1000)
            for line in word_lines:
                word = line.split("|")[1].strip()
                tts = gTTS(text=word, lang='en')
                temp_audio_path = "temp.mp3"
                tts.save(temp_audio_path)
                word_audio = AudioSegment.from_file(temp_audio_path)
                combined_audio += word_audio + AudioSegment.silent(duration=1000)
                os.remove(temp_audio_path)
            
            combined_audio.export(word_audio_path, format="mp3")
            log_message(log_file, f"Word list audio created: {word_audio_path}")
        else:
            log_message(log_file, f"Word list audio already exists: {word_audio_path}")

        print("Word list and audio have been successfully created.")

def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        return None

def move_files_to_source():
    source_dir = "source"
    if not os.path.exists(source_dir):
        os.makedirs(source_dir)

    for file in os.listdir():
        if file.endswith(".txt"):
            shutil.move(file, source_dir)

def list_files_in_source():
    source_dir = "source"
    files = [f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f))]
    return files

def main():
    move_files_to_source()
    
    while True:
        source_files = list_files_in_source()
        
        if not source_files:
            print("No text files found in the source directory.")
            break
        
        print("Available files:")
        for idx, file in enumerate(source_files, start=1):
            print(f"{idx}. {file}")
        
        selection = input("Enter the numbers or names of the files to process (comma separated, or type 'exit' to quit): ")
        if selection.lower() == 'exit':
            break
        
        selected_files = []
        selections = selection.split(',')
        for sel in selections:
            sel = sel.strip()
            if sel.isdigit() and 1 <= int(sel) <= len(source_files):
                selected_files.append(source_files[int(sel) - 1])
            elif sel in source_files:
                selected_files.append(sel)
            else:
                print(f"Invalid selection: {sel}")
        
        if not selected_files:
            print("No valid files selected. Please try again.")
            continue
        
        for selected_file in selected_files:
            file_path = os.path.join("source", selected_file)
            user_input = read_file(file_path)
            if user_input:
                articles, word_list = parse_input(user_input)
                save_articles(articles, word_list)

if __name__ == "__main__":
    main()

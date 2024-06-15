import os
from gtts import gTTS
from datetime import datetime

def parse_input(text):
    articles = {}
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
        else:
            current_content.append(line)
    
    if current_topic_level and current_title:
        articles[(current_topic_level, current_title)] = "\n".join(current_content).strip()
    
    return articles

def save_articles(articles):
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    for idx, ((topic_level, title), text) in enumerate(articles.items(), start=1):
        # Split topic and level correctly even if the topic contains ": "
        split_topic_level = topic_level.split(": ")
        if len(split_topic_level) == 3:
            category, topic, level = split_topic_level
            base_dir = os.path.join("output", current_date, f"{category}_{topic}".replace(' ', '_').replace('-', '_'))
        else:
            print(f"Error: Unexpected format in topic_level: {topic_level}")
            continue

        os.makedirs(base_dir, exist_ok=True)
        
        file_name = f"{level}_{title.replace(' ', '_').replace('-', '_')}"
        
        # Save text file
        text_file_path = os.path.join(base_dir, f"{file_name}.txt")
        if not os.path.exists(text_file_path):
            with open(text_file_path, "w", encoding="utf-8") as file:
                file.write(text.strip())
        
        # Save audio file
        audio_file_path = os.path.join(base_dir, f"{file_name}.mp3")
        if not os.path.exists(audio_file_path):
            tts = gTTS(text=text.strip(), lang='en')
            tts.save(audio_file_path)

        print(f"Processed {idx}/{len(articles)}: {topic_level} - {title}")

    print("All files have been successfully created and saved.")

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

# Example usage
if __name__ == "__main__":
    file_path = "test.txt"  # 여기에 입력 파일 경로를 설정하세요
    user_input = read_file(file_path)
    articles = parse_input(user_input)
    save_articles(articles)

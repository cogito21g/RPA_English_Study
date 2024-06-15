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

# Example usage with user input
if __name__ == "__main__":
    user_input = """
### 소설: 꿈: 초급

**Title: Emily's Magical Dream**

```text
Emily loved to dream. Every night, she closed her eyes and entered a world of magic. One night, she dreamed of a beautiful garden filled with colorful flowers and sparkling streams. In the garden, she met a friendly butterfly who guided her through the enchanted place. Emily felt happy and free as she explored. When she woke up, she smiled, remembering her magical adventure. She knew that in her dreams, anything was possible.
```

### 소설: 꿈: 중급

**Title: The Dreamer's Journey**

```text
Emily had always been fascinated by the world of dreams. Each night, she looked forward to the moment when she could escape reality and explore the landscapes of her imagination. One evening, after a particularly tiring day, Emily fell into a deep sleep. She found herself standing at the edge of a vast forest bathed in the golden light of a setting sun. The trees were unlike any she had seen before, their leaves shimmering with hues of blue and purple.

As she ventured deeper into the forest, she encountered a wise old owl who spoke to her in a gentle voice. "Welcome, Emily. This is the Dreamwood, a place where your deepest thoughts and desires take form." Emily felt a sense of awe and curiosity. She followed the owl through the forest, discovering hidden glades and secret paths. Along the way, she met various dream creatures who shared their wisdom and stories with her.

Emily learned that the Dreamwood was a reflection of her inner self, a place where she could confront her fears and embrace her hopes. When she awoke the next morning, she felt rejuvenated and inspired. Her journey through the Dreamwood had taught her the power of dreams and the importance of staying true to oneself.
```

### 소설: 꿈: 고급

**Title: The Dream Weaver's Legacy**

```text
Emily had long been captivated by the mysteries of the dream world. From a young age, she possessed an uncanny ability to recall her dreams in vivid detail. Each night, as she drifted into slumber, she would embark on fantastical adventures that felt more real than her waking life. One fateful night, Emily found herself in a realm unlike any she had previously encountered. The sky was painted in swirling shades of pink and gold, and the air was filled with the scent of blooming jasmine.

As she wandered through this ethereal landscape, Emily came upon an ancient, ivy-covered archway. Intrigued, she stepped through and found herself in a grand library filled with countless books. An old man with kind eyes and a flowing beard greeted her. "I am the Dream Weaver," he said. "This library contains the dreams of every soul, past, present, and future."

The Dream Weaver explained that Emily had a unique gift: the ability to navigate and shape her dreams with conscious intent. He offered to teach her the ancient art of dream weaving, a skill that allowed one to influence their dreams and, by extension, their reality. Under his tutelage, Emily learned to craft intricate dreamscapes, harnessing the power of her imagination to explore the deepest corners of her psyche.

Through her training, Emily discovered that dreams were more than mere figments of the mind; they were a bridge to the subconscious, a way to understand and heal one's innermost wounds. She faced her darkest fears and insecurities, transforming them into sources of strength and wisdom. Her journeys in the dream world brought her profound insights, which she carried into her waking life.

As the years passed, Emily became a master dream weaver. She used her abilities to help others, guiding them through their own dream journeys and helping them uncover their hidden potential. The legacy of the Dream Weaver lived on through her, a testament to the enduring power of dreams and the limitless possibilities they hold. Emily's story became a beacon of hope, inspiring others to embrace the magic within their dreams and realize their true potential.
"""
    articles = parse_input(user_input)
    save_articles(articles)
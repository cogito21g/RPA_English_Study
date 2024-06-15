import os
from gtts import gTTS
from datetime import datetime

def parse_input(text):
    articles = {}
    lines = text.strip().split("\n")
    current_level = None
    current_content = []
    for line in lines:
        if line.startswith("### "):
            if current_level:
                articles[current_level] = "\n".join(current_content).strip()
                current_content = []
            current_level = line.replace("### ", "").strip()
        elif line.startswith("**Title: "):
            continue
        elif line.startswith("```text"):
            continue
        elif line.startswith("```"):
            continue
        else:
            current_content.append(line)
    
    if current_level:
        articles[current_level] = "\n".join(current_content).strip()
    
    return articles

def save_articles(articles):
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    for idx, (topic_level, text) in enumerate(articles.items(), start=1):
        # Split topic and level correctly even if the topic contains ": "
        split_topic_level = topic_level.split(": ")
        if len(split_topic_level) == 3:
            category, topic, level = split_topic_level
            base_dir = os.path.join("output", current_date, f"{category}_{topic}".replace(' ', '_').replace('-', '_'))
        else:
            print(f"Error: Unexpected format in topic_level: {topic_level}")
            continue

        os.makedirs(base_dir, exist_ok=True)
        
        file_name = f"{level}_{topic.replace(' ', '_').replace('-', '_')}"
        
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

        print(f"Processed {idx}/{len(articles)}: {topic_level}")

    print("All files have been successfully created and saved.")

# Example usage with user input
if __name__ == "__main__":
    user_input = """
### 뉴스 기사: 최근 글로벌 경제 동향: 초급

**Title: Global Economy Today**

```text
The global economy is changing. Many countries are seeing growth in technology and services. Some countries are also facing challenges like inflation and unemployment. Governments are working hard to balance growth and stability. Trade between nations is increasing, helping some economies to recover faster. People are hopeful for a better future as new opportunities arise. Overall, the world economy is slowly improving, but there are still many obstacles to overcome.
```

### 뉴스 기사: 최근 글로벌 경제 동향: 중급

**Title: Current Trends in the Global Economy**

```text
The global economy has experienced significant shifts in recent months. Technological advancements and a resurgence in the services sector have fueled growth in many regions. However, challenges such as rising inflation rates and persistent unemployment continue to pose threats to economic stability. Governments worldwide are implementing policies to address these issues, striving to strike a balance between fostering growth and maintaining stability.

International trade has seen a notable increase, with many countries lifting restrictions and promoting cross-border commerce. This has led to a faster recovery for some economies, particularly those heavily reliant on exports. Despite these positive trends, the global economic landscape remains fragile. Supply chain disruptions, geopolitical tensions, and environmental concerns add layers of complexity to the recovery process.

Overall, while the global economy is on a path to recovery, the pace is uneven, and uncertainties remain. Policymakers and businesses must remain vigilant and adaptable to navigate the ongoing challenges and seize new opportunities as they emerge.
```

### 뉴스 기사: 최근 글로벌 경제 동향: 고급

**Title: Navigating the Complexities of the Current Global Economy**

```text
In recent months, the global economy has undergone a series of transformative changes, driven by both advancements and adversities. Technological innovation continues to be a primary catalyst for growth, particularly in sectors such as information technology, healthcare, and renewable energy. The services sector, having rebounded from pandemic-induced contractions, is now experiencing robust expansion in various regions.

Despite these positive developments, the global economy faces significant headwinds. Inflationary pressures are mounting, exacerbated by supply chain bottlenecks and rising energy costs. Central banks are responding with a mix of monetary tightening and cautious optimism, seeking to curb inflation without stifling growth. Unemployment, although declining in some areas, remains a persistent issue, particularly in economies that have been slower to recover from the pandemic's impact.

Trade dynamics are also evolving. The relaxation of trade barriers and the resumption of international travel have reinvigorated global commerce. However, geopolitical tensions, particularly between major powers, pose risks to trade stability. Environmental concerns, highlighted by the increasing frequency of extreme weather events, are prompting a reevaluation of economic practices and policies.

Moreover, the global economic recovery is marked by stark disparities. Advanced economies are generally recovering at a faster pace due to higher vaccination rates and substantial fiscal support. In contrast, many developing nations are grappling with slower vaccine rollouts and limited economic stimulus options, leading to a more protracted recovery period.

In conclusion, while there are clear signs of recovery and growth in the global economy, it is a landscape fraught with uncertainties. Policymakers, businesses, and international organizations must collaborate closely to address these challenges, foster sustainable growth, and ensure that the benefits of economic recovery are equitably distributed across all nations.
```

### 단어장 (고급 지문 기준)

| 단어                | 뜻                                  | 예문                                                              |
|---------------------|-------------------------------------|-----------------------------------------------------------------|
| transformative      | 변화의, 변혁의                       | The global economy has undergone a series of transformative changes. |
| catalyst            | 촉매제, 기폭제                       | Technological innovation is a primary catalyst for growth.     |
| robust              | 강건한, 활발한                       | The services sector is experiencing robust expansion.          |
| headwinds           | 역풍, 방해 요소                      | The global economy faces significant headwinds.                |
| inflationary        | 인플레이션의, 물가 상승의            | Inflationary pressures are mounting globally.                  |
| bottlenecks         | 병목 현상                            | Supply chain bottlenecks are exacerbating inflation.           |
| monetary tightening | 통화 긴축                           | Central banks are responding with monetary tightening.         |
| stifling            | 억제하는, 질식시키는                 | Measures are taken to curb inflation without stifling growth.  |
| disparities         | 격차, 차이                           | The recovery is marked by stark disparities between economies. |
| protracted          | 오래 끄는, 지연된                    | Developing nations are facing a more protracted recovery period. |

다른 지문 종류나 주제를 원하시면 말씀해주세요!

"""
    articles = parse_input(user_input)
    save_articles(articles)

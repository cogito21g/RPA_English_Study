import os
from gtts import gTTS
from datetime import datetime

# Function to save articles as text and audio files with date-based folders
def save_articles(articles):
    # Get current date
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    base_dir = os.path.join("output", current_date)
    text_dir = os.path.join(base_dir, "text_files")
    audio_dir = os.path.join(base_dir, "audio_files")
    os.makedirs(text_dir, exist_ok=True)
    os.makedirs(audio_dir, exist_ok=True)

    total_articles = len(articles)
    print(f"Starting to process {total_articles} articles...")

    for idx, (title, text) in enumerate(articles.items(), start=1):
        # Extract level and create appropriate file names
        level = title.split(" - ")[1]
        file_name = f"{level}_{title.replace(' ', '_').replace('-', '_')}"
        
        # Save text file
        text_file_path = os.path.join(text_dir, f"{file_name}.txt")
        if not os.path.exists(text_file_path):
            with open(text_file_path, "w", encoding="utf-8") as file:
                file.write(text.strip())
        
        # Save audio file
        audio_file_path = os.path.join(audio_dir, f"{file_name}.mp3")
        if not os.path.exists(audio_file_path):
            tts = gTTS(text=text.strip(), lang='en')
            tts.save(audio_file_path)

        print(f"Processed {idx}/{total_articles}: {title}")

    print("All files have been successfully created and saved.")

# Example usage with the provided articles
articles = {
    "Global Economy Today - 초급": """
The global economy is changing. Many countries are seeing growth in technology and services. Some countries are also facing challenges like inflation and unemployment. Governments are working hard to balance growth and stability. Trade between nations is increasing, helping some economies to recover faster. People are hopeful for a better future as new opportunities arise. Overall, the world economy is slowly improving, but there are still many obstacles to overcome.
    """,
    "Current Trends in the Global Economy - 중급": """
The global economy has experienced significant shifts in recent months. Technological advancements and a resurgence in the services sector have fueled growth in many regions. However, challenges such as rising inflation rates and persistent unemployment continue to pose threats to economic stability. Governments worldwide are implementing policies to address these issues, striving to strike a balance between fostering growth and maintaining stability.

International trade has seen a notable increase, with many countries lifting restrictions and promoting cross-border commerce. This has led to a faster recovery for some economies, particularly those heavily reliant on exports. Despite these positive trends, the global economic landscape remains fragile. Supply chain disruptions, geopolitical tensions, and environmental concerns add layers of complexity to the recovery process.

Overall, while the global economy is on a path to recovery, the pace is uneven, and uncertainties remain. Policymakers and businesses must remain vigilant and adaptable to navigate the ongoing challenges and seize new opportunities as they emerge.
    """,
    "Navigating the Complexities of the Current Global Economy - 고급": """
In recent months, the global economy has undergone a series of transformative changes, driven by both advancements and adversities. Technological innovation continues to be a primary catalyst for growth, particularly in sectors such as information technology, healthcare, and renewable energy. The services sector, having rebounded from pandemic-induced contractions, is now experiencing robust expansion in various regions.

Despite these positive developments, the global economy faces significant headwinds. Inflationary pressures are mounting, exacerbated by supply chain bottlenecks and rising energy costs. Central banks are responding with a mix of monetary tightening and cautious optimism, seeking to curb inflation without stifling growth. Unemployment, although declining in some areas, remains a persistent issue, particularly in economies that have been slower to recover from the pandemic's impact.

Trade dynamics are also evolving. The relaxation of trade barriers and the resumption of international travel have reinvigorated global commerce. However, geopolitical tensions, particularly between major powers, pose risks to trade stability. Environmental concerns, highlighted by the increasing frequency of extreme weather events, are prompting a reevaluation of economic practices and policies.

Moreover, the global economic recovery is marked by stark disparities. Advanced economies are generally recovering at a faster pace due to higher vaccination rates and substantial fiscal support. In contrast, many developing nations are grappling with slower vaccine rollouts and limited economic stimulus options, leading to a more protracted recovery period.

In conclusion, while there are clear signs of recovery and growth in the global economy, it is a landscape fraught with uncertainties. Policymakers, businesses, and international organizations must collaborate closely to address these challenges, foster sustainable growth, and ensure that the benefits of economic recovery are equitably distributed across all nations.
    """
}

save_articles(articles)

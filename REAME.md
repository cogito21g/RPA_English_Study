# RPA English Study

## Introduction
영어 스크립트 지문을 텍스트 파일과 오디오 파일로 자동 변환하는 프로그램입니다.

## 입력 형식

"""
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

"""

### 사용방법

1. 입력 형식에 맞는 text 파일 생성
2. 생성된 txt 파일을 source에 이동
3. 아래의 순서로 코드 실행

```bash
# 파일 실행
python main.py

```









- main_01.py
    - 위와 같은 형태에서 ###을 파일명(초급_제목)으로 사용

- main_02.py
    - Title을 기준으로 사용

- main_03.py
    - txt 파일을 읽어오도록 처리

- main_04.py
    - txt 파일명을 입력해서 처리

- main_05.py
    - source 폴더로 원본 텍스트 파일을 이동후 선택하도록 변경

- main_06.py
    - 여러개의 텍스트 파일을 ,(콤마)를 이용해서 동시에 선택할 수 있도록 변경

- main_07.py
    - 단어장 생성 추가, 단어는 1초 간격

- main_08.py
    - 백업

- main_09.py
    - 음성 폴더안의 파일들을 읽어. image1.png와 결합해 동영상 파일 생성

- main_10.py
    - 동영상 파일 중복 생성 방지

- main_11.py
    - 동영상 생성시 로그 기록 추가

- main_12.py
    - main_08.py에 로그 기능 추가
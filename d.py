import streamlit as st
st.set_page_config(
    page_title="독도 퀴즈",
    page_icon="🇰🇷",
    layout="centered"
)
st.title("독도 퀴즈")

# 배경 스타일 설정
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Nanum+Myeongjo:wght@700&display=swap');
    .stApp {
        background-color: #f0f8ff;
        background-image: linear-gradient(45deg, #f0f8ff 25%, #d7e3fc 75%);
    }
    .title {
        font-family: 'Nanum Myeongjo', serif;
        font-size: 3rem;
        text-align: center;
        color: #2c3e50;
    }
    .description {
        font-size: 1.2rem;
        text-align: center;
        color: #34495E;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.header(":gray[표어]")

st.snow()

# 제목
st.markdown('<h1 class="title"> 독도 지킴이 퀴즈 </h1>', unsafe_allow_html=True)

# 퀴즈 내용
st.markdown('<p class="text-color">독도에 관한 퀴즈를 풀어보세요!</p>', unsafe_allow_html=True)

# 질문 1
question_1 = st.radio(
    "독도 주변 해역에서 발견된 해조류는 총 몇 종일까요?",
    ("150종", "250종", "350종", "450종")
)

if question_1 == "250종":
    st.success("정답입니다! 독도 주변 해역에서 발견된 해조류는 약 250여종입니다.")
else:
    st.error("틀렸습니다. 정답은 '250종'입니다.")

# 질문 2
question_2 = st.radio(
    "독도에서 발견된 곤충의 주요 종 중 가장 많은 종류는 무엇일까요?",
    ("딱정벌레", "잠자리", "메뚜기", "나비")
)

if question_2 == "딱정벌레":
    st.success("정답입니다! 독도에서 발견된 곤충 중 딱정벌레가 15종으로 가장 많은 종을 차지합니다.")
else:
    st.error("틀렸습니다. 정답은 '딱정벌레'입니다.")

# 질문 3
question_3 = st.radio(
    "독도에서 번식하는 대표적인 조류는 무엇인가요?",
    ("괭이갈매기", "뿔쇠오리", "쇠가마우지", "매")
)

if question_3 == "괭이갈매기":
    st.success("정답입니다! 괭이갈매기는 독도에서 4월에서 6월 사이에 번식을 합니다.")
else:
    st.error("틀렸습니다. 정답은 '괭이갈매기'입니다.")

# 질문 4
question_4 = st.radio(
    "독도에서 자생하는 식물 중 어떤 식물이 포함되지 않나요?",
    ("개밀", "왕호장근", "초종용", "해송")
)

if question_4 == "해송":
    st.success("정답입니다! 해송은 독도의 자생식물이 아닙니다.")
else:
    st.error("틀렸습니다. 정답은 '해송'입니다.")

# 퀴즈 종료 메시지
st.markdown("### 퀴즈를 다 풀었습니다! 모든 답을 확인하고 독도에 대해 더 배워보세요.")

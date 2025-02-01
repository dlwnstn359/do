import streamlit as st
from PIL import Image

# 페이지 기본 설정
st.set_page_config(
    page_title="독도 지킴이",
    page_icon="🇰🇷",
    layout="centered"
)

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

# 제목
st.markdown('<h1 class="title">🇰🇷 독도, 대한민국의 자랑 🇰🇷</h1>', unsafe_allow_html=True)

# 소개글
st.markdown('<p class="description">독도는 대한민국의 동쪽 끝에 위치한 아름다운 섬입니다. 역사적, 지리적, 생태학적으로 중요한 가치를 지닌 독도를 알아보세요!</p>', unsafe_allow_html=True)


# 사용자 채팅 입력
st.text_input("💬 독도에 대해 하고 싶은 말을 남겨보세요!", placeholder="여기에 입력하세요...")


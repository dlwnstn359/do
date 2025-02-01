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
st.snow()
# 제목
st.title(' :gray[독도 지킴이] ')

# 소개글
st.markdown(''' :red[독도] :gray[지킴이]:ocean: :gray[홈페이지에 오신것을 환영합니다! 독도의 자연,역사,위치 등 독도에 관한 정보를 알려드립니다. 표어와 퀴즈를 구경할 수 있습니다.] ''')

st.image('독도 메인.jpg')

st.header(":gray[표어]")

st.markdown(
    """
    ---
    
    🌐 :gray[**독도 지킴이** | 만든이: [이준수] | 모든 권리 보유.]

    ---
    
    """
)

# 사용자 채팅 입력
st.text_input("💬 :gray[독도에 대해 하고 싶은 말을 남겨보세요!", placeholder="여기에 입력하세요...]")


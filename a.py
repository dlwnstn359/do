import streamlit as st



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
)      이코드 구체적으로 설명해줘

st.snow()
# 제목
st.title(' 독도 지킴이 ')

# 소개글
st.markdown('독도 지킴이 홈페이지에 오신것을 환영합니다! 독도의 자연,역사,위치 등 독도에 관한 정보를 알려드립니다. 표어와 퀴즈를 구경할 수 있습니다. 독도는 대한민국 동쪽 끝에 위치한 아름다운 섬으로, 역사적, 지리적, 국제법적으로 대한민국의 영토입니다. 울릉도에서 약 87.4km 떨어져 있으며, 89개의 작은 섬들로 이루어져 있습니다. 독도는 다양한 해양 생물들이 서식하는 생태계의 보고로, 대한민국의 경비대가 상주하며 지키고 있습니다. 독도는 대한민국의 주권과 자존심을 상징하는 곳으로, 모두가 사랑하고 지켜야 할 소중한 땅입니다. 💙🌊')

st.image('KakaoTalk_20250202_235649064.jpg')


st.header("독도의 위치")
st.map(data={
"latitude": [37.241086],
"longitude": [131.864544]
 })


st.link_button("독도 실시간 영상","https://www.ulleung.go.kr/live/index.do")

st.markdown(
    """
    ---
    
    🌐 **독도 지킴이** | 만든이: [이준수,이우진] | 모든 권리 보유.

    ---
    
    """
)

# 사용자 채팅 입력
st.text_input("💬 독도에 대해 하고 싶은 말을 남겨보세요!", placeholder="여기에 입력하세요...")


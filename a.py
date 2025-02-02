import streamlit as st
from PIL import Image

# 페이지 기본 설정
st.set_page_config(
    page_title="독도 지킴이",
    page_icon="🇰🇷",
    layout="centered"
)


st.snow()
# 제목
st.title(' :gray[독도 지킴이] ')

# 소개글
st.markdown('독도 지킴이 홈페이지에 오신것을 환영합니다! 독도의 자연,역사,위치 등 독도에 관한 정보를 알려드립니다. 표어와 퀴즈를 구경할 수 있습니다.')

st.image('독도 메인.jpg')
# 독도의 위치 (지도 표시)
st.header("독도의 위치")
st.map(data={
    "latitude": [37.241086],
    "longitude": [131.864544]
})
st.header("표어")

if st.button('더 보기'):
        st.video("https://www.youtube.com/watch?v=iNDRFPcNLns")

st.markdown(
    """
    ---
    
    🌐 **독도 지킴이** | 만든이: [이준수] | 모든 권리 보유.

    ---
    
    """
)

# 사용자 채팅 입력
st.text_input("💬 독도에 대해 하고 싶은 말을 남겨보세요!", placeholder="여기에 입력하세요...")


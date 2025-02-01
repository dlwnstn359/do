import streamlit as st
st.set_page_config(
    page_title="독도 역사",
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
st.title("독도 역사")

st.header("삼국 시대")
st.write("『삼국사기』 기록에 512년 우산국이 항복하여 복속하고 해마다 토산물을 공물로 바치기로 했다는 기록이 있다. 여기서 우산국의 위치를 명주(강원도 강릉)의 정동쪽 바다에 있는 섬으로 혹은 울릉도라고 부른다고 하였다. 또 『삼국유사』에는 아슬라주(강원도 강릉)의 동쪽 바다 가운데에 순풍으로 이틀 걸리는 거리에 울릉도가 있다고 하였다. 신라의 이사부가 군대를 거느리고 울릉도 토착민을 토벌하여 울릉도가 항복함으로써 신라에 속하게 되었다.")

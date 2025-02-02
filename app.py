import streamlit as st
from PIL import Image

# 사이드바에 로고 이미지 추가
logo = Image.open("독도 메인.jpg")  
st.sidebar.image(logo, use_column_width=True)

pages = {
    "Your account": [
        st.Page("a.py", title="메인"),
        st.Page("b.py", title="독도 역사"),
        st.Page("c.py", title="독도 자연"),
        st.Page("d.py", title="독도 퀴즈"),
        st.Page("e.py", title="독도 표어"),
    ]
    }

pg = st.navigation(pages)
pg.run()


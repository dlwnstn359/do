import streamlit as st
from PIL import Image



pages = {
   "Your account": [
        st.Page("a.py", title="메인"),
        st.Page("b.py", title="독도 역사"),
        st.Page("c.py", title="독도 자연"),
        st.Page("d.py", title="독도 퀴즈"),
        st.Page("e.py", title="독도 표어"),
        st.image("독도 메인.jpg"),
    ]
    }



pg = st.navigation(pages)
pg.run()


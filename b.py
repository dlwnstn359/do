import streamlit as st
st.set_page_config(
    page_title="독도 역사",
    page_icon="🇰🇷",
    layout="centered"
)
st.title("독도 역사")
if st.button('더 보기'):
  st.image("common.jpg", caption="독도 사진", use_column_width=True)

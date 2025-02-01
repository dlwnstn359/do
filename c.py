import streamlit as st

import gspread
from oauth2client.service_account import ServiceAccountCredentials

st.title("독도 자연")



# Google Sheets API 인증 설정
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

# 시트 열기
sheet = client.open("DokdoChat").sheet1

# 사용자 입력 받기
message = st.text_input("💬 독도에 대해 하고 싶은 말을 남겨보세요!", placeholder="여기에 입력하세요...")

if st.button("전송"):
    if message:
        sheet.append_row([message])

# 저장된 메시지 불러오기
messages = sheet.get_all_records()
for msg in messages:
    st.write(f"💬 {msg['Message']}")

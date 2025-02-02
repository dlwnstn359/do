import streamlit as st
st.set_page_config(
    page_title="독도 자연",
    page_icon="🇰🇷",
    layout="centered"
)


st.title("독도 자연")

st.header("육상 생태계")
col1, col2, col3 = st.columns(3)

with col1:
    st.header(" 식물 ")
    st.write("독도는 얕은 토양과 강한 해풍으로 식물이 자라기 어려운 환경이지만, 약 50~60종의 식물이 서식한다. 대표적으로 민들레, 질경이, 해송, 해당화, 참나리 등이 있으며, 도깨비쇠고비, 개밀, 번행초 같은 자생·귀화식물도 있다. 식생은 각종 생물의 서식처 역할을 하며, 연구 가치가 높다.")
    
with col2:
    st.header("곤충")
    st.write("약 50여 종의 곤충이 발견되었으며, 딱정벌레류(15종)가 가장 많다. 주요 곤충으로는 긴뺨모래거저리, 독도장님노린재, 섬땅방아벌레 등이 있다. 일부 나비와 잠자리는 태풍 등에 의해 유입된 것으로 추정된다.")
    
with col3:
    st.header("조류")
    st.write("120종 이상의 새가 관찰되며, 대표적으로 괭이갈매기, 쇠가마우지, 바다제비, 슴새 등이 번식한다. 철새들의 중간 기착지 역할을 하며, 46월에는 괭이갈매기 약 8,00010,000마리가 독도를 찾는다.")
    st.image("KakaoTalk_20250202_235453847.jpg")
st.header("해양 생태계")
st.image('KakaoTalk_20250202_235037972.jpg')
st.header("해조류")
st.write("독도 해역은 동한난류와 북한한류의 영향을 받아 해조류가 풍부하게 서식하는 환경이다. 현재까지 확인된 해조류는 녹조류(26종), 갈조류(67종), 홍조류(160종) 등 총 250여 종에 달한다.")
st.image("KakaoTalk_20250202_234939897.jpg")
st.header("해양무척추동물")
st.write("조간대에는 검은큰따개비, 거북손, 바위게, 홍합 등의 갑각류와 연체동물이 우점하며, 조하대에는 군소, 불똥해면, 짧은가시거미불가사리 등이 분포한다. 특히, 서도 서측 수심 25m 부근에서 국내 최대 규모의 유착나무돌산호 군집(폭 5m, 높이 3.3m)이 발견되었으나, 최근 서식지가 감소하는 추세다.")

if st.button('The Easter Egg'):
        st.image("yeUOsiAsiQoptMGhH8A-ToAQSm-8fPTj1Y5QRD7kf7y8bdksg3zorJLGRWRmJavA5jAIZ86uCTkB7syQFBLLHg.png")
    









import streamlit as st
st.set_page_config(
    page_title="독도 자연",
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
st.title("독도 자연")
st.header("육상 생태계")
col1, col2, col3 = st.columns(3)

with col1:
    st.header(" :gray[식물] ")
    st.write(" :gray[독도는 오랜 세월 동안 풍화되며 만들어진 흙이 땅을 얇게 덮고 있다. 쌓인 흙은 깊이가 고작 30㎝ 정도며, 경사가 심해 씨가 뿌리를 내리고 싹을 틔울 수 있는 흙이 많지 않다.비가 내리면 흙이 흘러내리니 토양은 항상 건조하고, 소금기 머금은 해풍이 강하게 불어 식물이 자라기에 좋은 환경이 아니지만, 끈질긴 생명력을 가진 야생화들이 봄이 되면 독도를 화려하게 장식한다. 독도에서 조사된 식물은 약 50~60종에 달한다. 민들레, 질경이, 구절초, 개여뀌, 참억새, 강아지풀, 참나리, 사철나무, 해송, 해당화, 술패랭이꽃, 명아주, 해국, 개머루처럼 친숙한 식물도 있다. 그렇지만 소루쟁이, 갯까치수염, 괭이밥, 땅채송화, 큰조롱, 방가지똥, 섬장대, 도깨비고비, 섬괴불나무, 왜젓가락나물, 쇠비름, 갯괴불주머니, 기린초, 댕댕이덩굴, 박주가리, 털머위, 돌피처럼 생소하지만 재미있는 이름을 가진 식물도 있다. 독도는 표층이 얕은 바위섬이며, 심한 바람과 염분 등 혹한 환경에 적응한 식물상을 보이고 있다. 독도의 식생은 각종 생물의 서식처, 산란처, 피난처의 기능을 하며, 육상과 해양의 생물간 연관성을 연구함에 있어서도 중요한 표본 역할을 한다. 특히, 식물종 침입 역사가 짧고 식물상의 성숙에 소요되는 충분한 시간이 경과되지 않았기에 식생천이 과정 등에 있어 그 연구가치가 높다. 독도는 위치상 아한대 남단 해역에 속해 있지만 해류의 영향과 비교적 온난 다습한 날씨 때문에 그 식물상이 아열대와 비슷한 양상을 보인다. 또한 울릉도보다 생성시기가 약 150만년 이상 빨라 울릉도와는 다른 경로로 식물이 유입 ·진화한 것으로 추정된다. 도깨비쇠고비, 곰솔, 초종용 등의 자생식물과 왕호장근, 번행초, 개밀 등 귀화식물이 독도의 식생을 구성하고 있다. 최근에는 새포아풀, 금강아지풀, 닭의장풀, 둥근잎나팔꽃 등의 추가적 유입이 확인되었다. 독도는 식물종 급원지로부터 멀리 떨어져 있고 연중 파도와 강한 해풍의 영향을 받을 뿐 아니라, 면적이 좁고 해발고도가 낮으며 경사가 가파른 이유로 식생의 정착이 매우 어렵다. 토양층이 없는 건조한 해안절벽지대에는 땅채송화군락, 왕김의털군락, 해국군락, 갯제비쑥군락이 분포하고, 습기가 있는 바위틈에는 독도의 유일한 양치식물인 도깨비쇠고비군락이 분포한다. 완경사지에는 개밀-돌피군락이 우점하고 있으며, 토양 발달 정도와 인위적 간섭 정도에 따라 갯까치수염군락, 술패랭이꽃군락, 참억새군락, 번행초군락, 왕호장근군락, 참나리군락 등이 분포한다. 반면 급경사지에는 땅채송화군락, 왕김의털군락, 해국군락, 갯제비쑥군락과 함께 사철나무군락이 분포한다. 이들 군락 외에도 독도의 등대 서쪽 완경사지와 서도의 주민숙소에서 물골로 이어지는 완경사지에는 섬괴불나무, 사철나무, 보리밥나무, 동백나무 등의 식재목군락이 분포하고 있다.] ")
with col2:
    st.header("곤충")
    st.write("독도에서 발견된 곤충은 50여종에 달한다. 잠자리, 집게벌레, 메뚜기, 노린재, 매미, 풀잠자리, 딱정벌레, 파리, 나비, 등으로 딱정벌레가 15종류로 가장 많은 종을 차지한다. 독도에는 당도가 높은 과실을 맺는 식물이 없어서 초본식물의 잎이나 줄기에서 먹이를 얻는 매미목, 파리목 등이 곤충의 대부분을 차지한다. 주요 종으로는 쟈바꽃등에, 긴뺨모래거저리, 해변애녹슬은방아벌레, 모래섶벌레, 민집게벌레, 애긴노린재, 애꽃노린재, 애먼지벌레, 배검은꼬마개미, 독도장님노린재, 섬땅방아벌레, 초록다홍알락매미충 등이 있다. 나비목(호랑나비, 작은멋쟁이나비 등) 및 잠자리목(왕잠자리, 된장잠자리 등)의 비례성 곤충이 발견된 경우도 있으나, 이는 일본이나 울릉도에서 태풍 등의 영향을 받아 날려 온 것으로 추정되고 있다.")

with col3:
    st.header("조류")
    st.write("봄이 되어 번식기가 시작되면 독도의 하늘은 온통 괭이갈매기로 가득하다. 독도에 사는 바닷새로는 괭이갈매기, 쇠가마우지, 바다제비, 슴새 등이 있다. 독도에서 발견된 새 종류는 120종이 넘는 것으로 알려져 있다. 5월에 관찰된 새로는 해오라기, 황로, 흑비둘기, 매, 괭이갈매기, 개똥지빠귀, 바다직박구리, 멧새, 딱새, 되새, 방울새, 까마귀 등 30여종에 달한다. 그리고 10월 독도에서 관찰된 새로는 솔개, 매, 황조롱이, 흑비둘기, 종다리, 노랑할미새, 딱새, 개똥지빠귀, 쑥새, 촉새, 되새, 방울새, 섬참새 등 20여종이 된다. 계절에 따라 종 숫자가 다른 것은 봄, 가을 철새들이 이동하다가 날개를 쉬기 위해 독도에 잠시 머물기 때문이다. 독도는 우리나라 주변을 지나는 철새 뿐 아니라 먼 거리를 지나가는 나그네새의 중간 기착지, 태풍과 폭우 등 불규칙한 기상조건에서 조류의 피난처 역할을 하는 섬으로 조류생태학적 가치 가 높게 평가되어 왔다. 독도에서 번식하는 대표적인 조류로는 괭이갈매기와 바다제비가 있다. 괭이갈매기는 4월에서 6월 사이 8,000~10,000여 마리가 번식을 위하여 독도를 찾고 있다. 바다제비의 번식기는 7월에서 8월 사이로 부드러운 흙이 있는 경사면에 굴을 파고 산란한다. 이 밖에도 독도에서 번식하는 조류로는 슴새, 뿔쇠오리, 매 등이 있으며, 나그네새로는 진홍가슴, 흰배멧새, 유리딱새 등이 관찰되었다.")
    









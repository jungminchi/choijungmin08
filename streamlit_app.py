import streamlit as st

st.title("cjm honda nsx")
st.info("nissan")
st.write("supra")
# 페이지 구조용 제목 출력
st.title("아스팔트 9")
st.header("람보르기니 센티네리오")
st.subheader("뉘르부르크링")
# LaTeX 수식 출력
st.latex(r"E = mc^2")
st.latex(r"\int_{a}^{b} x^2 dx = \frac{b^3 - a^3}{3}")
st.image("https://p4.wallpaperbetter.com/wallpaper/903/206/564/toyota-supra-toyota-supra-a80-garage-defend-bbs-white-cars-hd-wallpaper-preview.jpg")
st.image("https://media0.giphy.com/media/aWI5bSkuFosSQgEKIP/giphy.webp?cid=ecf05e47uc0gam1pqjeo59odvyj88i5n72xrhjr1x7s4x3ga&ep=v1_gifs_search&rid=giphy.webp&ct=g")
st.image("https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExbmdldGZ1Z2tvdmRlZGdmMDRoYTAwbGFzZXNvMW84N2c3Mjk5YmVoYiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/FX7hNJZZYZhQXXHwN9/200w.webp")
st.code("""
import streamlit as st
st.title('Hello carman')
""", language="python")
st.link_button("suv가 의미 없어??????", 'https://www.youtube.com/watch?v=szQpMDGKFD8')
# 버튼 클릭 여부에 따라 실행
if st.button("클릭하세요"):
    st.write("당신은 논바이어리티 입니다")
    # 한 줄 텍스트 입력
name = st.text_input("이름을 입력하세요")
st.write("입력된 이름:", name)

# 여러 줄 텍스트 입력
feedback = st.text_area("의견을 입력하세요")
st.write("입력된 의견:", feedback)
# 정수 혹은 실수 입력
age = st.number_input("나이를 입력하세요", min_value=0, max_value=120, step=1)
st.write("입력된 나이:", age)
# 체크 여부에 따라 분기
agree = st.checkbox("위 조건에 동의합니다")
if agree:
    st.write("감사합니다! 계속 진행합니다.")
    # 여러 옵션 중 하나 선택
gender = st.radio("성별을 선택하세요", ["남성", "여성", "기타"])
st.write("선택한 성별:", gender)
# 드롭다운에서 하나 선택
color = st.selectbox("좋아하는 색을 선택하세요", ["빨강", "초록", "파랑"])
st.write("선택한 색상:", color)

# 여러 개 선택
subjects = st.multiselect("관심 있는 과목을 선택하세요", ["수학", "영어", "과학"])
st.write("선택한 과목:", subjects)
# 범위 내 숫자 슬라이드 선택
level = st.slider("난이도를 선택하세요", 1, 10, 5)
st.write("선택한 난이도:", level)
# 날짜 입력
date = st.date_input("날짜를 선택하세요")
st.write("선택한 날짜:", date)

# 시간 입력
time = st.time_input("시간을 선택하세요")
st.write("선택한 시간:", time)
# 파일 업로드 처리
uploaded_file = st.file_uploader("파일을 업로드하세요", type=["csv", "txt", "pdf"])
if uploaded_file:
    st.success("파일 업로드 완료!")
    # 카메라로 사진 촬영
image_data = st.camera_input("사진을 찍어보세요")
if image_data:
    st.image(image_data)
import streamlit as st

# 페이지 설정
st.set_page_config(page_title="MBTI별 애완동물 추천기", page_icon="🐾", layout="centered")

# 헤더
st.title("🐶 MBTI별 애완동물 추천기")
st.markdown("당신의 MBTI에 가장 잘 어울리는 귀여운 반려동물을 추천해드릴게요!")

# MBTI 목록
mbti_types = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

# 추천 데이터
mbti_pet_map = {
    "ISTJ": ["🐢 거북이", "🐠 금붕어", "🐦 잉꼬"],
    "ISFJ": ["🐰 토끼", "🐱 고양이", "🐹 햄스터"],
    "INFJ": ["🦜 앵무새", "🐈 고양이", "🦔 고슴도치"],
    "INTJ": ["🐍 뱀", "🐟 베타피쉬", "🦎 도마뱀"],
    "ISTP": ["🐸 개구리", "🦎 도마뱀", "🐢 거북이"],
    "ISFP": ["🐱 고양이", "🐠 구피", "🐦 잉꼬"],
    "INFP": ["🦔 고슴도치", "🐇 토끼", "🐱 고양이"],
    "INTP": ["🦎 도마뱀", "🐢 거북이", "🐠 금붕어"],
    "ESTP": ["🐶 강아지", "🐴 조랑말", "🦜 앵무새"],
    "ESFP": ["🐶 강아지", "🦜 앵무새", "🐹 햄스터"],
    "ENFP": ["🦜 앵무새", "🐶 강아지", "🦙 알파카"],
    "ENTP": ["🐍 뱀", "🐸 개구리", "🦜 앵무새"],
    "ESTJ": ["🐶 셰퍼드", "🐦 앵무새", "🐟 금붕어"],
    "ESFJ": ["🐶 비숑", "🐱 페르시안 고양이", "🐰 토끼"],
    "ENFJ": ["🐶 골든리트리버", "🐱 고양이", "🐹 햄스터"],
    "ENTJ": ["🦎 이구아나", "🐠 금붕어", "🐦 앵무새"]
}

# 사용자 입력
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요 👇", mbti_types)

# 추천 결과 출력
if selected_mbti:
    st.subheader(f"🧡 {selected_mbti} 유형에게 잘 어울리는 반려동물은?")
    pets = mbti_pet_map[selected_mbti]
    for pet in pets:
        st.markdown(f"- {pet}")

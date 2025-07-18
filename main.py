import streamlit as st

# 페이지 설정
st.set_page_config(page_title="MBTI별 반려동물 추천기", page_icon="🐾", layout="centered")

# 타이틀 및 설명
st.title("🐾 MBTI별 반려동물 추천기")
st.markdown("당신의 MBTI 성격 유형에 어울리는 **귀여운 반려동물**을 추천해드릴게요!")

# MBTI 설명과 추천 반려동물 데이터
mbti_data = {
    "ISTJ": {
        "desc": "신중하고 책임감 있으며 현실적인 성격으로, 꾸준한 관리가 필요한 반려동물과 잘 맞아요.",
        "pets": ["🐢 거북이", "🐠 금붕어", "🐦 잉꼬"]
    },
    "ISFJ": {
        "desc": "다정하고 배려심이 깊으며 조용한 환경을 좋아해요. 조용하고 온순한 반려동물이 잘 어울려요.",
        "pets": ["🐰 토끼", "🐱 고양이", "🐹 햄스터"]
    },
    "INFJ": {
        "desc": "이상주의자이며 조용하지만 깊은 내면의 세계를 가진 INFJ는 섬세한 반려동물과 잘 어울려요.",
        "pets": ["🦜 앵무새", "🐈 고양이", "🦔 고슴도치"]
    },
    "INTJ": {
        "desc": "분석적이고 계획적인 성격으로, 독립적인 동물과의 조용한 유대감을 선호해요.",
        "pets": ["🐍 뱀", "🐟 베타피쉬", "🦎 도마뱀"]
    },
    "ISTP": {
        "desc": "논리적이고 탐구적인 성향의 ISTP는 관찰과 관리가 필요한 반려동물에 흥미를 느껴요.",
        "pets": ["🐸 개구리", "🦎 도마뱀", "🐢 거북이"]
    },
    "ISFP": {
        "desc": "감성적이고 예술적인 ISFP는 아름답고 조용한 반려동물과 잘 어울려요.",
        "pets": ["🐱 고양이", "🐠 구피", "🐦 잉꼬"]
    },
    "INFP": {
        "desc": "상상력이 풍부하고 따뜻한 INFP는 자신만의 정서적 교감을 중요시해요.",
        "pets": ["🦔 고슴도치", "🐇 토끼", "🐱 고양이"]
    },
    "INTP": {
        "desc": "지적인 탐구를 좋아하는 INTP는 특이하고 관리가 필요한 동물을 좋아할 수 있어요.",
        "pets": ["🦎 도마뱀", "🐢 거북이", "🐠 금붕어"]
    },
    "ESTP": {
        "desc": "활동적이고 도전적인 ESTP는 함께 뛰어놀 수 있는 반려동물을 선호해요.",
        "pets": ["🐶 강아지", "🐴 조랑말", "🦜 앵무새"]
    },
    "ESFP": {
        "desc": "즐거움을 추구하고 사교적인 ESFP는 활발하고 귀여운 동물을 좋아해요.",
        "pets": ["🐶 강아지", "🦜 앵무새", "🐹 햄스터"]
    },
    "ENFP": {
        "desc": "창의적이고 열정적인 ENFP는 감정 교류가 풍부한 반려동물을 선호해요.",
        "pets": ["🦜 앵무새", "🐶 강아지", "🦙 알파카 인형?!"]
    },
    "ENTP": {
        "desc": "도전과 변화를 즐기는 ENTP는 독특하고 새로운 반려동물을 좋아해요.",
        "pets": ["🐍 뱀", "🐸 개구리", "🦜 앵무새"]
    },
    "ESTJ": {
        "desc": "조직적이고 단호한 ESTJ는 훈련이 잘 되는 똑똑한 반려동물을 선호해요.",
        "pets": ["🐶 셰퍼드", "🐦 앵무새", "🐟 금붕어"]
    },
    "ESFJ": {
        "desc": "친절하고 정이 많은 ESFJ는 외로움을 잘 타는 귀여운 동물과 잘 어울려요.",
        "pets": ["🐶 비숑", "🐱 페르시안 고양이", "🐰 토끼"]
    },
    "ENFJ": {
        "desc": "리더십 있고 따뜻한 ENFJ는 감정 교류가 활발한 반려동물을 좋아해요.",
        "pets": ["🐶 골든리트리버", "🐱 고양이", "🐹 햄스터"]
    },
    "ENTJ": {
        "desc": "결단력 있고 분석적인 ENTJ는 독립적이면서 관리가 용이한 반려동물을 선호해요.",
        "pets": ["🦎 이구아나", "🐠 금붕어", "🐦 앵무새"]
    },
}

# MBTI 선택 위젯
mbti_selected = st.selectbox("당신의 MBTI를 선택하세요 👇", list(mbti_data.keys()))

# 결과 표시
if mbti_selected:
    data = mbti_data[mbti_selected]
    st.subheader(f"🧠 {mbti_selected} 유형의 성격 요약")
    st.markdown(f"_{data['desc']}_")
    st.subheader("🐾 추천 반려동물 3종")
    for pet in data["pets"]:
        st.markdown(f"- {pet}")
    st.balloons()  # 풍선 효과

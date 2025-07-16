import streamlit as st
import pandas as pd
import altair as alt
import os

# 페이지 설정
st.set_page_config(
    page_title="MBTI 분석 - 대한민국",
    page_icon="🧠",
    layout="centered"
)

# 전체 배경 및 텍스트 색상 설정 (다크+화이트 텍스트 스타일)
st.markdown("""
    <style>
    body {
        background-color: #223344;
        color: white;
    }
    .stApp {
        background-color: #223344;
        color: white;
    }
    h1, h2, h3, h4, h5, h6, p {
        color: white !important;
    }
    .css-18ni7ap.e8zbici2 { color: white !important; }
    </style>
""", unsafe_allow_html=True)

# 상단 헤더
st.markdown("""
    <div style='text-align: center; padding: 10px;'>
        <h1 style='color:white;'>📊 대한민국 MBTI Top 3</h1>
        <p style='font-size:18px;'>당신과 비슷한 성격의 사람들이 많은 유형은?</p>
    </div>
""", unsafe_allow_html=True)

# 파일 경로
file_path = "countriesMBTI_16types.csv"

# 파일 확인
if not os.path.exists(file_path):
    st.error("❗ 'countriesMBTI_16types.csv' 파일이 현재 폴더에 없습니다.")
    st.stop()

# 데이터 불러오기
@st.cache_data
def load_data():
    return pd.read_csv(file_path)

df = load_data()

# 대한민국 데이터 추출
if "South Korea" not in df["Country"].values:
    st.error("❗ 'South Korea'라는 국가명이 데이터에 없습니다.")
    st.stop()

korea_row = df[df["Country"] == "South Korea"].iloc[0]
mbti_series = korea_row.drop(labels="Country").astype(float)

# Top 3 추출
top3 = mbti_series.sort_values(ascending=False).head(3).reset_index()
top3.columns = ["MBTI", "비율"]
top3["백분율"] = (top3["비율"] * 100).round(2)

# Altair 색상 리스트
color_list = ['#FF6B6B', '#FFD93D', '#6BCB77']

# Altair 그래프
chart = alt.Chart(top3).mark_bar(size=60).encode(
    x=alt.X("MBTI", sort='-y', title=None),
    y=alt.Y("백분율", title="백분율 (%)"),
    color=alt.Color("MBTI:N", scale=alt.Scale(domain=top3["MBTI"].tolist(), range=color_list), legend=None),
    tooltip=["MBTI", "백분율"]
).properties(
    width=500,
    height=400,
    title="🧠 대한민국에서 가장 많은 MBTI 유형"
).configure_axis(
    labelFontSize=14,
    titleFontSize=16,
    labelColor='white',
    titleColor='white'
).configure_title(
    fontSize=20,
    anchor='start',
    color="white"
).configure_view(
    stroke=None
)

# 출력
st.altair_chart(chart, use_container_width=True)

# 해설 텍스트 박스 (다크 배경용)
top1, top2, top3_type = top3["MBTI"].tolist()
st.markdown(f"""
<div style='
    padding: 16px;
    background-color: #2f4f70;
    border-radius: 12px;
    font-size: 17px;
    color: white;
    line-height: 1.6;
    border: 1px solid #446688;
'>
✅ <strong>{top1}</strong> 유형이 가장 많았어요!<br>
🥈 그 다음은 <strong>{top2}</strong>,<br>
🥉 그리고 <strong>{top3_type}</strong> 유형도 많이 나타났어요.<br><br>
중학생 여러분, 혹시 이 중에 여러분 MBTI도 있나요? 😊
</div>
""", unsafe_allow_html=True)

# 데이터표 보기
with st.expander("📑 데이터 보기"):
    st.dataframe(top3.style.format({"비율": "{:.4f}", "백분율": "{:.2f}%"}))

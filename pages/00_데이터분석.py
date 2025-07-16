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

# 상단 헤더
st.markdown("""
    <div style='text-align: center; padding: 10px;'>
        <h1 style='color:#4A90E2;'>📊 대한민국 MBTI Top 3</h1>
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

# 'South Korea' 행 추출
if "South Korea" not in df["Country"].values:
    st.error("❗ 'South Korea'라는 국가명이 데이터에 없습니다.")
    st.stop()

korea_row = df[df["Country"] == "South Korea"].iloc[0]
mbti_series = korea_row.drop(labels="Country").astype(float)

# Top 3 추출
top3 = mbti_series.sort_values(ascending=False).head(3).reset_index()
top3.columns = ["MBTI", "비율"]
top3["백분율"] = (top3["비율"] * 100).round(2)

# 색상 리스트
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
    titleFontSize=16
).configure_title(
    fontSize=20,
    anchor='start',
    color="#333"
)

# 출력
st.altair_chart(chart, use_container_width=True)

# 해설 텍스트
top1, top2, top3_type = top3["MBTI"].tolist()
st.markdown(f"""
<div style='padding: 10px; background-color: #f0f8ff; border-radius: 10px; font-size: 16px; line-height: 1.6'>
    ✅ <strong>{top1}</strong> 유형이 가장 많았어요!<br>
    🥈 그 다음은 <strong>{top2}</strong>,<br>
    🥉 그리고 <strong>{top3_type}</strong> 유형도 많이 나타났어요.<br><br>
    중학생 여러분, 혹시 이 중에 여러분 MBTI도 있나요? 😊
</div>
""", unsafe_allow_html=True)

# 데이터표 보기
with st.expander("📑 데이터 보기"):
    st.dataframe(top3.style.format({"비율": "{:.4f}", "백분율": "{:.2f}%"}))

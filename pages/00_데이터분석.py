import streamlit as st
import pandas as pd
import altair as alt
import os

# 제목
st.title("🇰🇷 대한민국 MBTI 상위 3유형 시각화")
st.caption("📁 데이터: countriesMBTI_16types.csv (현재 폴더 내)")

# 파일 경로
file_path = "countriesMBTI_16types.csv"

# 파일 유무 확인
if not os.path.exists(file_path):
    st.error("❗ 'countriesMBTI_16types.csv' 파일이 현재 폴더에 없습니다. 파일을 추가해 주세요.")
    st.stop()

# 데이터 불러오기 함수
@st.cache_data
def load_data():
    return pd.read_csv(file_path)

df = load_data()

# 'South Korea' 행 추출
if "South Korea" not in df["Country"].values:
    st.error("❗ 'South Korea'라는 국가명이 데이터에 없습니다. 정확히 입력되어 있는지 확인하세요.")
    st.stop()

korea_row = df[df["Country"] == "South Korea"].iloc[0]

# MBTI 컬럼만 추출 (Country 제외)
mbti_series = korea_row.drop(labels="Country")

# 형변환: object → float
mbti_series = mbti_series.astype(float)

# 상위 3개 추출
top3 = mbti_series.sort_values(ascending=False).head(3).reset_index()
top3.columns = ["MBTI", "비율"]
top3["백분율"] = (top3["비율"] * 100).round(2)

# 시각화 (Altair 막대 그래프)
chart = alt.Chart(top3).mark_bar(size=50).encode(
    x=alt.X("MBTI", sort='-y', title="MBTI 유형"),
    y=alt.Y("백분율", title="백분율 (%)"),
    tooltip=["MBTI", "백분율"]
).properties(
    width=500,
    height=400,
    title="🇰🇷 South Korea Top 3 MBTI 유형"
)

# 출력
st.altair_chart(chart, use_container_width=True)

# 데이터표 확인
with st.expander("📊 Top 3 데이터 보기"):
    st.dataframe(top3)

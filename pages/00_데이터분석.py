import streamlit as st
import pandas as pd
import altair as alt
import os

# 제목
st.title("🇰🇷 대한민국에서 가장 흔한 MBTI 유형 Top 3")
st.caption("데이터 출처: countriesMBTI_16types.csv")

# 파일 경로
file_path = "countriesMBTI_16types.csv"

# 파일 존재 여부 확인
if not os.path.exists(file_path):
    st.error("❗ 파일 'countriesMBTI_16types.csv'이 현재 폴더에 없습니다. 파일을 추가해주세요.")
    st.stop()

# 데이터 불러오기
@st.cache_data
def load_data():
    return pd.read_csv(file_path)

df = load_data()

# 대한민국 데이터 추출
if "South Korea" not in df["Country"].values:
    st.error("❗ 'South Korea'라는 국명이 데이터에 없습니다. 정확한 국명인지 확인해주세요.")
    st.stop()

korea_row = df[df["Country"] == "South Korea"].iloc[0]

# MBTI 16유형 값만 추출
mbti_values = korea_row.drop(labels="Country")

# 상위 3개 MBTI 유형 추출
top3 = mbti_values.sort_values(ascending=False).head(3).reset_index()
top3.columns = ["MBTI", "비율"]
top3["백분율"] = (top3["비율"] * 100).round(2)

# Altair 막대그래프
chart = alt.Chart(top3).mark_bar(size=50).encode(
    x=alt.X("MBTI", sort='-y', title="MBTI 유형"),
    y=alt.Y("백분율", title="백분율 (%)"),
    tooltip=["MBTI", "백분율"]
).properties(
    width=500,
    height=400,
    title="🇰🇷 대한민국 Top 3 MBTI 유형"
)

# 그래프 출력
st.altair_chart(chart, use_container_width=True)

# 데이터 표 출력
with st.expander("📊 Top 3 데이터 보기"):
    st.dataframe(top3)

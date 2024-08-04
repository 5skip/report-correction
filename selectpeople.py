import streamlit as st
def people_select_box():
    st.selectbox(
        "人の名前を選択して下さい",
        ("松岡修造","橋本環奈","ずんだもん","福山雅治"),
        index=None,
        placeholder="人の名前",
    )

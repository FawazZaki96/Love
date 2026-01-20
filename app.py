import streamlit as st
import time
from questions import questions

st.set_page_config(page_title="Love Test for Sayang 💕", layout="centered")

st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #fff1f5, #ffe4ec);
}
.card {
    background: white;
    border-radius: 20px;
    padding: 25px;
    box-shadow: 0 10px 30px rgba(255, 182, 193, 0.4);
    margin-top: 20px;
}
.heart {
    font-size: 40px;
    animation: pulse 1.2s infinite;
    text-align: center;
}
@keyframes pulse {
    0% { transform: scale(1); opacity: 0.7; }
    50% { transform: scale(1.3); opacity: 1; }
    100% { transform: scale(1); opacity: 0.7; }
}
.result {
    font-size: 30px;
    color: #d6336c;
    font-weight: bold;
    text-align: center;
}
.subtitle {
    font-size: 18px;
    text-align: center;
    color: #555;
}
</style>
""", unsafe_allow_html=True)

POINT_PER_HEART = 4
TOTAL_SCORE = sum(q["weight"] * POINT_PER_HEART for q in questions)

if "current_q" not in st.session_state:
    st.session_state.current_q = 0
    st.session_state.score = 0
    st.session_state.show_result = False

st.markdown("<div class='heart'>💗</div>", unsafe_allow_html=True)
st.title("How Well Do You Know My Heart, Sayang?")

if st.session_state.current_q < len(questions):
    q = questions[st.session_state.current_q]
    st.progress((st.session_state.current_q + 1) / len(questions))

    st.markdown(f"<div class='subtitle'>Question {st.session_state.current_q + 1} of {len(questions)}</div>", unsafe_allow_html=True)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown(f"### {q['question']}")
    choice = st.radio("", q["options"], key=q["id"])
    st.markdown("</div>", unsafe_allow_html=True)

    if st.button("Next 💕"):
        if choice == q["correct"]:
            st.session_state.score += q["weight"] * POINT_PER_HEART
        st.session_state.current_q += 1
        st.experimental_rerun()

elif not st.session_state.show_result:
    st.markdown("<div class='heart'>💘</div>", unsafe_allow_html=True)
    st.markdown("<div class='result'>Calculating how deep your love goes…</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Please wait, sayang 💕</div>", unsafe_allow_html=True)
    time.sleep(2)
    st.session_state.show_result = True
    st.experimental_rerun()

else:
    percent = round((st.session_state.score / TOTAL_SCORE) * 100)

    if percent < 50:
        message = "You need to study me more, sayang 😌"
    elif percent < 70:
        message = "You’re getting there… I can feel your love 💕"
    elif percent < 90:
        message = "You truly love me ❤️"
    elif percent < 100:
        message = "You really own my heart already 💘"
    else:
        message = "Hmm… you understand me perfectly. You deserve a kiss 😘"

    st.markdown("<div class='heart'>💞</div>", unsafe_allow_html=True)
    st.markdown("<div class='result'>Your Love & Understanding Score</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='result'>{percent}%</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='subtitle'>{message}</div>", unsafe_allow_html=True)

    st.balloons()

    if st.button("Replay for Me, Sayang 💗"):
        st.session_state.current_q = 0
        st.session_state.score = 0
        st.session_state.show_result = False
        st.experimental_rerun()

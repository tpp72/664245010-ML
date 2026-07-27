from pathlib import Path

import streamlit as st

st.set_page_config(
    page_title="ผู้พัฒนา | ML Hub",
    page_icon="🧑‍💻",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Prompt:wght@300;500;700&family=Orbitron:wght@700&display=swap');

.stApp {
    background: #0a0e27;
    background-image:
        radial-gradient(circle at 20% 20%, rgba(0,255,200,0.08) 0%, transparent 40%),
        radial-gradient(circle at 80% 70%, rgba(120,0,255,0.10) 0%, transparent 40%),
        linear-gradient(rgba(255,255,255,0.03) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255,255,255,0.03) 1px, transparent 1px);
    background-size: auto, auto, 40px 40px, 40px 40px;
}
html, body, [class*="css"] { font-family: 'Prompt', sans-serif; }

.hero { text-align: center; padding: 30px 10px 10px 10px; }
.hero h1 {
    font-family: 'Orbitron', sans-serif;
    font-size: 2.6rem;
    background: linear-gradient(90deg,#00ffc8,#00a2ff,#b400ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0;
}
.hero p { color:#8fa3c8; letter-spacing:1px; margin-top:6px; }

[data-testid="stImage"] {
    display: flex;
    justify-content: center;
}
[data-testid="stImage"] img {
    border-radius: 50%;
    border: 3px solid transparent;
    background:
        linear-gradient(#0a0e27,#0a0e27) padding-box,
        linear-gradient(135deg,#00ffc8,#00a2ff,#b400ff) border-box;
    box-shadow: 0 0 35px rgba(0,255,200,0.25);
    object-fit: cover;
    aspect-ratio: 1 / 1;
}

.profile-card {
    max-width: 420px;
    margin: 24px auto 0 auto;
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(0,255,200,0.25);
    border-radius: 18px;
    padding: 26px 30px;
    text-align: center;
    backdrop-filter: blur(8px);
}
.profile-card h2 {
    color: #eaf4ff;
    font-family: 'Orbitron', sans-serif;
    font-size: 1.4rem;
    margin: 4px 0 14px 0;
}
.info-row {
    display: flex;
    justify-content: space-between;
    padding: 10px 4px;
    border-top: 1px solid rgba(255,255,255,0.08);
    color: #cfe0ff;
    font-size: 0.95rem;
}
.info-row:first-of-type { border-top: none; }
.info-row span.label { color: #8fa3c8; }
.info-row span.value { font-weight: 600; }

footer, #MainMenu { visibility:hidden; }
[data-testid="stSidebar"], [data-testid="stSidebarCollapsedControl"] { visibility:visible !important; }

/* Sidebar */
[data-testid="stSidebar"] {
    background: #0a0e27;
    border-right: 1px solid rgba(0,255,200,0.15);
}
[data-testid="stSidebarNav"] {
    padding-top: 6px;
}
[data-testid="stSidebarNav"]::before {
    content: "MACHINE LEARNING HUB";
    display: block;
    margin: 14px 16px 12px 16px;
    padding-bottom: 12px;
    border-bottom: 1px solid rgba(0,255,200,0.15);
    font-family: 'Orbitron', sans-serif;
    font-size: 0.78rem;
    letter-spacing: 1.5px;
    background: linear-gradient(90deg,#00ffc8,#00a2ff,#b400ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
[data-testid="stSidebarNav"] a {
    margin: 2px 10px;
    padding: 10px 14px !important;
    border-radius: 10px;
    color: #8fa3c8 !important;
    font-family: 'Prompt', sans-serif;
    font-weight: 500;
    transition: all .2s ease;
}
[data-testid="stSidebarNav"] a:hover {
    background: rgba(0,255,200,0.08);
    color: #eaf4ff !important;
}
[data-testid="stSidebarNav"] a[aria-current="page"] {
    background: linear-gradient(90deg, rgba(0,255,200,0.18), rgba(120,0,255,0.12));
    color: #eaf4ff !important;
    box-shadow: inset 3px 0 0 #00ffc8;
}
/* เปลี่ยนข้อความเมนู: app -> หน้าหลัก, about -> ผู้พัฒนา */
[data-testid="stSidebarNav"] li:nth-child(1) a { font-size: 0; }
[data-testid="stSidebarNav"] li:nth-child(1) a::after { content: "หน้าหลัก"; font-size: 1rem; }
[data-testid="stSidebarNav"] li:nth-child(2) a { font-size: 0; }
[data-testid="stSidebarNav"] li:nth-child(2) a::after { content: "ผู้พัฒนา"; font-size: 1rem; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>ผู้พัฒนา</h1>
    <p>ข้อมูลผู้จัดทำโปรเจค Machine Learning Hub</p>
</div>
""", unsafe_allow_html=True)

photo_path = Path(__file__).resolve().parent.parent / "assets" / "profile.jpg"
_, center_col, _ = st.columns([1, 1, 1])
with center_col:
    st.image(str(photo_path), width=220)

st.markdown("""
<div class="profile-card">
    <h2>ต่อพงศ์ เพียรพัฒน์กุล</h2>
    <div class="info-row"><span class="label">รหัสนักศึกษา</span><span class="value">664245010</span></div>
    <div class="info-row"><span class="label">หมู่เรียน</span><span class="value">Sec. 66/43</span></div>
</div>
""", unsafe_allow_html=True)

st.markdown("<p style='text-align:center;color:#5a6b8c;margin-top:30px;'>Made with Streamlit · Machine Learning Projects</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:#5a6b8c;margin-top:4px;'>Develop By tpp72</p>", unsafe_allow_html=True)

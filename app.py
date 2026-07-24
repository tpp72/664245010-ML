import streamlit as st

st.set_page_config(page_title="ML Hub", page_icon="🤖", layout="wide")

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

.hero {
    text-align: center;
    padding: 30px 10px 10px 10px;
}
.hero h1 {
    font-family: 'Orbitron', sans-serif;
    font-size: 3rem;
    background: linear-gradient(90deg,#00ffc8,#00a2ff,#b400ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0;
}
.hero p { color:#8fa3c8; letter-spacing:1px; margin-top:6px; }

.card {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(0,255,200,0.25);
    border-radius: 18px;
    padding: 22px;
    height: 250px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    backdrop-filter: blur(8px);
    transition: all .3s ease;
    margin-bottom: 18px;
}
.card:hover {
    transform: translateY(-6px);
    border-color: #00ffc8;
    box-shadow: 0 0 25px rgba(0,255,200,0.25);
}
.card .icon { font-size: 2.2rem; }
.card h3 { color:#eaf4ff; margin:8px 0 4px 0; font-size:1.15rem; }
.card p { color:#8fa3c8; font-size:0.85rem; line-height:1.4; }

.btn {
    display:block;
    text-align:center;
    text-decoration:none !important;
    padding:10px;
    border-radius:10px;
    font-weight:600;
    color:#0a0e27 !important;
    background:linear-gradient(90deg,#00ffc8,#00a2ff);
    transition: filter .2s;
}
.btn:hover { filter: brightness(1.15); }

footer, #MainMenu, header { visibility:hidden; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>MACHINE LEARNING HUB</h1>
    <p>ศูนย์รวมเว็บแอปพลิเคชัน Machine Learning</p>
</div>
""", unsafe_allow_html=True)

st.write("")

APPS = [
    ("🌳", "Decision Tree", "โมเดลต้นไม้ตัดสินใจสำหรับงานจำแนกประเภท", "https://decisiontree-ml.streamlit.app/"),
    ("❤️", "Heart Disease", "ทำนายความเสี่ยงโรคหัวใจด้วย Decision Tree", "https://dtreeheartdisease.streamlit.app/"),
    ("🚢", "Titanic Survival", "ทำนายการรอดชีวิตของผู้โดยสารเรือไททานิค", "https://dtreetitanic-tpp72.streamlit.app/"),
    ("🍷", "Wine Classifier", "จำแนกประเภทไวน์จากคุณสมบัติทางเคมี", "https://dtwine.streamlit.app/"),
    ("🎯", "K-Means Clustering", "จัดกลุ่มข้อมูลแบบ Unsupervised Learning", "https://k-means-664245010.streamlit.app/"),
    ("🔍", "K-Nearest Neighbors", "จำแนกข้อมูลด้วยเพื่อนบ้านที่ใกล้ที่สุด", "https://knn-ml.streamlit.app/"),
    ("📈", "Regression", "วิเคราะห์และทำนายค่าต่อเนื่องด้วย Regression", "https://regression-664245010.streamlit.app/"),
    ("🌲", "Random Forest", "จำแนกประเภทข้อมูลด้วยการรวมกลุ่มต้นไม้ตัดสินใจ", "https://rndforest-664245010.streamlit.app/"),
]

cols = st.columns(3)
for i, (icon, title, desc, url) in enumerate(APPS):
    with cols[i % 3]:
        st.markdown(f"""
        <div class="card">
            <div>
                <div class="icon">{icon}</div>
                <h3>{title}</h3>
                <p>{desc}</p>
            </div>
            <a class="btn" href="{url}" target="_blank">เปิดแอป →</a>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<p style='text-align:center;color:#5a6b8c;margin-top:30px;'>Made with Streamlit · Machine Learning Projects</p>", unsafe_allow_html=True)
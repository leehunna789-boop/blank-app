import streamlit as st
import time

# --- 1. UI Setup: ดำเงา #050505, ขอบม่วง, ฟังก์ชันแดง-น้ำเงิน ---
st.set_page_config(page_title="BigBoss GitHub Player", layout="wide")

st.markdown(f"""
    <style>
    .stApp {{
        background-color: #050505; /* สีที่ช่างใหญ่เลือก */
        color: white;
        border: 4px solid #8B00FF; /* ขอบม่วงไม่หนามาก */
        border-radius: 20px;
    }}
    
    /* หัวข้อและตัวหนังสือสีขาวเงา */
    h1, h2, h3, p {{
        color: #ffffff !important;
        text-shadow: 0px 0px 8px rgba(255,255,255,0.6);
    }}

    /* ฟังก์ชันภายใน: แดงนำ น้ำเงินตาม */
    .stSelectbox div[data-baseweb="select"] {{
        border: 2px solid #FF0000 !important; /* ขอบแดง */
        background-color: #001f3f !important; /* พื้นน้ำเงินเข้ม */
    }}

    /* ไฟกระพริบสถานะ */
    .status-dot {{
        height: 10px;
        width: 10px;
        background-color: #00FF00;
        border-radius: 50%;
        display: inline-block;
        box-shadow: 0 0 10px #00FF00;
        margin-right: 10px;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- 2. ส่วนหัว ---
st.title("📻 สถานีบำบัดใจ (GitHub Edition)")
st.markdown('<p><span class="status-dot"></span> ระบบเชื่อมต่อ GitHub สำเร็จ</p>', unsafe_allow_html=True)

# --- 3. ข้อมูลเพลงจาก GitHub ---
# ช่างใหญ่ครับ: เอา Link 'Raw' จาก GitHub มาวางใน list นี้ได้เลยครับ
songs = {
    "บทเพลงฮีลใจ 01": "https://raw.githubusercontent.com/ชื่อUser/ชื่อRepo/main/song1.mp3",
    "บทเพลงฮีลใจ 02": "https://raw.githubusercontent.com/ชื่อUser/ชื่อRepo/main/song2.mp3",
    "บทเพลงฮีลใจ 03": "https://raw.githubusercontent.com/ชื่อUser/ชื่อRepo/main/song3.mp3"
}

# ส่วนเลือกเพลง (UI น้ำเงิน-แดง)
selected_song_name = st.selectbox("เลือกเพลงจาก GitHub ของช่างใหญ่:", list(songs.keys()))
song_url = songs[selected_song_name]

# --- 4. เครื่องเล่นเพลงและการต่อเพลง 10 วิ ---
st.audio(song_url)

st.divider()
st.markdown("### 🔄 ฟังก์ชันการต่อเพลง (Transition)")
st.write("⏱️ *ระบบเตรียมความเนียน 10 วินาที เพื่อรอยต่อที่สมบูรณ์*")

# กราฟิกแสดงการ Fade (สีน้ำเงิน-แดง)
col_a, col_b = st.columns(2)
with col_a:
    st.markdown('<div style="background:#FF0000; padding:10px; border-radius:10px; text-align:center;">🔴 Fade Out (10s)</div>', unsafe_allow_html=True)
with col_b:
    st.markdown('<div style="background:#0000FF; padding:10px; border-radius:10px; text-align:center;">🔵 Next Track Sync</div>', unsafe_allow_html=True)

# --- 5. ท้ายแอป ---
st.write("")
st.write("---")
st.markdown("<h4 style='text-align: center; color: white;'>..ฟังเพลงอยู่นิ้งๆไม่เจ็บตัว..ตลอด 24 ชั่วโมง..</h4>", unsafe_allow_html=True)

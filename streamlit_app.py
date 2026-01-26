import streamlit as st
import os

# --- 1. UI Setup: ดำเงา #050505, ขอบม่วง, ตัวหนังสือขาวเงา ---
st.set_page_config(page_title="BigBoss Healing V2", layout="wide")

st.markdown("""
    <style>
    .stApp {
        background-color: #050505; 
        color: white;
        border: 3px solid #8B00FF; 
        border-radius: 15px;
    }
    h1, h2, h3, p, span {
        color: #ffffff !important;
        text-shadow: 0px 0px 10px rgba(255,255,255,0.8);
    }
    .stSelectbox div[data-baseweb="select"] {
        border: 2px solid #FF0000 !important; 
        background-color: #000080 !important; 
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. ส่วนหัวและโลโก้ Globe ---
col1, col2, col3 = st.columns([1,1,1])
with col2:
    try:
        st.image("globe.jpg", width=180)
    except:
        st.markdown("<h1 style='text-align:center;'>🌐</h1>", unsafe_allow_html=True)

st.markdown("<h2 style='text-align:center;'>สถานีบำบัดใจโดยช่างใหญ่</h2>", unsafe_allow_html=True)

# --- 3. แก้ไขจุดที่ Error (SONG_LIST) ---
# ช่างใหญ่ครับ: ผมใส่ชื่อเพลงและครอบฟันหนูให้แล้ว 
# เปลี่ยน 'ชื่อไฟล์เพลง.mp3' เป็นชื่อไฟล์จริงๆ ใน GitHub ของช่างใหญ่นะครับ
SONG_LIST = {
    "บทเพลงฮีลใจของช่างใหญ่": "https://raw.githubusercontent.com/leehunna789-boop/blank-app/main/ชื่อไฟล์เพลง.mp3"
}

st.write("---")
selected_song = st.selectbox("💿 เลือกบทเพลงบรรเลง:", list(SONG_LIST.keys()))

# เล่นเพลง (บินแน่นอน)
audio_url = SONG_LIST[selected_song]
st.audio(audio_url, format="audio/mp3")

# --- 4. ส่วนสำหรับเพื่อนๆ อัพโหลดไฟล์ ---
st.divider()
st.subheader("📸 ร่วมแบ่งปันภาพความสุขของคุณ")
uploaded_files = st.file_uploader(
    "เลือกไฟล์รูปภาพหรือวิดีโอจากเครื่องคุณ:",
    type=['png', 'jpg', 'jpeg', 'mp4'],
    accept_multiple_files=True
)

if uploaded_files:
    cols = st.columns(2)
    for index, file in enumerate(uploaded_files):
        with cols[index % 2]:
            if file.type.startswith('image'):
                st.image(file, use_container_width=True)
            elif file.type.startswith('video'):
                st.video(file)

# --- 5. ตัวหนังสือวิ่ง ---
st.markdown("""
    <div style="background: rgba(255,255,255,0.1); padding: 5px; border-top: 2px solid #8B00FF; margin-top:20px;">
        <marquee scrollamount="7" style="color: white; font-weight: bold;">
            ..ฟังเพลงอยู่นิ้งๆไม่เจ็บตัว..ตลอด 24 ชั่วโมง... ✨ 🟢 ✨ สร้างความสงบสุข ฮิวใจนิดๆ โดยช่างใหญ่...
        </marquee>
    </div>
    """, unsafe_allow_html=True)

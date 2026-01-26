import streamlit as st

# --- 1. UI Setup: ดำเงา #050505, ขอบม่วง, ตัวหนังสือขาวเงา ---
st.set_page_config(page_title="BigBoss Healing V3", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #050505; color: white; border: 4px solid #8B00FF; border-radius: 20px; }
    h1, h2, h3, p { color: white !important; text-shadow: 0px 0px 10px rgba(255,255,255,0.8); }
    /* กล่องลากไฟล์เพลง (สีน้ำเงิน-แดง) */
    .stFileUploader section { border: 2px dashed #FF0000 !important; background-color: #000080 !important; color: white !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. ส่วนหัวและโลโก้ ---
col1, col2, col3 = st.columns([1,1,1])
with col2:
    try: st.image("globe.jpg", width=180)
    except: st.title("🌐")
st.markdown("<h2 style='text-align:center;'>สถานีบำบัดใจ: อยู่นิ้งๆไม่่เจ็บตัว</h2>", unsafe_allow_html=True)


# --- 5. ตัวหนังสือวิ่ง Marquee ---
st.markdown('<div style="border-top:2px solid #8B00FF; margin-top:20px;"><marquee scrollamount="8" style="color:white; font-weight:bold; padding:10px;">..ลากเพลงลงร่อง..ฟังเพลงอยู่นิ้งๆไม่เจ็บตัว..ตลอด 24 ชั่วโมง... ✨ 🟢 ✨ โดยช่างใหญ่...</marquee></div>', unsafe_allow_html=True)

# --- 3. Logic: เครื่องเล่นเพลงแบบลากวาง ---
st.write("---")
st.markdown("### 🎵 ลากไฟล์เพลง .mp3 ของช่างใหญ่มาวางที่นี่")
# รองรับการลากทีละหลายเพลง (สูงสุด 20 เพลงตามที่ช่างใหญ่ต้องการ)
uploaded_songs = st.file_uploader("ลากไฟล์เพลงจากเครื่องมาวางได้เลยครับ (MP3)", type=['mp3'], accept_multiple_files=True)

if uploaded_songs:
    # สร้างรายการชื่อเพลงให้เลือกเล่น
    song_names = [song.name for song in uploaded_songs]
    selected_song_name = st.selectbox("💿 เลือกเพลงที่จะเล่นตอนนี้:", song_names)
    
    # ค้นหาไฟล์ที่เลือกและเล่น
    for song in uploaded_songs:
        if song.name == selected_song_name:
            st.audio(song, format="audio/mp3", autoplay=True)
            st.success(f"กำลังเล่นร่องเพลง: {song.name}")
else:
    st.warning("⚠️ ยังไม่มีเพลงในเครื่องเล่น... ช่างใหญ่ลากไฟล์เพลงมาวางได้เลยครับ!")

# --- 4. ส่วนสำหรับเพื่อนๆ (รูปภาพ/วิดีโอ) ---
st.divider()
st.subheader("📸 พื้นที่แชร์ภาพความสุข")
uploaded_media = st.file_uploader("ลากรูปภาพหรือวิดีโอมาวาง:", type=['png', 'jpg', 'jpeg', 'mp4'], accept_multiple_files=True, key="media")

if uploaded_media:
    cols = st.columns(2)
    for i, file in enumerate(uploaded_media):
        with cols[i % 2]:
            if file.type.startswith('image'): st.image(file, use_container_width=True)
            else: st.video(file)

# --- 5. ตัวหนังสือวิ่ง Marquee ---
st.markdown('<div style="border-top:2px solid #8B00FF; margin-top:20px;"><marquee scrollamount="8" style="color:white; font-weight:bold; padding:10px;">..ลากเพลงลงร่อง..ฟังเพลงอยู่นิ้งๆไม่เจ็บตัว..ตลอด 24 ชั่วโมง... ✨ 🟢 ✨ โดยช่างใหญ่...</marquee></div>', unsafe_allow_html=True)

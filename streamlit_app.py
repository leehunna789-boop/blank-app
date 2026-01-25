import streamlit as st
import os
import base64

# 1. ตั้งค่าหน้าจอแบบ Full Dark Mode
st.set_page_config(page_title="MUSIC 6D - NEW UI", layout="wide", initial_sidebar_state="collapsed")

# 2. CSS ขั้นเทพ: เน้นความหรูหรา แดง-น้ำเงิน-ทอง
st.markdown("""
    <style>
    .stApp { background: linear-gradient(180deg, #000 0%, #111 100%); color: #fff; }
    header, footer, [data-testid="stToolbar"] {visibility:hidden !important;}
    
    /* กรอบลูกโลกแบบใหม่: ทรงกลมในกรอบสี่เหลี่ยม */
    .main-monitor {
        border: 8px double #FF0000;
        border-right-color: #0000FF;
        border-bottom-color: #0000FF;
        border-radius: 50px;
        width: 100%;
        height: 420px;
        background: radial-gradient(circle, #222 0%, #000 100%);
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        box-shadow: 0 0 50px rgba(255, 0, 0, 0.3);
        margin-bottom: 30px;
        position: relative;
    }

    /* ตกแต่งรูปลูกโลกให้หมุนนิ่มๆ */
    .globe-style {
        width: 280px;
        height: 280px;
        border-radius: 50%;
        border: 5px solid #fff;
        box-shadow: 0 0 25px #0000FF;
        animation: rotateGlobe 15s linear infinite;
        object-fit: cover;
    }
    @keyframes rotateGlobe { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }

    /* ป้ายไฟสโลแกนแบบวิ่งเนียนๆ */
    .led-marquee {
        width: 100%;
        background: #FF0000;
        color: #fff;
        padding: 8px 0;
        font-size: 22px;
        font-weight: bold;
        text-transform: uppercase;
        letter-spacing: 2px;
        box-shadow: 0 5px 15px rgba(255,0,0,0.5);
    }

    /* กล่องควบคุมเพลง */
    .control-panel {
        background: #1a1a1a;
        border: 2px solid #333;
        border-radius: 20px;
        padding: 20px;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. ส่วนแสดงผลหลัก (Monitor) ---
st.markdown('<div class="main-monitor">', unsafe_allow_html=True)

# ดึงรูป globe.jpg มาใส่ในจอหลัก
if os.path.exists("globe.jpg"):
    with open("globe.jpg", "rb") as f:
        img_data = base64.b64encode(f.read()).decode()
    st.markdown(f'<img src="data:image/jpeg;base64,{img_data}" class="globe-style">', unsafe_allow_html=True)
else:
    st.markdown('<h1 style="color:#FF0000;">🌍 NO GLOBE FOUND</h1>', unsafe_allow_html=True)

st.markdown('<div style="margin-top:15px; font-size:20px; color:#0000FF; font-weight:bold;">SYSTEM ONLINE</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- 4. แถวสโลแกน (วิ่งพาดกลางจอ) ---
st.markdown('<div class="led-marquee"><marquee scrollamount="12">★ อยู่นิ่งๆ ไม่เจ็บตัว ★ MUSIC 6D PRODUCTION ★ สถานีความบันเทิง 24 ชั่วโมง ★</marquee></div>', unsafe_allow_html=True)

# --- 5. แผงควบคุมดีเจ ---
st.markdown('<div class="control-panel">', unsafe_allow_html=True)
col1, col2 = st.columns([1, 1])

with col1:
    st.write("### 💿 คลังเพลงของลูกพี่")
    music_files = [f for f in os.listdir('.') if f.endswith('.mp3')]
    if music_files:
        selected_song = st.selectbox("เลือกเพลงเพื่อเริ่มบรรเลง:", music_files)
        st.write(f"🎧 **Now Playing:** {selected_song}")
        st.audio(selected_song)
    else:
        st.error("⚠️ ยังไม่มีเพลงในคลัง (อัปไฟล์ .mp3 ลงหน้าหลัก GitHub)")

with col2:
    st.write("### 📸 มุมโชว์รูปจากเพื่อน")
    friend_pics = st.file_uploader("ส่งรูปมาโชว์บนบอร์ดได้เลยจ้า", type=['jpg','png','jpeg'], accept_multiple_files=True)

st.markdown('</div>', unsafe_allow_html=True)

# --- 6. แสดงรูปจากเพื่อน (Gallery) ---
if friend_pics:
    st.write("---")
    st.write("### 🔥 เพื่อนๆ กำลังแชร์รูป:")
    cols = st.columns(4)
    for idx, pic in enumerate(friend_pics):
        with cols[idx % 4]:
            st.image(pic, use_container_width=True)

st.write("---")
st.markdown("<center>MUSIC 6D - อยู่นิ่งๆ ไม่เจ็บตัว</center>", unsafe_allow_html=True)

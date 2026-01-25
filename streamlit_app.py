import streamlit as st
import os
import base64

# 1. ตั้งค่าหน้าจอ
st.set_page_config(page_title="MUSIC 6D PRO", layout="wide", initial_sidebar_state="collapsed")

# 2. CSS คาถาล็อกรูปเข้ากรอบ
st.markdown("""
    <style>
    .stApp { background-color: #000; color: #fff; }
    header, footer, [data-testid="stToolbar"] {display:none !important;}
    
    /* กรอบสี่เหลี่ยมหลัก (ที่ลูกพี่อยากให้รูปไปอยู่) */
    .display-screen {
        border: 15px solid #FF0000;
        border-right-color: #0000FF;
        border-bottom-color: #0000FF;
        border-radius: 45px;
        width: 100%;
        height: 400px;
        background: #111;
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
        position: relative;
        box-shadow: 0 0 30px #FF0000;
        margin-bottom: 20px;
    }

    /* บังคับรูปให้เต็มกรอบ */
    .display-screen img {
        width: 100%;
        height: 100%;
        object-fit: cover; /* ให้รูปเต็มกรอบพอดี ไม่เบี้ยว */
    }

    /* ตัวหนังสือวิ่งในจอ */
    .screen-text {
        position: absolute;
        bottom: 0;
        width: 100%;
        background: rgba(0,0,0,0.7);
        color: #FF0000;
        font-weight: bold;
        padding: 10px;
        font-size: 20px;
    }

    /* ปรับปุ่มอัปโหลดให้ดูเล็กลง ไม่เกะกะ */
    .stFileUploader { padding-top: 0px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. ส่วนควบคุม (เบื้องหลัง) ---
# ลูกพี่ลงเพลงใน GitHub ไว้เลยครับ
music_files = [f for f in os.listdir('.') if f.endswith('.mp3')]

# --- 4. ส่วนให้เพื่อนลงรูป ---
st.write("### 📸 เพื่อนลงรูปตรงนี้...")
friend_file = st.file_uploader("", type=['jpg','png','jpeg'], label_visibility="collapsed")

# --- 5. จอแสดงผล (กรอบสี่เหลี่ยมที่ลูกพี่ต้องการ) ---
st.markdown('<div class="display-screen">', unsafe_allow_html=True)

if friend_file:
    # แปลงรูปที่เพื่อนอัปโหลดเป็น Base64 เพื่อยัดเข้าในกรอบ HTML
    img_data = base64.b64encode(friend_file.read()).decode()
    st.markdown(f'<img src="data:image/png;base64,{img_data}">', unsafe_allow_html=True)
else:
    # ถ้ายังไม่มีรูป ให้โชว์ข้อความกะพริบในกรอบ
    st.markdown('<h2 style="color:#555; animation: blinker 1s infinite alternate;">รอรูปจากเพื่อน...</h2><style>@keyframes blinker { from {opacity: 1;} to {opacity: 0.3;} }</style>', unsafe_allow_html=True)

# ใส่ชื่อเพลงวิ่งในกรอบเลย (ถ้ามีเพลง)
if music_files:
    st.markdown('<div class="screen-text"><marquee scrollamount="8">🎶 อยู่นิ่งๆ ไม่เจ็บตัว... กำลังเตรียมเพลงให้เพื่อนฟัง... 🎧</marquee></div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# --- 6. ส่วนเล่นเพลงของลูกพี่ ---
st.title("🔴 MUSIC 6D - LOOK-PHEE")

if music_files:
    selected_song = st.selectbox("💿 เพื่อนๆ เลือกฟังเพลงที่นี่นะ:", music_files)
    st.audio(selected_song)
else:
    st.warning("⚠️ ลูกพี่ลืมลงเพลงใน GitHub หรือเปล่าครับ?")

st.markdown('---')
st.write("*สโลแกน: อยู่นิ่งๆ ไม่เจ็บตัว*")

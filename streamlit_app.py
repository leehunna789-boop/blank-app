import streamlit as st
import base64

# 1. ตั้งค่าหน้าจอและซ่อนส่วนเกิน
st.set_page_config(page_title="MUSIC 6D PRO", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    .stApp { background-color: #000; color: #fff; }
    header, footer, [data-testid="stToolbar"] {display:none !important;}
    
    /* กรอบสี่เหลี่ยมด้านบนสำหรับใส่รูปปก */
    .top-frame {
        border: 12px solid #FF0000;
        border-right-color: #0000FF;
        border-bottom-color: #0000FF;
        border-radius: 35px;
        padding: 10px;
        text-align: center;
        background: #000;
        box-shadow: 0 0 25px #FF0000;
        margin-bottom: 20px;
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
        min-height: 300px;
    }

    /* รูปปกในกรอบปรับให้พอดี */
    .cover-fit {
        max-width: 100%;
        max-height: 280px;
        border-radius: 20px;
        box-shadow: 0 0 15px #0000FF;
    }

    /* ตัวหนังสือวิ่งสโลแกน */
    .marquee-style {
        color: #FF0000;
        font-size: 26px;
        font-weight: bold;
        text-shadow: 0 0 10px #FF0000;
        background: #111;
        padding: 10px;
        border-radius: 10px;
        border: 2px solid #0000FF;
    }

    /* ไฟกะพริบ */
    .led-container { display: flex; justify-content: center; gap: 8px; margin-top: 15px; }
    .led-bulb { width: 30px; height: 12px; border-radius: 5px; background: #FF0000; animation: blinker 0.6s infinite alternate; }
    @keyframes blinker { from { opacity: 0.3; } to { opacity: 1; } }
    </style>
    """, unsafe_allow_html=True)

# --- ส่วนการจัดการไฟล์ ---
st.write("### ➕ ตั้งค่าเครื่องเล่น")
c1, c2 = st.columns(2)
with c1:
    uploaded_songs = st.file_uploader("🎵 อัปโหลดเพลง (หลายเพลงได้)", type=['mp3'], accept_multiple_files=True)
with c2:
    uploaded_cover = st.file_uploader("🖼️ อัปโหลดรูปปก", type=['jpg','png','jpeg'])

# --- ส่วนแสดงผลในกรอบ (ย้ายรูปปกมานี่) ---
st.markdown('<div class="top-frame">', unsafe_allow_html=True)
if uploaded_cover:
    # แสดงรูปปกที่อัปโหลด
    img_base64 = base64.b64encode(uploaded_cover.read()).decode()
    st.markdown(f'<img src="data:image/png;base64,{img_base64}" class="cover-fit">', unsafe_allow_html=True)
else:
    # ถ้ายังไม่มีรูปให้โชว์ข้อความ
    st.markdown('<h2 style="color:#555;">รออัปโหลดรูปปก...</h2>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- ชื่อแอปและสโลแกนวิ่ง ---
st.title("🔴 MUSIC 6D อยู่นิ้งๆไม่เจ็บตัว")
st.markdown('<div class="marquee-style"><marquee scrollamount="8">อยู่นิ่งๆ ไม่เจ็บตัว... เพลงเพราะถล่มโรงช่าง... จัดเต็มคุณภาพ HD...</marquee></div>', unsafe_allow_html=True)

# ไฟกะพริบเท่ๆ
st.markdown('<div class="led-container"><div class="led-bulb"></div><div class="led-bulb" style="background:#0000FF; animation-delay:0.2s;"></div><div class="led-bulb" style="animation-delay:0.4s;"></div></div>', unsafe_allow_html=True)

# --- ระบบเล่นเพลง ---
if uploaded_songs:
    st.write("---")
    # ทำรายการเลือกเพลง
    song_dict = {f.name: f for f in uploaded_songs}
    selected_song_name = st.selectbox("💿 เลือกเพลงจากคลังของคุณ:", list(song_dict.keys()))
    
    current_audio = song_dict[selected_song_name]
    st.success(f"กำลังเล่น: {selected_song_name}")
    
    # ตัวเล่นเพลงมาตรฐาน (เสถียรที่สุด)
    st.audio(current_audio)
else:
    st.info("กรุณาอัปโหลดเพลงเพื่อเริ่มความมันส์ครับลูกพี่!")

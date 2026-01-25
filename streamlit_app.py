import streamlit as st
import base64

# 1. ตั้งค่าหน้าจอ (กว้างสุด & ซ่อนทุกอย่าง)
st.set_page_config(page_title="MUSIC 6D FINAL EDITION", layout="wide", initial_sidebar_state="collapsed")

# 2. CSS สายดุดันขั้นสุด (แดง-ดำ-น้ำเงิน-ขาว, ขอบหนา, ไฟกะพริบ, ตัวหนังสือวิ่ง)
st.markdown("""
    <style>
    /* พื้นหลังดำสนิท ตัวหนังสือขาว */
    .stApp { background-color: #000; color: #fff; }
    /* ซ่อน Header, Footer, Streamlit Toolbar ให้เนียนกริบ */
    header, footer, [data-testid="stToolbar"], .stDeployButton {display:none !important;}
    
    /* กรอบหลัก: หนา 15px แดงเงา แสงเรืองน้ำเงิน */
    .main-frame {
        border: 15px solid #FF0000; 
        border-radius: 40px;
        padding: 40px;
        box-shadow: 0 0 50px #0000FF, inset 0 0 20px #8B0000; /* เงาด้านนอกน้ำเงิน ด้านในแดงเข้ม */
        background: linear-gradient(145deg, #1a1a1a, #000000); /* ไล่สีพื้นหลังมีมิติ */
        animation: border-glow 3s infinite alternate; /* แสงขอบกะพริบ */
    }

    /* แอนิเมชั่นขอบเรืองแสง */
    @keyframes border-glow {
        0% { box-shadow: 0 0 50px #0000FF, inset 0 0 20px #8B0000; }
        100% { box-shadow: 0 0 60px #42a7ff, inset 0 0 25px #ff4500; }
    }
    
    /* รูปปกหมุนและมีขอบน้ำเงินเรืองแสง */
    .album-art {
        border: 10px solid #0000FF;
        border-radius: 50%;
        animation: spin 8s linear infinite, glow 2s infinite alternate; /* หมุน + เรืองแสง */
        display: block;
        margin: 0 auto 30px auto; /* จัดกลาง */
    }
    @keyframes spin { 100% { transform:rotate(360deg); } }
    @keyframes glow {
        0% { box-shadow: 0 0 15px #0000FF; }
        100% { box-shadow: 0 0 25px #42a7ff; }
    }

    /* ตัวหนังสือวิ่ง (Marquee) */
    .marquee-container {
        width: 100%;
        overflow: hidden;
        white-space: nowrap;
        box-sizing: border-box;
        border: 2px solid #0000FF; /* ขอบน้ำเงิน */
        border-radius: 10px;
        padding: 10px;
        background: #111;
        margin-bottom: 20px;
    }
    .marquee-text {
        display: inline-block;
        padding-left: 100%;
        animation: marquee 15s linear infinite; /* วิ่ง 15 วิ */
        font-size: 28px;
        font-weight: bold;
        color: #FF0000; /* สีแดง */
        text-shadow: 0 0 5px #ff4500;
    }
    @keyframes marquee {
        0%   { transform: translate(0, 0); }
        100% { transform: translate(-100%, 0); }
    }

    /* ไฟกระพริบ Visualizer (UI Effect) */
    .visualizer-bar {
        height: 15px;
        background: linear-gradient(to right, #0000FF, #FF0000);
        border-radius: 5px;
        margin: 5px 0;
        animation: visualize 0.5s infinite alternate; /* กะพริบเร็ว */
        opacity: 0.8;
    }
    @keyframes visualize {
        0% { transform: scaleX(0.1); opacity: 0.5; }
        100% { transform: scaleX(1); opacity: 1; }
    }

    /* ปุ่มเล่นเพลงใหญ่พิเศษ */
    .play-button {
        background: linear-gradient(135deg, #FF0000 0%, #8B0000 100%);
        color: white;
        border: 5px solid #FFFFFF;
        border-radius: 20px;
        padding: 20px 60px;
        font-size: 36px;
        font-weight: bold;
        box-shadow: 0 0 30px #FF0000;
        cursor: pointer;
        transition: 0.3s;
        display: block; /* ทำให้เป็นบล็อกเพื่อจัดกลาง */
        margin: 30px auto;
        width: fit-content;
    }
    .play-button:hover {
        box-shadow: 0 0 40px #0000FF;
        transform: scale(1.05);
    }
    </style>
    """, unsafe_allow_html=True)

# --- โครงสร้างแอป ---
st.markdown('<div class="main-frame">', unsafe_allow_html=True)
st.title("🔴 MUSIC อยู่นิ้งๆไม่เจ็บตัว.")
st.markdown("### *<span style='color:#0000FF; text-shadow: 0 0 10px #0000FF;'>อยู่นิ่งๆ ไม่เจ็บตัว...</span>*", unsafe_allow_html=True)

# 3. ส่วนอัปโหลด
col1, col2 = st.columns(2)
with col1:
    songs = st.file_uploader("🎵 เลือกเพลง (MP3)", type=['mp3'], accept_multiple_files=True)
with col2:
    cover = st.file_uploader("🖼️ เลือกรูปปก", type=['jpg','png','jpeg'])

st.markdown("---") # เส้นคั่น

# 4. แสดงผลเพลงและปก
if songs:
    song_names = [f.name for f in songs]
    
    # เลือกเพลงปัจจุบัน (ถ้าไม่มี ให้เลือกเพลงแรก)
    if 'current_song_idx' not in st.session_state:
        st.session_state.current_song_idx = 0

    selected_song_obj = songs[st.session_state.current_song_idx]

    # รูปปกหมุน
    if cover:
        st.image(cover, width=250, use_column_width=False, output_format="PNG", caption="", 
                 clamp=False, channels="RGB", format="PNG", class_name="album-art")
    else:
        # รูปไอคอนถ้าไม่มีปก
        st.markdown('<img src="https://cdn-icons-png.flaticon.com/512/26/26433.png" class="album-art" style="width:250px;">', unsafe_allow_html=True)
    
    # ตัวหนังสือวิ่งชื่อเพลง
    st.markdown(f'<div class="marquee-container"><div class="marquee-text">{selected_song_obj.name}</div></div>', unsafe_allow_html=True)
    
    # ไฟกระพริบ Visualizer (UI เท่ๆ)
    st.markdown('<div class="visualizer-bar"></div>', unsafe_allow_html=True)
    st.markdown('<div class="visualizer-bar" style="transform: scaleX(0.7); animation-delay: -0.2s;"></div>', unsafe_allow_html=True)
    st.markdown('<div class="visualizer-bar" style="transform: scaleX(0.5); animation-delay: -0.4s;"></div>', unsafe_allow_html=True)

    # ปุ่ม Play/Pause
    play_button_text = "เล่น / หยุด"
    if st.button(play_button_text, key="play_pause_button", help="คลิกเพื่อเล่น/หยุดเพลง", class_name="play-button"):
        # สำหรับ Streamlit การเล่นต้องใช้ st.audio()
        pass # ปุ่มนี้จะ trigger การเล่นจาก st.audio ด้านล่าง
    
    # ปุ่มเปลี่ยนเพลง
    col_nav1, col_nav2 = st.columns(2)
    with col_nav1:
        if st.button("⏮️ เพลงก่อนหน้า", key="prev_song"):
            st.session_state.current_song_idx = (st.session_state.current_song_idx - 1) % len(songs)
            st.rerun()
    with col_nav2:
        if st.button("เพลงถัดไป ⏭️", key="next_song"):
            st.session_state.current_song_idx = (st.session_state.current_song_idx + 1) % len(songs)

import streamlit as st
import os
import base64

# 1. ตั้งค่าหน้าจอ (ปิดขอบขาว ซ่อนเมนู)
st.set_page_config(page_title="MUSIC 6D PRO", layout="wide", initial_sidebar_state="collapsed")

# 2. CSS สายโหด: ล็อกรูปเข้ากรอบ + ปรับแต่ง Font
st.markdown("""
    <style>
    .stApp { background-color: #000; color: #fff; }
    header, footer, [data-testid="stToolbar"] {visibility:hidden !important;}
    
    /* กรอบสี่เหลี่ยมทีวีหลัก */
    .tv-display {
        border: 15px solid #FF0000;
        border-right: 15px solid #0000FF;
        border-bottom: 15px solid #0000FF;
        border-radius: 40px;
        width: 100%;
        height: 380px;
        background: #000;
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
        box-shadow: 0 0 35px #FF0000;
        margin-bottom: 15px;
    }

    /* บังคับลูกโลกให้เต็มกรอบ */
    .tv-display img {
        width: 100%;
        height: 100%;
        object-fit: cover; /* ให้รูปเต็มกรอบพอดี */
    }

    /* ตัวหนังสือวิ่ง */
    .marquee-style {
        background: #111;
        border: 2px solid #0000FF;
        border-radius: 12px;
        padding: 12px;
        color: #FF0000;
        font-size: 26px;
        font-weight: bold;
        margin-bottom: 20px;
    }

    /* ตกแต่งช่องเลือกเพลง */
    .stSelectbox div[data-baseweb="select"] {
        background-color: #111 !important;
        border: 2px solid #0000FF !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. จอ TV หลัก (ดึงลูกโลกขึ้นมาโชว์) ---
st.markdown('<div class="tv-display">', unsafe_allow_html=True)

# ใช้เทคนิค Base64 เพื่อบังคับให้รูปแสดงในตำแหน่งที่ต้องการ
if os.path.exists("globe.jpg"):
    with open("globe.jpg", "rb") as f:
        data = base64.b64encode(f.read()).decode()
    st.markdown(f'<img src="data:image/jpeg;base64,{data}">', unsafe_allow_html=True)
else:
    st.markdown('<h1 style="color:#555;">รอไฟล์ globe.jpg...</h1>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# --- 4. ตัวหนังสือวิ่งสไตล์ลูกพี่ ---
st.markdown('<div class="marquee-style"><marquee scrollamount="12">อยู่นิ่งๆ ไม่เจ็บตัว... คลังเพลง HD ของลูกพี่... ยินดีต้อนรับเพื่อนๆ ทุกคน!</marquee></div>', unsafe_allow_html=True)

# --- 5. เครื่องเล่นเพลง (ดึงจาก GitHub 5 เพลงที่ลูกพี่ลงไว้) ---
music_files = [f for f in os.listdir('.') if f.endswith('.mp3')]

if music_files:
    st.markdown(f"### 💿 มีเพลงทั้งหมด {len(music_files)} เพลง")
    selected_song = st.selectbox("เลือกเพลงที่ต้องการฟัง:", music_files)
    
    st.markdown(f"#### 🎧 กำลังบรรเลง: <span style='color:#0000FF;'>{selected_song}</span>", unsafe_allow_html=True)
    st.audio(selected_song)
else:
    st.warning("⚠️ ไม่พบไฟล์เพลงใน GitHub ครับลูกพี่")

# --- 6. มุมเพื่อนโชว์รูป (ไว้ข้างล่างสุด) ---
st.write("---")
st.subheader("📸 มุมเพื่อนโชว์รูป (รูปจะอยู่ด้านล่างตรงนี้จ้า)")
friend_pics = st.file_uploader("ลงรูปโชว์กันตรงนี้จ้า", type=['jpg','png','jpeg'], accept_multiple_files=True)

if friend_pics:
    for pic in friend_pics:
        st.image(pic, use_container_width=True)

st.write("#### *สโลแกน: อยู่นิ่งๆ ไม่เจ็บตัว*")

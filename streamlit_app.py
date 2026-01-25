import streamlit as st
import os
import base64

# 1. ตั้งค่าหน้าจอ
st.set_page_config(page_title="MUSIC 6D PRO", layout="wide", initial_sidebar_state="collapsed")

# 2. CSS คาถาล็อกรูปและจัดระเบียบ
st.markdown("""
    <style>
    .stApp { background-color: #000; color: #fff; }
    header, footer, [data-testid="stToolbar"] {visibility:hidden !important;}
    
    /* กรอบลูกโลกหลัก */
    .tv-display {
        border: 15px solid #FF0000;
        border-right: 15px solid #0000FF;
        border-bottom: 15px solid #0000FF;
        border-radius: 40px;
        width: 100%;
        height: 350px;
        background: #000;
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
        box-shadow: 0 0 30px #FF0000;
        margin-bottom: 20px;
    }
    .tv-display img { max-width: 100%; max-height: 100%; object-fit: contain; }

    /* ปรับแต่งช่องเลือกเพลง (Selectbox) */
    .stSelectbox [data-baseweb="select"] {
        background-color: #111 !important;
        border: 2px solid #0000FF !important;
        color: #fff !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. จอทีวีลูกโลก
st.markdown('<div class="tv-display">', unsafe_allow_html=True)
if os.path.exists("globe.jpg"):
    with open("globe.jpg", "rb") as f:
        img_b64 = base64.b64encode(f.read()).decode()
    st.markdown(f'<img src="data:image/jpeg;base64,{img_b64}">', unsafe_allow_html=True)
else:
    st.markdown('<h1 style="color:#FF0000;">MUSIC 6D</h1>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# 4. ตัวหนังสือวิ่ง
st.markdown('<marquee scrollamount="10" style="color:#FF0000; font-size:24px; font-weight:bold;">อยู่นิ่งๆ ไม่เจ็บตัว... คลังเพลง HD ของลูกพี่จัดเต็มครับ!</marquee>', unsafe_allow_html=True)

# 5. ค้นหาและแสดงรายชื่อเพลง
music_files = [f for f in os.listdir('.') if f.endswith('.mp3')]

if music_files:
    st.write(f"### 💿 มีเพลงทั้งหมด {len(music_files)} เพลง")
    # ช่องเลือกเพลงแบบ Dropdown (ต่อให้มี 100 เพลงก็ไม่รก เพราะต้องกดลงมาดู)
    selected_song = st.selectbox("เลือกเพลงที่ต้องการฟัง:", music_files)
    
    st.write(f"🎧 **กำลังบรรเลง:** {selected_song}")
    st.audio(selected_song)
else:
    st.error("⚠️ ยังไม่มีเพลงในคลังครับลูกพี่ โยนไฟล์ .mp3 เข้า GitHub ได้เลย!")

# 6. มุมเพื่อนโชว์รูป
st.write("---")
st.subheader("📸 มุมเพื่อนโชว์รูป")
friend_pics = st.file_uploader("ลงรูปโชว์กันตรงนี้จ้า", type=['jpg','png','jpeg'], accept_multiple_files=True)
if friend_pics:
    for pic in friend_pics:
        st.image(pic, use_container_width=True)

st.markdown('<p style="text-align:center;">อยู่นิ่งๆ ไม่เจ็บตัว</p>', unsafe_allow_html=True)

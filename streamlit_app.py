import streamlit as st
import os

# 1. ตั้งค่าหน้าจอ
st.set_page_config(page_title="MUSIC 6D PRO", layout="wide", initial_sidebar_state="collapsed")

# 2. CSS สายโหด: ล็อกรูปเข้ากรอบสี่เหลี่ยม
st.markdown("""
    <style>
    .stApp { background-color: #000; color: #fff; }
    header, footer, [data-testid="stToolbar"] {visibility:hidden !important;}
    
    /* กรอบสี่เหลี่ยมด้านบน (ล็อกรูปไว้ข้างใน) */
    .tv-frame {
        border: 15px solid #FF0000;
        border-right-color: #0000FF;
        border-bottom-color: #0000FF;
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

    /* บังคับรูปในกรอบให้พอดี */
    .tv-frame img {
        max-width: 100%;
        max-height: 100%;
        object-fit: contain;
    }

    /* สไตล์ตัวหนังสือวิ่ง */
    .marquee-box {
        background: #111;
        border: 2px solid #0000FF;
        border-radius: 10px;
        padding: 10px;
        color: #FF0000;
        font-size: 24px;
        font-weight: bold;
    }

    /* ปรับช่องอัปโหลดให้ดูเนียนขึ้น */
    .stFileUploader { margin-top: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. จอ TV หลัก (ที่ลูกพี่อยากให้ลูกโลกอยู่) ---
st.markdown('<div class="tv-frame">', unsafe_allow_html=True)

# ดึงรูปลูกโลกมาแสดง (ลูกพี่อัปรูปชื่อ globe.jpg หรือ globe.png ไว้ใน GitHub นะครับ)
globe_files = [f for f in os.listdir('.') if f.lower().startswith('globe')]

if globe_files:
    # ถ้ามีรูปลูกโลกใน GitHub ให้ดึงมาใส่ในกรอบทันที
    st.image(globe_files[0])
else:
    # ถ้ายังไม่มีรูปลูกโลก ให้โชว์ชื่อแอปเท่ๆ รอไว้
    st.markdown('<h1 style="color:#FF0000; text-shadow: 0 0 10px #FF0000;">MUSIC 6D STATION</h1>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# --- 4. ชื่อแอปและสโลแกนวิ่ง ---
st.markdown('<div class="marquee-box"><marquee scrollamount="10">อยู่นิ่งๆ ไม่เจ็บตัว... คลังเพลง HD ของลูกพี่... เพื่อนๆ ลงรูปด้านล่างได้เลย!</marquee></div>', unsafe_allow_html=True)

# --- 5. ระบบเครื่องเล่นเพลงของลูกพี่ ---
music_list = [f for f in os.listdir('.') if f.endswith('.mp3')]

if music_list:
    st.subheader("💿 เลือกเพลงที่ลูกพี่ลงไว้")
    choice = st.selectbox("", music_list)
    st.audio(choice)
else:
    st.error("⚠️ ลูกพี่อย่าลืมอัปเพลง .mp3 ลง GitHub นะครับ!")

# --- 6. ส่วนของเพื่อน: ลงรูปไว้ด้านล่าง ---
st.write("---")
st.subheader("📸 มุมเพื่อนโชว์รูป (รูปจะอยู่ด้านล่างตรงนี้)")
friend_pics = st.file_uploader("เพื่อนๆ เลือกรูปจากมือถือมาลงได้เลยจ้า", type=['jpg','png','jpeg'], accept_multiple_files=True)

if friend_pics:
    # แสดงรูปที่เพื่อนลงแบบเรียงกันสวยๆ
    for pic in friend_pics:
        st.image(pic, use_container_width=True)

st.write("### *สโลแกน: อยู่นิ่งๆ ไม่เจ็บตัว*")

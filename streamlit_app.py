import streamlit as st
import streamlit.components.v1 as components

# 1. ตั้งค่าหน้าสถานี
st.set_page_config(page_title="สถานีเพลงฟังสบายใจ ขอเพลงได้ อยู่นิ้งไม่เจ็บตัว", page_icon="🌍", layout="centered")

# 2. แต่ง UI สีมืด-ทอง
st.markdown("""
    <style>
    .stApp {
        background-color: #050505;
        color: #FFFFFF;
        text-align: center;
    }
    div.stButton > button {
        background-color: #00B900;
        color: white;
        border-radius: 20px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. ดึงรูปภาพ (เช็คชื่อไฟล์ globe.jpg ให้ตรงกับใน GitHub นะครับ)
try:
    st.image("globe.jpg", width=300)
except:
    st.header("🌍")

# 4. ชื่อสถานี
st.markdown("<h2 style='color: #FFD700;'>📻 STATION: อยู่นิ้งๆไม่เจ็บตัว</h2>", unsafe_allow_html=True)
st.write("คัดมาให้แล้ว เพลงเน้นๆ เพื่อเพื่อนๆ")
st.write("---")
# --- [ส่วนของตัวหนังสือวิ่ง] ---
st.markdown("""
    <style>
    .marquee-container {
        width: 100%;
        overflow: hidden;
        white-space: nowrap;
        background: #1A0000; /* สีพื้นหลังแถบวิ่ง */
        padding: 10px 0;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .marquee-text {
        display: inline-block;
        padding-left: 100%;
        color: white;
        font-weight: bold;
        font-size: 1.1rem;
        animation: marquee 20s linear infinite;
    }
    @keyframes marquee {
        0%   { transform: translate(0, 0); }
        100% { transform: translate(-100%, 0); }
    }
    </style>
    <div class="marquee-container">
        <div class="marquee-text">
            📢 ยินดีต้อนรับเข้าสู่สถานี อยู่นิ่งๆ ไม่เจ็บตัว ...บอกเรื่องราวชีวิตมาได้เลย เดวจัดเพลงของคุณให้ฟัง ขอเพลงกันเข้ามาได้เลยครับ! 🎵 
            ทีมงานอยู่่นิ้งๆไม่เจ็บตัว กำลังจัดเตรียมเพลงให้คุณอยู่ 🎧 ขอบคุณที่ติดตามรับฟังครับ ✨
        </div>
    </div>
    """, unsafe_allow_html=True)


# 5. วิธีใหม่: ฝัง YouTube Player (วิธีนี้จะขึ้นแน่นอน 100%)
# ผมใช้ ID เพลย์ลิสต์ของช่างใหญ่โดยตรงเลยครับ
st.subheader("📺 รายการเพลง (กดฟังยาว ต่อเนื้อง24 ชม อัปเด็ดตลอดเวลา)")
playlist_id = "PL6S211I3urvpt47sv8mhbexif2YOzs2gO"
embed_code = f"""
<iframe width="100%" height="400" src="https://www.youtube.com/embed/videoseries?list={playlist_id}" 
title="YouTube video player" frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
allowfullscreen></iframe>
"""
components.html(embed_code, height=450)

# 6. ปุ่ม LINE (เปลี่ยน YOUR_ID เป็นไอดีไลน์ช่างใหญ่นะครับ)
st.write("---")
line_id = "ta0970801941" 
st.link_button("➖ แตะ LINE ถามได้ทุกเรื่อง คุยโดยตรง", f"https://line.me/ti/p/~{line_id}")

# 7. ปิดท้าย
st.caption("© 2026 สถานีเพลงฟังสบายใจ | อยู่นิ้งๆ ไม่เจ็บตัว")

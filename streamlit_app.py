import streamlit as st
import os

# 1. ตั้งค่าหน้าจอ (เน้นความกว้างและซ่อนเมนู)
st.set_page_config(page_title="MUSIC 6D - DJ LOOK-PHEE", layout="wide", initial_sidebar_state="collapsed")

# 2. CSS สายโหด: เน้นกรอบรูปของเพื่อนให้เด่นที่สุด
st.markdown("""
    <style>
    .stApp { background-color: #000; color: #fff; }
    header, footer, [data-testid="stToolbar"] {visibility:hidden !important;}
    
    /* กรอบสี่เหลี่ยมด้านบนสำหรับโชว์รูปเพื่อน */
    .top-frame {
        border: 15px solid #FF0000;
        border-right: 15px solid #0000FF;
        border-bottom: 15px solid #0000FF;
        border-radius: 40px;
        padding: 5px;
        text-align: center;
        background: #111;
        box-shadow: 0 0 40px #FF0000;
        margin-bottom: 20px;
        min-height: 350px;
        display: flex;
        justify-content: center;
        align-items: center;
        overflow: hidden;
    }

    /* ตัวหนังสือวิ่ง */
    .marquee-style {
        background: #000;
        border: 3px solid #0000FF;
        border-radius: 12px;
        padding: 10px;
        color: #FF0000;
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 20px;
    }

    /* ปุ่มอัปโหลดรูปของเพื่อน (ปรับให้ดูเท่) */
    .stFileUploader section {
        background-color: #111 !important;
        border: 2px dashed #FF0000 !important;
        color: #fff !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. ส่วนกรอบบน: โชว์รูปที่เพื่อนอัปโหลด ---
# เราจะสร้างพื้นที่โชว์รูปไว้ก่อน
st.markdown('<div class="top-frame">', unsafe_allow_html=True)

# รับรูปจากเพื่อน (เพื่อนเลือกรูปจากมือถือได้เลย)
friend_pic = st.file_uploader("📸 เพื่อนๆ ลงรูปที่อยากให้ขึ้นจอตรงนี้จ้า", type=['jpg','png','jpeg'])

if friend_pic:
    st.image(friend_pic, use_container_width=True)
else:
    st.markdown('<h2 style="color:#444;">ส่งรูปมาโชว์บนจอสิเพื่อน!<br>เพลงเด็ดรออยู่แล้ว</h2>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- 4. ชื่อแอปและสโลแกนวิ่ง ---
st.title("🔴 MUSIC 6D - LOOK-PHEE STATION")
st.markdown('<div class="marquee-style"><marquee scrollamount="12">อยู่นิ่งๆ ไม่เจ็บตัว... เพลงคัดโดยลูกพี่... รูปโชว์โดยเพื่อนๆ... ฟังเพลง HD กันยาวๆ!</marquee></div>', unsafe_allow_html=True)

# --- 5. ระบบคลังเพลงของลูกพี่ (ดึงจาก GitHub) ---
# ลูกพี่เอาไฟล์ .mp3 ไปวางคู่กับโค้ดนี้ใน GitHub ได้เลยครับ
music_list = [f for f in os.listdir('.') if f.endswith('.mp3')]

if music_list:
    st.write("### 💿 เลือกเพลงจากคลังของลูกพี่")
    song_choice = st.selectbox("", music_list)
    
    st.markdown(f"#### 🎧 กำลังบรรเลง: <span style='color:#0000FF;'>{song_choice}</span>", unsafe_allow_html=True)
    st.audio(song_choice)
else:
    st.info("⚠️ ลูกพี่ครับ ลงเพลงใน GitHub หน่อย เพื่อนๆ รอฟังอยู่!")

st.write("---")
st.caption("แอปนี้สร้างมาเพื่อเพื่อน: อยู่นิ่งๆ ไม่เจ็บตัว")

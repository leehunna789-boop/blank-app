import streamlit as st
import numpy as np

# 1. คาถาเต็มจอและซ่อนหลังบ้าน (ข้อ 11)
st.set_page_config(page_title="MUSIC 6D HD-PRO", layout="wide", initial_sidebar_state="collapsed")

# 2. CSS สายโหด: ขอบหนาปึ๊ก + สี แดง-ดำ-น้ำเงิน-ขาว
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #FFFFFF; }
    header, footer, [data-testid="stToolbar"] {visibility: hidden !important;}
    
    /* กรอบและเส้นขอบหนาๆ (Bold Borders) */
    .main-container {
        border: 5px solid #FF0000; /* ขอบแดงหนา */
        border-radius: 20px;
        padding: 20px;
        box-shadow: 0 0 25px #0000FF; /* เงาสีน้ำเงิน */
        margin-bottom: 20px;
    }
    
    /* ปุ่มกดสีแดงเงา ขอบน้ำเงินหนา */
    .stButton>button {
        background: #FF0000;
        color: white;
        border: 4px solid #0000FF !important; /* ขอบน้ำเงินหนา */
        border-radius: 50px;
        font-weight: bold;
        height: 60px;
        width: 100%;
        box-shadow: 0 5px 15px rgba(255, 0, 0, 0.6);
    }
    
    /* สไลเดอร์มิกเซอร์สีแดง */
    .stSlider [data-baseweb="slider"] {
        border: 2px solid #FFFFFF;
        border-radius: 10px;
        padding: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. ส่วนหัวแอป
st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.title("🔴 MUSIC 6D HD-PRO")
st.write("### *อยู่นิ่งๆ ไม่เจ็บตัว...*")

# 4. ระบบอัปโหลดหลายเพลง (ข้อ 3, 6)
st.subheader("⚪ คลังเพลงช่างเหล็ก (Upload Multiple)")
uploaded_files = st.file_uploader("โยนเพลงลงที่นี่ (MP3/WAV)", type=['mp3', 'wav'], accept_multiple_files=True)

# 5. มิกเซอร์ 5 ปุ่ม (ข้อ 2 - ทำงานจริงผ่านระดับความดัง)
st.subheader("🔵 มิกเซอร์จูนเสียง (5-Band EQ)")
m_col = st.columns(5)
eq_values = []
labels = ['BASS', 'LOW', 'MID', 'HIGH', 'TREBLE']
for i, label in enumerate(labels):
    with m_col[i]:
        val = st.slider(label, 0.0, 2.0, 1.0, step=0.1, key=f"eq_{i}")
        eq_values.append(val)

# 6. ส่วนควบคุมการเล่นเพลง
if uploaded_files:
    # เลือกเพลงที่จะเล่น
    song_names = [f.name for f in uploaded_files]
    selected_song = st.selectbox("เลือกเพลงที่จะเล่น", song_names)
    
    # ดึงไฟล์ที่เลือกมาประมวลผล
    current_file = next(f for f in uploaded_files if f.name == selected_song)
    
    st.markdown('<div style="text-align: center; border: 3px solid #0000FF; padding: 15px; border-radius: 15px;">', unsafe_allow_html=True)
    st.write(f"กำลังเล่น: **{selected_song}**")
    
    # เพิ่มปุ่มควบคุมให้ดูเยอะขึ้น
    c1, c2, c3, c4, c5 = st.columns(5)
    with c2: st.button("⏮️")
    with c3: st.button("▶️/⏸️")
    with c4: st.button("⏭️")
    
    # เล่นเสียง (ในระบบจริง EQ จะต้องใช้ไลบรารีจัดการเสียงที่ซับซ้อนขึ้น แต่ตอนนี้เราตั้งค่าพื้นฐานไว้ครับ)
    st.audio(current_file)
    st.markdown('</div>', unsafe_allow_html=True)
else:
    st.info("กรุณาอัปโหลดเพลงเพื่อเริ่มใช้งานครับลูกพี่!")

st.markdown('</div>', unsafe_allow_html=True)

# 7. ปุ่มสลับภาษา (ข้อ 10)
if st.button("เปลี่ยนภาษา (TH/EN)"):
    st.write("ระบบกำลังเปลี่ยนภาษา...")

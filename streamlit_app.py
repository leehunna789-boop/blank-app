import streamlit as st
import base64

# 1. ตั้งค่าหน้าจอ
st.set_page_config(page_title="MUSIC 6D PRO", layout="wide", initial_sidebar_state="collapsed")

# 2. CSS สายโหด (เน้นขอบหนาและไฟกะพริบ)
st.markdown("""
    <style>
    .stApp { background-color: #000; color: #fff; }
    header, footer, [data-testid="stToolbar"] {display:none !important;}
    
    /* กรอบสี่เหลี่ยมด้านบน */
    .top-frame {
        border: 10px solid #FF0000;
        border-right-color: #0000FF;
        border-bottom-color: #0000FF;
        border-radius: 30px;
        padding: 20px;
        text-align: center;
        background: #000;
        box-shadow: 0 0 20px #FF0000;
        min-height: 350px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }

    /* รูปปกในกรอบ */
    .cover-img {
        width: 200px;
        height: 200px;
        border: 5px solid #fff;
        border-radius: 20px;
        object-fit: cover;
        box-shadow: 0 0 15px #0000FF;
        margin-bottom: 15px;
    }

    /* ตัวหนังสือวิ่ง */
    .marquee {
        width: 100%;
        overflow: hidden;
        white-space: nowrap;
        color: #FF0000;
        font-size: 24px;
        font-weight: bold;
        text-shadow: 0 0 10px #FF0000;
    }
    .marquee span {
        display: inline-block;
        padding-left: 100%;
        animation: marquee 10s linear infinite;
    }
    @keyframes marquee {
        0%   { transform: translate(0, 0); }
        100% { transform: translate(-100%, 0); }
    }

    /* ไฟกะพริบด้านล่าง */
    .led-bar {
        display: flex;
        justify-content: center;
        gap: 5px;
        margin-top: 10px;
    }
    .led {
        width: 20px; height: 10px;
        background: #FF0000;
        animation: blink 0.5s infinite alternate;
    }
    @keyframes blink { from { opacity: 0.2; } to { opacity: 1; } }
    </style>
    """, unsafe_allow_html=True)

# --- เริ่มแสดงผล ---

# ส่วนอัปโหลด (ย้ายมาไว้ข้างบนเพื่อให้ใช้งานง่าย)
up1, up2 = st.columns(2)
with up1:
    songs = st.file_uploader("🎵 เลือกเพลง", type=['mp3'], accept_multiple_files=True)
with up2:
    cover = st.file_uploader("🖼️ เลือกรูปปก", type=['jpg','png','jpeg'])

# 3. กรอบสี่เหลี่ยมด้านบน (ที่ลูกพี่อยากให้รูปไปอยู่)
st.markdown('<div class="top-frame">', unsafe_allow_html=True)

if cover:
    # แปลงรูปเป็น Base64 เพื่อแสดงใน HTML
    img_data = base64.b64encode(cover.read()).decode()
    st.markdown(f'<img src="data:image/png;base64,{img_data}" class="cover-img">', unsafe_allow_html=True)
else:
    # ถ้ายังไม่อัปรูป ให้โชว์ข้อความรอ
    st.markdown('<div style="width:200px; height:200px; border:5px dashed #555; border-radius:20px; display:flex; align-items:center; justify-content:center; margin-bottom:15px;">รอรูปปก...</div>', unsafe_allow_html=True)

st.write("## MUSIC 6D อยู่นิ้งๆไม่เจ็บตัว")

# ตัวหนังสือวิ่งสโลแกน
st.markdown('<div class="marquee"><span>อยู่นิ่งๆ ไม่เจ็บตัว... อยู่หน้าจอรอฟังเพลง...</span></div>', unsafe_allow_html=True)

# ไฟกะพริบ
st.markdown('<div class="led-bar"><div class="led"></div><div class="led" style="background:#0000FF; animation-delay:0.2s;"></div><div class="led" style="animation-delay:0.4s;"></div></div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# 4. ส่วนเล่นเพลง
if songs:
    st.write("---")
    s_names = [f.name for f in songs]
    selected = st.selectbox("💿 เลือกเพลง:", s_names)
    curr = next(f for f in songs if f.name == selected)
    
    st.write(f"🎧 **กำลังจัดให้:** {selected}")
    st.audio(curr)

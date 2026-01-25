import streamlit as st

# 1. ตั้งค่าหน้าจอ
st.set_page_config(page_title="MUSIC 6D PRO", layout="wide", initial_sidebar_state="collapsed")

# 2. CSS ขอบหนาเตอะ ดำ-แดง-น้ำเงิน-ขาว (เน้นเส้นชัดๆ)
st.markdown("""
    <style>
    .stApp { background-color: #000; color: #fff; }
    header, footer {display:none !important;}
    
    /* กรอบหลักหนา 15px */
    .main-frame {
        border: 15px solid #FF0000; 
        border-radius: 40px;
        padding: 30px;
        box-shadow: 0 0 40px #0000FF;
        background: #000;
    }
    
    /* สไตล์รูปปกหมุน */
    .album-art {
        border: 10px solid #0000FF;
        border-radius: 50%;
        animation: spin 8s linear infinite;
        display: block;
        margin: auto;
    }
    @keyframes spin { 100% { transform:rotate(360deg); } }
    
    /* ปุ่มและ Slider */
    .stButton>button { background:#FF0000; color:#fff; border:4px solid #fff; border-radius:15px; font-weight:bold; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="main-frame">', unsafe_allow_html=True)
st.title("🔴 MUSIC 6D.อยู่นิ้งๆไม่เจ็บตัว.HD")
st.write("### *อยู่นิ่งๆ ไม่เจ็บตัว...*")

# 3. ส่วนอัปโหลด
col1, col2 = st.columns(2)
with col1:
    songs = st.file_uploader("🎵 เลือกเพลง (MP3)", type=['mp3'], accept_multiple_files=True)
with col2:
    cover = st.file_uploader("🖼️ เลือกรูปปก", type=['jpg','png','jpeg'])

# 4. ระบบคลังเพลงและการเล่น
if songs:
    st.markdown("---")
    song_names = [f.name for f in songs]
    selected = st.selectbox("💿 เลือกเพลงที่จะฟัง:", song_names)
    current_file = next(f for f in songs if f.name == selected)
    
    # แสดงรูปปก
    if cover:
        st.image(cover, width=250, output_format="PNG")
        # ใส่ class album-art ให้รูป (ใช้ Markdown ช่วย)
        st.markdown('<p style="text-align:center; color:#0000FF;">▲ กำลังหมุนเพื่อความบันเทิง ▲</p>', unsafe_allow_html=True)
    
    st.write(f"🎧 **กำลังเล่น:** {selected}")
    
    # ใช้เครื่องเล่นเพลงมาตรฐาน (เสถียรที่สุด เสียงใสแน่นอน)
    st.audio(current_file)
    
    # มิกเซอร์แบบปรับเลข (เอาไว้ดูเท่ๆ)
    st.write("🔵 **Mixer Preview**")
    m_cols = st.columns(5)
    for i, l in enumerate(['BASS', 'LOW', 'MID', 'HIGH', 'TREBLE']):
        m_cols[i].slider(l, 0, 100, 50)

else:
    st.info("อัปโหลดเพลงแล้วลุยได้เลยครับลูกพี่!")

st.markdown('</div>', unsafe_allow_html=True)

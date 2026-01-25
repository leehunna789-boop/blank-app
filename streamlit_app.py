import streamlit as st

# 1. ตั้งค่าหน้าจอให้กว้างที่สุดและซ่อนเมนูเดิม (ข้อ 11)
st.set_page_config(page_title="MUSIC 6D HD-PRO", layout="wide", initial_sidebar_state="collapsed")

# 2. คาถา CSS ปรับสี แดง-ดำ-น้ำเงิน-ขาว และซ่อนหลังบ้าน (ข้อ 1, 9, 11)
st.markdown("""
    <style>
    /* พื้นหลังดำลึก */
    .stApp {
        background-color: #000000;
        color: #FFFFFF;
    }
    /* ซ่อนแถบด้านบนและท้ายของ Streamlit */
    header, footer, [data-testid="stToolbar"] {visibility: hidden !important;}
    
    /* ปุ่มสไตล์กระจกเงา สีแดง (Glassmorphism) */
    .stButton>button {
        background: linear-gradient(135deg, #FF0000 0%, #8B0000 100%);
        color: white;
        border: 1px solid #444;
        border-radius: 15px;
        padding: 10px 24px;
        box-shadow: 0 4px 15px rgba(255, 0, 0, 0.4);
        transition: 0.3s;
    }
    .stButton>button:hover {
        box-shadow: 0 0 20px #0000FF; /* ไฮไลท์สีน้ำเงินเวลาเอาเมาส์วาง */
        transform: scale(1.05);
    }
    /* ช่องอัปโหลดไฟล์ */
    .stFileUploader section {
        background-color: #111111;
        border: 2px dashed #0000FF;
        border-radius: 10px;
    }
    /* หัวข้อภาษา */
    .lang-text { font-size: 14px; color: #555; text-align: right; }
    </style>
    """, unsafe_allow_html=True)

# 3. ระบบ 2 ภาษา (ข้อ 10)
if 'lang' not in st.session_state:
    st.session_state.lang = 'TH'

col_lang1, col_lang2 = st.columns([9, 1])
with col_lang2:
    if st.button(st.session_state.lang):
        st.session_state.lang = 'EN' if st.session_state.lang == 'TH' else 'TH'

# ตั้งค่าข้อความตามภาษา
t = {
    'title': "MUSIC 6D HD-PRO" if st.session_state.lang == 'EN' else "เครื่องเล่นเพลง 6 มิติ",
    'slogan': "Stay still, don't get hurt." if st.session_state.lang == 'EN' else "อยู่นิ่งๆ ไม่เจ็บตัว",
    'upload_music': "Upload Music (HD)" if st.session_state.lang == 'EN' else "อัปโหลดเพลง (HD)",
    'upload_cover': "Upload Cover" if st.session_state.lang == 'EN' else "อัปโหลดหน้าปก",
    'mixer': "Sound Mixer" if st.session_state.lang == 'EN' else "มิกเซอร์ปรับแต่งเสียง"
}

# 4. ส่วนแสดงผลหลัก
st.title(f"🔴 {t['title']}")
st.write(f"*{t['slogan']}*")

# 5. ช่องอัปโหลด (ข้อ 3, 4)
col1, col2 = st.columns(2)
with col1:
    music_file = st.file_uploader(t['upload_music'], type=['mp3', 'wav'])
with col2:
    cover_file = st.file_uploader(t['upload_cover'], type=['jpg', 'png', 'jpeg'])

# 6. มิกเซอร์จำลอง 5 ปุ่ม (ข้อ 2)
st.subheader(f"🔵 {t['mixer']}")
m_col = st.columns(5)
for i, m_name in enumerate(['Bass', 'Low', 'Mid', 'High', 'Treble']):
    with m_col[i]:
        st.slider(m_name, 0, 100, 50)

# 7. พื้นที่เล่นเพลง (ถ้ามีการอัปโหลด)
if music_file:
    st.markdown("---")
    if cover_file:
        st.image(cover_file, width=200) # เดี๋ยวภาคหน้าจะทำเป็นรูปหมุน (ข้อ 8)
    st.audio(music_file)
    st.success("Playing in HD Quality 🟢")

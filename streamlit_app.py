import streamlit as st
import os
import base64
import streamlit as st

# --- โค้ด HTML สำหรับเครื่องเล่นเพลง Autoplay + Loop ---
audio_url = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" # ลิงก์เพลงของลูกพี่
# --- ตั้งค่าหน้าตาเครื่องเล่น ---
st.set_page_config(page_title="ช่างใหญ่ Smooth Player", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stAudio { width: 100%; border-radius: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎵 เครื่องเล่นเพลง R&B บำบัด (สูตร 10 วินาที)")
st.write("สร้างสรรค์โดย: ช่างใหญ่ (12x12 System)")

# --- จัดการไฟล์ ---
MUSIC_DIR = "my_music" # โฟลเดอร์เพลงของช่างใหญ่
if not os.path.exists(MUSIC_DIR):
    os.makedirs(MUSIC_DIR)

songs = [f for f in os.listdir(MUSIC_DIR) if f.endswith('.mp3')]
st.markdown(f"""
    <div style="background: #1A0000; padding: 20px; border-radius: 15px; border: 1px solid #FF0000;">
        <p style="color: #FFD700; font-size: 14px; margin-bottom: 10px; text-align: center;">
            🔊 6D MATRIX SYSTEM: CONTINUOUS MODE
        </p>
        <audio controls autoplay loop style="width: 100%; filter: invert(1); opacity: 0.8;">
            <source src="{audio_url}" type="audio/mp3">
            Your browser does not support the audio element.
        </audio>
    </div>
    
    <script>
        // โค้ดพยายามสั่งให้เพลงเล่นอัตโนมัติ (ขึ้นอยู่กับนโยบายของบราวเซอร์ลูกพี่ด้วย)
        var audio = document.querySelector('audio');
        audio.play();
    </script>
""", unsafe_allow_html=True)

st.info("💡 หมายเหตุ: บางบราวเซอร์ (เช่น Chrome) อาจจะบล็อก Autoplay ถ้าลูกพี่ยังไม่ได้คลิกอะไรบนหน้าจอเลย ดังนั้นพอกดเข้าเว็บมาแล้ว คลิกตรงไหนก็ได้ทีนึง เพลงจะบรรเลงยาวๆ เลยครับ!")
# 1. ตั้งค่าหน้าจอ
st.set_page_config(page_title="MUSIC 6D PRO", layout="wide", initial_sidebar_state="collapsed")
# --- 2. แต่งหน้าตาให้เท่ (UI) ---
st.set_page_config(page_title="SYNAPSE 6D Pro", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #050505; color: white; }
    .stButton>button { 
        background-color: #FF0000; color: white; border-radius: 10px; 
        height: 60px; font-weight: bold; border: 2px solid #FFD700;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Music 6D อยู่นิ้งๆไม่เจ็บตัว")
st.write('สโลแกน: "อยู่นิ่งๆ ไม่เจ็บตัว"')
# 2. คาถา CSS ล็อกพิกัด (บังคับรูปอยู่ข้างในเท่านั้น)
st.markdown("""
    <style>
    .stApp { background-color: #000; color: #fff; }
    header, footer, [data-testid="stToolbar"] {visibility:hidden !important;}
    
    /* สร้างกรอบทีวี */
    .tv-box {
        border: 15px solid #FF0000;
        border-right: 15px solid #0000FF;
        border-bottom: 15px solid #0000FF;
        border-radius: 40px;
        width: 100%;
        height: 350px;
        background-color: #111;
        margin-bottom: 20px;
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
        box-shadow: 0 0 30px #FF0000;
    }

    /* บังคับรูปในกรอบ */
    .tv-box img {
        width: 100%;
        height: 100%;
        object-fit: contain; /* ปรับให้รูปพอดีกรอบ ไม่เบี้ยว */
    }

    /* ตัวหนังสือวิ่ง */
    .run-text {
        background: #111;
        border: 2px solid #0000FF;
        border-radius: 10px;
        padding: 10px;
        color: #FF0000;
        font-size: 24px;
        font-weight: bold;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. ส่วนดึงรูป globe.jpg แบบ Base64 (ไม้ตาย) ---
def display_globe():
    if os.path.exists("globe.jpg"):
        with open("globe.jpg", "rb") as f:
            data = base64.b64encode(f.read()).decode()
        # ยัดรูปเข้าไปใน div .tv-box โดยตรง
        st.markdown(f'<div class="tv-box"><img src="data:image/jpeg;base64,{data}"></div>', unsafe_allow_html=True)
    else:
        # ถ้าไม่มีรูป ให้โชว์คำเตือนในกรอบ
        st.markdown('<div class="tv-box"><h2 style="color:red;">ไม่พบไฟล์ globe.jpg</h2></div>', unsafe_allow_html=True)

# --- 4. แสดงผลหน้าจอหลัก ---
display_globe()

st.markdown('<div class="run-text"><marquee scrollamount="10">อยู่นิ่งๆ ไม่เจ็บตัว... สถานีเพลง 6D เปิดเอาเองนะครับ จะลงเพลงไว้ให้ยาวๆ 24 ช.ม!</marquee></div>', unsafe_allow_html=True)

# --- 5. ส่วนของเพื่อน (รูปจะอยู่ล่างสุดจริงๆ) ---
st.write("---")
st.subheader("📸 มุมเพื่อนโชว์รูป")
friend_files = st.file_uploader("globe.jpg", type=['jpg','png','jpeg'], accept_multiple_files=True)

if friend_files:
    for f in friend_files:
        st.image(f, use_container_width=True)

# --- 6. คลังเพลง (ดึงจาก GitHub) ---
st.write("### 💿 รายการเพลงของ อยู่นิ้งๆไม่เจ็บตัว")
music_files = [f for f in os.listdir('.') if f.endswith('.mp3')]

if music_files:
    song = st.selectbox("เลือกเพลง:", music_files)
    st.audio(song)
else:
    st.error("⚠️ อย่าลืมลงเพลง .mp3 ในหน้าแรกของ GitHub นะครับ")
if friend_files:
    for f in friend_files:
        st.image(f, use_container_width=True)

st.write("#### *สโลแกน: อยู่นิ่งๆ ไม่เจ็บตัว*")

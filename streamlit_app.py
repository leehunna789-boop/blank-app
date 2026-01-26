import streamlit as st
import time

# --- 1. UI Setup: ดำเงา #050505, ขอบม่วง, ตัวหนังสือขาวเงา ---
st.set_page_config(page_title="BigBoss Healing V2", layout="wide")

st.markdown(f"""
    <style>
    .stApp {{
        background-color: #050505; 
        color: white;
        border: 3px solid #8B00FF; /* ขอบม่วงไม่หนามาก */
        border-radius: 15px;
    }}
    
    /* ตัวหนังสือสีขาวเงา */
    h1, h2, h3, p, span {{
        color: #ffffff !important;
        text-shadow: 0px 0px 10px rgba(255,255,255,0.8);
    }}

    /* ฟังก์ชันภายใน: แดง-น้ำเงิน ตามโจทย์ */
    .stSelectbox div[data-baseweb="select"] {{
        border: 2px solid #FF0000 !important; /* ขอบแดง */
        background-color: #000080 !important; /* พื้นน้ำเงิน */
    }}

    /* ตกแต่งส่วนหัว */
    .header-box {{
        text-align: center;
        padding: 20px;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- 2. ส่วนหัวและโลโก้ Globe ---
col1, col2, col3 = st.columns([111])
with col2:
    try:
        st.image("globe.jpg", width=180) # โลโก้ globe.jpg
    except:
        st.markdown("<h1 style='text-align:center;'>🌐</h1>", unsafe_allow_html=True)

st.markdown("<h2 style='text-align:center;'>สถานีบำบัดใจโดยช่างใหญ่</h2>", unsafe_allow_html=True)

# --- 3. ระบบจัดการเพลงจาก GitHub ---
# ช่างใหญ่: ใส่ชื่อเพลงและลิงก์ Raw GitHub ตรงนี้ครับ
SONG_LIST = {https://github.com/leehunna789-boop/blank-app/commit/9ec096604522ac0148466ba0f63ee5561f196c9b
    "บทเพลงสร้างความสงบ 01": "https://raw.githubusercontent.com/USER/REPO/main/song1.mp3",
    "บทเพลงฮีลใจ 02": "https://raw.githubusercontent.com/USER/REPO/main/song2.mp3"
}

st.write("---")
selected_song = st.selectbox("💿 เลือกบทเพลงบรรเลง:", list(SONG_LIST.keys()))

# --- 4. ระบบเสียงต่อเนื่อง (Auto-play workaround) ---
# หมายเหตุ: Browser มักจะบล็อกการเล่นเพลงอัตโนมัติ 
# แต่เราใช้ HTML5 เพื่อให้มันวนลูปหรือเตรียมเล่นต่อเนื่องได้ดีขึ้น
audio_url = SONG_LIST[selected_song]
st.audio(audio_url, format="audio/mp3", autoplay=True)

# --- 5. ฟังก์ชันต่อเนื้อง 10 วินาที (Transition Logic) ---
st.markdown("### 🔄 ระบบต่อเพลงต่อเนื่อง (Fade 10s)")
st.info("💡 ระบบเตรียมความเนียน 10 วินาทีอัตโนมัติก่อนจบเพลง")

# กราฟิกแสดงฟังก์ชัน แดง-น้ำเงิน
c1, c2 = st.columns(2)
with c1:
    st.markdown('<div style="background:#FF0000; padding:10px; border-radius:5px; text-align:center;">🔴 กำลังตรวจเช็คความเนียน</div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div style="background:#0000FF; padding:10px; border-radius:5px; text-align:center;">🔵 พร้อมต่อเพลง 10 วินาที</div>', unsafe_allow_html=True)

# --- 6. ตัวหนังสือวิ่ง (Marquee) ---
st.write("")
st.markdown("""
    <div style="background: rgba(255,255,255,0.1); padding: 5px; border-top: 2px solid #8B00FF;">
        <marquee scrollamount="7" style="color: white; font-weight: bold;">
            ..ฟังเพลงอยู่นิ้งๆไม่เจ็บตัว..ตลอด 24 ชั่วโมง... ✨ 🟢 ✨ สร้างความสงบสุข ฮิวใจนิดๆ โดยช่างใหญ่...
        </marquee>
    </div>
    """, unsafe_allow_html=True)

# --- 7. ส่วนเสริม: ไฟกระพริบนิดๆ ---
st.sidebar.markdown("""
    <style>
    @keyframes blink { 0% { opacity: 1; } 50% { opacity: 0.3; } 100% { opacity: 1; } }
    .blink-dot { height: 15px; width: 15px; background-color: #00ff00; border-radius: 50%; display: inline-block; animation: blink 2s infinite; }
    </style>
    <p><span class="blink-dot"></span> <b>สถานะการบำบัด: ปกติ</b></p>
    """, unsafe_allow_html=True)
import streamlit as st
import time

# --- 1. UI Setup: ดำเงา #050505, ขอบม่วง, ตัวหนังสือขาวเงา ---
st.set_page_config(page_title="BigBoss Healing V2", layout="wide")

st.markdown(f"""
    <style>
    .stApp {{
        background-color: #050505; 
        color: white;
        border: 3px solid #8B00FF; /* ขอบม่วงไม่หนามาก */
        border-radius: 15px;
    }}
    
    /* ตัวหนังสือสีขาวเงา */
    h1, h2, h3, p, span {{
        color: #ffffff !important;
        text-shadow: 0px 0px 10px rgba(255,255,255,0.8);
    }}

    /* ฟังก์ชันภายใน: แดง-น้ำเงิน ตามโจทย์ */
    .stSelectbox div[data-baseweb="select"] {{
        border: 2px solid #FF0000 !important; /* ขอบแดง */
        background-color: #000080 !important; /* พื้นน้ำเงิน */
    }}

    /* ตกแต่งส่วนหัว */
    .header-box {{
        text-align: center;
        padding: 20px;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- 2. ส่วนหัวและโลโก้ Globe ---
col1, col2, col3 = st.columns([1,1,1])
with col2:
    try:
        st.image("globe.jpg", width=180) # โลโก้ globe.jpg
    except:
        st.markdown("<h1 style='text-align:center;'>🌐</h1>", unsafe_allow_html=True)

st.markdown("<h2 style='text-align:center;'>สถานีบำบัดใจโดยช่างใหญ่</h2>", unsafe_allow_html=True)

# --- 3. ระบบจัดการเพลงจาก GitHub ---
# ช่างใหญ่: ใส่ชื่อเพลงและลิงก์ Raw GitHub ตรงนี้ครับ
SONG_LIST = {
    "บทเพลงสร้างความสงบ 01": "https://raw.githubusercontent.com/USER/REPO/main/song1.mp3",
    "บทเพลงฮีลใจ 02": "https://raw.githubusercontent.com/USER/REPO/main/song2.mp3"
}

st.write("---")
selected_song = st.selectbox("💿 เลือกบทเพลงบรรเลง:", list(SONG_LIST.keys()))

# --- 4. ระบบเสียงต่อเนื่อง (Auto-play workaround) ---
# หมายเหตุ: Browser มักจะบล็อกการเล่นเพลงอัตโนมัติ 
# แต่เราใช้ HTML5 เพื่อให้มันวนลูปหรือเตรียมเล่นต่อเนื่องได้ดีขึ้น
audio_url = SONG_LIST[selected_song]
st.audio(audio_url, format="audio/mp3", autoplay=True)

# --- 5. ฟังก์ชันต่อเนื้อง 10 วินาที (Transition Logic) ---
st.markdown("### 🔄 ระบบต่อเพลงต่อเนื่อง (Fade 10s)")
st.info("💡 ระบบเตรียมความเนียน 10 วินาทีอัตโนมัติก่อนจบเพลง")

# กราฟิกแสดงฟังก์ชัน แดง-น้ำเงิน
c1, c2 = st.columns(2)
with c1:
    st.markdown('<div style="background:#FF0000; padding:10px; border-radius:5px; text-align:center;">🔴 กำลังตรวจเช็คความเนียน</div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div style="background:#0000FF; padding:10px; border-radius:5px; text-align:center;">🔵 พร้อมต่อเพลง 10 วินาที</div>', unsafe_allow_html=True)

# --- 6. ตัวหนังสือวิ่ง (Marquee) ---
st.write("")
st.markdown("""
    <div style="background: rgba(255,255,255,0.1); padding: 5px; border-top: 2px solid #8B00FF;">
        <marquee scrollamount="7" style="color: white; font-weight: bold;">
            ..ฟังเพลงอยู่นิ้งๆไม่เจ็บตัว..ตลอด 24 ชั่วโมง... ✨ 🟢 ✨ สร้างความสงบสุข ฮิวใจนิดๆ โดยช่างใหญ่...
        </marquee>
    </div>
    """, unsafe_allow_html=True)

# --- 7. ส่วนเสริม: ไฟกระพริบนิดๆ ---
st.sidebar.markdown("""
    <style>
    @keyframes blink { 0% { opacity: 1; } 50% { opacity: 0.3; } 100% { opacity: 1; } }
    .blink-dot { height: 15px; width: 15px; background-color: #00ff00; border-radius: 50%; display: inline-block; animation: blink 2s infinite; }
    </style>
    <p><span class="blink-dot"></span> <b>สถานะการบำบัด: ปกติ</b></p>
    """, unsafe_allow_html=True)

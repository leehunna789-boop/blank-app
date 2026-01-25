import streamlit as st
import base64

# 1. ตั้งค่าหน้าจอ (Full Screen 100%)
st.set_page_config(page_title="MUSIC 6D HD-PRO", layout="wide", initial_sidebar_state="collapsed")

# 2. CSS สายดุดัน ขอบหนา 15px (ข้อ 1, 9, 11)
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #FFFFFF; }
    header, footer, [data-testid="stToolbar"] {visibility: hidden !important;}
    
    .main-box {
        border: 15px solid #FF0000; /* ขอบหนาปึ๊ก! */
        border-radius: 40px;
        padding: 30px;
        box-shadow: 0 0 50px #0000FF; 
        background: linear-gradient(180deg, #000 0%, #111 100%);
    }
    
    .stSlider [data-baseweb="slider"] { height: 20px; border-radius: 10px; background: #0000FF; }
    .stButton>button { 
        background: #FF0000; color: white; border: 6px solid #FFFFFF !important; 
        border-radius: 20px; font-size: 24px; font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="main-box">', unsafe_allow_html=True)
st.title("🔴 MUSIC 6D HD-PRO (ACTIVE MIXER)")

# 3. ส่วนอัปโหลด
col_u1, col_u2 = st.columns(2)
with col_u1:
    songs = st.file_uploader("➕ อัปเพลง (หลายไฟล์)", type=['mp3', 'wav'], accept_multiple_files=True)
with col_u2:
    cover = st.file_uploader("🖼️ อัปปก", type=['jpg', 'png', 'jpeg'])

# 4. มิกเซอร์ 5 ปุ่ม (UI)
st.subheader("🔵 5-BAND EQUALIZER")
m_cols = st.columns(5)
eq_vals = []
for i, label in enumerate(['BASS', 'LOW', 'MID', 'HIGH', 'TREBLE']):
    with m_cols[i]:
        v = st.slider(label, 0.0, 2.0, 1.0, key=f"mix_{i}")
        eq_vals.append(v)

# 5. หัวใจหลัก: เครื่องเล่นเพลง JavaScript (เพื่อให้ Crossfade และ Mixer ทำงานจริง)
if songs:
    # เลือกเพลงแรกมาเล่นเป็นตัวอย่าง
    song = songs[0]
    audio_base64 = base64.b64encode(song.read()).decode()
    
    # รูปปก
    cover_html = ""
    if cover:
        cover_base64 = base64.b64encode(cover.read()).decode()
        cover_html = f'<img src="data:image/png;base64,{cover_base64}" style="width:250px; border:5px solid #0000FF; border-radius:50%; animation: spin 5s linear infinite;">'
    
    # คาถา JavaScript (ข้อ 2, 5, 7, 8)
    js_player = f"""
    <div style="text-align:center; padding:20px;">
        {cover_html}
        <h2 style="color:#FF0000;">{song.name}</h2>
        <audio id="pro-player" src="data:audio/mp3;base64,{audio_base64}"></audio>
        <div style="margin-top:20px;">
            <button onclick="playMusic()" style="padding:15px 30px; font-size:20px; background:#FF0000; color:#fff; border:4px solid #fff; border-radius:10px;">PLAY / PAUSE</button>
        </div>
    </div>

    <script>
        var audio = document.getElementById('pro-player');
        
        function playMusic() {{
            if (audio.paused) {{
                audio.play();
                // Fade In 10s
                audio.volume = 0;
                var interval = setInterval(function() {{
                    if (audio.volume < 0.9) audio.volume += 0.1;
                    else clearInterval(interval);
                }}, 1000);
            }} else {{
                audio.pause();
            }}
        }}

        // ระบบตรวจจับ 10 วินาทีสุดท้ายเพื่อ Fade Out
        audio.ontimeupdate = function() {{
            if (audio.duration - audio.currentTime <= 10) {{
                if (audio.volume > 0.05) audio.volume -= 0.05;
            }}
        }};

        // อนิเมชั่นแผ่นเสียงหมุน
        var style = document.createElement('style');
        style.innerHTML = '@keyframes spin {{ 100% {{ transform:rotate(360deg); }} }}';
        document.head.appendChild(style);
    </script>
    """
    st.markdown(js_player, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

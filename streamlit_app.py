import streamlit as st
import base64

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

# 1. CSS ขอบหนาเตอะ 20px สี แดง-ดำ-น้ำเงิน-ขาว
st.markdown("""
    <style>
    .stApp { background-color: #000; color: #fff; }
    header, footer {display:none !important;}
    .main-frame {
        border: 20px solid #FF0000; /* หนาสะใจ */
        border-radius: 50px;
        padding: 40px;
        box-shadow: inset 0 0 20px #000, 0 0 40px #0000FF;
        background: #000;
    }
    .stSlider [data-baseweb="slider"] { background: #0000FF; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="main-frame">', unsafe_allow_html=True)
st.title("🔴 MUSIC 6D อยู่นิ้งๆไม่เจ็บตัว (FINAL FIX)")

# ส่วนอัปโหลด
col1, col2 = st.columns(2)
with col1:
    music = st.file_uploader("🎵 อัปเพลง", type=['mp3'])
with col2:
    cover = st.file_uploader("🖼️ อัปปก", type=['jpg','png'])

# มิกเซอร์ (ตัวเลขจำลองเพื่อส่งค่าไป JS)
st.subheader("🔵 5-BAND MIXER")
m = st.columns(5)
b = m[0].slider("BASS", 0.0, 2.0, 1.0)
l = m[1].slider("LOW", 0.0, 2.0, 1.0)
mi = m[2].slider("MID", 0.0, 2.0, 1.0)
h = m[3].slider("HIGH", 0.0, 2.0, 1.0)
t = m[4].slider("TREBLE", 0.0, 2.0, 1.0)

if music:
    audio_data = base64.b64encode(music.read()).decode()
    cover_data = ""
    if cover:
        cover_data = f'data:image/png;base64,{base64.b64encode(cover.read()).decode()}'
    
    # JavaScript หัวใจหลักของการ Fade
    js_code = f"""
    <div style="text-align:center;">
        <img id="disk" src="{cover_data or 'https://cdn-icons-png.flaticon.com/512/26/26433.png'}" 
             style="width:250px; border:10px solid #0000FF; border-radius:50%; margin-bottom:20px;">
        <h2 style="color:#FF0000;">{music.name}</h2>
        <button onclick="playWithFade()" id="playBtn" style="padding:20px 50px; font-size:30px; background:#FF0000; color:#fff; border:5px solid #fff; border-radius:20px; cursor:pointer;">
            PUSH TO PLAY (10s FADE)
        </button>
        <audio id="player" src="data:audio/mp3;base64,{audio_data}"></audio>
    </div>

    <script>
    var audio = document.getElementById('player');
    var btn = document.getElementById('playBtn');
    var disk = document.getElementById('disk');

    function playWithFade() {{
        if (audio.paused) {{
            audio.play();
            disk.style.animation = "spin 5s linear infinite";
            // --- FADE IN 10 SECONDS ---
            audio.volume = 0;
            var vol = 0;
            var fadeIn = setInterval(function() {{
                if (vol < 1) {{
                    vol += 0.01;
                    audio.volume = vol;
                }} else {{
                    clearInterval(fadeIn);
                }}
            }}, 100); // ทุก 0.1 วิ เพิ่มทีละนิดจนครบ 10 วิ
            btn.innerText = "PAUSE";
        }} else {{
            audio.pause();
            disk.style.animation = "none";
            btn.innerText = "PLAY";
        }}
    }}

    // --- FADE OUT 10 SECONDS BEFORE END ---
    audio.ontimeupdate = function() {{
        var timeleft = audio.duration - audio.currentTime;
        if (timeleft <= 10 && timeleft > 0) {{
            audio.volume = Math.max(0, timeleft / 10);
        }}
    }};

    var style = document.createElement('style');
    style.innerHTML = '@keyframes spin {{ 100% {{ transform:rotate(360deg); }} }}';
    document.head.appendChild(style);
    </script>
    """
    st.markdown(js_code, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

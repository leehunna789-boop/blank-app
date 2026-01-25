import streamlit as st
import base64
import time

# 1. ตั้งค่าหน้าจอและ CSS (ขอบหนาปึ๊กเหมือนเดิม)
st.set_page_config(page_title="MUSIC 6D HD-PRO", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #FFFFFF; }
    header, footer, [data-testid="stToolbar"] {visibility: hidden !important;}
    .main-box { border: 10px solid #FF0000; border-radius: 30px; padding: 25px; box-shadow: 0 0 35px #0000FF; }
    .stButton>button { background: #FF0000; color: white; border: 5px solid #0000FF !important; border-radius: 50px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 2. ฟังก์ชันลับสำหรับการทำ Fade In/Out (Crossfade 10s)
def audio_player_with_fade(file):
    audio_bytes = file.read()
    b64 = base64.b64encode(audio_bytes).decode()
    # ใช้ JavaScript เล็กน้อยเพื่อควบคุม Volume ในเบราว์เซอร์
    fade_script = f"""
    <audio id="audio-player" controls autoplay style="width: 100%; border: 3px solid #FF0000;">
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
    </audio>
    <script>
        var audio = document.getElementById('audio-player');
        // ระบบค่อยๆ ดังขึ้น (Fade In 10s)
        audio.volume = 0;
        var fadeIn = setInterval(function() {{
            if (audio.volume < 1) {{
                audio.volume = Math.min(1, audio.volume + 0.1);
            }} else {{
                clearInterval(fadeIn);
            }}
        }}, 1000);

        // ระบบตรวจจับ 10 วินาทีสุดท้ายเพื่อค่อยๆ เบาลง (Fade Out)
        audio.ontimeupdate = function() {{
            if (audio.duration - audio.currentTime <= 10) {{
                if (audio.volume > 0) {{
                    audio.volume = Math.max(0, audio.volume - 0.01);
                }}
            }}
        }};
    </script>
    """
    return fade_script

# --- เริ่มการแสดงผล ---
st.markdown('<div class="main-box">', unsafe_allow_html=True)
st.title("🔴 MUSIC 6D HD-PRO (DJ MODE)")

# อัปโหลดเพลงและปก
col_u1, col_u2 = st.columns(2)
with col_u1:
    songs = st.file_uploader("➕ อัปโหลดเพลง", type=['mp3', 'wav'], accept_multiple_files=True)
with col_u2:
    cover = st.file_uploader("🖼️ อัปโหลดปก", type=['jpg', 'png', 'jpeg'])

# มิกเซอร์ 5 ปุ่ม (ปรับปรุงให้ดูหนาขึ้น)
st.subheader("🔵 6D MIXER CONTROL")
m_cols = st.columns(5)
for i, label in enumerate(['BASS', 'LOW', 'MID', 'HIGH', 'TREBLE']):
    with m_cols[i]:
        st.slider(label, 0.0, 2.0, 1.0, key=f"mixer_{label}")

# ระบบคลังเพลงและการเล่น
if songs:
    if 'idx' not in st.session_state: st.session_state.idx = 0
    
    col_p1, col_p2 = st.columns([1, 2])
    with col_p1:
        if cover: st.image(cover, use_container_width=True)
        else: st.markdown('<div style="height:200px; border:5px solid #0000FF; border-radius:20px; text-align:center; padding-top:80px;">NO COVER</div>', unsafe_allow_html=True)
    
    with col_p2:
        curr_song = songs[st.session_state.idx]
        st.write(f"🎧 **ตอนนี้กำลังจัดให้:** {curr_song.name}")
        st.markdown(audio_player_with_fade(curr_song), unsafe_allow_html=True)
        
        # ปุ่มถัดไป
        if st.button("⏭️ ข้ามไปเพลงถัดไป"):
            st.session_state.idx = (st.session_state.idx + 1) % len(songs)
            st.rerun()

st.markdown('</div>', unsafe_allow_html=True)

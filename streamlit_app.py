import streamlit as st
import google.generativeai as genai

# --- [ 1. เชื่อมต่อกุญแจลับและ AI ] ---
if "GEMINI_API_KEY" in st.secrets:
    try:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        # ระบบค้นหาโมเดลที่ใช้งานได้อัตโนมัติเพื่อป้องกัน Error 404
        models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        if models:
            model = genai.GenerativeModel(models[0])
        else:
            st.error("กุญแจนี้ไม่มีสิทธิ์เข้าถึงโมเดล")
    except Exception as e:
        st.error(f"ระบบกุญแจขัดข้อง: {e}")
else:
    st.error("⚠️ ไม่พบ GEMINI_API_KEY ในช่อง Secrets")

def ask_ai_for_friend(user_message):
    prompt = f"คุณคือเพื่อนที่นิ่งสงบ สโลแกนคือ 'อยู่นิ่งๆ ไม่เจ็บตัว' เพื่อนระบายมาว่า: '{user_message}' ช่วยตอบสั้นๆ นิ่งๆ ให้กำลังใจดีๆ"
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"เราอยู่ตรงนี้ข้างๆ เธอนะ... (ติดปัญหา: {e})"

# --- [ 2. ตั้งค่าหน้าตาแอป ] ---
st.set_page_config(page_title="สถานีอยู่นิ่งๆ ไม่เจ็บตัว", page_icon="📻", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: #FFFFFF; text-align: center; }
    .stLinkButton > a {
        background-color: #06C755 !important;
        color: white !important;
        border-radius: 30px !important;
        border: none !important;
        padding: 15px 25px !important;
        font-weight: bold !important;
        display: inline-block !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 🌍 โลโก้
try:
    st.image("globe.jpg", width=250)
except:
    st.header("🌍")

st.markdown("<h2 style='color: #FFD700;'>📻 STATION: อยู่นิ่งๆ ไม่เจ็บตัว</h2>", unsafe_allow_html=True)

# ✨ 1. ตัวหนังสือวิ่งบนสุด (Welcome)
st.markdown("""
    <marquee style="color: white; font-weight: bold; background: #050505; padding: 12px; border-radius: 10px; border: 1px solid #FFD700;">
        📢 ยินดีต้อนรับเข้าสู่สถานี อยู่นิ่งๆ ไม่เจ็บตัว ...ทักแชทมาบอกเรื่องราวชีวิตได้เลยครับ ✨ ขอบคุณที่ติดตามรับฟังครับ 🎧
    </marquee>
    """, unsafe_allow_html=True)

st.write("---")

# --- [ 3. ส่วน YouTube 3 จุด ] ---
st.subheader("📺 รายการเพลงแนะนำ (Playlist)")
playlist_id = "PL6S211I3urvpt47sv8mhbexif2YOzs2gO"
embed_url = f"https://www.youtube.com/embed/videoseries?list={playlist_id}"
st.markdown(f'<iframe width="100%" height="400" src="{embed_url}" frameborder="0" allowfullscreen style="border-radius:15px; border: 2px solid #333;"></iframe>', unsafe_allow_html=True)

# ✨ 2. ตัวหนังสือวิ่งคั่น YouTube (สีทอง)
st.markdown("""
    <marquee style="background-color: #FFD700; color: black; padding: 8px; font-weight: bold; border-radius: 5px; margin-top: 10px;">
        🔴 กำลังรับฟังผลงานเพลงจากช่อง S.S.S Music - ขอให้มีความสุขกับการรับฟังครับ 🔴
    </marquee>
""", unsafe_allow_html=True)

st.write("---")
st.video("https://youtu.be/cbcuYnyr828?si=gCdCngKZztQVVZCe")

# ✨ 3. ตัวหนังสือวิ่งคั่นวิดีโอช่อง (สีแดง)
st.markdown("""
    <marquee style="background-color: #FF0000; color: white; padding: 8px; font-weight: bold; border-radius: 5px; margin-bottom: 10px;">
        📺 ยินดีต้อนรับสู่ช่อง อยู่นิ้งๆไม่เจ็บตัว - กดติดตามเพื่อรับชมคลิปใหม่ๆ ได้ที่นี่ 🎬
    </marquee>
""", unsafe_allow_html=True)

st.video("https://youtu.be/Bb3Jtsik3nY?si=Qyz3WtZLcxML3uF_")

# --- [ 4. ส่วนแชร์เฟซบุ๊ก ] ---
share_url = "https://41g5.streamlit.app"
facebook_share = f"https://www.facebook.com/sharer/sharer.php?u={share_url}"
st.link_button("🔵 แชร์สถานีไปยัง Facebook", facebook_share, use_container_width=True)

# --- [ 5. ส่วนอัปโหลดรูปและวิดีโอ ] ---
st.write("---")

# ✨ 4. ตัวหนังสือวิ่งคั่นส่วนอัปโหลด (สีน้ำเงิน)
st.markdown("""
    <marquee style="background-color: #0000FF; color: white; padding: 8px; font-weight: bold; border-radius: 5px;">
        📸 ส่วนอัปโหลดรูปภาพและวิดีโอส่วนตัว - ทดสอบไฟล์ของคุณได้ที่นี่ 📸
    </marquee>
""", unsafe_allow_html=True)

st.subheader("📸 อัปโหลดส่วนตัว")
col_up1, col_up2 = st.columns(2)
with col_up1:
    uploaded_image = st.file_uploader("รูปภาพของคุณ", type=["jpg", "png"], key="img_final")
    if uploaded_image: st.image(uploaded_image)
with col_up2:
    uploaded_video = st.file_uploader("วิดีโอของคุณ", type=["mp4"], key="vid_final")
    if uploaded_video: st.video(uploaded_video)

# --- [ 6. แชท AI ] ---
st.write("---")
st.subheader("💬 พื้นที่ระบายความในใจ (AI เพื่อนคู่คิด)")
user_text = st.text_area("เพื่อนอยากระบายอะไรไหม?", placeholder="พิมพ์เรื่องที่เจอมาได้เลย...")

if st.button("ส่งความรู้สึก"):
    if user_text:
        with st.spinner('กำลังฟังอย่างตั้งใจ...'):
            reply = ask_ai_for_friend(user_text)
            st.chat_message("assistant").write(reply)
            st.balloons()
    else:
        st.info("บอกอะไรเราหน่อยสิ")

# --- [ 7. ปุ่มลูกเล่นและ LINE ] ---
st.write("---")
col1, col2, col3 = st.columns(3)
with col1:
    if st.button('🎊 ฉลอง!'): st.balloons()
with col2:
    if st.button('❄️ หิมะตก'): st.snow()
with col3:
    if st.button('🔔 ทักทาย'): st.toast('สวัสดีครับ!')

# ✨ 5. ตัวหนังสือวิ่งปิดท้าย (สีเขียว Retro)
st.markdown("""
    <marquee style='color: #00FF00; font-family: Courier; font-size: 20px; background: #000; padding: 10px; border-radius: 10px; border: 1px solid #00FF00;'> 
    🚀 ขอบคุณที่รับชมสถานีเพลงช่างใหญ่... อยู่นิ่งๆ ไม่เจ็บตัว... เพลงดี ดนตรีเพราะ... 🎧 🎶
    </marquee>
    """, unsafe_allow_html=True)

line_link = "https://line.me/ti/p/e-8n-__If_" 
st.link_button("🟢 แตะเพื่อแชทกับเรา (LINE)", line_link, use_container_width=True)

st.sidebar.write('**สโลแกน:** "อยู่นิ่งๆ ไม่เจ็บตัว"')
st.caption("© 2026 สถานีเพลงฟังสบายใจ | อยู่นิ่งๆ ไม่เจ็บตัว")

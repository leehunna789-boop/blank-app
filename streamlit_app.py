import streamlit as st
import streamlit.components.v1 as components
import google.generativeai as genai

# --- 1. ตั้งค่า API และโมเดล (ส่วนหัวใจ) ---
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
else:
    # หากรันในเครื่องตัวเอง ให้ใส่ API Key ตรงๆ เพื่อทดสอบได้
    # genai.configure(api_key="ใส่_KEY_ตรงนี้_ถ้ายังไม่รันบน_Github")
    st.warning("รอการเชื่อมต่อ API Key จากระบบ...")

model = genai.GenerativeModel('gemini-1.5-flash')

def ask_ai_for_friend(user_message):
    prompt = f"คุณคือเพื่อนที่นิ่งสงบ สโลแกนคือ 'อยู่นิ่งๆ ไม่เจ็บตัว' เพื่อนระบายมาว่า: '{user_message}' ช่วยตอบกลับแบบสั้นๆ เข้าใจใจ ให้กำลังใจดีๆ"
    try:
        response = model.generate_content(prompt)
        return response.text
    except:
        return "เราอยู่ตรงนี้ข้างๆ เธอนะ... (ระบบขัดข้องชั่วคราว)"

# --- 2. ตั้งค่าหน้าตาแอป ---
st.set_page_config(page_title="สถานีอยู่นิ่งๆ ไม่เจ็บตัว", page_icon="📻", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: #FFFFFF; text-align: center; }
    .stLinkButton > a {
        background-color: #06C755 !important;
        color: white !important;
        border-radius: 30px !important;
        border: none !important;
        padding: 18px 35px !important;
        font-weight: bold !important;
        font-size: 1.2rem !important;
        text-decoration: none !important;
        display: inline-block !important;
        box-shadow: 0px 4px 15px rgba(6, 199, 85, 0.4);
        transition: 0.3s;
    }
    .stLinkButton > a:hover { transform: scale(1.05); background-color: #05b34c !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. ส่วนหัวสถานี ---
try:
    st.image("globe.jpg", width=250)
except:
    st.header("🌍")

st.markdown("<h2 style='color: #FFD700;'>📻 STATION: อยู่นิ่งๆ ไม่เจ็บตัว</h2>", unsafe_allow_html=True)

st.markdown("""
    <marquee style="color: white; font-weight: bold; background: #050505; padding: 12px; border-radius: 10px; border: 1px solid #FFD700;">
        📢 ยินดีต้อนรับเข้าสู่สถานี อยู่นิ่งๆ ไม่เจ็บตัว ...ทักแชทมาบอกเรื่องราวชีวิตได้เลย เดวจัดเพลงให้ฟังครับ! 🎵 🎧 ขอบคุณที่ติดตามรับฟังครับ ✨
    </marquee>
    """, unsafe_allow_html=True)

st.write("---")

# --- 4. ส่วนวิทยุ/เพลง YouTube ---
st.subheader("📺 รายการเพลงแนะนำ")
playlist_id = "PL6S211I3urvpt47sv8mhbexif2YOzs2gO"
embed_url = f"https://www.youtube.com/embed/videoseries?list={playlist_id}"

st.markdown(f"""
    <iframe width="100%" height="450" src="{embed_url}" 
    title="YouTube Playlist" frameborder="0" 
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
    allowfullscreen style="border-radius:15px; border: 2px solid #333;"></iframe>
    """, unsafe_allow_html=True)

# วิดีโอเด่น
st.write("---")
st.markdown("<h3 style='color: #FF0000;'>🔴 ผลงานเพลงล่าสุด</h3>", unsafe_allow_html=True)
st.video("https://youtu.be/cbcuYnyr828?si=gCdCngKZztQVVZCe")

# --- 5. ส่วนพูดคุยกับ AI (จุดที่แก้ไข) ---
st.write("---")
st.subheader("💬 พื้นที่ระบายความในใจ")
# สร้างกล่องรับข้อความ
user_text = st.text_area("เพื่อนอยากบอกอะไรเราไหม? (พิมพ์ที่นี่นะ)", placeholder="วันนี้เจออะไรมา... บอกดีเจได้นะ")

if st.button("ส่งความรู้สึกให้ AI"):
    if user_text:
        with st.spinner('กำลังฟังอย่างตั้งใจ...'):
            reply = ask_ai_for_friend(user_text)
            st.chat_message("assistant").write(reply)
            st.balloons() # ใส่ลูกเล่นฉลองที่ได้ระบาย
    else:
        st.info("ลองพิมพ์อะไรบางอย่างก่อนกดปุ่มนะ")

# --- 6. ปุ่มลูกเล่นและช่องทางติดตาม ---
st.write("---")
col_sub1, col_sub2 = st.columns(2)
with col_sub1:
    st.link_button("📂 ดูวิดีโอทั้งหมด", "https://www.youtube.com/channel/UC6S211I3urvpt47sv8mhbexif2YOzs2gO/videos", use_container_width=True)
with col_sub2:
    st.link_button("🔴 กดติดตาม (SUB)", "https://www.youtube.com/channel/UC6S211I3urvpt47sv8mhbexif2YOzs2gO?sub_confirmation=1", use_container_width=True)

st.write("---")
col_btn1, col_btn2, col_btn3 = st.columns(3)
with col_btn1:
    if st.button('🎊 ฉลอง!'): st.balloons()
with col_btn2:
    if st.button('❄️ หิมะตก'): st.snow()
with col_btn3:
    if st.button('🔔 ทักทาย'): st.toast('ยินดีต้อนรับครับ!', icon='🙏')

# --- 7. ส่วนอัปโหลดรูปภาพ/วิดีโอ ---
st.write("---")
st.subheader("📸 อัปโหลดส่วนตัว")
col_up1, col_up2 = st.columns(2)
with col_up1:
    uploaded_image = st.file_uploader("รูปของคุณ", type=["jpg", "png"])
    if uploaded_image: st.image(uploaded_image)
with col_up2:
    uploaded_video = st.file_uploader("วิดีโอของคุณ", type=["mp4"])
    if uploaded_video: st.video(uploaded_video)

# --- 8. ส่วนปิดท้ายและปุ่ม LINE ---
st.write("---")
line_link = "https://line.me/ti/p/e-8n-__If_" 
st.link_button("🟢 แตะเพื่อแชทกับเรา (LINE)", line_link, use_container_width=True)

st.sidebar.markdown('**สโลแกน:** "อยู่นิ่งๆ ไม่เจ็บตัว"')
st.caption("© 2026 สถานีเพลงฟังสบายใจ | อยู่นิ่งๆ ไม่เจ็บตัว")

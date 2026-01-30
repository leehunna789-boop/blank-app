import streamlit as st
import google.generativeai as genai

# --- [ 1. การดึง API Key ที่ซ่อนไว้ ] ---
# ระบบจะไปดึงกุญแจจากหน้า Settings > Secrets ของ Streamlit Cloud
try:
    if "GEMINI_API_KEY" in st.secrets:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        model = genai.GenerativeModel('gemini-1.5-flash')
    else:
        st.error("⚠️ ยังไม่ได้ใส่ API Key ในระบบ Secrets ของ Streamlit!")
except Exception as e:
    st.error(f"เกิดข้อผิดพลาดในการเชื่อมต่อ: {e}")

# ฟังก์ชันคุยกับ AI
def ask_ai_for_friend(user_message):
    prompt = f"คุณคือดีเจและเพื่อนที่นิ่งสงบ สโลแกนคือ 'อยู่นิ่งๆ ไม่เจ็บตัว' เพื่อนระบายมาว่า: '{user_message}' ช่วยตอบกลับแบบสั้นๆ นิ่งๆ ให้กำลังใจดีๆ"
    try:
        response = model.generate_content(prompt)
        return response.text
    except:
        return "เราอยู่ตรงนี้ข้างๆ เธอนะ... (ตอนนี้ระบบแชทกำลังพักผ่อน)"

# --- [ 2. ตั้งค่าหน้าสถานีและ UI ] ---
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

# ส่วนหัว
st.markdown("<h2 style='color: #FFD700;'>📻 STATION: อยู่นิ่งๆ ไม่เจ็บตัว</h2>", unsafe_allow_html=True)

st.markdown("""
    <marquee style="color: white; font-weight: bold; background: #050505; padding: 12px; border-radius: 10px; border: 1px solid #FFD700;">
        📢 ยินดีต้อนรับเข้าสู่สถานี อยู่นิ่งๆ ไม่เจ็บตัว ...ทักแชทมาบอกเรื่องราวชีวิตได้เลย เดวจัดเพลงให้ฟังครับ! 🎵 🎧
    </marquee>
    """, unsafe_allow_html=True)

# --- [ 3. ส่วนรายการเพลง YouTube ] ---
st.subheader("📺 รายการเพลงแนะนำ")
playlist_id = "PL6S211I3urvpt47sv8mhbexif2YOzs2gO"
embed_url = f"https://www.youtube.com/embed/videoseries?list={playlist_id}"

st.markdown(f"""
    <iframe width="100%" height="400" src="{embed_url}" 
    frameborder="0" allowfullscreen style="border-radius:15px; border: 2px solid #333;"></iframe>
    """, unsafe_allow_html=True)

# --- [ 4. ส่วนไฮไลท์: แชทกับ AI ] ---
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

# --- [ 5. แผงควบคุมและปุ่มลูกเล่น ] ---
st.write("---")
col_btn1, col_btn2, col_btn3 = st.columns(3)
with col_btn1:
    if st.button('🎊 ฉลอง!'): st.balloons()
with col_btn2:
    if st.button('❄️ หิมะตก'): st.snow()
with col_btn3:
    if st.button('🔔 ทักทาย'): st.toast('ยินดีต้อนรับครับ!', icon='🙏')

# --- [ 6. ส่วนอัปโหลดรูปภาพ/วิดีโอ ] ---
st.write("---")
uploaded_file = st.file_uploader("📸 แบ่งปันรูปภาพหรือวิดีโอของคุณ", type=["jpg", "png", "mp4"])
if uploaded_file:
    if uploaded_file.type.startswith('image'):
        st.image(uploaded_file)
    else:
        st.video(uploaded_file)

# --- [ 7. ส่วนท้ายและปุ่ม LINE ] ---
st.write("---")
line_link = "https://line.me/ti/p/e-8n-__If_" 
st.link_button("🟢 แตะเพื่อแชทกับเรา (LINE)", line_link, use_container_width=True)

st.sidebar.markdown('**สโลแกน:** "อยู่นิ่งๆ ไม่เจ็บตัว"')
st.caption("© 2026 สถานีเพลงช่างใหญ่ | อยู่นิ่งๆ ไม่เจ็บตัว")

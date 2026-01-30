import streamlit as st
import google.generativeai as genai

# --- [ 1. การดึง API Key จาก Secrets ] ---
try:
    if "GEMINI_API_KEY" in st.secrets:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        model = genai.GenerativeModel('gemini-1.5-flash')
    else:
        st.error("⚠️ ยังไม่ได้ใส่ API Key ในระบบ Secrets!")
except Exception as e:
    st.error(f"การเชื่อมต่อผิดพลาด: {e}")

def ask_ai_for_friend(user_message):
    prompt = f"คุณคือดีเจและเพื่อนที่นิ่งสงบ สโลแกนคือ 'อยู่นิ่งๆ ไม่เจ็บตัว' เพื่อนระบายมาว่า: '{user_message}' ช่วยตอบกลับแบบสั้นๆ นิ่งๆ ให้กำลังใจดีๆ"
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"เราอยู่ตรงนี้ข้างๆ เธอนะ... (ติดปัญหา: {e})"

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
        padding: 15px 25px !important;
        font-weight: bold !important;
        text-decoration: none !important;
        display: inline-block !important;
    }
    .fb-button > a {
        background-color: #1877F2 !important; /* สีน้ำเงิน Facebook */
    }
    </style>
    """, unsafe_allow_html=True)

# 🌍 โลโก้
try:
    st.image("globe.jpg", width=250)
except:
    st.header("🌍")

st.markdown("<h2 style='color: #FFD700;'>📻 STATION: อยู่นิ่งๆ ไม่เจ็บตัว</h2>", unsafe_allow_html=True)

# ✨ ตัวหนังสือวิ่งอันที่ 1
st.markdown("""
    <marquee style="color: white; font-weight: bold; background: #050505; padding: 12px; border-radius: 10px; border: 1px solid #FFD700;">
        📢 ยินดีต้อนรับเข้าสู่สถานี อยู่นิ่งๆ ไม่เจ็บตัว ...ทักแชทมาบอกเรื่องราวชีวิตได้เลย เดวจัดเพลงให้ฟังครับ! 🎵 🎧
    </marquee>
    """, unsafe_allow_html=True)

st.write("---")

# --- [ 3. YouTube ส่วนที่ 1: Playlist ] ---
st.subheader("📺 รายการเพลงแนะนำ (Playlist)")
playlist_id = "PL6S211I3urvpt47sv8mhbexif2YOzs2gO"
embed_url = f"https://www.youtube.com/embed/videoseries?list={playlist_id}"
st.markdown(f"""
    <iframe width="100%" height="400" src="{embed_url}" frameborder="0" allowfullscreen style="border-radius:15px; border: 2px solid #333;"></iframe>
    """, unsafe_allow_html=True)

# ✨ ตัวหนังสือวิ่งคั่น
st.markdown("<marquee style='background: #FFD700; color: black; padding: 5px; font-weight: bold;'>🔴 กำลังรับฟังผลงานเพลงจากช่อง S.S.S Music 🔴</marquee>", unsafe_allow_html=True)

# --- [ 4. YouTube ส่วนที่ 2 & 3 และปุ่มแชร์ ] ---
st.write("---")
st.video("https://youtu.be/cbcuYnyr828?si=gCdCngKZztQVVZCe")
st.video("https://youtu.be/Bb3Jtsik3nY?si=Qyz3WtZLcxML3uF_")

# 📢 ส่วนของปุ่มแชร์ Facebook (ใส่กลับมาให้แล้วครับ!)
st.write("📢 **ถูกใจสถานีเรา แชร์บอกเพื่อนได้เลย!**")
share_url = "https://41g5.streamlit.app" # เปลี่ยนเป็น URL จริงของแอปคุณนะครับ
facebook_share = f"https://www.facebook.com/sharer/sharer.php?u={share_url}"
st.markdown(f'<div class="fb-button">', unsafe_allow_html=True)
st.link_button("🔵 แชร์สถานีไปยัง Facebook", facebook_share, use_container_width=True)
st.markdown(f'</div>', unsafe_allow_html=True)

# --- [ 5. ส่วนแชท AI ] ---
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

# --- [ 6. ปุ่มลูกเล่นและตัววิ่งปิดท้าย ] ---
st.write("---")
col1, col2, col3 = st.columns(3)
with col1:
    if st.button('🎊 ฉลอง!'): st.balloons()
with col2:
    if st.button('❄️ หิมะตก'): st.snow()
with col3:
    if st.button('🔔 ทักทาย'): st.toast('สวัสดีครับ!')

st.markdown("""
    <marquee style='color: #00FF00; font-family: Courier; font-size: 20px; background: #000; padding: 10px; border-radius: 10px;'> 
    🚀 ขอบคุณที่รับชมสถานีเพลงช่างใหญ่... อยู่นิ่งๆ ไม่เจ็บตัว... เพลงดี ดนตรีเพราะ... 🎧 🎶
    </marquee>
    """, unsafe_allow_html=True)

# --- [ 7. ปุ่ม LINE ] ---
st.write("---")
line_link = "https://line.me/ti/p/e-8n-__If_" 
st.link_button("🟢 แตะเพื่อแชทกับเรา (LINE)", line_link, use_container_width=True)

st.sidebar.write('**สโลแกน:** "อยู่นิ่งๆ ไม่เจ็บตัว"')
st.caption("© 2026 สถานีเพลงฟังสบายใจ | อยู่นิ่งๆ ไม่เจ็บตัว")

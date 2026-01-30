import streamlit as st
import google.generativeai as genai

# --- [ 1. การดึง API Key และตั้งค่าโมเดล ] ---
try:
    if "GEMINI_API_KEY" in st.secrets:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        # แก้ไขชื่อโมเดลเป็นรุ่นมาตรฐานเพื่อลด Error 404
        model = genai.GenerativeModel('gemini-pro') 
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

# --- [ 2. UI และโลโก้ ] ---
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
    }
    </style>
    """, unsafe_allow_html=True)

try:
    st.image("globe.jpg", width=250)
except:
    st.header("🌍")

st.markdown("<h2 style='color: #FFD700;'>📻 STATION: อยู่นิ่งๆ ไม่เจ็บตัว</h2>", unsafe_allow_html=True)

st.markdown("""
    <marquee style="color: white; font-weight: bold; background: #050505; padding: 12px; border-radius: 10px; border: 1px solid #FFD700;">
        📢 ยินดีต้อนรับเข้าสู่สถานี อยู่นิ่งๆ ไม่เจ็บตัว ...ทักแชทมาบอกเรื่องราวชีวิตได้เลยครับ ✨
    </marquee>
    """, unsafe_allow_html=True)

# --- [ 3. YouTube ทั้ง 3 ส่วน ] ---
st.write("---")
playlist_id = "PL6S211I3urvpt47sv8mhbexif2YOzs2gO"
embed_url = f"https://www.youtube.com/embed/videoseries?list={playlist_id}"
st.markdown(f'<iframe width="100%" height="400" src="{embed_url}" frameborder="0" allowfullscreen style="border-radius:15px;"></iframe>', unsafe_allow_html=True)

st.write("---")
st.video("https://youtu.be/cbcuYnyr828?si=gCdCngKZztQVVZCe")
st.video("https://youtu.be/Bb3Jtsik3nY?si=Qyz3WtZLcxML3uF_")

# --- [ 4. ปุ่มแชร์เฟซบุ๊ก (Share) ] ---
share_url = "https://41g5.streamlit.app"
facebook_share = f"https://www.facebook.com/sharer/sharer.php?u={share_url}"
st.link_button("🔵 แชร์สถานีไปยัง Facebook", facebook_share, use_container_width=True)

# --- [ 5. ช่องอัปโหลดรูปและวิดีโอ (ดึงกลับมาแล้วครับ) ] ---
st.write("---")
st.subheader("📸 อัปโหลดส่วนตัว (รูป/วิดีโอของคุณ)")
col_up1, col_up2 = st.columns(2)
with col_up1:
    uploaded_image = st.file_uploader("อัปโหลดรูปภาพ", type=["jpg", "png"], key="img_up")
    if uploaded_image: st.image(uploaded_image)
with col_up2:
    uploaded_video = st.file_uploader("อัปโหลดวิดีโอ", type=["mp4"], key="vid_up")
    if uploaded_video: st.video(uploaded_video)

# --- [ 6. ส่วนแชท AI ] ---
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

line_link = "https://line.me/ti/p/e-8n-__If_" 
st.link_button("🟢 แตะเพื่อแชทกับเรา (LINE)", line_link, use_container_width=True)

st.sidebar.write('**สโลแกน:** "อยู่นิ่งๆ ไม่เจ็บตัว"')
st.caption("© 2026 สถานีเพลงฟังสบายใจ | อยู่นิ่งๆ ไม่เจ็บตัว")

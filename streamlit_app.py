import streamlit as st
import google.generativeai as genai
import random

# --- [ 1. ตั้งค่าหน้าสถานี - ต้องอยู่บนสุด ] ---
st.set_page_config(page_title="สถานีอยู่นิ่งๆ ไม่เจ็บตัว", page_icon="📻", layout="centered")

# --- [ 2. การตั้งค่า AI & Secrets ] ---
try:
    my_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=my_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
except:
    st.error("⚠️ ยังไม่ได้ใส่กุญแจลับ (API Key) ในระบบ Secrets")
    model = None

# --- [ 3. ฟังก์ชันและลูกเล่นเสริม ] ---
def ask_ai_for_friend(user_message):
    prompt = f"คุณคือดีเจเพื่อนคู่คิด ชื่อช่างใหญ่ สโลแกนคือ 'อยู่นิ่งๆ ไม่เจ็บตัว' เพื่อนระบายว่า: '{user_message}' ตอบแบบนิ่งๆ กวนนิดๆ ให้กำลังใจดีๆ"
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        if "429" in str(e): return "วันนี้คุยเยอะแล้วนะ... พักผ่อนบ้างเพื่อน (โควตาหมด)"
        return f"เรารับฟังอยู่นะ... ({e})"

# ลูกเล่นเพิ่ม: สุ่มคำคมปลอบใจ
quotes = [
    "นิ่งไว้เพื่อน... เดี๋ยวดีเอง", 
    "ชีวิตมันสั้น... อย่าปั่นให้มันเหนื่อย", 
    "อยู่นิ่งๆ ไม่เจ็บตัว เชื่อช่างใหญ่",
    "ถ้าใจเรานิ่ง... ปัญหาก็แค่สิ่งสมมติ"
]
random_quote = random.choice(quotes)

# --- [ 4. ปรับแต่งหน้าตา (CSS) ] ---
st.markdown(f"""
    <style>
    .stApp {{ background-color: #0E1117; color: #FFFFFF; text-align: center; }}
    .quote-box {{
        padding: 20px;
        border-radius: 15px;
        background: rgba(255, 215, 0, 0.1);
        border-left: 5px solid #FFD700;
        margin-bottom: 20px;
    }}
    .on-air {{ color: #FF0000; font-weight: bold; animation: blinker 1s linear infinite; }}
    @keyframes blinker {{ 50% {{ opacity: 0; }} }}
    </style>
    """, unsafe_allow_html=True)

# 🌍 โลโก้และหัวข้อ
try:
    st.image("globe.jpg", width=250)
except:
    st.header("🌍")

st.markdown("<h2 style='color: #FFD700;'>📻 STATION: อยู่นิ่งๆ ไม่เจ็บตัว ไอ้บอล พร้อมครอบครัว</h2>", unsafe_allow_html=True)

# ลูกเล่นเพิ่ม: คำคมประจำวัน
st.markdown(f'<div class="quote-box">✨ <b>คำคมช่างใหญ่:</b> {random_quote}</div>', unsafe_allow_html=True)

# ✨ ตัวหนังสือวิ่งบนสุด
st.markdown("""<marquee style="color: white; font-weight: bold; background: #050505; padding: 12px; border-radius: 10px; border: 1px solid #FFD700;">📢 ยินดีต้อนรับเข้าสู่สถานี อยู่นิ่งๆ ไม่เจ็บตัว ...ทักแชทระบายเรื่องราวชีวิตได้เลยครับ ✨</marquee>""", unsafe_allow_html=True)

# --- [ 5. YouTube & สื่อ ] ---
st.write("---")
playlist_url = "https://www.youtube.com/embed/videoseries?list=PL6S211I3urvpt47sv8mhbexif2YOzs2gO"
st.markdown(f'<iframe width="100%" height="400" src="{playlist_url}" frameborder="0" allowfullscreen style="border-radius:15px; border: 2px solid #333;"></iframe>', unsafe_allow_html=True)

st.markdown("<marquee style='background: #FFD700; color: black; padding: 8px; font-weight: bold; border-radius: 5px; margin-top: 10px;'>🔴 กำลังรับฟังผลงานเพลงจากช่อง S.S.S Music 🔴</marquee>", unsafe_allow_html=True)

st.write("---")
st.video("https://youtu.be/cbcuYnyr828?si=gCdCngKZztQVVZCe")

st.markdown("<marquee style='background: #FF0000; color: white; padding: 8px; font-weight: bold; border-radius: 5px; margin-bottom: 10px;'>📺 ยินดีต้อนรับสู่ช่อง อยู่นิ้งๆไม่เจ็บตัว 🎬</marquee>", unsafe_allow_html=True)
st.video("https://youtu.be/Bb3Jtsik3nY?si=Qyz3WtZLcxML3uF_")

# --- [ 6. ระบบแชท AI เพื่อนคู่คิด ] ---
st.write("---")
st.subheader("💬 พื้นที่ระบายความในใจ (เพื่อนคู่คิด)")
user_input = st.text_area("อยากระบายอะไรไหมเพื่อน?", placeholder="พิมพ์เรื่องที่เจอมาได้เลย...", key="ai_chat_input")

if st.button("ส่งความรู้สึกให้ช่างใหญ่"):
    if user_input:
        with st.spinner('กำลังฟังอย่างตั้งใจ...'):
            reply = ask_ai_for_friend(user_input)
            st.chat_message("assistant").write(reply)
            st.balloons()
            # เก็บลงลิสต์ประวัติ
            if 'msg_list' not in st.session_state: st.session_state.msg_list = []
            st.session_state.msg_list.append(user_input)
    else:
        st.info("บอกอะไรเราหน่อยสิ")

# โชว์ข้อความที่ระบายไว้ (จากโค้ดเดิม)
if 'msg_list' in st.session_state:
    with st.expander("📌 ประวัติการระบาย"):
        for m in st.session_state.msg_list[::-1]:
            st.info(m)

# --- [ 7. อัปโหลด & โซเชียล ] ---
st.write("---")
share_url = "https://41g5.streamlit.app"
st.link_button("🔵 แชร์สถานีไปยัง Facebook", f"https://www.facebook.com/sharer/sharer.php?u={share_url}", use_container_width=True)

st.markdown("<marquee style='background: #0000FF; color: white; padding: 8px; font-weight: bold; border-radius: 5px;'>📸 พื้นที่อัปโหลดรูปภาพและวิดีโอส่วนตัว 📸</marquee>", unsafe_allow_html=True)
st.subheader("📸 อัปโหลดส่วนตัว")
c1, c2 = st.columns(2)
with c1:
    up_img = st.file_uploader("อัปโหลดรูป", type=["jpg", "png"], key="img_up")
    if up_img: st.image(up_img)
with c2:
    up_vid = st.file_uploader("อัปโหลดวิดีโอ", type=["mp4"], key="vid_up")
    if up_vid: st.video(up_vid)

# --- [ 8. ปุ่มเล่นเอฟเฟกต์ ] ---
st.write("---")
col1, col2, col3 = st.columns(3)
with col1:
    if st.button('🎊 ฉลอง'): st.balloons()
with col2:
    if st.button('❄️ หิมะ'): st.snow()
with col3:
    if st.button('🔔 ทักทาย'): st.toast('สวัสดีครับ!')

# ปิดท้าย
st.markdown("<marquee style='color: #050505; font-family: Courier; font-size: 20px; background: #000; padding: 10px; border-radius: 10px; border: 1px solid #00FF00;'>🚀 ขอบคุณที่รับชมสถานีเพลงช่างใหญ่... อยู่นิ่งๆ ไม่เจ็บตัว... 🎧 🎶</marquee>", unsafe_allow_html=True)
st.link_button("🟢 แตะเพื่อแชทกับเรา (LINE)", "https://line.me/ti/p/e-8n-__If_", use_container_width=True)

# Sidebar ลูกเล่นเพิ่ม
st.sidebar.markdown('### <span class="on-air">● ON AIR</span>', unsafe_allow_html=True)
st.sidebar.write('**DJ:** บอล (ช่างใหญ่)')
st.sidebar.write('**สโลแกน:** "อยู่นิ่งๆ ไม่เจ็บตัว"')
st.sidebar.caption("© 2026 สถานีเพลงช่างใหญ่")

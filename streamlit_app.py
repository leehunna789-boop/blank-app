import streamlit as st
import google.generativeai as genai
import random

# --- [ 1. ตั้งค่าหน้าสถานี ] ---
st.set_page_config(page_title="สถานีอยู่นิ่งๆ ไม่เจ็บตัว", page_icon="📻", layout="centered")

# --- [ 2. การตั้งค่าความปลอดภัย (Secrets) ] ---
try:
    my_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=my_key)
    model = genai.GenerativeModel('gemini-1.5-flash-latest') 
except Exception as e:
    st.error(f"⚠️ ปัญหาการตั้งค่ากุญแจ: {e}")
    model = None

# --- [ 3. ฟังก์ชันการทำงานของ AI ] ---
def ask_ai_for_friend(user_message):
    if model is None:
        return "ตอนนี้ช่างใหญ่ทำกุญแจหาย... (กรุณาเช็ค API Key ใน Secrets)"
    
    prompt = f"คุณคือดีเจเพื่อนคู่คิด ชื่อช่างใหญ่ สโลแกนคือ 'อยู่นิ่งๆ ไม่เจ็บตัว' เพื่อนระบายว่า: '{user_message}' ตอบแบบนิ่งๆ กวนนิดๆ ให้กำลังใจดีๆ"
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        if "429" in str(e):
            return "วันนี้คุยกันเยอะแล้วนะเพื่อน... พักผ่อนบ้างนะ (โควตาฟรีหมดชั่วคราว)"
        return f"เรารับฟังอยู่นะ... (ระบบขัดข้องนิดหน่อย: {e})"

# สุ่มคำคม
quotes = ["นิ่งไว้เพื่อน... เดี๋ยวดีเอง", "ชีวิตมันสั้น... อย่าปั่นให้มันเหนื่อย", "อยู่นิ่งๆ ไม่เจ็บตัว เชื่อช่างใหญ่"]
random_quote = random.choice(quotes)

# --- [ 4. การตกแต่งหน้าตาด้วย CSS (เพิ่มไฟกระพริบเยอะๆ) ] ---
st.markdown(f"""
    <style>
    .stApp {{ background-color: #0E1117; color: #FFFFFF; text-align: center; }}
    .quote-box {{ padding: 20px; border-radius: 15px; background: rgba(255, 215, 0, 0.1); border-left: 5px solid #FFD700; margin-bottom: 20px; }}
    .on-air {{ color: #FF0000; font-weight: bold; animation: blinker 1s linear infinite; }}
    @keyframes blinker {{ 50% {{ opacity: 0; }} }}
    .flashing-text-red {{ color: #FF0000; font-weight: bold; animation: flash-red 0.5s infinite alternate; }}
    .flashing-text-yellow {{ color: #FFFF00; font-weight: bold; animation: flash-yellow 0.7s infinite alternate; }}
    .flashing-text-blue {{ color: #00FFFF; font-weight: bold; animation: flash-blue 0.6s infinite alternate; }}

    @keyframes flash-red {{ from {{ opacity: 1; }} to {{ opacity: 0.3; }} }}
    @keyframes flash-yellow {{ from {{ opacity: 1; }} to {{ opacity: 0.2; }} }}
    @keyframes flash-blue {{ from {{ opacity: 1; }} to {{ opacity: 0.4; }} }}
    </style>
    """, unsafe_allow_html=True)

# 🌍 โลโก้
try:
    st.image("globe.jpg", width=250)
except:
    st.header("🌍")

st.markdown("<h2 style='color: #FFD700;'>📀 STATION:🎉 อยู่นิ่งๆ ไม่เจ็บตัว 🎊</h2>", unsafe_allow_html=True)
st.markdown(f'<div class="quote-box">✨ <b>คำคมวันนี้:</b> {random_quote}</div>', unsafe_allow_html=True)

# ✨ ตัวหนังสือวิ่ง (ยังคงเดิม)
st.markdown("""<marquee style="color: white; font-weight: bold; background: #050505; padding: 12px; border-radius: 10px; border: 1px solid #FFD700;">📢 ยินดีต้อนรับเข้าสู่สถานี อยู่นิ่งๆ ไม่เจ็บตัว ...ทักแชทระบายเรื่องราวชีวิตได้เลยครับ ✨</marquee>""", unsafe_allow_html=True)

# --- [ 5. YouTube 5 ช่อง (จัดเต็ม) ] ---
st.write("---")
st.markdown("<h3 class='flashing-text-red'>🎵 เพลงฮิตติดสถานี 🎵</h3>", unsafe_allow_html=True)

# YouTube Playlist 1
playlist_url_1 = "https://www.youtube.com/embed/videoseries?list=PL6S211I3urvpt47sv8mhbexif2YOzs2gO"
st.markdown(f'<iframe width="100%" height="300" src="{playlist_url_1}" frameborder="0" allowfullscreen style="border-radius:15px; border: 2px solid #FFD700;"></iframe>', unsafe_allow_html=True)
st.markdown("<marquee style='background: #FFD700; color: black; padding: 8px; font-weight: bold; border-radius: 5px; margin-top: 10px;'>🔴 กำลังรับฟังผลงานเพลงจากช่อง S.S.S Music 🔴</marquee>", unsafe_allow_html=True)
st.write("---")

# YouTube Video 2
st.markdown("<h3 class='flashing-text-yellow'>🎬 วิดีโอแนะนำจากช่างใหญ่ 🎬</h3>", unsafe_allow_html=True)
st.video("https://youtu.be/cbcuYnyr828?si=gCdCngKZztQVVZCe")
st.markdown("<marquee style='background: #FFFF00; color: black; padding: 8px; font-weight: bold; border-radius: 5px; margin-top: 10px;'>🟡 อย่าลืมกดติดตามช่องช่างใหญ่ด้วยนะ 🟡</marquee>", unsafe_allow_html=True)
st.write("---")

# YouTube Video 3
st.markdown("<h3 class='flashing-text-blue'>🔵 มิวสิควิดีโอโดนใจ 🔵</h3>", unsafe_allow_html=True)
st.video("https://youtu.be/Bb3Jtsik3nY?si=Qyz3WtZLcxML3uF_")
st.markdown("<marquee style='background: #00FFFF; color: black; padding: 8px; font-weight: bold; border-radius: 5px; margin-top: 10px;'>🔵 เพลงเพราะฟังวนไป 🔵</marquee>", unsafe_allow_html=True)
st.write("---")

# YouTube Video 4 (ตัวอย่าง)
st.markdown("<h3 class='flashing-text-red'>🔥 โชว์สดสุดมันส์ 🔥</h3>", unsafe_allow_html=True)
# **TODO: เปลี่ยนลิงก์ YouTube นี้เป็นวิดีโอที่คุณต้องการ**
st.video("https://youtu.be/cbcuYnyr828?si=YW9hXquVFRSa03gO") # ลิงก์ตัวอย่าง (Rickroll)
st.markdown("<marquee style='background: #FF0000; color: white; padding: 8px; font-weight: bold; border-radius: 5px; margin-top: 10px;'>🔴 สนุกจนหยุดไม่อยู่ 🔴</marquee>", unsafe_allow_html=True)
st.write("---")

# YouTube Video 5 (ตัวอย่าง)
st.markdown("<h3 class='flashing-text-yellow'>🌟 เพลงใหม่มาแรง 🌟</h3>", unsafe_allow_html=True)
# **TODO: เปลี่ยนลิงก์ YouTube นี้เป็นวิดีโอที่คุณต้องการ**
st.video("https://youtube.com/shorts/4529wwOotw4?si=XlE3rOogM_-8lh_j") # ลิงก์ตัวอย่าง (เพลง)
st.markdown("<marquee style='background: #FFFF00; color: black; padding: 8px; font-weight: bold; border-radius: 5px; margin-top: 10px;'>🟡 ห้ามพลาดเด็ดขาด 🟡</marquee>", unsafe_allow_html=True)
st.write("---")


# --- [ 6. แชท AI ] ---
st.subheader("💬 พื้นที่ระบายความในใจ (ช่างใหญ่ AI)")
user_input = st.text_area("อยากระบายอะไรไหมเพื่อน?", placeholder="พิมพ์เรื่องที่เจอมาได้เลย...", key="ai_input_main")

if st.button("ส่งความรู้สึกให้ช่างใหญ่"):
    if user_input:
        with st.spinner('กำลังฟังอย่างตั้งใจ...'):
            reply = ask_ai_for_friend(user_input)
            st.chat_message("assistant").write(reply)
            st.balloons()
            st.toast("555+ นิ่งไว้เพื่อน ช่างใหญ่ขำรอแล้ว!", icon="🤣")
            
            if 'msg_list' not in st.session_state: st.session_state.msg_list = []
            st.session_state.msg_list.append(user_input)
    else:
        st.info("บอกอะไรเราหน่อยสิ")

if 'msg_list' in st.session_state:
    with st.expander("📌 การระบายที่ผ่านมา..."):
        for m in st.session_state.msg_list[::-1]:
            st.write(f"• {m}")

# --- [ 7. อัปโหลดรูปภาพและวิดีโอ (เยอะขึ้น) & โซเชียล ] ---
st.write("---")
st.markdown("<marquee style='background: #0000FF; color: white; padding: 8px; font-weight: bold; border-radius: 5px;'>📸 พื้นที่อัปโหลดรูปภาพและวิดีโอส่วนตัว 📸</marquee>", unsafe_allow_html=True)
st.subheader("📸 อัปโหลดส่วนตัว (สูงสุด 4 ไฟล์)")

# เพิ่มช่องอัปโหลดเป็น 2 แถว แถวละ 2 คอลัมน์
col_img1, col_vid1 = st.columns(2)
with col_img1:
    up_img1 = st.file_uploader("รูปภาพ 1", type=["jpg", "png"], key="img_up1")
    if up_img1: st.image(up_img1)
with col_vid1:
    up_vid1 = st.file_uploader("วิดีโอ 1", type=["mp4"], key="vid_up1")
    if up_vid1: st.video(up_vid1)

col_img2, col_vid2 = st.columns(2)
with col_img2:
    up_img2 = st.file_uploader("รูปภาพ 2", type=["jpg", "png"], key="img_up2")
    if up_img2: st.image(up_img2)
with col_vid2:
    up_vid2 = st.file_uploader("วิดีโอ 2", type=["mp4"], key="vid_up2")
    if up_vid2: st.video(up_vid2)

st.link_button("🔵 แชร์สถานีไปยัง Facebook", f"https://www.facebook.com/sharer/sharer.php?u=https://41g5.streamlit.app", use_container_width=True)

# --- [ 8. ปุ่มลูกเล่น ] ---
st.write("---")
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button('🎊 ฉลอง'): st.balloons()
with col2:
    if st.button('❄️ หิมะ'): st.snow()
with col3:
    if st.button('👏 ตบมือ'): st.toast('แปะๆๆๆๆ! สุดยอด!', icon="👏")
with col4:
    if st.button('🤣 หัวเราะ'): st.toast('5555+ นิ่งไว้เพื่อน!', icon="🤣")

# ปิดท้าย
st.markdown("<marquee style='color: #050505; font-family: Courier; background: #000; padding: 10px; border-radius: 10px; border: 1px solid #00FF00;'>🚀 ขอบคุณที่รับชมสถานีเพลงช่างใหญ่... อยู่นิ่งๆ ไม่เจ็บตัว... 🎧</marquee>", unsafe_allow_html=True)
st.link_button("🟢 แตะเพื่อแชทกับเรา (LINE)", "https://line.me/ti/p/e-8n-__If_", use_container_width=True)

# Sidebar
st.sidebar.markdown('### <span class="on-air">● DJ บอล ON AIR</span>', unsafe_allow_html=True)
st.sidebar.write('สโลแกน: **"อยู่นิ่งๆ ไม่เจ็บตัว"**')

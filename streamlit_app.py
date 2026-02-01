import streamlit as st
import google.generativeai as genai
import streamlit as st
import google.generativeai as genai

# แทนที่จะใส่รหัสตรงๆ ให้เรียกใช้จากระบบ Secrets ของ Streamlit
# มันจะไปดึงค่าจาก "ลิ้นชักลับ" ที่เราจะไปตั้งค่าในเว็บครับ
try:
    my_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=my_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
except:
    st.error("⚠️ ยังไม่ได้ใส่กุญแจลับ (API Key) ในระบบ Secrets ")
    st.write("---")
st.subheader("💬 อยากระบายอะไรไหมเพื่อน?")

# ช่องรับข้อความ
user_msg = st.text_area("พิมพ์ความรู้สึกที่นี่...", placeholder="เบื่อจริงต้องทำไง...")

if st.button("ส่งความรู้สึก"):
    if user_msg:
        # แสดงข้อความตอบกลับแบบกวนๆ สไตล์ช่างใหญ่
        st.balloons()
        st.success("ช่างใหญ่ได้รับข้อความแล้ว! นิ่งไว้เพื่อน เดี๋ยวดีเอง 555")
        
        # เก็บข้อความไว้ในลิสต์โชว์หน้าจอ (รกๆ ดีครับ)
        if 'messages' not in st.session_state:
            st.session_state.messages = []
        st.session_state.messages.append(user_msg)
    else:
        st.warning("พิมพ์อะไรมาหน่อยสิเพื่อน!")

# โชว์สิ่งที่เพื่อนๆ พิมพ์มา (ความรกที่ช่างใหญ่ชอบ)
if 'messages' in st.session_state:
    st.write("---")
    st.write("📌 **สิ่งที่เพื่อนๆ ระบายไว้:**")
    for m in st.session_state.messages[::-1]: # เอาอันล่าสุดขึ้นก่อน
        st.info(m)

def ask_ai_for_friend(user_message):
    prompt = f"คุณคือดีเจเพื่อนคู่คิด สโลแกนคือ 'อยู่นิ่งๆ ไม่เจ็บตัว' เพื่อนระบายว่า: '{user_message}' ตอบแบบนิ่งๆ ให้กำลังใจดีๆ"
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        # ดักจับ Error 429 (โควตาเต็ม)
        if "429" in str(e):
            return "วันนี้เราคุยกันเยอะแล้วนะเพื่อน... พักผ่อนบ้างนะ เดี๋ยวพรุ่งนี้มาคุยกันใหม่ (โควตาฟรีหมดชั่วคราวครับ)"
        return f"เรารับฟังอยู่นะ... (ติดปัญหา: {e})"

# --- [ 2. ตั้งค่าหน้าสถานี ] ---
st.set_page_config(page_title="สถานีอยู่นิ่งๆ ไม่เจ็บตัว", page_icon="📻", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: #FFFFFF; text-align: center; }
    .stLinkButton > a {
        background-color: #06C755 !important;
        color: white !important;
        border-radius: 30px !important;
        font-weight: bold !important;
        text-decoration: none !important;
        display: inline-block !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 🌍 โลโก้
try:
    st.image("globe.jpg", width=250)
except:
    st.header("🌍")

st.markdown("<h2 style='color: #FFD700;'>📻 STATION: อยู่นิ่งๆ ไม่เจ็บตัว ไอ้บอล พร้อมครอบครัว</h2>", unsafe_allow_html=True)

# ✨ 1. ตัวหนังสือวิ่งบนสุด
st.markdown("""<marquee style="color: white; font-weight: bold; background: #050505; padding: 12px; border-radius: 10px; border: 1px solid #FFD700;">📢 ยินดีต้อนรับเข้าสู่สถานี อยู่นิ่งๆ ไม่เจ็บตัว ...ทักแชทระบายเรื่องราวชีวิตได้เลยครับ ✨</marquee>""", unsafe_allow_html=True)

# --- [ 3. YouTube 3 จุด ] ---
st.write("---")
# 1. Playlist
playlist_url = "https://www.youtube.com/embed/videoseries?list=PL6S211I3urvpt47sv8mhbexif2YOzs2gO"
st.markdown(f'<iframe width="100%" height="400" src="{playlist_url}" frameborder="0" allowfullscreen style="border-radius:15px; border: 2px solid #333;"></iframe>', unsafe_allow_html=True)

# ✨ 2. ตัวหนังสือวิ่งคั่น YouTube 1 (สีทอง)
st.markdown("<marquee style='background: #FFD700; color: black; padding: 8px; font-weight: bold; border-radius: 5px; margin-top: 10px;'>🔴 กำลังรับฟังผลงานเพลงจากช่อง S.S.S Music 🔴</marquee>", unsafe_allow_html=True)

st.write("---")
# 2. วิดีโอเพลง
st.video("https://youtu.be/cbcuYnyr828?si=gCdCngKZztQVVZCe")

# ✨ 3. ตัวหนังสือวิ่งคั่น YouTube 2 (สีแดง)
st.markdown("<marquee style='background: #FF0000; color: white; padding: 8px; font-weight: bold; border-radius: 5px; margin-bottom: 10px;'>📺 ยินดีต้อนรับสู่ช่อง อยู่นิ้งๆไม่เจ็บตัว 🎬</marquee>", unsafe_allow_html=True)

# 3. วิดีโอช่อง
st.video("https://youtu.be/Bb3Jtsik3nY?si=Qyz3WtZLcxML3uF_")

# --- [ 4. แชร์เฟซบุ๊ก & อัปโหลด ] ---
share_url = "https://41g5.streamlit.app"
facebook_share = f"https://www.facebook.com/sharer/sharer.php?u={share_url}"
st.link_button("🔵 แชร์สถานีไปยัง Facebook", facebook_share, use_container_width=True)

st.write("---")
# ✨ 4. ตัวหนังสือวิ่งส่วนอัปโหลด (สีน้ำเงิน)
st.markdown("<marquee style='background: #0000FF; color: white; padding: 8px; font-weight: bold; border-radius: 5px;'>📸 พื้นที่อัปโหลดรูปภาพและวิดีโอส่วนตัว 📸</marquee>", unsafe_allow_html=True)

st.subheader("📸 อัปโหลดส่วนตัว")
c1, c2 = st.columns(2)
with c1:
    up_img = st.file_uploader("อัปโหลดรูป", type=["jpg", "png"], key="img_final")
    if up_img: st.image(up_img)
with c2:
    up_vid = st.file_uploader("อัปโหลดวิดีโอ", type=["mp4"], key="vid_final")
    if up_vid: st.video(up_vid)

# --- [ 5. แชท AI ] ---
st.write("---")
st.subheader("💬 พื้นที่ระบายความในใจ (อยู่นิ้งๆไม่เจ็บตัว เพื่อนคู่คิด)")
user_input = st.text_area("อยากระบายอะไรไหมเพื่อน?", placeholder="พิมพ์เรื่องที่เจอมาได้เลย...")

if st.button("ส่งความรู้สึก"):
    if user_input:
        with st.spinner('กำลังฟังอย่างตั้งใจ...'):
            reply = ask_ai_for_friend(user_input)
            st.chat_message("assistant").write(reply)
            st.balloons()
    else:
        st.info("บอกอะไรเราหน่อยสิ")

# --- [ 6. ลูกเล่น & ปิดท้าย ] ---
st.write("---")
col1, col2, col3 = st.columns(3)
with col1:
    if st.button('🎊 ฉลอง'): st.balloons()
with col2:
    if st.button('❄️ หิมะ'): st.snow()
with col3:
    if st.button('🔔 ทักทาย'): st.toast('สวัสดีครับ!')

# ✨ 5. ตัวหนังสือวิ่งปิดท้าย (สีเขียว)
st.markdown("<marquee style='color: #050505; font-family: Courier; font-size: 20px; background: #000; padding: 10px; border-radius: 10px; border: 1px solid #00FF00;'>🚀 ขอบคุณที่รับชมสถานีเพลงช่างใหญ่... อยู่นิ่งๆ ไม่เจ็บตัว... 🎧 🎶</marquee>", unsafe_allow_html=True)

line_link = "https://line.me/ti/p/e-8n-__If_" 
st.link_button("🟢 แตะเพื่อแชทกับเรา (LINE)", line_link, use_container_width=True)

st.sidebar.write('**สโลแกน:** "อยู่นิ่งๆ ไม่เจ็บตัว"')
st.caption("© 2026 สถานีเพลงฟังสบายใจ | อยู่นิ่งๆ ไม่เจ็บตัว")

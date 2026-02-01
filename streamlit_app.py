import streamlit as st
import google.generativeai as genai
import streamlit.components.v1 as components

# --- [ 1. เชื่อมต่อ AI ] ---
try:
    my_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=my_key)
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
except:
    st.error("⚠️ ยังไม่ได้ใส่กุญแจลับ (API Key) ในระบบ Secrets")

def ask_ai_for_friend(user_message):
    prompt = f"คุณคือดีเจเพื่อนคู่คิด สโลแกนคือ 'อยู่นิ่งๆ ไม่เจ็บตัว' เพื่อนระบายว่า: '{user_message}' ตอบแบบนิ่งๆ ให้กำลังใจดีๆ"
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        if "429" in str(e):
            return "วันนี้เราคุยกันเยอะแล้วนะเพื่อน... พักผ่อนบ้างนะ เดี๋ยวพรุ่งนี้มาคุยกันใหม่"
        return f"เรารับฟังอยู่นะ... (ติดปัญหา: {e})"

# --- [ 2. ตั้งค่าหน้าสถานี ] ---
st.set_page_config(page_title="สถานีอยู่นิ่งๆ ไม่เจ็บตัว", page_icon="📻", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: #FFFFFF; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# 🌍 โลโก้
try:
    st.image("globe.jpg", width=250)
except:
    st.header("🌍")

st.markdown("<h2 style='color: #FFD700;'>📻 STATION: อยู่นิ่งๆ ไม่เจ็บตัว ไอ้บอล พร้อมครอบครัว</h2>", unsafe_allow_html=True)

# ✨ ตัวหนังสือวิ่งบนสุด
st.markdown("""<marquee style="color: white; font-weight: bold; background: #050505; padding: 12px; border-radius: 10px; border: 1px solid #FFD700;">📢 ยินดีต้อนรับเข้าสู่สถานี อยู่นิ่งๆ ไม่เจ็บตัว ...ทักแชทระบายเรื่องราวชีวิตได้เลยครับ ✨</marquee>""", unsafe_allow_html=True)

# --- [ 3. YouTube 3 จุด ] ---
st.write("---")
# 1. Playlist
playlist_url = "https://www.youtube.com/embed/videoseries?list=PL6S211I3urvpt47sv8mhbexif2YOzs2gO"
st.markdown(f'<iframe width="100%" height="400" src="{playlist_url}" frameborder="0" allowfullscreen style="border-radius:15px; border: 2px solid #333;"></iframe>', unsafe_allow_html=True)

st.markdown("<marquee style='background: #FFD700; color: black; padding: 8px; font-weight: bold; border-radius: 5px; margin-top: 10px;'>🔴 กำลังรับฟังผลงานเพลงจากช่อง S.S.S Music 🔴</marquee>", unsafe_allow_html=True)

st.write("---")
# 2. วิดีโอเพลง
st.video("https://youtu.be/cbcuYnyr828?si=gCdCngKZztQVVZCe")

st.markdown("<marquee style='background: #FF0000; color: white; padding: 8px; font-weight: bold; border-radius: 5px; margin-bottom: 10px;'>📺 ยินดีต้อนรับสู่ช่อง อยู่นิ้งๆไม่เจ็บตัว 🎬</marquee>", unsafe_allow_html=True)

# 3. วิดีโอช่อง
st.video("https://youtu.be/Bb3Jtsik3nY?si=Qyz3WtZLcxML3uF_")

# --- [ 4. ปุ่มแชร์ & อัปโหลด ] ---
st.write("---")
share_url = "https://41g5.streamlit.app"
facebook_share = f"https://www.facebook.com/sharer/sharer.php?u={share_url}"
st.link_button("🔵 แชร์สถานีไปยัง Facebook", facebook_share, use_container_width=True)

st.write("---")
st.markdown("<marquee style='background: #0000FF; color: white; padding: 8px; font-weight: bold; border-radius: 5px;'>📸 พื้นที่อัปโหลดรูปภาพและวิดีโอส่วนตัว 📸</marquee>", unsafe_allow_html=True)

st.subheader("📸 อัปโหลดส่วนตัว")
c1, c2 = st.columns(2)
with c1:
    up_img = st.file_uploader("อัปโหลดรูป", type=["jpg", "png"], key="up_img_unique")
    if up_img: st.image(up_img)
with c2:
    up_vid = st.file_uploader("อัปโหลดวิดีโอ", type=["mp4"], key="up_vid_unique")
    if up_vid: st.video(up_vid)

# --- [ 5. พื้นที่แชท AI (เพื่อนคู่คิด) ] ---
st.write("---")
st.subheader("💬 คุยกับ AI (เพื่อนคู่คิด)")
user_input_ai = st.text_area("อยากระบายอะไรไหมเพื่อน?", placeholder="พิมพ์เรื่องที่เจอมาได้เลย...", key="ai_chat_input")

if st.button("ส่งความรู้สึกให้ AI", key="btn_ai_chat"): # เติม KEY ป้องกันซ้ำ
    if user_input_ai:
        with st.spinner('กำลังฟังอย่างตั้งใจ...'):
            reply = ask_ai_for_friend(user_input_ai)
            st.chat_message("assistant").write(reply)
            st.balloons()
    else:
        st.info("บอกอะไรเราหน่อยสิ")

# --- [ 6. กระดานข้อความ (แบบเก็บประวัติ) ] ---
st.write("---")
st.subheader("📌 กระดานระบายใจ (ฝากข้อความ)")
user_msg_board = st.text_area("ฝากข้อความไว้ที่นี่...", key="board_input")

if st.button("ฝากข้อความ", key="btn_board_submit"): # เติม KEY ป้องกันซ้ำ
    if user_msg_board:
        if 'msg_list' not in st.session_state:
            st.session_state.msg_list = []
        st.session_state.msg_list.append(user_msg_board)
        st.success("ช่างใหญ่รับทราบ!")
        st.snow()

if 'msg_list' in st.session_state:
    for m in st.session_state.msg_list[::-1]:
        st.info(m)

# --- [ 7. ลูกเล่นปิดท้าย ] ---
st.write("---")
col1, col2, col3 = st.columns(3)
with col1:
    if st.button('🎊 ฉลอง', key="fun_1"): st.balloons()
with col2:
    if st.button('❄️ หิมะ', key="fun_2"): st.snow()
with col3:
    if st.button('🔔 ทักทาย', key="fun_3"): st.toast('สวัสดีครับ!')

st.markdown("<marquee style='color: #00FF00; font-family: Courier; font-size: 20px; background: #000; padding: 10px; border-radius: 10px; border: 1px solid #00FF00;'>🚀 ขอบคุณที่รับชมสถานีเพลงช่างใหญ่... อยู่นิ่งๆ ไม่เจ็บตัว... 🎧 🎶</marquee>", unsafe_allow_html=True)

st.link_button("🟢 แตะเพื่อแชทกับเรา (LINE)", "https://line.me/ti/p/e-8n-__If_", use_container_width=True)
st.caption("© 2026 สถานีเพลงฟังสบายใจ | อยู่นิ่งๆ ไม่เจ็บตัว")

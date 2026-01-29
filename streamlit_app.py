import streamlit as st
import streamlit.components.v1 as components

# 1. ตั้งค่าหน้าสถานี
st.set_page_config(page_title="สถานีอยู่นิ่งๆ ไม่เจ็บตัว", page_icon="📻", layout="centered")

# 2. แต่ง UI สีมืด-ทอง และปุ่ม LINE สีเขียว
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

# 3. ส่วนหัวและโลโก้
try:
    st.image("globe.jpg", width=250)
except:
    st.header("🌍")

st.markdown("<h2 style='color: #FFD700;'>📻 STATION: อยู่นิ่งๆ ไม่เจ็บตัว</h2>", unsafe_allow_html=True)

# 4. ตัวหนังสือวิ่งแจ้งข่าวสาร
st.markdown("""
    <marquee style="color: white; font-weight: bold; background: #050505; padding: 12px; border-radius: 10px; border: 1px solid #FFD700;">
        📢 ยินดีต้อนรับเข้าสู่สถานี อยู่นิ่งๆ ไม่เจ็บตัว ...ทักแชทมาบอกเรื่องราวชีวิตได้เลย เดวจัดเพลงให้ฟังครับ! 🎵 🎧 ขอบคุณที่ติดตามรับฟังครับ ✨
    </marquee>
    """, unsafe_allow_html=True)

st.write("---")

# 5. YouTube Playlist (ใช้ลิงก์ที่คุณส่งมาล่าสุด)
st.subheader("📺 รายการเพลงแนะนำ (กดฟังต่อเนื่อง)")
# ดึงเฉพาะ ID ของ Playlist มาใช้งาน
playlist_id = "PL6S211I3urvpt47sv8mhbexif2YOzs2gO"
embed_url = f"https://www.youtube.com/embed/videoseries?list={playlist_id}"
# --- [ 1. เส้นคั่นแยกส่วน ] ---
st.divider()
import streamlit as st

# --- ส่วนหัวของแอป ---
st.title("S.S.S Music Player")
st.write("ฟังเพลงจาก YouTube ของผม และแชร์รูป/วิดีโอของคุณได้ที่นี่!")

# --- 1. ส่วนเล่นเพลงจาก YouTube ของคุณ ---
# คุณสามารถเปลี่ยน URL เป็นเพลย์ลิสต์ของคุณได้เลย
url = "https://www.youtube.com/watch?v=YOUR_VIDEO_ID" 
st.video(url)

st.markdown("---")

# --- 2. ออฟชั่นเพิ่มรูปภาพ (Upload Image) ---
st.subheader("📸 เพิ่มรูปภาพของคุณ")
uploaded_image = st.file_uploader("เลือกไฟล์รูปภาพ...", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    # แสดงรูปที่อัปโหลด
    st.image(uploaded_image, caption='รูปภาพของคุณ', use_column_width=True)
    st.success("โหลดรูปภาพสำเร็จ!")

st.markdown("---")

# --- 3. ออฟชั่นเพิ่มวิดีโอ (Upload Video) ---
st.subheader("🎥 เพิ่มวิดีโอของคุณ")
uploaded_video = st.file_uploader("เลือกไฟล์วิดีโอ...", type=["mp4", "mov", "avi"])

if uploaded_video is not None:
    # แสดงวิดีโอที่อัปโหลด
    st.video(uploaded_video)
    st.success("โหลดวิดีโอสำเร็จ!")

# --- สโลแกนประจำตัว ---
st.sidebar.markdown("---")
st.sidebar.write('**สโลแกน:** "อยู่นิ่งๆ ไม่เจ็บตัว"')

# --- [ 2. ออฟชัน: ปุ่มแชร์สถานี ] ---
st.subheader("📢 แชร์สถานีนี้ให้เพื่อน")
st.link_button("🔵 แชร์ไปยัง Facebook", "https://www.facebook.com/sharer/sharer.php?u=URL_แอปของคุณ")

# --- [ 3. ออฟชัน: แบบสำรวจแนวเพลง ] ---
st.write("") # เว้นบรรทัดนิดหน่อย
genre = st.radio("🎸 รอบหน้าอยากฟังแนวไหนเป็นพิเศษ?", ["ลูกทุ่งอินดี้", "สตริงเก่า", "เพื่อชีวิต"], horizontal=True)
if st.button("บันทึกโหวต"):
    st.toast(f"รับทราบครับ! เดี๋ยวจัดแนว {genre} ให้")

# --- [ 4. ออฟชัน: กล่องรับข้อความทิ้งไว้ ] ---
st.write("")
user_note = st.text_area("📝 ฝากข้อความถึงดีเจ (พิมพ์ทิ้งไว้ได้เลย):", placeholder="เช่น... วันนี้เพลงเพราะมากครับ")
if user_note:
    st.info(f"ข้อความของคุณ: '{user_note}' ถูกบันทึกแล้ว (ในใจดีเจ)")

# --- [ 5. ปุ่ม LINE ของคุณ (วางไว้ล่างสุดเสมอ) ] ---
st.write("---")
line_link = "https://line.me/ti/p/e-8n-__If_" 
st.link_button("🟢 แตะเพื่อแชทกับเรา (LINE)", line_link)

st.markdown(f"""
    <iframe width="100%" height="450" src="{embed_url}" 
    title="YouTube Playlist" frameborder="0" 
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
    allowfullscreen style="border-radius:15px; border: 2px solid #333;"></iframe>
    """, unsafe_allow_html=True)

# 6. ปุ่ม LINE แชทสด (ใช้ลิงก์ QR Code ที่ถูกต้อง)
st.write("---")
st.subheader("💬 คุยกับเรา / ขอเพลงผ่าน LINE")
line_link = "https://line.me/ti/p/e-8n-__If_" 

st.link_button("🟢 แตะเพื่อเพิ่มเพื่อนและส่งแชทคุยกับเรา", line_link)

# 7. ปิดท้าย
st.write("")
st.caption("© 2026 สถานีเพลงฟังสบายใจ | อยู่นิ่งๆ ไม่เจ็บตัว")

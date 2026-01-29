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
# --- ตัวหนังสือวิ่งคั่นส่วน YouTube ---
st.markdown("""
    <style>
    .marquee-yt {
        width: 100%;
        background-color: #FFD700; /* สีทอง */
        color: black; /* ตัวหนังสือสีดำจะอ่านง่ายบนพื้นสีทอง */
        padding: 8px;
        font-weight: bold;
        border-radius: 5px;
        font-size: 18px;
    }
    </style>
    <marquee class="marquee-yt" scrollamount="6">🔴 กำลังรับฟังผลงานเพลงจากช่อง S.S.S Music - ขอให้มีความสุขกับการรับฟังครับ 🔴</marquee>
""", unsafe_allow_html=True)

# (ตามด้วยโค้ด st.video(url) ของคุณ...)

# --- 1. ส่วนเล่นเพลงจาก YouTube ของคุณ ---
# คุณสามารถเปลี่ยน URL เป็นเพลย์ลิสต์ของคุณได้เลย
url = "https://youtube.com/channel/UC1R7q05iNCx2COiWNGYE1Iw?si=mIfX5u_CYzPbx1Uo" 
st.video(url)
# --- จอที่ 3: แนะนำช่องช่างใหญ่ + ปุ่มติดตาม ---
st.write("---")
st.markdown("<h2 style='color: #FF0000;'>📺 ยินดีต้อนรับสู่ช่อง อยู่นิ้งๆไม่เจ็บตัว</h2>", unsafe_allow_html=True)

# 1. จอวิดีโอตัวอย่างของช่อง (แนะนำเอาคลิปที่ยาวที่สุดหรือเด่นที่สุดมาใส่ครับ)
channel_trailer_url = "https://www.youtube.com/watch?v=ไอดีคลิปในช่องอยู่นิ้งๆไม่เจ็บตัว"
st.video(channel_trailer_url)

# 2. ปุ่มติดตามแบบพรีเมียม (UI รกๆ แต่สวย)
st.write("📢 **กดปุ่มด้านล่างเพื่อติดตามความมันส์!**")

col_sub1, col_sub2 = st.columns([1, 1])

with col_sub1:
    # ปุ่มไปหน้าวิดีโอทั้งหมด
    st.link_button("📂 ดูวิดีโอทั้งหมดในช่อง", "https://www.youtube.com/channel/UC6S211I3urvpt47sv8mhbexif2YOzs2gO/videos", use_container_width=True)

with col_sub2:
    # ปุ่มกด Subscribe โดยตรง (ถ้าเพื่อนกดปุ่มนี้ มันจะเด้งไปหน้ายืนยันการติดตาม)
    sub_url = "https://www.youtube.com/channel/UC6S211I3urvpt47sv8mhbexif2YOzs2gO?sub_confirmation=1"
    st.link_button("🔴 กดติดตาม (SUBSCRIBE)", sub_url, use_container_width=True)

# 3. ใส่ตัวเลขสมมติเพิ่มความขลัง
st.markdown("<p style='text-align: center; color: gray;'>ยอดการรับชมรวม: 41,472 ครั้ง (📀📲)</p>", unsafe_allow_html=True)

st.markdown("---")
# --- ตัวหนังสือวิ่งคั่นส่วนรูปภาพ ---
st.markdown("""
    <style>
    .marquee {
        width: 100%;
        background-color: #FF0000; /* สีพื้นหลัง (สีแดง) */
        color: white; /* สีตัวอักษร */
        padding: 5px;
        font-weight: bold;
        border-radius: 5px;
    }
    </style>
    <marquee class="marquee">📸 ยินดีต้อนรับเข้าสู่ส่วนอัปโหลดรูปภาพส่วนตัว - ลองวางรูปสวยๆ ของคุณได้ที่นี่ 📸</marquee>
""", unsafe_allow_html=True)
# --- เริ่มส่วนปุ่มลูกเล่นข้างล่าง YouTube ---
st.write("---")
st.subheader("🕹️ แผงควบคุมสถานี (กดเล่นได้ครับ)")

# 1. แถวปุ่มกดแล้วมีเอฟเฟกต์
col_btn1, col_btn2, col_btn3 = st.columns(3)
with col_btn1:
    if st.button('🎊 ฉลอง!'):
        st.balloons()
with col_btn2:
    if st.button('❄️ หิมะตก'):
        st.snow()
with col_btn3:
    if st.button('🔔 ทักทาย'):
        st.toast('อยู่นิ้งๆไม่เจ็บตัว ยินดีต้อนรับครับ!', icon='🙏')

# 2. แถวสถิติแบบเท่ๆ (รกๆ แบบดูดี)
st.write("---")
col_stat1, col_stat2, col_stat3 = st.columns(3)
col_stat1.metric("คนฟังขณะนี้", "1,250", "+52")
col_stat2.metric("ความชัด", "4K", "Ultra")
col_stat3.metric("สถานะ", "Online", "🟢")

# 3. ปุ่ม LINE แบบใหญ่เบิ้ม
st.write("---")
st.subheader("💬 ติดต่ออยู่นิ้งๆไม่เจ็บตัว")
line_id = "ta0970801941" 
st.link_button("🟢 กดแอดไลน์มาคุยกันได้เลย (ขอเพลงได้นะ)", f"https://line.me/ti/p/~{line_id}", use_container_width=True)

# 4. ข้อความวิ่งปิดท้ายแบบ Retro
st.markdown("""
    <marquee style='color: #00FF00; font-family: Courier; font-size: 20px;'> 
    ขอบคุณที่รับชมสถานีเพลงช่างใหญ่... อยู่นิ่งๆ ไม่เจ็บตัว... เพลงดี ดนตรีเพราะ... 🚀 🎧 🎶
    </marquee>
    """, unsafe_allow_html=True)
# --- จบส่วนปุ่มลูกเล่น ---

# (ตามด้วยโค้ดอัปโหลดรูปของคุณ...)

# --- 2. ออฟชั่นเพิ่มรูปภาพ (Upload Image) ---
st.subheader("📸 เพิ่มรูปภาพของคุณ")
uploaded_image = st.file_uploader("เลือกไฟล์รูปภาพ...", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    # แสดงรูปที่อัปโหลด
    st.image(uploaded_image, caption='รูปภาพของคุณ', use_column_width=True)
    st.success("โหลดรูปภาพสำเร็จ!")

st.markdown("---")
# --- ตัวหนังสือวิ่งคั่นส่วนวิดีโอ ---
st.markdown("""
    <style>
    .marquee-video {
        width: 100%;
        background-color: #0000FF; /* เปลี่ยนเป็นสีน้ำเงิน */
        color: white;
        padding: 5px;
        font-weight: bold;
        border-radius: 5px;
    }
    </style>
    <marquee class="marquee-video" scrollamount="7">🎬 ส่วนอัปโหลดวิดีโอส่วนตัว - ทดสอบไฟล์วิดีโอของคุณได้ที่นี่ 🎬</marquee>
""", unsafe_allow_html=True)

# (ตามด้วยโค้ดอัปโหลดวิดีโอของคุณ...)

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
# --- ตัวหนังสือวิ่งคั่นส่วน YouTube ---
st.markdown("""
    <style>
    .marquee-yt {
        width: 100%;
        background-color: #FFD700; /* สีทอง */
        color: black; /* ตัวหนังสือสีดำจะอ่านง่ายบนพื้นสีทอง */
        padding: 8px;
        font-weight: bold;
        border-radius: 5px;
        font-size: 18px;
    }
    </style>
    <marquee class="marquee-yt" scrollamount="6">🔴 กำลังรับฟังผลงานเพลงจากช่อง อยู่นิ้งๆไม่เจ็บตัว - ขอให้มีความสุขกับการรับฟังครับ 🔴</marquee>
""", unsafe_allow_html=True)

# (ตามด้วยโค้ด st.video(url) ของคุณ...)

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

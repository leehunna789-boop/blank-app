import pyaudio
import numpy as np
import audioop
import math
import tkinter as tk
from tkinter import ttk
# นำเข้าไลบรารี Image และ ImageTk จาก Pillow
from PIL import Image, ImageTk

# --- ตั้งค่าเสียง ---
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
audio = pyaudio.PyAudio()
stream = None
running = False
# ----------------------

def start_audio_stream():
    global stream, running
    if running: return
    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    running = True
    status_label.config(text="สถานะ: กำลังวัดเสียง...", foreground="green")
    start_button.config(state=tk.DISABLED)
    update_meter()

def update_meter():
    if not running: return
    try:
        data = stream.read(CHUNK, exceptionOnOverflow=False)
        rms = audioop.rms(data, 2)
        if rms == 0: db = 0
        else: db = 20 * math.log10(rms / 1.0)
        if db > 120: db = 120 

        db_label.config(text=f"{db:.1f}")
        if db > 80: db_label.config(foreground="red")
        elif db > 60: db_label.config(foreground="orange")
        else: db_label.config(foreground="green")

        root.after(50, update_meter)
    except IOError:
        root.after(50, update_meter)
    except Exception as e:
        status_label.config(text=f"ข้อผิดพลาด: {e}", foreground="red")

# --- ตั้งค่า Tkinter GUI ---
root = tk.Tk()
app_name = "SOUND MASTER PRO BY [ใส่ชื่อของคุณที่นี่]"
root.title(app_name)
root.geometry("400x400")
root.resizable(False, False)

style = ttk.Style()
style.configure("TButton", padding=6, font=('Arial', 12))

# >>> ส่วนการใส่โลโก้ JPG <<<
try:
    # โหลดไฟล์ JPG ด้วย Pillow
    img = Image.open("logo.jpg") 
    # ปรับขนาดรูปภาพตามต้องการ (ย่อเหลือครึ่งนึง)
    img = img.resize((100, 100), Image.Resampling.LANCZOS)
    # แปลงรูปภาพให้เป็นรูปแบบที่ Tkinter เข้าใจ
    logo_image = ImageTk.PhotoImage(img) 
    logo_label = tk.Label(root, image=logo_image)
    logo_label.image = logo_image # จำเป็นเพื่อป้องกัน GC ลบรูปทิ้ง
    logo_label.pack(pady=10)
except Exception as e:
    print(f"ไม่พบไฟล์ logo.jpg หรือไฟล์เสียหาย: {e}")

# Label แสดงค่า dB
db_label = tk.Label(root, text="0.0", font=("Arial", 80, "bold"), foreground="green")
db_label.pack(pady=10)

# Label หน่วยวัด
unit_label = tk.Label(root, text="dB", font=("Arial", 20))
unit_label.pack()

# ปุ่มเริ่มการวัด
start_button = ttk.Button(root, text="เริ่มวัดเสียง", command=start_audio_stream)
start_button.pack(pady=20)

# สถานะ
status_label = tk.Label(root, text="สถานะ: รอเริ่ม", font=("Arial", 10), foreground="gray")
status_label.pack(pady=10)

# เริ่ม Main Loop ของ GUI
root.mainloop()

# --- ปิด Stream เมื่อโปรแกรมปิด ---
if stream:
    stream.stop_stream()
    stream.close()
audio.terminate()

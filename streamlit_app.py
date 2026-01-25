import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Industrial Sound Meter", layout="wide")

# ซ่อน UI Streamlit
st.markdown("""
    <style>
    #MainMenu, footer, header, .stDeployButton, #stDecoration, [data-testid="stStatusWidget"] {visibility: hidden; display:none !important;}
    body { background-color: #000; }
    </style>
""", unsafe_allow_html=True)

html_code = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { background: #000; color: white; font-family: 'Courier New', monospace; display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh; margin: 0; }
        .meter-card { border: 5px solid #333; padding: 40px; border-radius: 30px; text-align: center; width: 350px; background: #111; }
        .db-val { font-size: 6rem; font-weight: bold; color: #00ff88; margin: 10px 0; }
        .peak-val { color: #ffcc00; font-size: 1.2rem; margin-bottom: 20px; }
        .btn-start { background: #00ff88; color: #000; border: none; padding: 15px 30px; border-radius: 10px; font-weight: bold; cursor: pointer; font-size: 1.2rem; }
        .warning { color: #ff3300; font-weight: bold; font-size: 1.5rem; display: none; margin-top: 15px; }
    </style>
</head>
<body>
    <div class="meter-card">
        <div style="color: #ff3300"; letter-spacing: 3px;">LIVE SOUND LEVEL.อยู่นิ้งไม่เจ็บตัว</div>
        <div id="dbDisplay" class="db-val">0.0</div>
        <div id="peakDisplay" class="peak-val">MAX PEAK: 0.0 dB</div>
        <button id="startBtn" class="btn-start">เริ่มวัดเสียง (Start)</button>
        <div id="warnMsg" class="warning">⚠️ ตามรัฐบาลกำหนด!</div>
    </div>

    <script>
        let audioCtx, analyser, microphone, dataArray;
        let maxDb = 0;
        const dbDisplay = document.getElementById('dbDisplay');
        const peakDisplay = document.getElementById('peakDisplay');
        const warnMsg = document.getElementById('warnMsg');
        const startBtn = document.getElementById('startBtn');

        startBtn.onclick = async () => {
            if (audioCtx) return;
            
            try {
                const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
                audioCtx = new (window.AudioContext || window.webkitAudioContext)();
                analyser = audioCtx.createAnalyser();
                analyser.fftSize = 512;
                microphone = audioCtx.createMediaStreamSource(stream);
                microphone.connect(analyser);
                dataArray = new Uint8Array(analyser.frequencyBinCount);
                
                startBtn.style.display = 'none';
                update();
            } catch (err) {
                alert("กรุณากดอนุญาตให้ใช้ไมโครโฟนด้วยนะครับลูกพี่!");
            }
        };

        function update() {
            requestAnimationFrame(update);
            analyser.getByteFrequencyData(dataArray);
            
            let sum = 0;
            for(let i = 0; i < dataArray.length; i++) { sum += dataArray[i]; }
            let avg = sum / dataArray.length;
            
            // สูตรคำนวณ dB แบบประมาณการสำหรับไมค์มือถือ
            let db = (avg / 255) * 110; 
            db = Math.max(0, db + 20); // Offset เพื่อให้ใกล้เคียงค่าจริงมากขึ้น
            
            dbDisplay.innerText = db.toFixed(1);

            if (db > maxDb) {
                maxDb = db;
                peakDisplay.innerText = "MAX PEAK: " + maxDb.toFixed(1) + " dB";
            }

            // ถ้าเกิน 90dB (เสียงเครื่องตัดเหล็กมักจะอยู่แถวนี้) ให้เตือน
            if (db > 90) {
                dbDisplay.style.color = "#ff3300";
                warnMsg.style.display = 'block';
            } else {
                dbDisplay.style.color = "#00ff88";
                warnMsg.style.display = 'none';
            }
        }
    </script>
</body>
</html>
"""

components.html(html_code, height=600)

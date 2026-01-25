import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Pro Audio Meter & Player", layout="wide")

# ซ่อน UI Streamlit
st.markdown("""
    <style>
    #MainMenu, footer, header, .stDeployButton, #stDecoration, [data-testid="stStatusWidget"] {visibility: hidden; display:none !important;}
    body { background-color: #050505; }
    </style>
""", unsafe_allow_html=True)

html_code = """
<!DOCTYPE html>
<html>
<head>
    <style>
        :root { --neon: #00ff88; --bg: #111; }
        body { background: #050505; color: white; font-family: sans-serif; display: flex; justify-content: center; padding: 20px; }
        .main-box {
            background: var(--bg); border: 8px solid var(--neon); border-radius: 40px;
            padding: 30px; width: 350px; text-align: center; box-shadow: 0 0 30px rgba(0,255,136,0.2);
        }
        .db-display { font-size: 5rem; font-weight: bold; color: var(--neon); margin: 10px 0; font-family: monospace; }
        .peak-label { color: #ffcc00; font-size: 1rem; margin-bottom: 20px; }
        .player-controls { border-top: 1px solid #333; margin-top: 20px; padding-top: 20px; }
        .btn-main { background: var(--neon); border: none; width: 60px; height: 60px; border-radius: 50%; font-size: 1.5rem; cursor: pointer; }
        .file-label { display: block; margin-top: 20px; color: var(--neon); border: 1px dashed var(--neon); padding: 10px; cursor: pointer; border-radius: 10px; }
    </style>
</head>
<body>
    <div class="main-box">
        <div style="font-size: 0.8rem; letter-spacing: 2px;">LIVE DECIBEL (dB)</div>
        <div id="dbDisplay" class="db-display">0.0</div>
        <div id="peakDisplay" class="peak-label">MAX PEAK: 0.0 dB</div>
        
        <button id="micBtn" style="padding: 10px; border-radius: 10px; cursor: pointer; background: #333; color: white; border: none;">
            🎤 เปิดไมค์วัดเสียงเครื่องตัดเหล็ก
        </button>

        <div class="player-controls">
            <div id="trackName" style="font-size: 0.8rem; color: #888; margin-bottom: 10px;">หยุดเล่นเพลง</div>
            <button onclick="document.getElementById('audio').play()" class="btn-main">▶</button>
            <button onclick="document.getElementById('audio').pause()" class="btn-main" style="background:#444; color:white;">⏸</button>
            
            <label class="file-label">
                <input type="file" id="files" accept="audio/*" style="display:none;">
                [ + ใส่เพลงฟังชิลๆ ]
            </label>
        </div>
    </div>

    <audio id="audio" crossorigin="anonymous"></audio>

    <script>
        const audio = document.getElementById('audio');
        const dbDisplay = document.getElementById('dbDisplay');
        const peakDisplay = document.getElementById('peakDisplay');
        const micBtn = document.getElementById('micBtn');
        
        let audioCtx, analyser, dataArray, maxDb = 0;

        async function initAudio() {
            if (audioCtx) return;
            audioCtx = new (window.AudioContext || window.webkitAudioContext)();
            analyser = audioCtx.createAnalyser();
            analyser.fftSize = 256;
            dataArray = new Uint8Array(analyser.frequencyBinCount);
            
            // เชื่อมต่อไมโครโฟน
            try {
                const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
                const micSource = audioCtx.createMediaStreamSource(stream);
                micSource.connect(analyser);
                micBtn.style.background = "#00ff88";
                micBtn.style.color = "#000";
                micBtn.innerText = "🎤 ไมค์กำลังทำงาน...";
                update();
            } catch (err) {
                alert("กรุณากดอนุญาตไมค์เพื่อวัดเสียงเครื่องตัดเหล็กนะครับ");
            }

            // เชื่อมต่อเครื่องเล่นเพลง (อยู่นิ้งๆไม่เจ็บตัว)
            const songSource = audioCtx.createMediaElementSource(audio);
            songSource.connect(analyser);
            analyser.connect(audioCtx.destination);
        }

        micBtn.onclick = initAudio;

        document.getElementById('files').onchange = (e) => {
            initAudio();
            const file = e.target.files[0];
            audio.src = URL.createObjectURL(file);
            document.getElementById('trackName').innerText = file.name;
        };

        function update() {
            requestAnimationFrame(update);
            analyser.getByteFrequencyData(dataArray);
            let sum = 0;
            for(let i=0; i<dataArray.length; i++) sum += dataArray[i];
            let avg = sum / dataArray.length;
            
            let db = (avg / 255) * 110;
            db = Math.max(0, db + 20); 
            
            dbDisplay.innerText = db.toFixed(1);
            if (db > maxDb) {
                maxDb = db;
                peakDisplay.innerText = "MAX PEAK: " + maxDb.toFixed(1) + " dB";
            }
        }
    </script>
</body>
</html>
"""

components.html(html_code, height=750)

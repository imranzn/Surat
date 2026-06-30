import streamlit as st
import time

st.set_page_config(
    page_title="Surat Ulang Tahun Untuk Ibu 🎀",
    page_icon="🎀",
    layout="centered"
)

# ===================== EDIT BAGIAN INI =====================
NAMA_IBU = "Rahmatang"      # Ganti dengan nama ibu kamu
UMUR = ""                       # Opsional, contoh: "ke-50" (kosongkan jika tidak perlu)
ISI_SURAT = """
Selamat ulang tahun, Mama tersayang 🎀

Tidak terasa waktu berjalan begitu cepat, dan hari ini adalah hari yang spesial untuk Mama. Aku ingin meluangkan waktu sejenak untuk bilang betapa bersyukurnya aku punya Mama sehebat ini.

Terima kasih atas semua cinta, doa, dan pengorbanan yang Mama berikan tanpa pernah mengeluh. Setiap hal kecil yang Mama lakukan untuk keluarga, mulai dari bangun lebih pagi, memastikan semua baik-baik saja, sampai selalu ada di saat dibutuhkan, adalah bukti betapa besarnya kasih sayang Mama.

Mama adalah sosok yang selalu kuat menghadapi apapun, sabar menghadapi semua tingkah kami, dan selalu punya cara untuk membuat rumah terasa hangat meskipun hari sedang sulit. Senyum Mama selalu jadi alasan untuk tetap semangat menjalani hari.

Di hari spesial ini, aku cuma ingin bilang: terima kasih sudah menjadi Mama terbaik yang pernah ada. Semoga Mama selalu sehat, panjang umur, diberi kelancaran rezeki, dan selalu dikelilingi kebahagiaan, aamiin.

Aku sayang Mama, lebih dari yang bisa diungkapkan kata-kata. Selamat ulang tahun, Ma 🎀💗
"""
PENUTUP = "Dengan segenap cinta, anakmu Imran ❤️"
# =============================================================

# ================= STATE =================
if "open" not in st.session_state:
    st.session_state.open = False

# ================= CSS =================
st.markdown("""
<style>

/* Hide Streamlit default */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* Background dreamy pink */
.stApp{
    background: radial-gradient(circle at top, #ffd1dc, #ffb6c1, #ff9ecd, #ffc8e4);
    background-size: 400% 400%;
    animation: bgMove 10s ease infinite;
}

@keyframes bgMove {
    0% {background-position:0% 50%;}
    50% {background-position:100% 50%;}
    100% {background-position:0% 50%;}
}

/* Floating hearts/sparkles decoration */
.floaters{
    position:fixed;
    top:0; left:0;
    width:100%;
    height:100%;
    pointer-events:none;
    overflow:hidden;
    z-index:0;
}

.floaters span{
    position:absolute;
    bottom:-50px;
    font-size:24px;
    opacity:0.6;
    animation: rise linear infinite;
}

@keyframes rise{
    0%{ transform: translateY(0) rotate(0deg); opacity:0.7;}
    100%{ transform: translateY(-110vh) rotate(360deg); opacity:0;}
}

/* Header wrapper - memastikan benar-benar center di semua ukuran layar */
.header-wrap{
    display:flex;
    flex-direction:column;
    align-items:center;
    justify-content:center;
    width:100%;
    box-sizing:border-box;
    padding:0 16px;
    text-align:center;
}

/* Title Responsive */
.title{
    width:100%;
    max-width:700px;
    text-align:center;
    font-size: clamp(24px, 5.5vw, 50px);
    font-weight:800;
    color:#7a1f4d;
    margin-top:30px;
    text-shadow: 0 6px 20px rgba(255,255,255,0.5);
    line-height:1.25;
    word-break:keep-all;
    box-sizing:border-box;
}

.subtitle{
    width:100%;
    max-width:600px;
    text-align:center;
    font-size: clamp(13px, 3vw, 18px);
    color:#8a3a64;
    margin-top:8px;
    font-weight:500;
    box-sizing:border-box;
}

@media (max-width: 480px){
    .title{
        font-size:24px;
        line-height:1.3;
        margin-top:20px;
    }
    .subtitle{
        font-size:13px;
    }
}

/* Envelope */
.envelope{
    width:300px;
    height:200px;
    margin:30px auto;
    background: rgba(255,255,255,0.4);
    backdrop-filter: blur(10px);
    border-radius:25px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:80px;
    box-shadow: 0 20px 50px rgba(122,31,77,0.25);
    transition:0.3s;
    animation: float 2s ease-in-out infinite;
}

.envelope:hover{
    transform: scale(1.05);
}

@keyframes float{
    0%{transform:translateY(0);}
    50%{transform:translateY(-10px);}
    100%{transform:translateY(0);}
}

/* Responsive HP */
@media (max-width: 768px){

    .envelope{
        width:230px;
        height:160px;
        font-size:65px;
    }

    .letter{
        padding:25px !important;
        margin:20px 10px !important;
    }

    .nama{
        font-size:26px !important;
    }

    .isi{
        font-size:16px !important;
        line-height:1.8 !important;
    }
}

/* Button */
div.stButton > button{
    width:100%;
    padding:14px;
    border-radius:15px;
    border:none;
    font-size:18px;
    font-weight:bold;
    background:white;
    color:#c2185b;
    transition:0.3s;
    box-shadow: 0 8px 20px rgba(0,0,0,0.15);
}

div.stButton > button:hover{
    transform:scale(1.03);
    background:#fff0f5;
}

/* Letter */
.letter{
    max-width:720px;
    margin:30px auto;
    padding:40px;
    background: rgba(255,255,255,0.92);
    border-radius:25px;
    box-shadow: 0 25px 60px rgba(122,31,77,0.2);
    animation: openLetter 0.8s ease;
    backdrop-filter: blur(10px);
    border: 2px solid #ffd6e8;
}

@keyframes openLetter{
    from{
        opacity:0;
        transform:translateY(40px) scale(0.9);
    }
    to{
        opacity:1;
        transform:translateY(0) scale(1);
    }
}

.nama{
    text-align:center;
    font-size:36px;
    font-weight:800;
    color:#c2185b;
    margin-bottom:5px;
}

.umur{
    text-align:center;
    font-size:18px;
    color:#d4658f;
    margin-bottom:20px;
    font-style:italic;
}

.isi{
    font-size:18px;
    line-height:2;
    color:#3a2433;
}

.penutup{
    margin-top:30px;
    text-align:right;
    font-style:italic;
    color:#c2185b;
    font-weight:600;
}

</style>

<div class="floaters">
<span style="left:5%; animation-duration:9s;">🎀</span>
<span style="left:18%; animation-duration:12s; animation-delay:2s;">💗</span>
<span style="left:32%; animation-duration:8s; animation-delay:1s;">🌸</span>
<span style="left:48%; animation-duration:11s; animation-delay:3s;">💕</span>
<span style="left:62%; animation-duration:10s;">🎀</span>
<span style="left:75%; animation-duration:9s; animation-delay:2s;">🌷</span>
<span style="left:88%; animation-duration:13s; animation-delay:1s;">💗</span>
</div>
""", unsafe_allow_html=True)

# ================= HEADER =================
st.markdown(
    "<div class='header-wrap'>"
    f"<div class='title'>🎀 Untuk {NAMA_IBU} 🎀</div>"
    "<div class='subtitle'>Selamat ulang tahun, Ma ❤️</div>"
    "</div>",
    unsafe_allow_html=True
)

st.write("")
st.write("")

# ================= ENVELOPE =================
if not st.session_state.open:

    st.markdown(
        "<div class='envelope'>🎀</div>",
        unsafe_allow_html=True
    )

    if st.button("Buka Surat Untuk Mama 💌"):
        st.session_state.open = True
        st.balloons()
        st.rerun()

# ================= LETTER =================
else:

    placeholder = st.empty()
    displayed = ""

    for char in ISI_SURAT:
        displayed += char

        umur_html = f'<div class="umur">{UMUR}</div>' if UMUR else ''
        letter_html = (
            f'<div class="letter">'
            f'<div class="nama">🌸 Untuk {NAMA_IBU} 🌸</div>'
            f'{umur_html}'
            f'<div class="isi">{displayed.replace(chr(10), "<br>")}</div>'
            f'<div class="penutup">{PENUTUP}</div>'
            f'</div>'
        )
        placeholder.markdown(letter_html, unsafe_allow_html=True)

        time.sleep(0.01)
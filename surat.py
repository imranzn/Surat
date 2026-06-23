import streamlit as st
import time

st.set_page_config(
    page_title="Surat Untukmu 💌",
    page_icon="💌",
    layout="centered"
)

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

/* Background dreamy */
.stApp{
    background: radial-gradient(circle at top, #ff9a9e, #fad0c4, #a18cd1, #fbc2eb);
    background-size: 400% 400%;
    animation: bgMove 10s ease infinite;
}

@keyframes bgMove {
    0% {background-position:0% 50%;}
    50% {background-position:100% 50%;}
    100% {background-position:0% 50%;}
}

/* Title Responsive */
.title{
    text-align:center;
    font-size: clamp(28px, 6vw, 55px);
    font-weight:800;
    color:white;
    margin-top:30px;
    text-shadow: 0 10px 30px rgba(0,0,0,0.3);
    line-height:1.2;
    padding:0 10px;
}

/* Envelope */
.envelope{
    width:320px;
    height:220px;
    margin:auto;
    background: rgba(255,255,255,0.25);
    backdrop-filter: blur(10px);
    border-radius:25px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:90px;
    box-shadow: 0 20px 50px rgba(0,0,0,0.3);
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
        width:250px;
        height:170px;
        font-size:70px;
    }

    .letter{
        padding:25px !important;
        margin:20px 10px !important;
    }

    .nama{
        font-size:28px !important;
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
    color:#7b2cbf;
    transition:0.3s;
}

div.stButton > button:hover{
    transform:scale(1.03);
    background:#f3f3f3;
}

/* Letter */
.letter{
    max-width:720px;
    margin:30px auto;
    padding:40px;
    background: rgba(255,255,255,0.9);
    border-radius:25px;
    box-shadow: 0 25px 60px rgba(0,0,0,0.25);
    animation: openLetter 0.8s ease;
    backdrop-filter: blur(10px);
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
    font-size:38px;
    font-weight:800;
    color:#7b2cbf;
    margin-bottom:20px;
}

.isi{
    font-size:18px;
    line-height:2;
    color:#333;
}

.penutup{
    margin-top:30px;
    text-align:right;
    font-style:italic;
    color:#7b2cbf;
    font-weight:600;
}

</style>
""", unsafe_allow_html=True)

# ================= HEADER =================
st.markdown(
    "<div class='title'>💌 Kaisa Nabila Yuniar 💌</div>",
    unsafe_allow_html=True
)

st.write("")
st.write("")

# ================= ENVELOPE =================
if not st.session_state.open:

    st.markdown(
        "<div class='envelope'>💌</div>",
        unsafe_allow_html=True
    )

    if st.button("Buka Surat ✨"):
        st.session_state.open = True
        st.balloons()
        st.rerun()

# ================= LETTER =================
else:

    placeholder = st.empty()

    text = """
Halo Kai,

Thanks dah jadi temen yang menyenangkan. Selama ini aku ngelihat kamu sebagai orang yang rajin belajar, baik, dan peduli dengan orang-orang di sekitarmu.

Kamu selalu ngingetin teman ketika melakukan hal yang kurang baik. Itu karena kamu peduli dan pengen yang terbaik buat mereka.

Aku juga sering lihat kamu perhatian sama teman-teman yang lain, mulai dari nelpon teman yang ketiduran supaya masuk kelas sampai nyemangatin dan ngingetin teman yang lagi malas belajar supaya tetap semangat mengikuti pelajaran.

Semangat terus ya, dan semoga kamu bisa meraih semua impian yang kamu cita-citakan.

Aku harap kamu selalu bahagia, sehat, dan dikelilingi orang-orang baik. ✨
"""

    displayed = ""

    for char in text:
        displayed += char

        placeholder.markdown(f"""
        <div class="letter">
            <div class="nama">Untuk Kaisa 🌷</div>
            <div class="isi">{displayed.replace(chr(10), "<br>")}</div>
            <div class="penutup">Dengan penuh harapan ❤️</div>
        </div>
        """, unsafe_allow_html=True)

        time.sleep(0.01)
import streamlit as st
import time

st.set_page_config(page_title="Happy Birthday Mom", page_icon="🎂", layout="centered")

if "open" not in st.session_state:
    st.session_state.open=False

st.markdown("""
<style>
#MainMenu,header,footer{visibility:hidden;}
.stApp{
background:linear-gradient(135deg,#ffb6c1,#ffd6e7,#cdb4db);
}
.title{text-align:center;color:white;font-size:52px;font-weight:800;text-shadow:2px 2px 10px #a64d79;}
.envelope{width:300px;height:200px;margin:auto;background:rgba(255,255,255,.25);backdrop-filter:blur(10px);
border-radius:20px;display:flex;align-items:center;justify-content:center;flex-direction:column;font-size:80px;
box-shadow:0 10px 30px rgba(0,0,0,.25);animation:f 2s infinite;}
@keyframes f{50%{transform:translateY(-10px)}}
div.stButton>button{width:100%;border-radius:15px;font-size:18px;background:white;color:#b03060;font-weight:bold}
.letter{background:rgba(255,255,255,.95);padding:35px;border-radius:20px;box-shadow:0 10px 30px rgba(0,0,0,.2)}
.nama{text-align:center;font-size:34px;color:#b03060;font-weight:bold}
.isi{font-size:19px;line-height:2;color:#333}
.penutup{text-align:right;color:#b03060;font-style:italic;margin-top:25px}
</style>
""",unsafe_allow_html=True)

st.markdown("<div class='title'>🎂 Happy Birthday Mom 🎂</div>",unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:white'>Untuk wanita terhebat dalam hidupku ❤️</p>",unsafe_allow_html=True)

if not st.session_state.open:
    st.markdown("<div class='envelope'>💌<div style='font-size:20px'>Untuk Ibu</div></div>",unsafe_allow_html=True)
    if st.button("✨ Buka Surat"):
        st.session_state.open=True
        st.balloons()
        st.rerun()
else:
    text="""Untuk Ibu tercinta,

Selamat ulang tahun, Ibu. ❤️

Hari ini adalah hari yang sangat istimewa.

Terima kasih atas semua cinta, doa, perhatian, kesabaran, dan pengorbanan yang selalu Ibu berikan untukku.

Maaf jika sampai hari ini aku masih sering membuat Ibu khawatir atau belum bisa membalas semua kebaikan Ibu.

Aku ingin Ibu tahu bahwa aku sangat bersyukur memiliki seorang ibu seperti Ibu.

Semoga Allah selalu memberikan Ibu kesehatan, kebahagiaan, umur yang penuh berkah, rezeki yang melimpah, dan hati yang selalu tenang.

Semoga semua doa Ibu dikabulkan, setiap langkah Ibu dipermudah, dan setiap harinya dipenuhi kebahagiaan.

Aku akan terus berusaha menjadi anak yang bisa membuat Ibu bangga.

Terima kasih telah menjadi rumah terbaik untukku.

Aku sayang Ibu, lebih dari yang bisa diungkapkan dengan kata-kata.

Selamat ulang tahun, Ibu. 🤍"""
    ph=st.empty()
    shown=""
    for ch in text:
        shown+=ch
        ph.markdown(f"""
<div class='letter'>
<div class='nama'>🌸 Untuk Ibu Tercinta 🌸</div>
<div class='isi'>{shown.replace(chr(10),'<br>')}</div>
<div class='penutup'>Dengan cinta yang tak akan pernah habis ❤️<br>— Anakmu</div>
</div>""",unsafe_allow_html=True)
        time.sleep(0.01)

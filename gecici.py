import streamlit as st

st.set_page_config(
    page_title="Quantum Analiz — Yakında Buradayız",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────────────────────────
# GLOBAL CSS
# ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@400;500;600;700&family=Inter:wght@300;400;500;600&display=swap');

*, *::before, *::after { box-sizing: border-box; }

.stApp {
    background: #020617 !important;
    font-family: 'Inter', sans-serif;
}

/* Gereksiz Streamlit arayüz elemanlarını ve Profil Rozetini Gizleme */
section[data-testid="stSidebar"],
button[data-testid="collapsedControl"],
header[data-testid="stHeader"],
.viewerBadge_container,
.viewerBadge_link,
div[data-testid="stToolbar"] { 
    display: none !important; 
}

#MainMenu, footer { 
    visibility: hidden !important; 
}

.block-container {
    padding: 0 !important;
    max-width: 100% !important;
}

/* Tek sayfa (tam ekran) tasarımı için Hero Wrapper */
.hero-wrap {
    height: 100vh;
    display: flex; flex-direction: column;
    align-items: center; justify-content: center;
    text-align: center; padding: 20px;
    background:
        radial-gradient(ellipse 90% 55% at 50% -5%, #0369a130, transparent),
        radial-gradient(ellipse 45% 35% at 85% 65%, #38BDF810, transparent),
        #020617;
}

/* Logo Stili */
.q-logo {
    font-family: 'Rajdhani', sans-serif;
    font-size: clamp(36px, 5vw, 54px);
    font-weight: 700;
    letter-spacing: .2em; color: #38BDF8;
    text-decoration: none;
    margin-bottom: 4px;
}
.q-logo em { color: #F1F5F9; font-style: normal; }

/* Alt Başlık Stili */
.q-sub {
    font-family: 'Rajdhani', sans-serif;
    font-size: clamp(14px, 2vw, 18px);
    letter-spacing: .2em; color: #94A3B8;
    text-transform: uppercase;
    margin-bottom: 60px;
}

/* Ana Başlık (Yakında Buradayız) */
.hero-h1 {
    font-family: 'Rajdhani', sans-serif;
    font-size: clamp(48px, 8vw, 100px);
    font-weight: 700; line-height: 1.05;
    letter-spacing: .05em; color: #F1F5F9;
    margin-bottom: 40px;
}
.hero-h1 .c { color: #38BDF8; }

/* Opsiyonel İletişim Butonu */
.qbtn-outline {
    border: 1px solid #1E293B !important; color: #94A3B8 !important;
    padding: 12px 32px; border-radius: 4px;
    font-family: 'Rajdhani', sans-serif;
    font-weight: 600; letter-spacing: .15em; font-size: 13px;
    text-decoration: none !important; transition: all .2s;
}
.qbtn-outline:hover { 
    border-color: #38BDF8 !important; 
    color: #38BDF8 !important; 
    background: rgba(56, 189, 248, 0.05); 
}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────
# HTML İÇERİK (Sıfır Girinti)
# ─────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-wrap">
<div class="q-logo">QUANTUM<em> ANALİZ</em></div>
<div class="q-sub">Yapay Zeka Destekli Borsa Analiz Terminali</div>
<div class="hero-h1">
YAKINDA <span class="c">BURADAYIZ</span>
</div>
<a href="mailto:info@quantumanaliz.com" class="qbtn-outline">İLETİŞİME GEÇ</a>
</div>
""", unsafe_allow_html=True)

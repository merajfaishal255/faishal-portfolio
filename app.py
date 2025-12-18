import streamlit as st
from PIL import Image
import time

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Faishal Meraj | AI Portfolio",
    page_icon="🤖",
    layout="wide"
)

# ================= LOAD IMAGE =================
profile_img = Image.open("profile.jpg")

# ================= DARK NEON AI CSS =================
st.markdown("""
<style>
html { scroll-behavior: smooth; }

.stApp {
    background: radial-gradient(circle at top, #050014, #000000);
    color: #e6faff;
}

/* NAVBAR */
.navbar {
    position: fixed;
    top: 0;
    width: 100%;
    background: rgba(5,0,20,0.9);
    backdrop-filter: blur(12px);
    z-index: 999;
    padding: 12px 0;
}
.navbar a {
    color: #00ffe7;
    margin: 0 18px;
    font-weight: 600;
    text-decoration: none;
}
.navbar a:hover { color: #ffffff; }

/* SECTIONS */
.section { padding: 110px 0; }

/* CARDS */
.card {
    background: rgba(255,255,255,0.07);
    border-radius: 22px;
    padding: 28px;
    margin: 22px 0;
    border: 1px solid rgba(0,255,231,0.25);
}

/* SKILLS */
.skill-box {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(0,255,231,0.25);
    border-radius: 18px;
    padding: 22px;
    margin: 18px 0;
}

/* TAGS */
.tag {
    display: inline-block;
    padding: 8px 16px;
    border-radius: 20px;
    background: linear-gradient(90deg,#00ffe7,#4facfe);
    color: #000;
    margin: 6px;
    font-size: 14px;
    font-weight: 600;
}

/* BUTTON */
.neon-btn {
    padding: 14px 28px;
    border-radius: 30px;
    border: none;
    background: linear-gradient(90deg,#00ffe7,#4facfe);
    font-weight: bold;
    cursor: pointer;
}
.neon-btn:hover { transform: scale(1.06); }
</style>
""", unsafe_allow_html=True)

# ================= NAVBAR =================
st.markdown("""
<div class="navbar">
<center>
<a href="#home">Home</a>
<a href="#about">About</a>
<a href="#skills">Skills</a>
<a href="#projects">Projects</a>
<a href="#contact">Get In Touch</a>
</center>
</div>
""", unsafe_allow_html=True)

st.markdown("<br><br><br><br>", unsafe_allow_html=True)

# ================= HOME =================
st.markdown('<div id="home" class="section">', unsafe_allow_html=True)
col1, col2 = st.columns([1.2, 1])

with col1:
    st.markdown("<h1>Faishal Meraj</h1>", unsafe_allow_html=True)

    typing_placeholder = st.empty()
    text = "Aspiring Data Scientist | AI & Machine Learning Enthusiast"
    typed = ""
    for char in text:
        typed += char
        typing_placeholder.markdown(
            f"<h3 style='color:#00ffe7;'>{typed}</h3>",
            unsafe_allow_html=True
        )
        time.sleep(0.04)

    st.markdown("""
    <p>
    Transforming complex datasets into actionable insights using
    <b>Python, SQL, and Machine Learning</b>.
    </p>
    """, unsafe_allow_html=True)

    with open("Faishal_Meraj_Resume.pdf", "rb") as file:
        st.download_button(
            "📄 Download Resume",
            file,
            file_name="Faishal_Meraj_Resume.pdf",
            mime="application/pdf"
        )

    st.markdown("""
    <br>
    <a href="mailto:merajfaishal255@gmail.com">
        <button class="neon-btn">📧 Email Me</button>
    </a>
    <a href="tel:+917033855268">
        <button class="neon-btn" style="margin-left:10px;">📞 Call Me</button>
    </a>
    """, unsafe_allow_html=True)

with col2:
    st.image(profile_img, use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

# ================= ABOUT =================
st.markdown('<div id="about" class="section">', unsafe_allow_html=True)
st.markdown("## About Me")

st.markdown("""
I am a **Data Science & Data Analytics student at Dev Bhoomi Uttarakhand University**,
focused on building **ML-powered web applications, predictive models, and dashboards**.

🎯 **Career Objective:**  
To work in a data-driven environment where I can apply **Data Science, Machine Learning, and AI** skills.
""")
st.markdown('</div>', unsafe_allow_html=True)

# ================= SKILLS & TECHNOLOGIES =================
st.markdown('<div id="skills" class="section">', unsafe_allow_html=True)
st.markdown("## Skills & Technologies")

st.markdown("""
<div class="skill-box">
<h4>Programming & Databases</h4>
<span class="tag">Python</span>
<span class="tag">SQL</span>
<span class="tag">MySQL</span>
<span class="tag">Git</span>
<span class="tag">GitHub</span>
</div>

<div class="skill-box">
<h4>Data Science & Machine Learning</h4>
<span class="tag">EDA</span>
<span class="tag">Data Analysis</span>
<span class="tag">Machine Learning</span>
<span class="tag">Statistics</span>
<span class="tag">Model Evaluation</span>
</div>

<div class="skill-box">
<h4>Tools & Frameworks</h4>
<span class="tag">Streamlit</span>
<span class="tag">Power BI</span>
<span class="tag">TensorFlow</span>
<span class="tag">Keras</span>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ================= PROJECTS =================
st.markdown('<div id="projects" class="section">', unsafe_allow_html=True)
st.markdown("## Projects")

st.markdown("""
<div class="card">
<h3>Customer Churn Prediction Web App</h3>
<p>Interactive ML-based Streamlit app with dashboards and export features.</p>
<a href="https://github.com/merajfaishal255" target="_blank">🔗 GitHub</a>
</div>

<div class="card">
<h3>Breast Cancer Prediction Web App</h3>
<p>Logistic Regression model with probability visualization.</p>
<a href="https://github.com/merajfaishal255" target="_blank">🔗 GitHub</a>
</div>

<div class="card">
<h3>Mushroom Classification Dashboard</h3>
<p>Decision Tree model (~99% accuracy) with visual explanations.</p>
<a href="https://github.com/merajfaishal255" target="_blank">🔗 GitHub</a>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ================= GET IN TOUCH =================
st.markdown('<div id="contact" class="section">', unsafe_allow_html=True)
st.markdown("## Get In Touch")

st.markdown("""
<p>
I’m always open to discussing <b>internships, projects, collaborations, or learning opportunities</b>.
Feel free to reach out — I’ll respond quickly.
</p>

📧 <b>Email:</b> <a href="mailto:merajfaishal255@gmail.com">merajfaishal255@gmail.com</a><br>
📞 <b>Phone:</b> <a href="tel:+917033855268">7033855268</a><br>
📍 <b>Location:</b> Dehradun, Uttarakhand, India<br><br>

<a href="https://wa.me/917033855268?text=Hello%20Faishal,%20I%20visited%20your%20portfolio%20and%20would%20like%20to%20connect." target="_blank">
    <button class="neon-btn">💬 WhatsApp Me</button>
</a>

<a href="mailto:merajfaishal255@gmail.com">
    <button class="neon-btn" style="margin-left:10px;">📧 Email Me</button>
</a>

<a href="tel:+917033855268">
    <button class="neon-btn" style="margin-left:10px;">📞 Call Me</button>
</a>

<br><br>

🔗 <a href="https://linkedin.com/in/faishal-meraj-b4837b295" target="_blank">LinkedIn</a> |
💻 <a href="https://github.com/merajfaishal255" target="_blank">GitHub</a>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)


import streamlit as st

import streamlit as st

# Page configuration
st.set_page_config(
    page_title="My Data Portfolio",
    page_icon="📊",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main {
        background-color: #f8fafc;
    }

    .hero {
        background-color: #eaf1f8;
        padding: 35px;
        border-radius: 15px;
        margin-bottom: 25px;
    }

    .hero h1 {
        color: #17365d;
        font-size: 42px;
    }

    .hero p {
        color: #475569;
        font-size: 18px;
    }

    .project-card {
        background-color: white;
        padding: 22px;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        min-height: 150px;
    }

    .project-card h3 {
        color: #17365d;
    }

    .project-card p {
        color: #475569;
    }
</style>
""", unsafe_allow_html=True)


# Hero section
st.markdown("""
<div class="hero">
    <h1>My Data Portfolio</h1>
    <h1>Hi, I'm Tripti 👋</h1>
    <p><b>Aspiring Data Analyst | Machine Learning Enthusiast</b></p>
    <p>
        Welcome! I enjoy working with data, discovering patterns
        and building machine learning projects.
    </p>
</div>
""", unsafe_allow_html=True)


# About Me
st.header("About Me")

st.write("""
I have a background in MCA and am currently developing my skills
in Python, SQL, Data Analytics and Machine Learning through
hands-on projects.
""")

st.divider()


# Technical Skills
st.header("Technical Skills")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🐍 Programming")
    st.info("Python")
    st.info("SQL")
    st.info("Pandas")

with col2:
    st.markdown("### 🤖 Machine Learning")
    st.info("Scikit-learn")
    st.info("Regression")
    st.info("Classification")

with col3:
    st.markdown("### 📊 Data & Visualization")
    st.info("Data Analysis")
    st.info("Power BI")
    st.info("Tableau")


# Projects Section
st.header("My Projects")

col1, col2 = st.columns(2)

# LEFT COLUMN
with col1:

    # Airline Price Prediction
    st.markdown("""
    <div class="project-card">
        <h3>✈️ Airline Price Prediction</h3>
        <p>Machine Learning model to predict flight ticket prices.</p>
    </div>
    """, unsafe_allow_html=True)

    st.link_button(
        "View GitHub Code",
        "https://github.com/Triptikedia/Airline-Price-Prediction-ML"
    )

    st.link_button(
        "View Live Project",
        "https://airline-price-prediction-ml.streamlit.app/"
    )

    st.write("")

    # Medical Insurance Prediction
    st.markdown("""
    <div class="project-card">
        <h3>🏥 Medical Insurance Prediction</h3>
        <p>Machine Learning model to predict medical insurance costs.</p>
    </div>
    """, unsafe_allow_html=True)

    st.link_button(
        "View GitHub Code",
        "https://github.com/Triptikedia/medical-insurance-cost-prediction"
    )

    st.link_button(
        "View Live Project",
        "https://medical-insurance-cost-prediction-gxgvhlmzwrgb5bzkentcds.streamlit.app/"
    )
st.subheader("Tableau Dashboard")

st.write("Explore my Tableau data visualization project.")

st.link_button(
    "View Tableau Dashboard",
    "https://public.tableau.com/app/profile/tripti.kedia/vizzes")

# RIGHT COLUMN
with col2:

    # Used Car Price Prediction
    st.markdown("""
    <div class="project-card">
        <h3>🚗 Used Car Price Prediction</h3>
        <p>Machine Learning model to estimate the resale price of used cars.</p>
    </div>
    """, unsafe_allow_html=True)

    st.link_button(
        "View GitHub Code",
        "https://github.com/Triptikedia/used-car-price-prediction"
    )

    st.link_button(
        "View Live Project",
        "https://tripti-used-car-predictor-20.streamlit.app/"
    )

    st.write("")

    # Dry Bean Classification
    st.markdown("""
    <div class="project-card">
        <h3>🌱 Dry Bean Classification</h3>
        <p>Machine Learning model to classify dry beans into different varieties.</p>
    </div>
    """, unsafe_allow_html=True)

    st.link_button(
        "View GitHub Code",
        "https://github.com/Triptikedia/Beans-Multiclass"
    )

    st.link_button(
        "View Live Project",
        "https://beans-multiclass-knqy4hjnzqsckmpwpfy92x.streamlit.app/"

    )


# Education Section
st.header("Education")

st.markdown("""
<div class="project-card">
    <h3>🎓 Master of Computer Applications (MCA)</h3>
    <p>Completed in 2016</p>
    <p>Academic background in computer applications and technology.</p>
</div>
""", unsafe_allow_html=True)


# Contact Section
st.header("Contact Me : 9773431760")

st.write(
    "I am open to learning opportunities, internships, "
    "and entry-level Data Analyst roles."
)

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Email**")
    st.write("triptikedia98@gmail.com")

st.subheader("My Resume")

with open("Resume_Tripti_Kedia.pdf", "rb") as file:
    st.download_button(
        label="📄 Download My Resume",
        data=file,
        file_name="Resume_Tripti_Kedia.pdf",
        mime="application/pdf"
    )

st.divider()

st.caption("© 2026 Tripti | My Data Portfolio")

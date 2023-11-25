from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if '__file__' in locals() else Path.cwd()
css_file = current_dir / 'styles' / 'main.css'
resume_file = current_dir / 'assets' / 'CV.pdf'
profile_pic = current_dir / 'assets' / 'perfil.png'


# --- GENERAL SETTINGS ---
PAGE_TITLE = 'Digital CV | Ricardo Pontes'
PAGE_ICON = '📊'
NAME = 'Ricardo Pontes'
DESCRIPTION = '''
Analista de Inteligência de Negócios, auxiliando organizações apoiando a tomada de decisão baseada em dados.
'''
EMAIL = 'pontes.projects@gmail.com'
SOCIAL_MEDIA = {
    'Linkedin': 'https://linkedin.com',
    'GitHub': 'https://github.com',
    'YouTube': 'https://youtube.com',
    'Twitter': 'https://twitter.com',
}
PROJECTS = {
    'Comparando vendas em três lojas': 'https://youtu.be/Sb0A916d320',
    'Income and Expense Tracker - Aplicativo Web com banco de dados NoSQL': 'https://youtu.be/3egaMfE9388',
    'Conversor de aplicativo de desktop Exce12CSV com configurações de usuário e barra de menu': 'https://youtu.be/LzCfNanq_9c',
    'MyToolBelt - suplemento personalizado do MS Excel para combinar Python e Excel': 'https://pythonandvba.com/mytoolbelt/',
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)  # layout='wide'


# --- CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
with open(resume_file, 'rb') as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- SECTION ---
col1, col2 = st.columns(2, gap='small')
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label='📄 Download currículo',
        data=PDFbyte,
        file_name=resume_file.name,
        mime='application/octet-stream',
    )
    st.write('📫', EMAIL)


# --- SOCIAL LINKS ---
st.write('#')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f'[{platform}]({link})')


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('#')
st.subheader('Experience & Qualifications')
st.write(
    '''    
- ✔️ 7 Years expereince extracting actionable insights from data 
- ✔️ Strong hands on experience and knowledge in Python and Excel
- ✔️ Good understanding of statistical principles and their respective applications 
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
'''
)


# --- SKILLS ---
st.write('#')
st.subheader('Hard Skills')
st.write(
    '''
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL, VBA 
- 📊 Data Visulization: PowerBi, MS Excel, Plotly
- 📚 Modeling: Logistic regression, linear regression, decition trees
- 🗄️ Databases: Postgres, MongoDB, MySQL
'''
)


# --- WORK HISTORY ---
st.write('#')
st.subheader('Work History')
st.write('---')

# --- JOB 1
st.write('🚧', '**Senior Data Analyst | Ross Industries**')
st.write('02/202 - Present')
st.write(
    '''
- ► Used PowerBI and SQL to redefine and track KPIs surrounding marketing initiatives, and supplied recommendations to boost landing page conversion rate by 38%
- ► Led a team of 4 analysts to brainstorm potential marketing and sales improvements, and implemented A/B tests to generate 15% more client leads
- ► Redesigned data model through iterations that improved predictions by 12%
'''
)

# JOB 2
st.write('#')
st.write('🚧', '**Data Analyst | Liberty Mutual Insurance**')
st.write('01/2018 - 02/2022')
st.write(
    '''
- ► Built data models and maps to generate meaningful insights from customer data, boosting successful sales efforts by 12%
- ► Modeled targets likely to renew, and presented analysis to leadership, which led to a YoY revenue increase of $300K
- ► Compiled, studied, and inferred large amounts of data, modeling information to drive auto policy pricing
'''
)

# JOB 3
st.write('#')
st.write('🚧', '**Data Analyst | Chegg**')
st.write('04/2015 - 01/2018')
st.write(
    '''
- ► Devised KPIs using SQL across company website in collaboration with cross-functional teams to achieve a 120% jump in organic traffic
- ► Analyzed, documented, and reported user survey results to improve customer communication processes by 18%
- ► Collaborated with analyst team to oversee end-to-end process surrounding customers' return data
'''
)


# --- Projects & Accomplishments ---
st.write('#')
st.subheader('Projects & Accomplishments')
st.write('---')
for project, link in PROJECTS.items():
    st.write(f'[{project}]({link})')
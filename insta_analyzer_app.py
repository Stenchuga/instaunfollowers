import json
import streamlit as st

# Funkcije za učitavanje username-a iz uploadovanih JSON fajlova
def load_usernames_following(file):
    data = json.load(file)
    usernames = set()
    for entry in data.get("relationships_following", []):
        if 'string_list_data' in entry and entry['string_list_data']:
            username = entry['string_list_data'][0]['value'].strip().lower()
            usernames.add(username)
    return usernames

def load_usernames_followers(file):
    data = json.load(file)
    usernames = set()
    for entry in data:
        if 'string_list_data' in entry and entry['string_list_data']:
            username = entry['string_list_data'][0]['value'].strip().lower()
            usernames.add(username)
    return usernames

st.markdown("""
    <style>
    /* Instagram gradient background za celu stranicu */
    body, .stApp {
        background: linear-gradient(135deg, #feda75, #fa7e1e, #d62976, #962fbf, #4f5bd5);
        min-height: 100vh;
        margin: 0;
        padding: 0 20px 40px 20px;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: white;
    }

    /* Stil za korisničke kartice */
    .card {
        background-color: white !important;
        color: black !important;
        border-radius: 15px;
        padding: 15px 20px;
        margin-bottom: 12px;
        box-shadow: 0 4px 10px rgb(0 0 0 / 0.1);
        transition: background-color 0.3s ease;
    }
    .card:hover {
        background-color: #f0f0f0 !important;
    }

    /* Stil za naslovne okvire */
    .header-box {
        background-color: white !important;
        color: black !important;
        border-radius: 15px;
        padding: 12px 18px;
        margin-top: 20px;
        margin-bottom: 15px;
        font-weight: 700;
        font-size: 22px;
        box-shadow: 0 4px 10px rgb(0 0 0 / 0.15);
        text-align: center;
    }

    /* Stil za linkove */
    a {
        color: #4f5bd5;
        font-weight: 600;
        text-decoration: none;
    }
    a:hover {
        text-decoration: underline;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Instagram Follower Analyzer")

followers_file = st.file_uploader("Upload your followers.json file", type=['json'])
following_file = st.file_uploader("Upload your following.json file", type=['json'])

if followers_file and following_file:
    followers = load_usernames_followers(followers_file)
    following = load_usernames_following(following_file)

    not_following_you_back = following - followers  # Ti pratiš njih, a oni tebe ne prate
    you_dont_follow_back = followers - following    # Oni prate tebe, a ti njih ne pratiš

    st.markdown('<div class="header-box">Users You Follow But Don’t Follow You Back</div>', unsafe_allow_html=True)
    with st.expander(f"Show {len(not_following_you_back)} users"):
        for user in sorted(not_following_you_back):
            st.markdown(f'<div class="card"><a href="https://instagram.com/{user}" target="_blank">{user}</a></div>', unsafe_allow_html=True)

    st.markdown('<div class="header-box">Users Who Follow You But You Don’t Follow Back</div>', unsafe_allow_html=True)
    with st.expander(f"Show {len(you_dont_follow_back)} users"):
        for user in sorted(you_dont_follow_back):
            st.markdown(f'<div class="card"><a href="https://instagram.com/{user}" target="_blank">{user}</a></div>', unsafe_allow_html=True)

    st.markdown(f"""
        <div style="margin-top:30px; color:white; font-weight:600; text-align:center;">
            Total Following: {len(following)}<br>
            Total Followers: {len(followers)}
        </div>
    """, unsafe_allow_html=True)

else:
    st.info("Please upload both JSON files (followers and following) to see the analysis.")

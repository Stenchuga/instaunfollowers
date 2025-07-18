import json
import io
import zipfile
import streamlit as st
import matplotlib.pyplot as plt
# Funkcije za učitavanje username-a iz podataka JSON struktura
def load_usernames_following_from_data(data):
    usernames = set()
    for entry in data.get("relationships_following", []):
        if 'string_list_data' in entry and entry['string_list_data']:
            username = entry['string_list_data'][0]['value'].strip().lower()
            usernames.add(username)
    return usernames

def load_usernames_followers_from_data(data):
    usernames = set()
    for entry in data:
        if 'string_list_data' in entry and entry['string_list_data']:
            username = entry['string_list_data'][0]['value'].strip().lower()
            usernames.add(username)
    return usernames

# Stilovi (CSS)
st.markdown("""
    <style>
    body, .stApp {
        background: linear-gradient(135deg, #feda75, #fa7e1e, #d62976, #962fbf, #4f5bd5);
        min-height: 100vh;
        margin: 0;
        padding: 0 20px 40px 20px;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: white;
    }
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

# Pie Chart za vizualizaciju odnosa praćenja
mutual_follow = followers & following
only_following = following - followers
only_followers = followers - following

labels = ['Ne prate te nazad', 'Ti ne pratiš njih', 'Obostrano']
sizes = [len(only_following), len(only_followers), len(mutual_follow)]
colors = ['#ff9999','#66b3ff','#99ff99']

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
ax.axis('equal')  # Jednaka proporcija

st.markdown('<div class="header-box">Grafički prikaz odnosa praćenja</div>', unsafe_allow_html=True)
st.pyplot(fig)

st.title("Instagram Follower Analyzer")

uploaded_zip = st.file_uploader("Upload your Instagram Data ZIP file", type=["zip"])

if uploaded_zip is not None:
    try:
        with zipfile.ZipFile(io.BytesIO(uploaded_zip.read())) as z:
            # Čitamo JSON fajlove iz foldera connections u ZIP-u
            followers_json = z.read('connections/followers_and_following/followers_1.json').decode('utf-8')
            following_json = z.read('connections/followers_and_following/following.json').decode('utf-8')

            followers_data = json.loads(followers_json)
            following_data = json.loads(following_json)

            followers = load_usernames_followers_from_data(followers_data)
            following = load_usernames_following_from_data(following_data)

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

    except KeyError:
        st.error("ZIP file does not contain 'connections/followers_1.json' or 'connections/following.json'. Please check your ZIP file.")
    except Exception as e:
        st.error(f"Error processing the ZIP file: {e}")

else:
    st.info("Please upload a ZIP file downloaded from Instagram containing your data.")

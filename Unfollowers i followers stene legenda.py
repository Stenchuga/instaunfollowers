import json

def load_usernames(json_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    usernames = set()
    # data je lista
    for entry in data:
        if 'string_list_data' in entry and entry['string_list_data']:
            username = entry['string_list_data'][0]['value'].strip().lower()
            usernames.add(username)
    return usernames

def load_usernames_following(json_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    usernames = set()
    # data je dict sa ključem "relationships_following"
    for entry in data.get("relationships_following", []):
        if 'string_list_data' in entry and entry['string_list_data']:
            username = entry['string_list_data'][0]['value'].strip().lower()
            usernames.add(username)
    return usernames

followers = load_usernames(r'C:\Users\Gamer\Desktop\Python\followers.json')
following = load_usernames_following(r'C:\Users\Gamer\Desktop\Python\following.json')

not_following_you_back = following - followers
you_dont_follow_back = followers - following

print("🔁 Ti pratiš njih, ali oni tebe NE prate nazad:")
for user in sorted(not_following_you_back):
    print(f"- {user}")

print("\n👀 Oni prate tebe, ali ti njih NE pratiš nazad:")
for user in sorted(you_dont_follow_back):
    print(f"- {user}")

print(f"\n📊 Ukupno pratiš: {len(following)}")
print(f"📊 Ukupno te prate: {len(followers)}")
print("🔁 Ti pratiš njih, ali oni tebe NE prate nazad:")
for user in sorted(not_following_you_back):
    insta_link = f"https://www.instagram.com/{user}/"
    print(f"- {user} ({insta_link})")

print("\n👀 Oni prate tebe, ali ti njih NE pratiš nazad:")
for user in sorted(you_dont_follow_back):
    insta_link = f"https://www.instagram.com/{user}/"
    print(f"- {user} ({insta_link})")

print(f"\n📊 Ukupno pratiš: {len(following)}")
print(f"📊 Ukupno te prate: {len(followers)}")
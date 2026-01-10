# tool Cəsarət tərəfindən yaradılmışdır tool dəyişiklik edən satan peyserdi anası qe#bedi kimdese satan veya deyişen görsəm vayroxun skecem.!!!
# Admin:@Mustafazade043 | Kanal:@DarkHackerCesi
#Daha çoxsu üçün kanala qatıla bilərsiz


import webbrowser
webbrowser.open('https://t.me/DarkHackerCesi')
import os
import time
import random
from instagrapi import Client
from termcolor import colored
from requests.exceptions import HTTPError

csfil = "cs.json"
vlim = 5

def random_sleep():
    return random.randint(1, 4.7) +random.random()

def random_color():
    colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
    return random.choice(colors)

def save_cs(username, password):
    with open(csfil, 'w') as f:
        f.write(f"{username}\n{password}")

def load_cs():
    if os.path.exists(csfil):
        with open(csfil, 'r') as f:
            username, password = f.read().strip().split('\n')
            return username, password
    return None, None

def login(client, username=None, password=None):
    try:
        if username is None or password is None:
            username, password = load_cs()
            if not username or not password:
                raise ValueError("Username and password are required for login.")
        client.login(username, password)
        print(colored("Logged in successfully.", random_color()))
    except Exception as e:
        print(colored(f"Error during login: {e}", random_color()))
        username = input("Enter username: ")
        password = input("Enter password: ")
        save_cs(username, password)
        login(client, username, password)

def watch_stories(client, user, view_count):
    if view_count >= vlim:
        print(colored("Reached view limit, re-logging in.", random_color()))
        client.logout()
        time.sleep(300) 
        username, password = load_cs()
        login(client, username, password)
        view_count = 0

    try:
        user_id = client.user_id_from_username(user)
        stories = client.user_stories(user_id)
        if stories:
            for story in stories:
                client.media_seen([story.pk])
                print(colored(f"{user} has a story viewed: {story.pk}", random_color()))
                time.sleep(random_sleep())
                view_count += 1
                if view_count >= vlim:
                    print(colored("Reached view limit, re-logging in.", random_color()))
                    client.logout()
                    time.sleep(300)  
                    username, password = load_cs()
                    login(client, username, password)
                    view_count = 0
            return view_count
        else:
            print(colored(f"{user} has no stories.", random_color()))
            time.sleep(random_sleep())
            return view_count
    except HTTPError as e:
        if e.response.status_code == 429:
            print(colored("Rate limit exceeded. Waiting for 30 minutes before retrying.", random_color()))
            time.sleep(1800) 
            return watch_stories(client, user, view_count)
        else:
            print(colored(f"Error viewing stories: {e}", random_color()))
            return view_count
    except Exception as e:
        print(colored(f"Error viewing stories: {e}", random_color()))
        return view_count

def extract_media_id(client, reel_url):
    try:
        media_id = client.media_pk_from_url(reel_url)
        return media_id
    except Exception as e:
        print(colored(f"Error extracting media id: {e}", random_color()))
        return None

def fetch_comments(client, media_id):
    try:
        comments = client.media_comments(media_id)
        return comments
    except HTTPError as e:
        if e.response.status_code == 429:
            print(colored("Rate limit exceeded. Waiting for 30 minutes before retrying.", random_color()))
            time.sleep(1800)  
            return fetch_comments(client, media_id)
        else:
            print(colored(f"Error fetching comments: {e}", random_color()))
            return []
    except Exception as e:
        print(colored(f"Error fetching comments: {e}", random_color()))
        return []

def main():
    client = Client()

    username, password = load_cs()
    if not username or not password:
        username = input("Enter username: ")
        password = input("Enter password: ")
        save_cs(username, password)
    login(client, username, password)

    reel_url = input("Enter the reel URL: ")
    print(colored("Fetching comments...", random_color()))
    media_id = extract_media_id(client, reel_url)

    if media_id:
        comments = fetch_comments(client, media_id)
        view_count = 0
        for comment in comments:
            username = comment.user.username
            print(colored(f"Watching stories of: {username}", random_color()))
            view_count = watch_stories(client, username, view_count)

if __name__ == "__main__":
    main()
    
    
    #Mustafazade043 
    #DarkHackerCesi
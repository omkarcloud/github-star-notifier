import time
import requests
import telegram
from config import *


# Function to get the number of stars and the latest star details for a repository
def get_repository_stars(repo):
    url = f'{GITHUB_API_URL}/repos/{repo}'
    print(url)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        stars_count = data['stargazers_count']
        stars_url = f'{GITHUB_API_URL}/repos/{repo}/stargazers'
        stars_response = requests.get(stars_url)
        if stars_response.status_code == 200:
            stars_data = stars_response.json()
            if len(stars_data) > 0:
                latest_star = stars_data[-1]
                return stars_count, latest_star
    return None, None

# Function to send a Telegram message
def send_telegram_message(message):
    bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)
    bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)

# Function to check for new stars
def check_new_stars():
    stars = {}
    while True:
        print("Checking new stars")
        for repo in REPOSITORIES:
            current_stars, latest_star = get_repository_stars(repo)
            if current_stars is not None and latest_star is not None:
                if repo in stars:
                    if current_stars > stars[repo][0]:
                        username = latest_star['login']
                        # print(username)
                        message = f'someone starred {repo}'
                        send_telegram_message(message)
                stars[repo] = (current_stars, latest_star['id'])
        time.sleep(WAIT_TIME)  # Wait for 5 minutes

# Start checking for new stars
check_new_stars()

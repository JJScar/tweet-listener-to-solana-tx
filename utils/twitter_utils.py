import os
import tweepy
from dotenv import load_dotenv

# Load API keys from the .env file
load_dotenv()

# Custom Tweet Listener for Real-Time Streaming
class MyTweetListener(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        print(f"\n📢 New Tweet Detected: {tweet.text}")

    def on_connect(self):
        print("✅ Connected to Twitter Stream Successfully!")

    def on_connection_error(self):
        print("❌ Connection Error! Reconnecting...")

# Function to Start Real-Time Streaming for Multiple Users
def start_streaming(agent_usernames: list):
    bearer_token = os.getenv("TWITTER_BEARER_TOKEN")
    client = tweepy.Client(bearer_token=bearer_token)
    stream = MyTweetListener(bearer_token)

    # Convert usernames to user IDs for the stream filter
    user_ids = []
    for username in agent_usernames:
        try:
            user_data = client.get_user(username=username)
            user_ids.append(user_data.data.id)
        except Exception as e:
            print(f"❌ Error fetching user: {username} - {e}")

    # Adding streaming rules for each user ID
    for user_id in user_ids:
        stream.add_rules(tweepy.StreamRule(f"from:{user_id}"))

    # Start listening for tweets in real-time print(f"🎧 Listening for real-time tweets from: {', '.join(agent_usernames)}...")
    stream.filter()

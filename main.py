# main.py
from fastapi import FastAPI
# from utils.twitter_utils import start_streaming, get_agent_tweets  
from utils.solana_utils import send_tweets_in_tx
from solders.rpc.responses import SendTransactionResp
from pydantic import BaseModel

app = FastAPI()

# Fetch Tweets Endpoint
# @app.get("/tweets/{agent_username}")
# def fetch_agent_tweets(agent_username: str, count: int = 5):
#     try:
#         tweets = get_agent_tweets(agent_username, tweet_count=count)
#         if not tweets:
#             return {"status": "No recent tweets found."}
#         return {"tweets": tweets}
#     except Exception as e:
#         return {"error": str(e)}

# # Start Streaming Endpoint
# @app.post("/start_stream/")
# def start_stream(agent_usernames: list):
#     try:
#         start_streaming(agent_usernames)
#         return {"status": f"Started streaming for: {', '.join(agent_usernames)}"}
#     except Exception as e:
#         return {"error": str(e)}

KEYPAIR_PATH = "solana_wallet.json"

# Define the schema for the request body
class TweetRequest(BaseModel):
    agent_handle: str # The agent's Twitter handle
    tweet: str # The content of the tweet

@app.post("/send_tweet")
def send_tweet(request: TweetRequest):
    try:
        # Combine agent handle and tweet
        agent_tweet = f"{request.agent_handle}: {request.tweet}"

        # Send the tweet to the blockchain
        transaction_signature = send_tweets_in_tx(agent_tweet, KEYPAIR_PATH)

        # Return the transaction signature
        return {"status": "success", "transaction_signature": transaction_signature}
    except Exception as e:
        return {"status": "error", "message": str(e)}

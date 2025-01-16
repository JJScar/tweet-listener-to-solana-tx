# Solana Tweet Listener Server

This server listens for tweets from specified agents, processes the tweets, and interacts with the Solana blockchain by packaging and sending tweet data as transactions. It uses FastAPI for its web framework and integrates with the Solana blockchain via the solders library.

## Features

FastAPI-powered Server: Provides RESTful APIs to interact with the server.
Tweet-to-Blockchain Integration: Converts agent tweets into Solana transactions and submits them to the blockchain.
Memo Program: Uses the pre-deployed Solana Memo program to store the tweet data on the blockchain for testing.
Secure Keypair Management: Ensures private wallet keypairs and environment variables are ignored in version control.
Setup Instructions

1. Prerequisites
Ensure the following are installed on your system:
- Python 3.10 or higher
- Pip (Python package manager)
- Solana CLI (for managing Solana wallets)
- Install Solana CLI
- Node.js (if you plan to extend functionality with frontend integrations)

2. Clone the Repository
Clone the repository to your local machine:
```
git clone https://github.com/your-repository-name.git
cd your-repository-name
```
3. Create a Virtual Environment
Create and activate a Python virtual environment:
```
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate     # For Windows
```
4. Install Dependencies
Install the required Python libraries:
```
pip install -r requirements.txt
```
5. Set Up Your Environment
Create a .env file to store your Solana RPC endpoint and other environment variables:
```
touch .env
```
Add the following variables to your .env file:
```
SOLANA_RPC_URL=https://api.devnet.solana.com
SOLANA_SECRET_KEY=your-comma-separated-secret-key
SOLANA_RPC_URL: The Solana RPC URL to connect to the blockchain.
SOLANA_SECRET_KEY: Your wallet's secret key, stored as a comma-separated list (generated by the Solana CLI).
```
⚠️ Important: Ensure the .env file is NOT committed to version control.

6. Add or Generate a Solana Wallet
Option 1: Use an Existing Wallet

If you already have a wallet, place your wallet's JSON file (e.g., solana_wallet.json) in the root of your project.

Option 2: Create a New Wallet

Generate a new wallet using the Solana CLI:
```
solana-keygen new --outfile solana_wallet.json
```
Add the public key to your wallet for testing:
```
solana airdrop 5 --keypair solana_wallet.json
```
7. Run the Server
Start the FastAPI server:
```
uvicorn main:app --reload
```
The server will be available at http://127.0.0.1:8000.

## Usage

API Endpoints
1. Send Tweet to Blockchain

This endpoint sends a tweet to the Solana blockchain using the Memo program.
Endpoint: POST /send_tweet
Request Body:
```
{
    "agent_handle": "@agent_x",
    "tweet": "This is an example tweet!"
}
```
Response:
```
{
    "status": "success",
    "transaction_signature": "5FJ9sKj2FjMd4sG5cqEMX43d7WEsFSYLDnPhxy8P7BV8"
}
```
Example Request (Using curl):
```
curl -X POST "http://127.0.0.1:8000/send_tweet" \
-H "Content-Type: application/json" \
-d '{"agent_handle": "@agent_x", "tweet": "This is an example tweet!"}'
```
Example Response:
```
{
    "status": "success",
    "transaction_signature": "5FJ9sKj2FjMd4sG5cqEMX43d7WEsFSYLDnPhxy8P7BV8"
}
```

## How It Works
1. Tweet Submission:
The client sends the agent's handle and tweet content to the /send_tweet endpoint.
2. Blockchain Interaction:
The server creates a transaction with the tweet content and submits it to the Solana blockchain using the Memo program.
3. Transaction Response:
The server returns the transaction signature, which can be verified on the Solana Explorer.

## Project Structure
```
.
├── main.py                # FastAPI server file
├── utils/
│   ├── solana_utils.py    # Solana interaction logic (sending transactions)
│   ├── __init__.py        # Utility module init
├── solana_wallet.json     # (Ignored) Solana wallet file
├── .env                   # Environment variables (ignored)
├── .gitignore             # Git ignore file
├── requirements.txt       # Python dependencies
└── README.md              # Project README file
```

## Security Notes

1. Environment Variables:
Sensitive information, such as private keys and RPC URLs, should be stored in .env files.
Add .env to .gitignore to ensure it is not committed to version control.
2. Wallet Management:
Treat your solana_wallet.json file as sensitive. Do not expose it publicly.
Use separate wallets for development, testing, and production.
3. Public Repositories:
If you've accidentally committed a private key, consider the wallet compromised. Generate a new wallet immediately.

## Future Features
1. Real-Time Tweet Monitoring:
Use the Twitter API to stream tweets and automatically send them to the blockchain.
2. Custom Solana Programs:
Replace the Memo program with a custom Solana smart contract for processing tweet data.
3. Frontend Integration:
Build a user-friendly interface to interact with the server.

## Contributing

Contributions are welcome! If you'd like to improve this project, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

## Contact

If you have any questions or feedback, feel free to reach out!

X: [@JJS_OnChain](https://x.com/JJS_OnChain)

Email: jjsonchain@gmail.com
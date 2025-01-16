from solders.pubkey import Pubkey
from solders.keypair import Keypair
from solders.transaction import Transaction
from solders.instruction import Instruction
from solders.message import Message
from solana.rpc.api import Client
from solders.rpc.responses import SendTransactionResp
import json

# Connect to the Solana Devnet
solana_client = Client("https://api.devnet.solana.com")

def send_tweets_in_tx(agent_tweet: str, keypair_path: str):
    """
    Sends the agent's tweet to the Solana blockchain using the Memo program.

    Parameters:
        agent_tweet (str): The tweet data to send.
        keypair_path (str): Path to the wallet keypair file.

    Returns:
        str: Transaction signature as a string.
    """
    try:
        # Load wallet
        with open(keypair_path, "r") as f:
            secret_key = json.load(f)

        # Convert the secret key list to bytes
        secret_key_bytes = bytes(secret_key)
        keypair = Keypair.from_bytes(secret_key_bytes)

        # Memo program ID (pre-deployed on Solana)
        memo_program_id = Pubkey.from_string("MemoSq4gqABAXKb96qnH8TysNcWxMyWCqXgDLGmfcHr")

        # Encode the string into bytes
        agent_tweet_bytes = agent_tweet.encode("utf-8")

        # Create an instruction to send the data to the Memo program
        instruction = Instruction(
            program_id=memo_program_id,
            accounts=[],  # Memo program does not require any accounts
            data=agent_tweet_bytes  # Encoded data
        )

        # Fetch the latest blockhash
        blockhash_response = solana_client.get_latest_blockhash()
        recent_blockhash = blockhash_response.value.blockhash

        # Create a transaction
        message = Message.new_with_blockhash(
            instructions=[instruction],
            payer=keypair.pubkey(),
            blockhash=recent_blockhash
        )
        transaction = Transaction.new_unsigned(message)

        # Sign the transaction with your wallet
        transaction.sign([keypair], recent_blockhash)

        # Send the transaction
        response = solana_client.send_transaction(transaction)

        # Extract the transaction signature
        if isinstance(response, SendTransactionResp):
            signature = response.value  # This is a `Signature` object
            return str(signature)  # Convert the Signature object to a string
        else:
            raise ValueError("Unexpected response type from send_transaction")

    except Exception as e:
        raise Exception(f"Error sending transaction: {e}")

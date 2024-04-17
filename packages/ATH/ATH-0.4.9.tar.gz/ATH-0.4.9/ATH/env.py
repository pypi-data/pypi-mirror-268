from dotenv import load_dotenv
import os

def env(env_file, *args):
    load_dotenv(env_file)
    secrets = {}
    for arg in args:
        secrets[arg] = os.getenv(arg)
    return secrets
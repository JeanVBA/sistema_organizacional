import binascii
import os

def debug_env_var(name):
    val = os.getenv(name, "").strip()
    print(f"{name} = {val} | HEX: {binascii.hexlify(val.encode(errors='replace'))}")
    return val

DB_NAME = debug_env_var("DB_NAME")
DB_USER = debug_env_var("DB_USER")
DB_PASSWORD = debug_env_var("DB_PASSWORD")
DB_HOST = debug_env_var("DB_HOST")
DB_PORT = debug_env_var("DB_PORT") or "5432"
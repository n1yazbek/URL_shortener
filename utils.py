import sqlite3

DB_FILE = "url_shortener.db"

def initialize_database():
    """Initialize the database."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS url_mappings (
            short_url TEXT PRIMARY KEY,
            long_url TEXT
        )
    """)
    conn.commit()
    conn.close()

def store_mapping(short_url, long_url):
    """Store the mapping between short URL and long URL in the database."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO url_mappings (short_url, long_url) VALUES (?, ?)", (short_url, long_url))
    conn.commit()
    conn.close()

def get_long_url(short_url):
    """Retrieve the long URL corresponding to the given short URL from the database."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT long_url FROM url_mappings WHERE short_url = ?", (short_url,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None


# utils.py

import hashlib
# utils.py

import hashlib
import time

def generate_hash(long_url):
    """Generate a unique hash for the given long URL."""
    # Add current timestamp to long URL to ensure uniqueness
    unique_string = long_url + str(time.time())
    
    # Generate MD5 hash of the unique string
    hash_object = hashlib.md5(unique_string.encode())
    
    # Convert the hash to a hexadecimal representation
    hash_hex = hash_object.hexdigest()
    
    # Take the first 8 characters as the short URL
    short_url = hash_hex[:8]
    
    return short_url

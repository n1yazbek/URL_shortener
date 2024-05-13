# url_shortener.py

from utils import generate_hash, get_long_url, store_mapping

class URLShortener:
    def shorten_url(self, long_url):
        while True:
            # Generate short URL
            short_url = generate_hash(long_url)
            
            # Check if short URL already exists in the database
            existing_long_url = get_long_url(short_url)
            print("Generated Short URL:", short_url)
            print("Existing Long URL for Short URL:", existing_long_url)
            if existing_long_url:
                # Short URL already exists, generate a new one
                print("Short URL already exists:", existing_long_url)
                continue
            
            # Store mapping in database
            store_mapping(short_url, long_url)
            print("Mapping stored in database:", short_url, "->", long_url)
            
            return short_url

    def redirect(self, short_url):
        # Retrieve long URL from database
        return get_long_url(short_url)

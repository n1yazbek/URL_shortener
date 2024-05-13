# test_shortener.py

from url_shortener import URLShortener

def main():
    # Create an instance of URLShortener
    shortener = URLShortener()

    # Test shortening a long URL
    long_url = "https://www.example.com/this/is/a/very/long/url"
    short_url = shortener.shorten_url(long_url)
    print("Shortened URL:", short_url)

    # Test redirecting from short URL to long URL
    retrieved_url = shortener.redirect(short_url)
    print("Retrieved URL:", retrieved_url)

    # Verify if the retrieved URL matches the original long URL
    if retrieved_url == long_url:
        print("URL redirection successful!")
    else:
        print("URL redirection failed!")

if __name__ == "__main__":
    main()

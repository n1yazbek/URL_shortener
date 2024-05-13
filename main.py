# main.py

from url_shortener import URLShortener

def main():
    shortener = URLShortener()

    while True:
        print("1. Shorten URL")
        print("2. Redirect")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            long_url = input("Enter the long URL to shorten: ")
            short_url = shortener.shorten_url(long_url)
            print("Shortened URL:", short_url)
        elif choice == "2":
            short_url = input("Enter the short URL to redirect: ")
            long_url = shortener.redirect(short_url)
            if long_url:
                print("Redirecting to:", long_url)
            else:
                print("Short URL not found!")
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

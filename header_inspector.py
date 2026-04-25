from urllib.request import urlopen
from urllib.error import URLError

url = input("Enter URL: ")

try:
    response = urlopen(url)

    print("\nResponse Headers:\n")

    for key, value in response.getheaders():
        print(f"{key}: {value}")

except URLError:
    print("Failed to fetch URL.")

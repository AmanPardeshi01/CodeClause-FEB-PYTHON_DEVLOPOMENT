import pyshorteners 
url = input("Enter your url:-")
def shortener(url):
    s = pyshorteners.Shortener()
    print(s.tinyurl.short(url))
shortener(url)

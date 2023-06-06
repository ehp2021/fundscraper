import requests
from bs4 import BeautifulSoup
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("./serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

search_keywords = "Series A"
url = f"https://news.google.com/search?q={search_keywords}&hl=en-US&gl=US&ceid=US%3Aen"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

articles = soup.find_all("article")
for article in articles:
    title = article.find("h3").text
    link = article.find("a")["href"]
    #description = article.find("p").text

    # Extract other relevant information from the article as needed

    # Save the extracted data to Firebase
    doc_ref = db.collection("articles").document()
    doc_ref.set({
        "title": title,
        "link": link,
        #"description": description,
        # Add other relevant fields to the document
    })

# fundscraper

Just a side project I built to pull in news around "Series A" funding from Google News and save down certain pieces of information to FireStore

I'm still looking for the right serverless computing setup to automate this process

## When you run scraper.py

You should see all the news article titles and links show up in your Firestore like this:

![screenshot](https://github.com/ehp2021/zims/blob/main/screenshot1.png)

## To set up Firestore

To set it up correctly, you need to replace "serviceAccountKey.json" with the actual file path to your service account key JSON file. Here's what you need to do:

1) Go to the Firebase Console (console.firebase.google.com) and open your Firebase project.
2) Navigate to the "Settings" page of your project by clicking on the gear icon on the left side of the console.
3) Select the "Service Accounts" tab.
4) Under "Firebase Admin SDK," click on the "Generate new private key" button. This will download a JSON file containing your service account key. Save it down in the same folder as scraper.py file.
5) Don't forget to set up a .gitignore and add "serviceAccountKey.json" to it

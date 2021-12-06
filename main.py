from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import json
import imdb

googleScopes = ['https://www.googleapis.com/auth/contacts.readonly']






def main():
    """Logs user in to Google and prints data to confirm. Could be used as a suer account in the future
       Then asks for a movie to search for
    """
    creds = None
    
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', googleScopes)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', googleScopes)
            creds = flow.run_local_server(port=0)
        
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('people', 'v1', credentials=creds)


    print("ID: " + creds.client_id + "\n\n")


    sear = input("What movie would you like to search for?")
    

    im = imdb.IMDb()
    results = im.search_movie(sear)

    # Retrive the list and print
    for item in results:
        movie= im.get_movie(item.movieID)        
        print("Main: " + str(movie))

        print("Main: " + str(movie['plot'][0]))
        
        yesno = input("Would you like to see another result? [Y/N]")
        if yesno == "N":
        	   break

        print("\n\n")
            


if __name__ == '__main__':
    main()

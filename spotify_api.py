import json
import spotipy
import webbrowser
import pyautogui
import time

# pyautogui.displayMousePosition()


username = '31ich3a6llqhviexgvgrsxlcduz4'
clientID = '353b7f541a974b2e8e1f6ff39d732b69'
clientSecret = 'c1f2bbdcf3084f8e8630891aeaa257d6'
redirectURI = 'http://google.com/callback/' 

oauth_object = spotipy.SpotifyOAuth(clientID,clientSecret,redirectURI)
token_dict = oauth_object.get_access_token()
token = token_dict['access_token']
spotifyObject = spotipy.Spotify(auth=token)
user = spotifyObject.current_user()

print(json.dumps(user,sort_keys=True, indent=4))

def play_song(searchQuery):
       # Search for the Song.
        searchResults = spotifyObject.search(searchQuery,1,0,"track")
        # Get required data from JSON response.
        tracks_dict = searchResults['tracks']
        tracks_items = tracks_dict['items']
        song = tracks_items[0]['external_urls']['spotify']
        # Open the Song in Web Browser
        webbrowser.open(song)
        print('Song has opened in your browser.')
        print("Sleeping before playing")
        time.sleep(10)
        pyautogui.click(302,564)
        # pyautogui.press('enter') 


while True:
    print("Welcome, "+ user['display_name'])
    print("0 - Exit")
    print("1 - Enter Emotion")
    choice = int(input("Your Choice: "))

    if choice == 1:
        searchQuery = ("Aurora")
        play_song(searchQuery)


    elif choice == 2:
        # Get the Song Name.
        # searchQuery = input("Enter Song Name: ")
        searchQuery = ("Love me like you do")
        play_song(searchQuery)
     

    elif choice == 0:
        break
    else:
        print("Enter valid choice.")
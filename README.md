# Overview

Help me with my mood(named Mind Shift) is a cross platform desktop app built using Electron Js. It uses twitter usernames provided by the user, then accesses their public tweets, analyzes the tone attached with them and then recommends the user various things such as music, videos etc based on the mood.

# Usage

#### 1) New user
- **Get started:** Provide certain details, likes and dislikes and thus create a profile with Mind Shift. Mind Shift will then display results depending on users interests.
- **Quick Start:** Avoid providing any details and get quick access. In this case, only users mood will be taken into account while display results.

#### 2) Returning User
- **Continue:** Returning user can continue by just providing his user name, Mind Shift will then access his profile and   display results depending on users interests.

# Implementation

- **Accessing Tweets:** Twitter api is used to access the tweets of a user.
- **Tone Analyzing:** IBM's Waston tone analyzer is used for this purpose.
- **Backend:** Python3 is used as backend for Mind Shift. And python-shell for node JS is used for communication between backend and frontend.
- **Database:** JSON is used to store and retrieve all the data required by Mind Shift .


#### Main Function Descriprions (found in /engine/assets/functions.py)
- **getTweets():** Accepts a twitter username and returns the tweets for last 24 hours or 3 days if the username is valid and user has posted in the given time frame. Else returns appropriate error message

- **getTones():** Accepts an array of strings performs tone analysis on each using IBM Watson and returns the json

- **formatTones():** Accepts a json file that getTones returns and cleans it to make a dictionary with key val pair of tone name and probability respectively.

- **formatTonesHtml():** Accepts a dictionary that formatTones() returns, and forms a raw html string from it which is displayed to the user

- **getVideos():** Accepts a tone dictiionary and returns all valid videos that matches the tones.

- **getMusic():** Accepts a tone dictiionary and returns all valid music that matches the tones.

- **formatVideos():** Accepts an array that getVideos() returns and formats it to raw HTML.

- **formatMusic():** Accepts an array that getMusic() returns and formats it to raw HTML.

- **getPersonalisedVideos():** Accepts a tone dictionary and a user profile. Returns all valid videos that matches the tones and perefrences of the user.

- **getPersonalisedMusic():** Accepts a tone dictionary and a user profile. Returns all valid music that matches the tones and perefrences of the user.

# Current Limitations
- The data store for Music and Videos are currently very low, as a result on certain user preferences matching data are not found quite often.






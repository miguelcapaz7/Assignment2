# Python MP3 Player

## Description
A desktop-based python MP3 player that allows users to open media files to the program and to be able to play, pause, resume, and delete the song. The GUI provides information about each song that is played from an SQLite database. In addition, users have the option to rate a song out of 5.

**The following song properties are stored in the database:**
- Title
- Artist
- Runtime
- File Location
- Album
- Genre
- Date Added
- Last Played
- Play Count
- Rating
  
## Technologies Used
- Python
- Flask API
- SQLite
- Tkinter GUI
- GitHub
- VLC Media Player (python-vlc)

## Prerequisites
Prior to usage, you must install VLC Media Player.

**Dependencies**

To install modules, use... 

```
pip install sqlalchemy
pip install flask
pip install requests
pip install eyed3
pip install python-vlc
```

## Usage

To use the application, run both `song_api.py` and `main_controller.py`.

This project was built in the Object-Oriented Programming course at BCIT.

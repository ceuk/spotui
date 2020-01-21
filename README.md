# SpoTUI
![Version Badge](https://img.shields.io/pypi/v/spotui)
![License Badge](https://img.shields.io/github/license/ceuk/spotui)
![Code size Badge](https://img.shields.io/github/languages/code-size/ceuk/spotui)

Spotify in the terminal. 

![screenshot](https://i.imgur.com/7syOTKb.gif)

Getting Started
-----------

Install with ```pip install spotui```

Register a developer application at: [https://developer.spotify.com/dashboard/login]( https://developer.spotify.com/dashboard/login). Once you create the application you'll need to edit it to add a Redirect URI. Use something like 'http://localhost:8888/auth' (it doesn't matter what you use really as long as it matches what's in your config file).

Run `spotui` to generate a sample config file at ~/.config/spotui/.spotuirc or create one manually with the following:

```
  [spotify_api]
  user_name = *Your spotify username*
  client_id = *Your application client ID*
  client_secret = *Your application secret*
  redirect_uri = http://localhost:8888/callback
```

Once you're done start the app with `spotui`, log in via your browser and copy the URL of the broken web page you're taken to. *(This ugly authentication process is part of the underlying Spotipy library I use so don't blame me :stuck_out_tongue_winking_eye:)*

This app acts like a kind of remote control for Spotify. The best way to use it is in conjunction with [Spotifyd](https://github.com/Spotifyd/spotifyd) which means you won't need to actually have Spotify open. Alternatively, you can just open Spotify on your computer, phone etc. (press `d` to pick the device to play on).




Controls
-------

**Navigation**

`tab` Switch section

`k`/`↑` Up

`j`/`↓` Down

`Enter` Select

`/` Search 

`d` Open device menu

`Esc`/`q` Quit/Back

**Playback**

`space` Play/Pause

`n` Next track

`p` Previous track

`→` Seek 10s forwards

`←` Seek 10s backwards

`s` Toggle shuffle

`r` Toggle repeat


FAQ
----

* **Why did you make this?** To learn Python. This is literally the first thing I've ever made in Python
* **Why should I use this instead of [Rigellute's version](https://github.com/Rigellute/spotify-tui)?** You like the way mine looks better? Rigellute's version is great, and it's written in Rust which automatically makes it cool :sunglasses: 
* **What do I do if something breaks?** [Raise an issue](https://github.com/ceuk/spotui/issues/new) or submit a PR to fix my crappy code :pray:

Dependencies
-----------

* [Spotipy](https://spotipy.readthedocs.io/en/latest/)

LICENSE
------

MIT

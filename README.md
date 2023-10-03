# teh_tagger
tagger no taggin

$ find music/
music/
music/Herve Roy
music/Herve Roy/Romantic Themes
music/Herve Roy/Romantic Themes/i_am_trash_panda.txt
music/Herve Roy/Romantic Themes/Lovers Theme.mp3

$ python teh_tagger/teh_tagger.py music/
DEBUG:  Processing music/Herve Roy/Romantic Themes/Lovers Theme.mp3
DEBUG:  current tags {}
DEBUG:  new tags {'album': ['Romantic Themes'], 'artist': ['Herve Roy']}

#!/usr/bin/python

"""
Usage:  %s directory

Requires:  mutagen library

Caveats:  probably can't handle weird filenames that require escapes or operating systems that literally use escapes for directory separators
"""

import os,sys
import mutagen
from mutagen.easyid3 import EasyID3  #  typing shortcut

if len(sys.argv) != 2:
   print(__doc__ % (sys.argv[0]))
   sys.exit()

startdir=sys.argv[1]

#  in other words use Linux
PATH_SEP="/"

def dummy_function(pathlist, mp3):
   #print("DEBUG:  I AM A DUMMY FUNCTION %s" % (pathlist))
   pass

# translate from directory path;  "None" is unused
# can also push functions/objects into the list for custom processing i.e. if the filename contains track and you want to shove that into a tag
# also makes more sense for this list to be backwards, starting from the filename and then going uupwards for more relative behavior
# just remember it gets called in that order too, so overrides need to be careful...

# todo:  figure out how to recursively import or read in a tag map...
tag_map = [
dummy_function, #  actual filename
"album",
"artist",
None,
None,  #  buncha placeholders in case of crazy directory depth
None,
None,
None,
None,
None,
None,
None
]

for root,dirs,files in os.walk(startdir):
   #print("DEBUG:  root=%s, dirs=%s, files=%s" % (root, dirs, files))

   for fn in files:
      #  we only care about the mp3 files
      if fn.lower()[-4:] != ".mp3":
         continue

      #  full string pathspec to file
      fullspec = PATH_SEP.join([root,fn])
      print("DEBUG:  Processing %s" % (fullspec))

      #  broken out directory path to file as an array
      pathlist = root.split(PATH_SEP)
      pathlist.append(fn)
      pathlist.reverse();  #  not used for anything else so reverse it to match the tag_map

      #  prepare metadata for writing
      try:
         mp3 = EasyID3(fullspec)
      except mutagen.id3.ID3NoHeaderError:
         print("DEBUG:  No tag found, adding")
         mp3 = mutagen.File(fullspec, easy=True)
         mp3.add_tags()
         # mp3.save()

      print("DEBUG:  current tags %s" % (mp3))

      # mp3.delete()  #  delete all tags;  this WILL write to file even without save

      for i in range(len(pathlist)):
         if tag_map[i] == None:
            continue
         if type(tag_map[i]).__name__ == "function":
            tag_map[i](pathlist, mp3)
         else:
            #print("DEBUG:  %s(%s)" % (tag_map[i], pathlist[i]))
            mp3[tag_map[i]] = pathlist[i]
            
      print("DEBUG:  new tags %s" % (mp3))

      # mp3.save()


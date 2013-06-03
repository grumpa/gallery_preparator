 gallery preparator
====================

Program transforms picutres into form usable for web gallery makers.

Program reads directory with picutres and save them into destination
directory with required size of picture. It also makes subdirectory
with thumbnails. 

Program also generates file with descripition of the gallery as
PHP and Python (future) script/config file. It contains variables for
- gallery name,
- description of the gallery,
- which picture should be used as a gallery picture for main page with galleries
- array of descriptions for pictures (not generated by this program)

Program works from console and asks you for everything needed.


 current status
----------------

Program works well. Only some installator missing. 


 usage
-------

    $ gallery_preparator_console.py

    Source base directory with picture directory(s) []:
    Source subdirectory with pictures []:
    Destination base directory for galleries []:
    Destination subdirectory for the gallery []:
    Name for gallery (fee text) []:
    Description (free text include html tags) - all in one line. Write "x" for erase existing text.:
    Required size for picture (dimension of longer side) []:
    Required size for thumbnail (dimension of longer side) [220]:

Some terminology:

- source base directory - directory where are subdirectories with pictures
- source subdirectory - one particular subdirectory of base directory
- The same is for destination directories. 

The reason why the path is diveded is when you process serveral
directories, the base directory remains the same and it is simpler
to write or copy/paste subdirectory name only.

__Rotating pictures__

After generating pictures into destination directory program asks you if you want to
rotate pictures. You probably have possibility to view generated
pictures immediatelly after their generation. So if some of them
are not rotated correctly, you may make it good now:

    Rotate pictures? [y/N] ? y
    Rotate pictures in directory /tmp/gal2 [Y/n]: y
    Pictures numbers and direction of rotation (example: 6l 12r 16-23l 14r 35u):

First program ensures if the directory where to rotate is the destination
directory. Then asks for picture numbers and direction of rotation.
Your input may look like this:

8l 14r 16-21r 12u

It means that file 00008.jpg should be rotated left. Picture in file
00014.jpg rotate right. You may insert range. So 16-21 means files
00016.jpg, 00017.jpg, ..., 00021.jpg - all rotate right.
12u means rotate 00012.jpg 180 degrees.


Finally program asks you, if you want to process next directory - gallery.
And so forth until the end...


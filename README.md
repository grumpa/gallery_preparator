 gallery preparator
====================

Program transforms picture folder into form usable for web gallery makers.

 An Example
------------

You have directory with serveral subirectories with pictures:
```
/path/to/basedir/subdir1/pic1.jpg
/path/to/basedir/subdir1/pic2.jpg
/path/to/basedir/subdir1/pic3.jpg
/path/to/basedir/subdir2/pic1.jpg
/path/to/basedir/subdir2/pic2.jpg
/path/to/basedir/subdir2/pic3.jpg
```
And you want to generate directories with converted pictures
into required size and with subidr with thumnails:
```
/path/to/dstbasedir/dstdir1/thumbs/00001.jpg
/path/to/dstbasedir/dstdir1/thumbs/00002.jpg
/path/to/dstbasedir/dstdir1/thumbs/00003.jpg
/path/to/dstbasedir/dstdir1/00001.jpg
/path/to/dstbasedir/dstdir1/00002.jpg
/path/to/dstbasedir/dstdir1/00003.jpg
/path/to/dstbasedir/dstdir1/description
/path/t.... the same for next dir
```

File 'description' contains importrant info about gallery:
- gallery name
- gallery description (possilby with html tags)
- gallery picture = pic to show on title page with galleries
- pics[] - array with descriptions to particular picutres (not implemened)

And this is all for now. This application doesn't generate any html output.
It really only transforms source directories into destination with thumbnails.

Program works from Linux console and asks you for everything needed.


 Dependencies
--------------

- python standar library :)
- PIL

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


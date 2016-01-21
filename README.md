 gallery preparator
====================

Prepare photo gallery in bulk from source directory. Program converts photos
to required size perserving ratio. It also generates thumbnails subdirectory.

Target is usable as source for photo galleries written for web or simply generated
by javascript apps like http://galleria.io/ (it is what I really do).

As last step in bulk transformation you can rotate pictures - in bulk also.

Gallery_preparator also saves file "description.inc" in target directory. This file
is PHP style config file containig name for the gallery, detailed description and id of 
title photo.

Program works in console and it asks for parameters (source dir, target dir, size
of photos,...).


i18n
----

Program uses gettext so it is translatable to different languages. This time it has
base English and Czech translation (my mother language).


Requirements
------------

- python 3 - tested with 3.4
- pillow 3.1
 

How It Works
------------

In base directory you run:

    $ gallery_preparator_console.py

First program asks for source directory. They are two questions:
- base directory
- particular subdirecory with photos

The reason for doing it in two steps is that you may have more subdirs in base
directory. Program remebers base direcory and in next turn you don't need to
provide this path again and again if you have more subidrs with photos.

Target is provided similar way: Base direcory where you galleries reside
and subdirectory for one particular gallery.

Then you provide name for your gallery, next description with possible
html tags (all in one line - not very sophisticated way ;)

Next you provide size of photos and size of thumbnails. Longer side only.
The shorter size is calculated from ratio. Ratio is perserved.

Then the program prints summary of parameters povided by you and you can
confirm it or decline. In case of decline you are asked for all questions
again. Previously provided values are offered as defaults - so you provide
corrected values only.

If everything is OK you confirm that. Then the conversion runs.

The questionary looks like this:

    Source base directory with picture directory(s) []:
    Source subdirectory with pictures []:
    Destination base directory for galleries []:
    Destination subdirectory for the gallery []:
    Name for gallery (fee text) []:
    Description (free text include html tags) - all in one line. Write "x" for erase existing text.:
    Required size for picture (dimension of longer side) []:
    Required size for thumbnail (dimension of longer side) [220]:

Then you are asked if you want rotate some pictures. It is supposed you
have possibility preview your gallery and you can see if position of
photos is correct.

Also rotations go in bulk. You provide nubers of pictures with one character
saying rotation direction. For example: ***4l*** means photo No 4 rotate left.
You can provide all symbols separated by space. If more adacent photos needs
the same rotation, you can provide range this way: ***14-19r*** - means pictures
nuber 14 to 19 all rotate right. Rotation 180 degrees has symbol ***u***.

    Rotate pictures? [y/N] ? y
    Rotate pictures in directory /tmp/gal2 [Y/n]: y
    Pictures numbers and direction of rotation (example: 6l 12r 16-23l 14r 35u):


Future
------

I use this application by myself so I do some improvements from time to time.
This version is enough for me but if you try it and get some idea what to
make better, I'll be glad for your inspiration.

Surelly I want to rewrite structure of files and directories to standard python
package and put in to pypi. Sometimes... ;)


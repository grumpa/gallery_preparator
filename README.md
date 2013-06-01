--------------------
 gallery preparator
--------------------

Program transforms picutres into form usable for gallery makers.

It reads directory with picutres and save them into destination
directory with required size. It also makes subdirectory with
thumbnails. 

Program also generates file with descripition of the gallery
- gallery name, description, which picture use as gallery picture
for page with galleries. It is created in form usable in PHP scripts.

Program works from console and asks for everything.


 current status
----------------

Program works well. Currently it is in process of i18n and asks you
in Czech language :-) Learn it. It is nice language ;)


 usage
-------

$ gallery_preparator_console.py

Program asks you everything importrant. It is needed to explain some
terminology:

source base directory - directory where are subdirectories with pictures
source subdirectory - one particular subdirectory of base directory

the same is for destination. 

The reason is when you process serveral
directories, the base directory remains the same and it is simpler
to write or copy/paste it.

Next program asks for name of the gallery and description.
Description is optional. If you want it logner, you must write
on one long line. Console cannot work with more lines and web
browser breaks lines as it needs. ;)

Finally you tell size of picture and size of thumbnail.  It is ment
the logner side of picture: Width in landscape, height in portrait.

> Rotating pictures <

After generating destination diretory program asks you if you want to
rotate pictures. You probably have possibility to view generated
pictures immediatelly after their generation. So if some of them
are not rotated correctly, you may make it good now.

First program ensures if the directory where to rotate is the destination
directory. Then asks for picture numbers and direction of rotation.
Your input may look like this:

8l 14r 16-21r 12u

It means that file 00008.jpg should be rotated left. Picture in file
00014.jpg rotate right. You may insert range. So 16-21 means files
00016.jpg, 00017.jpg, ..., 00021.jpg - all rotate right.
12u means rotate 00012.jpg 180 degrees.

> ...and so on... <

Finally program asks you, if you want to process next directory - gallery.



#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
An executing class for gallery preparator independent on user interface.
"""

import sys
import os
import os.path
from PIL import Image, ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True


class Gallery:
    """Gallery source and destination."""

    def __init__(self,
                 basedir_src="",
                 dir_src="",
                 basedir_dst="",
                 dir_dst="",
                 name="",
                 description="",
                 pic_size=1600,
                 thm_size=220,
                 num_from=1):
        """
        Set initial values for a gallery.
        dir_src - source directory with original pictures
        basedir_dst - destination directory where save galeries to
        dir_dst - subir for pictures and thubms (ie for particular gallery
        name - name of the gallery (one line)
        description - long description of the gallery (optional)
        """
        self.basedir_src = basedir_src
        self.dir_src = dir_src
        self.basedir_dst = basedir_dst
        self.dir_dst = dir_dst
        self.name = name
        self.description = description
        self.pic_size = int(pic_size)
        self.thm_size = int(thm_size)
        self.num_from = int(num_from)

    def make_directories(self):
        """Make directories for picture gallery and thumbs"""
        try:
            os.mkdir(self.basedir_dst+"/"+self.dir_dst)
        except OSError as err:
            # TODO - impossible to use print - ui is unknown for us here
            print("Nejde vytvořit adresář pro obrázky ({0}): {1} - {2}".format(self.dir_dst, err.errno, err.strerror))
            sys.exit(1)
        else:
            os.mkdir(self.basedir_dst+"/"+self.dir_dst+"/thumbs")

    def make_description_file(self):
        """Make file describing gallery"""
        df = open("%s/%s/description.inc" % (self.basedir_dst, self.dir_dst), 'w')
        df.write("<?php\n")
        df.write("$gallery_name = \"%s\";\n" % self.name)
        df.write("$gallery_description = \"%s\";\n" % self.description)
        df.write("$gallery_pic = \"{0:0>5d}.jpg\";\n".format(self.num_from))
        df.write("$pics[] = \"\";\n")
        df.write("?>\n")
        df.close()

    def convert_pictures(self):
        """Reads pictures from source directory and makes required ones into destination."""
        number = self.num_from
        for item in os.listdir("%s/%s" % (self.basedir_src, self.dir_src)):
            try:
                im = Image.open("%s/%s/%s" % (self.basedir_src, self.dir_src, item))
            except IOError:
                # It is not a picture file
                continue
            w, h = im.size
            # temporary rotation makes resizing simpler
            rotated = False
            if w < h:
                im = im.rotate(angle=90, expand=True)
                rotated = True
            ratio = 1.0 * im.size[1] / im.size[0]
            # Don't resize picture, which is smaller then required size.
            if self.pic_size < im.size[0]:
                im = im.resize((self.pic_size, int(self.pic_size * ratio)))
            imt = im.copy()
            imt.thumbnail((self.thm_size, int(self.thm_size * ratio)))
            if rotated:
                im = im.rotate(angle=270, expand=True)
                imt = imt.rotate(angle=270, expand=True)
            # And save it finally
            im.save("%s/%s/%05d.jpg" % (self.basedir_dst, self.dir_dst, number))
            imt.save("%s/%s/thumbs/%05d.jpg" % (self.basedir_dst, self.dir_dst, number))
            number = number + 1

    def rotate_pics(self, pdir, pics):
        """
        Rotate pictures pics in directory pidr
        pics - string as "6l 27-45r 18u" i.e.:
                - pic 00006.jpg rotate left
                - pics from 00027.jpg to 00045.jpg rotate right
                - pic 00018.jpg rotate 180
        """
        # If no pictures supplied, no work to do.
        if pics == '' or pics is None:
            return
        pic_list = set()
        # is there some range input in picture list?
        for xpic in pics.split():
            if xpic.count("-") == 1:
                begin, end = xpic.split("-")
                rot = end[-1:]
                end = int(end[:-1])
                begin = int(begin)
                if begin > end:
                    x = begin
                    begin = end
                    end = x
                for num in range(begin, end+1):
                    pic_list.add(str(num)+rot)
            else:
                pic_list.add(xpic)
            # finally, rotate
        for xdir in (pdir, pdir+"/thumbs"):
            for xpic in pic_list:
                pic_no = xpic[:-1]
                pic_rot = xpic[-1:]
                pic_fn = "%05d.jpg" % int(pic_no)
                pic_cur = Image.open("%s/%s" % (xdir, pic_fn))
                if pic_rot.lower() == "l":
                    pic_cur = pic_cur.rotate(angle=90, expand=True)
                elif pic_rot.lower() == "u":
                    pic_cur = pic_cur.rotate(angle=180, expand=True)
                else:
                    pic_cur = pic_cur.rotate(angle=270, expand=True)
                pic_cur.save("%s/%s" % (xdir, pic_fn))


if __name__ == "__main__":
    g = Gallery()

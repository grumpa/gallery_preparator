#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
An executing class for gallery preparator independent on user interface.
"""

import os
import os.path
from PIL import Image, ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True

description_template = """<?php
$gallery_name = "{name}";
$gallery_description = "{descr}";
$gallery_pic = "{gall_pic:05d}.jpg";
$pics[] = "";
?>
"""


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
        self.src_path = os.path.join(basedir_src, dir_src)
        self.basedir_dst = basedir_dst
        self.dir_dst = dir_dst
        self.dst_path = os.path.join(basedir_dst, dir_dst)
        self.name = name
        self.description = description
        self.pic_size = int(pic_size)
        self.thm_size = int(thm_size)
        self.num_from = int(num_from)

    def make_directories(self):
        """Make directories for picture gallery and thumbs"""
        os.mkdir(self.dst_path)
        os.mkdir(os.path.join(self.dst_path, "thumbs"))

    def make_description_file(self):
        """Make file describing gallery"""
        df = open("{}/description.inc".format(self.dst_path), 'w')
        df.write(description_template.format(name=self.name, descr=self.description, gall_pic=self.num_from))
        df.close()

    def convert_pictures(self):
        """Reads pictures from source directory and makes required ones into destination."""
        number = self.num_from
        for item in os.listdir(self.src_path):
            try:
                im = Image.open(os.path.join(self.src_path, item))
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
            im.save("{}/{:05d}.jpg".format(self.dst_path, number))
            imt.save("{}/thumbs/{:05d}.jpg".format(self.dst_path, number))
            number = number + 1

    @staticmethod
    def rotate_pics(pdir, pics):
        """
        Rotate pictures pics in directory pidr
        pics - string as "6l 27-45r 18u" i.e.:
                - pic 00006.jpg rotate left
                - pics from 00027.jpg to 00045.jpg rotate right
                - pic 00018.jpg rotate 180
        returns set with numbers of not found pictures
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
        not_found_pics = set()
        for xdir in (pdir, pdir+"/thumbs"):
            for xpic in pic_list:
                pic_no = xpic[:-1]
                pic_rot = xpic[-1:]
                pic_fn = "%05d.jpg" % int(pic_no)
                try:
                    pic_cur = Image.open("%s/%s" % (xdir, pic_fn))
                except FileNotFoundError:
                    not_found_pics.add(pic_no)
                    continue
                if pic_rot.lower() == "l":
                    pic_cur = pic_cur.rotate(angle=90, expand=True)
                elif pic_rot.lower() == "u":
                    pic_cur = pic_cur.rotate(angle=180, expand=True)
                else:
                    pic_cur = pic_cur.rotate(angle=270, expand=True)
                pic_cur.save("%s/%s" % (xdir, pic_fn))
        return not_found_pics


if __name__ == "__main__":
    g = Gallery()

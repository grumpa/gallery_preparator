#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os.path
import gettext
import locale
import os.path
from gallery_preparator.core import Gallery


locale.setlocale(locale.LC_ALL, '')
_ = gettext.gettext
gettext.bindtextdomain('messages', 'gallery_preparator/locales')
# constants for local yes/no
LOC_Y = locale.nl_langinfo(locale.YESEXPR)[2].lower()
LOC_N = locale.nl_langinfo(locale.NOEXPR)[2].lower()
# strings for local question [Y/n], [y/N]
YN_Y = ' [{0}/{1}]? '.format(LOC_Y.upper(), LOC_N)
YN_N = ' [{0}/{1}]? '.format(LOC_Y, LOC_N.upper())

# maximum value for start numbering pics in a gallery
MAX_NUM_FROM = 99000


class UI(Gallery):

    def galeries(self):
        """Main loop for galeries"""
        cont = True
        while cont:
            self.console_ask_gallery()
            questext = _('Rotate pictures') + YN_N
            ret = input(questext)
            if ret.lower() == LOC_Y:
                self.console_rotate_pics(pdir=os.path.join(self.basedir_dst, self.dir_dst))
            questext = _('Another gallery') + YN_Y
            ret = input(questext)
            if ret.lower() != LOC_N:
                self.dir_src = ''
                self.dir_dst = ''
                self.name = ''
                self.description = ''
                self.num_from = 1
                cont = True
            else:
                cont = False

    def console_ask_gallery(self):
        """Loop for one gallery"""
        ok = False
        while not ok:
            # Acquire items from console
            self.console_ask_items()
            # List everything and ask for confirmation
            questext = _('Recapitulation')
            print(("\n{0}:\n".format(questext)))
            self.console_items_list()
            questext = _('Is everything O.K.') + YN_N
            ret = input(questext)
            if ret.lower() == LOC_Y:
                ok = True
            else:
                print((_('Check questions again and make corrections.')))
        self.make_directories()
        self.make_description_file()
        self.convert_pictures()

    def console_ask_items(self):
        """Ask parameters of source, destination, name and dimensions."""
        ok = False
        while not ok:
            basedir_src = input(_("Source base directory with picture directory(s)")+" [{0}]: ".format(self.basedir_src))
            if basedir_src != "":
                self.basedir_src = os.path.normpath(basedir_src)
            if not os.path.isdir(self.basedir_src):
                print((_("Source base directory doesn't exists") + " ({0}).".format(self.basedir_src)))
                self.basedir_src = ""
                ok = False
            else:
                ok = True
        ok = False
        while not ok:
            questext = _('Source subdirectory with pictures')
            dir_src = input("{0} [{1}]: ".format(questext, self.dir_src))
            if dir_src != "":
                self.dir_src = os.path.normpath(dir_src)
            if not os.path.isdir(os.path.join(self.basedir_src, self.dir_src)):
                print((_("Subdirectory doesn't exist") + " ({0}).".format(self.dir_src)))
                self.dir_src = ""
                ok = False
            else:
                ok = True
        ok = False
        while not ok:
            questext = _('Destination base directory for galleries')
            basedir_dst = input("{0} [{1}]: ".format(questext, self.basedir_dst))
            if basedir_dst != "":
                self.basedir_dst = os.path.normpath(basedir_dst)
            if not os.path.isdir(self.basedir_dst):
                print((_("Destination base directory doesn't exist") + " ({0}).".format(self.basedir_dst)))
                self.basedir_dst = ""
                ok = False
            else:
                ok = True
        ok = False
        while not ok:
            questext = _('Destination subdirectory for the gallery')
            dir_dst = input("{0} [{1}]: ".format(questext, self.dir_dst))
            if dir_dst != "":
                self.dir_dst = os.path.normpath(dir_dst)
            if os.path.exists(os.path.join(self.basedir_dst, self.dir_dst)):
                print((_("Destination subdirectory exists already. Provide different name or delete the directory.")))
                self.dir_dst = ""
                ok = False
            else:
                ok = True
        ok = False
        while not ok:
            questext = _('Name for gallery (fee text)')
            name = input("{0} [{1}] ".format(questext, self.name))
            if name + self.name == "": 
                print((_("Name is mandatory.")))
                continue
            if name != "":
                self.name = name
            ok = True
        if self.description != "":
            nl = "\n"
        else:
            nl = ""
        questext = _('Description (free text include html tags) - all in one line. Write "x" for erase existing text.')
        description = input("{0}:\n{1}{2}".format(questext, self.description, nl))
        if description != "":
            if description == "x":
                self.description = ""
            else:
                self.description = description
        questext = _('Required size for picture (dimension of longer side)')
        pic_size = input("{0} [{1}]: ".format(questext, self.pic_size))
        if pic_size != "":
            self.pic_size = int(pic_size)
        questext = _('Required size for thumbnail (dimension of longer side)')
        thm_size = input("{0} [{1}]: ".format(questext, self.thm_size))
        if thm_size != "":
            self.thm_size = int(thm_size)
        num_from = input(_("Number picures from") + " [{0}] ".format(self.num_from))
        try:
            num_from = int(num_from)
        except ValueError:
            num_from = self.num_from
        if 0 < num_from <= MAX_NUM_FROM:
            self.num_from = num_from

    def console_items_list(self):
        """List parameters of the gallery."""
        print((_("Source directory") + ": {0}".format(os.path.join(self.basedir_src, self.dir_src))))
        print((_("Destination directory") + ": {0}".format(os.path.join(self.basedir_dst, self.dir_dst))))
        print((_("Name for the gallery") + ": {0}".format(self.name)))
        print((_("Gallery description") + ": {0}".format(self.description)))
        print((_("Picture size") + ": {0}".format(self.pic_size)))
        print((_("Thumbnail size") + ": {0}".format(self.thm_size)))
        print((_("Number picures from") + ": {0}".format(self.num_from)))

    def console_rotate_pics(self, pdir=None):
        """Console ui wrapper for rotate_pics method."""
        example = " (" + _("example") + ": 6l 12r 16-23l 14r 35u)"
        repeat = True
        while repeat:
            pics = None
            ok = False
            while not ok:
                questext = _('Rotate pictures in directory')
                ret = input(" {0} [{1}]: ".format(questext, pdir))
                if ret != "":
                    if not os.path.isdir(ret):
                        print((_("This is not a directory. Again please.")))
                        continue
                    pdir = ret
                question = _("Pictures numbers and direction of rotation")
                if pics:
                    question += " [{0}]: ".format(pics)
                else:
                    question += example + ": "
                ret = input(question)
                if ret:
                    pics = ret
                questext = _('Reassurance')
                print(("\n{0}\n".format(questext)))
                print((_("directory") + ": {0}".format(pdir)))
                print((_("pictures") + ": {0}".format(pics)))
                questext = _("O.K.") + YN_N
                ret = input(questext)
                if ret.lower() == LOC_Y:
                    ok = True
                    not_found_pics = self.rotate_pics(pdir, pics)
                    if len(not_found_pics) > 0:
                        print(_("These picture numbers were not found") + ": {0}".format(not_found_pics))
            ret = input(_("Rotation finished. Is rotation O.K.") + YN_Y)
            if ret.lower() != LOC_N:
                repeat = False


if __name__ == "__main__":
    g = UI()
    g.galeries()

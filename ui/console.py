#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import gettext
import locale

locale.setlocale(locale.LC_ALL, '')
_ = gettext.gettext
gettext.bindtextdomain('messages', 'locales')

from core import Gallery


class UI(Gallery):
    def __init__(self):
        Gallery.__init__(self)

    def galeries(self):
        """Main loop for galeries"""
        cont = True
        while cont:
            self.console_ask_gallery()
            questext = _('Rotate pictures? [y/N]')
            ret = raw_input("\n %s ? " % questext)
            if ret.lower() == "y":
                self.console_rotate_pics(pdir="%s/%s" % (self.basedir_dst, self.dir_dst))
            questext = _('Another gallery [Y/n]')
            ret = raw_input("\n%s ? " % questext)
            if ret.lower() in ("", "y"):
                self.dir_src = ''
                self.dir_dst = ''
                self.name = ''
                self.description = ''
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
            print("\n%s:\n" % questext)
            self.console_items_list()
            questext = _('Is everything O.K. [y/N]')
            ret = raw_input("%s ? " % questext)
            if ret.lower() == 'y':
                ok = True
            else:
                print(_('Check questions again and make corrections.'))
        self.make_directories()
        self.make_description_file()
        self.convert_pictures()

    def console_ask_items(self):
        """Ask parameters of source, destination, name and dimensions."""
        ok = False
        while not ok:
            basedir_src = raw_input(_("Source base directory with picture directory(s)")+" [%s]: " % self.basedir_src)
            if basedir_src != "":
                self.basedir_src = basedir_src
            if self.basedir_src[-1:] == "/":
                self.basedir_src = self.basedir_src[:-1]
            if not os.path.isdir(self.basedir_src):
                print(_("Source base directory %s doesn't exists.") % self.basedir_src)
                ok = False
            else:
                ok = True
        ok = False
        while not ok:
            questext = _('Source subdirectory with pictures')
            dir_src = raw_input("%s [%s]: " % (questext, self.dir_src))
            if dir_src != "":
                self.dir_src = dir_src
            if self.dir_src[-1:] == "/":
                self.dir_src = self.dir_src[:-1]
            if not os.path.isdir(self.basedir_src+"/"+self.dir_src):
                print(_("Subdirectory doesn't exist") % self.dir_src)
                ok = False
            else:
                ok = True
        ok = False
        while not ok:
            questext = _('Destination base directory for galleries')
            basedir_dst = raw_input("%s [%s]: " % (questext, self.basedir_dst))
            if basedir_dst != "":
                self.basedir_dst = basedir_dst
            if self.basedir_dst[-1:] == "/":
                self.basedir_dst = self.basedir_dst[:-1]
            if not os.path.isdir(self.basedir_dst):
                print(_("Destination base directory %s doesn't exist.") % self.basedir_dst)
                ok = False
            else:
                ok = True
        ok = False
        while not ok:
            questext = _('Destination subdirectory for the gallery')
            dir_dst = raw_input("%s [%s]: " % (questext, self.dir_dst))
            if dir_dst != "":
                self.dir_dst = dir_dst
            if self.dir_dst[-1:] == "/":
                self.dir_dst = self.dir_dst[:-1]
            if os.path.exists(self.basedir_dst+"/"+self.dir_dst):
                print(_("Destination subdirectory exists already. Provide different name or delete the directory."))
                ok = False
            else:
                ok = True
        ok = False
        while not ok:
            questext = _('Name for gallery (fee text)')
            name = raw_input("%s [%s] " % (questext, self.name))
            if name + self.name == "": 
                print(_("Name is mandatory."))
                continue
            if name != "":
                self.name = name
            ok = True
        if self.description != "":
            nl = "\n"
        else:
            nl = ""
        questext = _('Description (free text include html tags) - all in one line. Write "x" for erase existing text.')
        description = raw_input("%s:\n%s%s" % (questext, self.description, nl))
        if description != "":
            if description == "x":
                self.description = ""
            else:
                self.description = description
        questext = _('Required size for picture (dimension of longer side)')
        pic_size = raw_input("%s [%s]: " % (questext, self.pic_size))
        if pic_size != "":
            self.pic_size = int(pic_size)
        questext = _('Required size for thumbnail (dimension of longer side)')
        thm_size = raw_input("%s [%s]: " % (questext, self.thm_size))
        if thm_size != "":
            self.thm_size = int(thm_size)

    def console_items_list(self):
        """List parameters of the gallery."""
        print(_("Source directory") + ": %s/%s" % (self.basedir_src, self.dir_src))
        print(_("Destination directory") + ": %s/%s" % (self.basedir_dst, self.dir_dst))
        print(_("Name for the gallery") + ": %s" % self.name)
        print(_("Gallery description") + ": %s" % self.description)
        print(_("Picture size") + ": %d" % self.pic_size)
        print(_("Thumbnail size") + ": %d" % self.thm_size)

    def console_rotate_pics(self, pdir=None):
        """Console ui wrapper for rotate_pics method."""
        example = " (" + _("example") + ": 6l 12r 16-23l 14r 35u)"
        repeat = True
        while repeat:
            pics = None
            ok = False
            while not ok:
                questext = _('Rotate pictures in directory')
                ret = raw_input("%s [%s]: " % (questext, pdir))
                if ret != "":
                    pdir = ret
                question = _("Pictures numbers and direction of rotation")
                if pics:
                    question += " [%s]: " % pics
                else:
                    question += example + ": "
                pics = raw_input(question)
                questext = _('Reassurance')
                print("\n%s\n" % questext)
                print(_("directory") + ": %s" % pdir)
                print(_("pictures") + ": %s" % pics)
                questext = _("O.K. [y/N]")
                ret = raw_input("\n%s? " % questext)
                if ret.lower() == "y":
                    ok = True
                self.rotate_pics(pdir, pics)
            ret = raw_input(_("Rotation finished. Is rotation O.K. [Y/n] ?") + " ")
            if ret.lower() != "n":
                repeat = False

        
if __name__ == "__main__":
    g = UI()
    g.galeries()

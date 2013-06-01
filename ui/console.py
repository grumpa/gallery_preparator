#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import gettext
import locale

locale.setlocale(locale.LC_ALL,'')
_ = gettext.gettext
gettext.bindtextdomain('messages', 'locales')

from core import Gallery

class UI(Gallery):
    def __init__(self):
        Gallery.__init__(self)

    def galeries(self):
        "Main loop for galeries"
        cont = True
        while cont:
            self.console_ask_gallery()
            ret = raw_input("\n Rotovat obrázky? [a/N]: ")
            if ret.lower() == "a":
                self.console_rotate_pics(pdir="%s/%s" % (self.basedir_dst, self.dir_dst))
            ret = raw_input("\n Další galerii [A/n] ? ")
            if ret.lower() in ("", "a"):
                self.dir_src = ''
                self.dir_dst = ''
                self.name = ''
                self.description = ''
                cont = True
            else:
                cont = False

    def console_ask_gallery(self):
        ok = False
        while not ok:
            # Acquire items from console
            self.console_ask_items()
            # List everything and ask for confirmation
            print "\nRekapitulace:\n"
            self.console_items_list()
            ret = raw_input("Je vše v pořádku [a/N]? ")
            if ret.lower() == 'a':
                ok = True
            else:
                print "Projeď znova odpovědi a chybné oprav."
        self.make_directories()
        self.make_description_file()
        self.convert_pictures()

    def console_ask_items(self):
        ok = False
        while not ok:
            #basedir_src = raw_input("Zdrojový adresář s galeriemi [%s]: " % self.basedir_src)
            basedir_src = raw_input(_("Source directory with pictures")+" [%s]: " % self.basedir_src)
            if basedir_src != "":
                self.basedir_src = basedir_src
            if self.basedir_src[-1:] == "/":
                self.basedir_src = self.basedir_src[:-1]
            if not os.path.isdir(self.basedir_src):
                print "Zdrojový adresář %s neexistuje" % self.basedir_src
                ok = False
            else:
                ok = True
        ok = False
        while not ok:
            dir_src = raw_input("Podadresář galerie [%s]: " % self.dir_src)
            if dir_src != "":
                self.dir_src = dir_src
            if self.dir_src[-1:] == "/":
                self.dir_src = self.dir_src[:-1]
            if not os.path.isdir(self.basedir_src+"/"+self.dir_src):
                print "Podadresář %s neexistuje" % self.dir_src
                ok = False
            else:
                ok = True
        ok = False
        while not ok:
            basedir_dst = raw_input("Cílový adresář pro galerie [%s]: " % self.basedir_dst)
            if basedir_dst != "":
                self.basedir_dst = basedir_dst
            if self.basedir_dst[-1:] == "/":
                self.basedir_dst = self.basedir_dst[:-1]
            if not os.path.isdir(self.basedir_dst):
                print "Cílový adresář %s neexistuje" % self.basedir_dst
                ok = False
            else:
                ok = True
        ok = False
        while not ok:
            dir_dst = raw_input("Podadresář galerie [%s]: " % self.dir_dst)
            if dir_dst != "":
                self.dir_dst = dir_dst
            if self.dir_dst[-1:] == "/":
                self.dir_dst = self.dir_dst[:-1]
            if os.path.exists(self.basedir_dst+"/"+self.dir_dst):
                print "Cílový adresář již existuje. Zadej jiný název, nebo ho teď smaž."
                ok = False
            else:
                ok = True
        ok = False
        while not ok:
            name = raw_input("Název galerie (volný text) [%s] " % self.name)
            if name + self.name == "": 
                print ("Název je nutné zadat.")
                continue
            if name != "":
                self.name = name
            ok = True
        if self.description != "":
            nl="\n"
        else:
            nl=""
        description = raw_input("Popis (volný text včetně případných html značek) v jednom řádku (x - vymaže popis):\n%s%s" % (self.description, nl))
        if description != "":
            if description == "x":
                self.description = ""
            else:
                self.description = description
        pic_size = raw_input("Požadovaná velikost obrázku (délka delší strany) [%s]: " % self.pic_size)
        if pic_size != "":
            self.pic_size = int(pic_size)
        thm_size = raw_input("Požadovaná velikost náhledu (délka delší strany) [%s]: " % self.thm_size)
        if thm_size != "":
            self.thm_size = int(thm_size)

    def console_items_list(self):
        print "Zdrojový adresář: %s/%s" % (self.basedir_src, self.dir_src)
        print "Cílový adresář: %s/%s" % (self.basedir_dst, self.dir_dst)
        print "Jméno galerie: %s" % self.name
        print "Popis galerie: %s" % self.description
        print "Velikost obrázku: %d" % self.pic_size
        print "Velikost náhledu: %d" % self.thm_size

    def console_rotate_pics(self, pdir=None):
        "Console ui wrapper for rotate_pics method."
        example = "(př 6l 12p 16-23l 14r 35u)"
        pics = None
        ok = False
        while not ok:
            ret = raw_input("Rotovat v adresáři [%s]: " % pdir)
            if ret != "":
                pdir = ret
            question = "Čísla fotek a směr"
            if pics:
                question += " [%s]: " % pics
            else:
                question += " (př 6l 12p 16-23l 14r 35u): "
            pics = raw_input(question)
            print("\nUjištění\n")
            print("adresář: %s" % pdir)
            print("fotky: %s" % pics)
            ret = raw_input("\nO.K. [a/N]? ")
            if ret.lower() == "a":
                ok = True
        self.rotate_pics(pdir,pics)

        
if __name__ == "__main__":
    g = UI()
    g.galeries()


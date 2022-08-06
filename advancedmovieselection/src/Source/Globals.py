# -*- coding: utf-8 -*-
#  Advanced Movie Selection for Dreambox-Enigma2
#
#  The plugin is developed on the basis from a lot of single plugins (thx for the code @ all)
#  Coded by JackDaniel and cmikula (c)2012
#  Support: www.i-have-a-dreambox.com
#
#  This plugin is licensed under the Creative Commons
#  Attribution-NonCommercial-ShareAlike 3.0 Unported
#  License. To view a copy of this license, visit
#  http://creativecommons.org/licenses/by-nc-sa/3.0/ or send a letter to Creative
#  Commons, 559 Nathan Abbott Way, Stanford, California 94305, USA.
#
#  Alternatively, this plugin may be distributed and executed on hardware which
#  is licensed by Dream Multimedia GmbH.
#
#  This plugin is NOT free software. It is open source, you are allowed to
#  modify it (if you keep the license), but it may not be commercially
#  distributed other than under the conditions noted above.
#
from enigma import getDesktop
from Tools.Directories import isPluginInstalled


def printStackTrace():
    import sys
    import traceback
    print("--- [AdvancedMovieSelection] STACK TRACE ---")
    traceback.print_exc(file=sys.stdout)
    print('-' * 50)


class SkinResolutionHelper():
    def __init__(self, alternativeSkinName=None):
        if alternativeSkinName:
            self.skinName = alternativeSkinName
        else:
            self.skinName = SkinTools.appendResolution(self.__class__.__name__)


class SkinTools():
    DESKTOP_WIDTH_SD = 720
    DESKTOP_WIDTH_XD = 1024
    DESKTOP_WIDTH_HD = 1280

    def __init__(self):
        pass

    @staticmethod
    def appendResolution(skinName):
        dw = SkinTools.getDesktopWidth()
        if dw == SkinTools.DESKTOP_WIDTH_XD:
            return skinName + "XD"
        elif dw == SkinTools.DESKTOP_WIDTH_HD:
            return skinName + "HD"
        elif dw == SkinTools.DESKTOP_WIDTH_SD:
            return skinName + "SD"
        return skinName

    @staticmethod
    def getDesktopWidth():
        try:
            desktopWidth = getDesktop(0).size().width()
        except:
            desktopWidth = SkinTools.DESKTOP_WIDTH_SD
        return desktopWidth


class Installed:
    def __init__(self):
        self.BludiscPlayer = isPluginInstalled("BludiscPlayer")
        self.DVDPlayer = isPluginInstalled("DVDPlayer")
        self.TMDb = isPluginInstalled("TMDb")
        self.IMDb = isPluginInstalled("IMDb")
        self.OFDb = isPluginInstalled("OFDb")
        self.TheTVDB = isPluginInstalled("TheTVDB")
        self.AdvancedProgramGuide = isPluginInstalled("AdvancedProgramGuide")
        self.MerlinEPG = isPluginInstalled("MerlinEPG")
        self.MerlinEPGCenter = isPluginInstalled("MerlinEPGCenter")
        self.CoolTVGuide = isPluginInstalled("CoolTVGuide")
        self.YTTrailer = isPluginInstalled("YTTrailer")
        self.pipzap = isPluginInstalled("pipzap")


pluginPresent = Installed()

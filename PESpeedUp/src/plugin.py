# -*- coding: utf-8 -*-
# for localized messages
from . import _
from enigma import getDesktop
from Screens.Screen import Screen
from Screens.MessageBox import MessageBox
from Screens.Standby import TryQuitMainloop
from Components.ActionMap import ActionMap
from Components.Label import Label
from Plugins.Plugin import PluginDescriptor
from Components.ConfigList import ConfigListScreen
from Components.config import getConfigListEntry, config, ConfigSelection, NoSave
from Components.Sources.List import List
from Tools.Directories import pathExists, fileExists, resolveFilename, SCOPE_PLUGINS
from Screens.Console import Console

sz_w = getDesktop(0).size().width()


class PESpeedUp(Screen, ConfigListScreen):
    if sz_w == 1280:
        skin = '''
		<screen position="center,center" size="902,570" title="PE Speed Up" backgroundColor="#16000000" flags="wfNoBorder">
			<widget name="lab1" position="10,10" size="882,60" font="Regular;20" verticalAlignment="top" transparent="1" backgroundColor="#16000000"/>
			<widget name="config" position="30,70" size="840,450" scrollbarMode="showOnDemand" backgroundColor="#16000000"/>
			<eLabel backgroundColor="#00ff2525" name="red" position="200,565" size="140,5" />
			<eLabel backgroundColor="#00389416" name="green" position="550,565" size="140,5" />
			<widget name="key_red" position="200,528" zPosition="1" size="140,40" font="Regular;20" horizontalAlignment="center" verticalAlignment="center" backgroundColor="#16000000" transparent="1"/>
			<widget name="key_green" position="550,528" zPosition="1" size="140,40" font="Regular;20" horizontalAlignment="center" verticalAlignment="center" backgroundColor="#16000000" transparent="1"/>
		</screen>
	'''
    else:
        skin = '''
		<screen position="center,center" size="1376,898" title="PE Speed Up" backgroundColor="#16000000" flags="wfNoBorder">
			<widget name="lab1" position="8,10" size="1359,80" font="Regular;30" verticalAlignment="top" transparent="1" backgroundColor="#16000000"/>
			<widget name="config" position="28,95" size="1321,745" font="Regular;35" itemHeight="50" scrollbarMode="showOnDemand" backgroundColor="#16000000"/>
			<widget name="key_red" position="365,845" zPosition="1" size="204,40" font="Regular;32" horizontalAlignment="center" verticalAlignment="center" backgroundColor="#16000000" transparent="1"/>
			<widget name="key_green" position="810,845" zPosition="1" size="204,40" font="Regular;32" horizontalAlignment="center" verticalAlignment="center" backgroundColor="#16000000" transparent="1"/>
			<eLabel backgroundColor="#00ff2525" name="red" position="365,885" size="204,10" />
			<eLabel backgroundColor="#00389416" name="green" position="810,885" size="204,10" />
		</screen>
	'''

    def __init__(self, session):
        Screen.__init__(self, session)
        self.list = []
        ConfigListScreen.__init__(self, self.list)
        self['lab1'] = Label(_("Remove all the packages you don't need.\nThis will speed up the performance."))
        self['key_red'] = Label(_("Cancel"))
        self['key_green'] = Label(_("Save"))
        self['actions'] = ActionMap(['WizardActions', 'ColorActions', 'OkCancelActions'], {'green': self.saveList,
         'red': self.cancel,
         'stop': self.cancel,
         'cancel': self.cancel,
         'back': self.cancel})
        self.packagelist = []
        self.packagelist.append(['                                        Binaries', 'astra-sm autofs cifs-utils cronie curl fuse-exfat minidlna nfs-utils ntfs-3g ntp openssh-sftp-server openvision-bootlogo enigma2-plugin-bootvideo-blackwhite-720p enigma2-plugin-bootvideo-color-720p enigma2-plugin-bootvideo-glass-720p enigma2-plugin-bootvideo-marvel-720p enigma2-plugin-bootvideo-more-720p enigma2-plugin-bootvideo-nosound-720p enigma2-plugin-bootvideo-oldtv-720p enigma2-plugin-bootvideo-santa-720p enigma2-plugin-bootvideo-space-720p samba-base shellinabox streamproxy ushare usb-modeswitch usb-modeswitch-data'])
        if fileExists('/usr/bin/astra'):
            self.packagelist.append(['astra-sm', 'astra-sm'])
        if fileExists('/usr/sbin/automount'):
            self.packagelist.append(['autofs', 'autofs'])
        if fileExists('/usr/sbin/mount.cifs'):
            self.packagelist.append(['cifs-utils', 'cifs-utils'])
        if fileExists('/usr/sbin/anacron'):
            self.packagelist.append(['cronie', 'cronie'])
        if fileExists('/usr/bin/curl'):
            self.packagelist.append(['curl', 'curl'])
        if fileExists('/sbin/mount.exfat-fuse'):
            self.packagelist.append(['fuse-exfat', 'fuse-exfat'])
        if fileExists('/usr/sbin/minidlnad'):
            self.packagelist.append(['minidlna', 'minidlna'])
        if fileExists('/usr/sbin/nfsconf'):
            self.packagelist.append(['nfs-utils', 'nfs-utils'])
        if fileExists('/usr/bin/ntfs-3g'):
            self.packagelist.append(['ntfs-3g', 'ntfs-3g'])
        if fileExists('/usr/sbin/ntpd.ntp'):
            self.packagelist.append(['ntp', 'ntp'])
        if fileExists('/usr/libexec/sftp-server'):
            self.packagelist.append(['openssh-sftp-server', 'openssh-sftp-server'])
        if fileExists('/usr/share/bootlogo.mvi'):
            self.packagelist.append(['openvision-bootlogo', 'openvision-bootlogo'])
        if fileExists('/usr/share/bootlogo.mp4'):
            self.packagelist.append(['openvision-bootvideo', 'enigma2-plugin-bootvideo-blackwhite-720p enigma2-plugin-bootvideo-color-720p enigma2-plugin-bootvideo-glass-720p enigma2-plugin-bootvideo-marvel-720p enigma2-plugin-bootvideo-more-720p enigma2-plugin-bootvideo-nosound-720p enigma2-plugin-bootvideo-oldtv-720p enigma2-plugin-bootvideo-santa-720p enigma2-plugin-bootvideo-space-720p'])
        if fileExists('/usr/sbin/smbd'):
            self.packagelist.append(['samba-base', 'samba-base'])
        if fileExists('/usr/bin/shellinaboxd'):
            self.packagelist.append(['shellinabox', 'shellinabox'])
        if fileExists('/usr/bin/streamproxy'):
            self.packagelist.append(['streamproxy', 'streamproxy'])
        if fileExists('/usr/sbin/usb_modeswitch'):
            self.packagelist.append(['usb-modeswitch', 'usb-modeswitch usb-modeswitch-data'])
        if fileExists('/usr/bin/ushare'):
            self.packagelist.append(['ushare', 'ushare'])
        self.packagelist.append(['                                        Cams', 'enigma2-plugin-softcams-oscam enigma2-plugin-softcams-oscam-emu enigma2-plugin-softcams-oscam-smod enigma2-plugin-softcams-ncam'])
        if fileExists('/usr/bin/oscam'):
            self.packagelist.append(['OSCam', 'enigma2-plugin-softcams-oscam'])
        if fileExists('/usr/bin/oscam-emu'):
            self.packagelist.append(['OSCam-Emu', 'enigma2-plugin-softcams-oscam-emu'])
        if fileExists('/usr/bin/oscam-smod'):
            self.packagelist.append(['OSCam-SMod', 'enigma2-plugin-softcams-oscam-smod'])
        if fileExists('/usr/bin/ncam'):
            self.packagelist.append(['NCam', 'enigma2-plugin-softcams-ncam'])
        self.packagelist.append(['                                        Frequency', 'frequency-xml-list-atsc frequency-xml-list-cables frequency-xml-list-satellites frequency-xml-list-satellites-america frequency-xml-list-satellites-asia frequency-xml-list-satellites-atlantic frequency-xml-list-satellites-europe frequency-xml-list-terrestrial frequency-xml-list-unicable'])
        if fileExists('/etc/tuxbox/atsc.xml'):
            self.packagelist.append(['ATSC', 'frequency-xml-list-atsc'])
        if fileExists('/etc/tuxbox/cables.xml'):
            self.packagelist.append(['Cables', 'frequency-xml-list-cables'])
        if fileExists('/etc/tuxbox/satellites.xml'):
            self.packagelist.append(['Satellites', 'frequency-xml-list-satellites'])
        if fileExists('/etc/tuxbox/satellites-america.xml'):
            self.packagelist.append(['Satellites-America', 'frequency-xml-list-satellites-america'])
        if fileExists('/etc/tuxbox/satellites-asia.xml'):
            self.packagelist.append(['Satellites-Asia', 'frequency-xml-list-satellites-asia'])
        if fileExists('/etc/tuxbox/satellites-atlantic.xml'):
            self.packagelist.append(['Satellites-Atlantic', 'frequency-xml-list-satellites-atlantic'])
        if fileExists('/etc/tuxbox/satellites-europe.xml'):
            self.packagelist.append(['Satellites-Europe', 'frequency-xml-list-satellites-europe'])
        if fileExists('/etc/tuxbox/terrestrial.xml'):
            self.packagelist.append(['Terrestrial', 'frequency-xml-list-terrestrial'])
        if fileExists('/usr/share/enigma2/unicable.xml'):
            self.packagelist.append(['Unicable', 'frequency-xml-list-unicable'])
        self.packagelist.append(['                                        Plugins (Extensions)', 'enigma2-plugin-extensions-audiosync enigma2-plugin-extensions-autobackup enigma2-plugin-extensions-autotimer enigma2-plugin-extensions-backupsuite enigma2-plugin-extensions-btdevicesmanager enigma2-plugin-extensions-cacheflush enigma2-plugin-extensions-cdinfo enigma2-plugin-extensions-cutlisteditor enigma2-plugin-extensions-dlnabrowser enigma2-plugin-extensions-dlnaserver enigma2-plugin-extensions-dreamirc enigma2-plugin-extensions-dvdplayer enigma2-plugin-extensions-epgimport enigma2-plugin-extensions-epgrefresh enigma2-plugin-extensions-filecommander enigma2-plugin-extensions-foreca enigma2-plugin-extensions-gbipboxclient enigma2-plugin-extensions-graphmultiepg enigma2-plugin-extensions-grautec enigma2-plugin-extensions-hbbtv enigma2-plugin-extensions-historyzapselector enigma2-plugin-extensions-internetspeedtest enigma2-plugin-extensions-iptvplayer enigma2-plugin-extensions-keyadder enigma2-plugin-extensions-lcd4linux enigma2-plugin-extensions-modem enigma2-plugin-extensions-moviecut enigma2-plugin-extensions-openmultiboot openmultiboot enigma2-plugin-extensions-openwebif-themes enigma2-plugin-extensions-openwebif-vxg enigma2-plugin-extensions-persianpalace enigma2-plugin-extensions-pluginskinmover enigma2-plugin-extensions-rcuselect enigma2-plugin-extensions-sh4multiboot enigma2-plugin-extensions-tmbd enigma2-plugin-extensions-tunerserver enigma2-plugin-extensions-vlcplayer enigma2-plugin-extensions-weatherplugin enigma2-plugin-extensions-xmodem enigma2-plugin-extensions-xtraevent'])
        if pathExists(resolveFilename(SCOPE_PLUGINS, 'Extensions/AudioSync')):
            self.packagelist.append(['AudioSync', 'enigma2-plugin-extensions-audiosync'])
        if pathExists(resolveFilename(SCOPE_PLUGINS, 'Extensions/AutoBackup')):
            self.packagelist.append(['AutoBackup', 'enigma2-plugin-extensions-autobackup'])
        if pathExists(resolveFilename(SCOPE_PLUGINS, 'Extensions/AutoTimer')):
            self.packagelist.append(['AutoTimer', 'enigma2-plugin-extensions-autotimer'])
        if pathExists(resolveFilename(SCOPE_PLUGINS, 'Extensions/BackupSuite')):
            self.packagelist.append(['BackupSuite', 'enigma2-plugin-extensions-backupsuite'])
        if pathExists(resolveFilename(SCOPE_PLUGINS, 'Extensions/BTDevicesManager')):
            self.packagelist.append(['BTDevicesManager', 'enigma2-plugin-extensions-btdevicesmanager'])
        if pathExists(resolveFilename(SCOPE_PLUGINS, 'Extensions/CacheFlush')):
            self.packagelist.append(['CacheFlush', 'enigma2-plugin-extensions-cacheflush'])
        if pathExists(resolveFilename(SCOPE_PLUGINS, 'Extensions/CDInfo')):
            self.packagelist.append(['CDInfo', 'enigma2-plugin-extensions-cdinfo'])
        if pathExists(resolveFilename(SCOPE_PLUGINS, 'Extensions/CutListEditor')):
            self.packagelist.append(['CutListEditor', 'enigma2-plugin-extensions-cutlisteditor'])
        if pathExists(resolveFilename(SCOPE_PLUGINS, 'Extensions/DLNABrowser')):
            self.packagelist.append(['DLNABrowser', 'enigma2-plugin-extensions-dlnabrowser'])
        if pathExists(resolveFilename(SCOPE_PLUGINS, 'Extensions/DLNAServer')):
            self.packagelist.append(['DLNAServer', 'enigma2-plugin-extensions-dlnaserver'])
        if pathExists(resolveFilename(SCOPE_PLUGINS, 'Extensions/dreamIRC')):
            self.packagelist.append(['dreamIRC', 'enigma2-plugin-extensions-dreamirc'])
        if pathExists(resolveFilename(SCOPE_PLUGINS, 'Extensions/DVDPlayer')):
            self.packagelist.append(['DVDPlayer', 'enigma2-plugin-extensions-dvdplayer'])
        if pathExists(resolveFilename(SCOPE_PLUGINS, 'Extensions/EPGImport')):
            self.packagelist.append(['EPGImport', 'enigma2-plugin-extensions-epgimport'])
        if pathExists(resolveFilename(SCOPE_PLUGINS, 'Extensions/EPGRefresh')):
            self.packagelist.append(['EPGRefresh', 'enigma2-plugin-extensions-epgrefresh'])
        if pathExists(resolveFilename(SCOPE_PLUGINS, 'Extensions/FileCommander')):
            self.packagelist.append(['FileCommander', 'enigma2-plugin-extensions-filecommander'])
        if pathExists(resolveFilename(SCOPE_PLUGINS, 'Extensions/Foreca')):
            self.packagelist.append(['Foreca', 'enigma2-plugin-extensions-foreca'])
        if pathExists(resolveFilename(SCOPE_PLUGINS, 'Extensions/GBIpboxClient')):
            self.packagelist.append(['GBIpboxClient', 'enigma2-plugin-extensions-gbipboxclient'])
        if pathExists(resolveFilename(SCOPE_PLUGINS, 'Extensions/GraphMultiEPG')):
            self.packagelist.append(['GraphMultiEPG', 'enigma2-plugin-extensions-graphmultiepg'])
        if pathExists('/usr/bin/usbtftdisplay'):
            self.packagelist.append(['GrauTec', 'enigma2-plugin-extensions-grautec'])
        if pathExists(resolveFilename(SCOPE_PLUGINS, 'Extensions/HbbTV')):
            self.packagelist.append(['HbbTV', 'enigma2-plugin-extensions-hbbtv'])
        if pathExists(resolveFilename(SCOPE_PLUGINS, 'Extensions/HistoryZapSelector')):
            self.packagelist.append(['HistoryZapSelector', 'enigma2-plugin-extensions-historyzapselector'])
        if pathExists(resolveFilename(SCOPE_PLUGINS, 'Extensions/InternetSpeedTest')):
            self.packagelist.append(['InternetSpeedTest', 'enigma2-plugin-extensions-internetspeedtest'])
        if pathExists(resolveFilename(SCOPE_PLUGINS, 'Extensions/IPTVPlayer')):
            self.packagelist.append(['IPTVPlayer', 'enigma2-plugin-extensions-iptvplayer'])
        if pathExists(resolveFilename(SCOPE_PLUGINS, 'Extensions/KeyAdder')):
            self.packagelist.append(['KeyAdder', 'enigma2-plugin-extensions-keyadder'])
        if pathExists(resolveFilename(SCOPE_PLUGINS, 'Extensions/LCD4linux')):
            self.packagelist.append(['LCD4linux', 'enigma2-plugin-extensions-lcd4linux'])
        if pathExists(resolveFilename(SCOPE_PLUGINS, 'Extensions/Modem')):
            self.packagelist.append(['Modem', 'enigma2-plugin-extensions-modem'])
        if pathExists(resolveFilename(SCOPE_PLUGINS, 'Extensions/MovieCut')):
            self.packagelist.append(['MovieCut', 'enigma2-plugin-extensions-moviecut'])
        if pathExists(resolveFilename(SCOPE_PLUGINS, 'Extensions/OpenMultiboot')):
            self.packagelist.append(['OpenMultiboot', 'enigma2-plugin-extensions-openmultiboot openmultiboot'])
        if pathExists(resolveFilename(SCOPE_PLUGINS, 'Extensions/OpenWebif/public/themes')):
            self.packagelist.append(['Open WebIF themes', 'enigma2-plugin-extensions-openwebif-themes'])
        if pathExists(resolveFilename(SCOPE_PLUGINS, 'Extensions/OpenWebif/public/vxg')):
            self.packagelist.append(['Open WebIF vxg', 'enigma2-plugin-extensions-openwebif-vxg'])
        if pathExists(resolveFilename(SCOPE_PLUGINS, 'Extensions/PersianPalace')):
            self.packagelist.append(['PersianPalace', 'enigma2-plugin-extensions-persianpalace'])
        if pathExists(resolveFilename(SCOPE_PLUGINS, 'Extensions/PluginSkinMover')):
            self.packagelist.append(['PluginSkinMover', 'enigma2-plugin-extensions-pluginskinmover'])
        if pathExists(resolveFilename(SCOPE_PLUGINS, 'Extensions/RCUSelect')):
            self.packagelist.append(['RCUSelect', 'enigma2-plugin-extensions-rcuselect'])
        if pathExists(resolveFilename(SCOPE_PLUGINS, 'Extensions/SH4MultiBoot')):
            self.packagelist.append(['SH4MultiBoot', 'enigma2-plugin-extensions-sh4multiboot'])
        if pathExists(resolveFilename(SCOPE_PLUGINS, 'Extensions/TMBD')):
            self.packagelist.append(['TMBD', 'enigma2-plugin-extensions-tmbd'])
        if pathExists(resolveFilename(SCOPE_PLUGINS, 'Extensions/TunerServer')):
            self.packagelist.append(['TunerServer', 'enigma2-plugin-extensions-tunerserver'])
        if pathExists(resolveFilename(SCOPE_PLUGINS, 'Extensions/VlcPlayer')):
            self.packagelist.append(['VlcPlayer', 'enigma2-plugin-extensions-vlcplayer'])
        if pathExists(resolveFilename(SCOPE_PLUGINS, 'Extensions/WeatherPlugin')):
            self.packagelist.append(['WeatherPlugin', 'enigma2-plugin-extensions-weatherplugin'])
        if pathExists(resolveFilename(SCOPE_PLUGINS, 'Extensions/xModem')):
            self.packagelist.append(['xModem', 'enigma2-plugin-extensions-xmodem'])
        if pathExists(resolveFilename(SCOPE_PLUGINS, 'Extensions/xtraEvent')):
            self.packagelist.append(['xtraEvent', 'enigma2-plugin-extensions-xtraevent'])
        self.packagelist.append(['                                        Plugins (System)', 'enigma2-plugin-systemplugins-3dsettings enigma2-plugin-systemplugins-3gmodemmanager enigma2-plugin-systemplugins-animationsetup enigma2-plugin-systemplugins-autobouquetsmaker enigma2-plugin-systemplugins-fsblupdater enigma2-plugin-systemplugins-hdmicec enigma2-plugin-systemplugins-keymapmanager enigma2-plugin-systemplugins-mountmanager enigma2-plugin-systemplugins-multitranscodingsetup enigma2-plugin-systemplugins-osd3dsetup enigma2-plugin-systemplugins-osdpositionsetup enigma2-plugin-systemplugins-satipclient enigma2-plugin-systemplugins-serviceapp enigma2-plugin-systemplugins-setpasswd enigma2-plugin-systemplugins-sh4boostercontrol enigma2-plugin-systemplugins-sh4osdadjustment enigma2-plugin-systemplugins-sparkuniontunertype enigma2-plugin-systemplugins-systemtime enigma2-plugin-systemplugins-videoenhancement enigma2-plugin-systemplugins-transcodingsetup openvision-core-plugin enigma2-plugin-systemplugins-weathercomponenthandler enigma2-plugin-systemplugins-xmlupdate'])
        if pathExists(resolveFilename(SCOPE_PLUGINS, 'SystemPlugins/3DSettings')):
            self.packagelist.append(['3DSettings', 'enigma2-plugin-systemplugins-3dsettings'])
        if pathExists(resolveFilename(SCOPE_PLUGINS, 'SystemPlugins/3GModemManager')):
            self.packagelist.append(['3GModemManager', 'enigma2-plugin-systemplugins-3gmodemmanager'])
        if pathExists(resolveFilename(SCOPE_PLUGINS, 'SystemPlugins/AnimationSetup')):
            self.packagelist.append(['AnimationSetup', 'enigma2-plugin-systemplugins-animationsetup'])
        if pathExists(resolveFilename(SCOPE_PLUGINS, 'SystemPlugins/AutoBouquetsMaker')):
            self.packagelist.append(['AutoBouquetsMaker', 'enigma2-plugin-systemplugins-autobouquetsmaker'])
        if pathExists(resolveFilename(SCOPE_PLUGINS, 'SystemPlugins/FSBLUpdater')):
            self.packagelist.append(['FSBLUpdater', 'enigma2-plugin-systemplugins-fsblupdater'])
        if pathExists(resolveFilename(SCOPE_PLUGINS, 'SystemPlugins/HdmiCEC')):
            self.packagelist.append(['HdmiCEC', 'enigma2-plugin-systemplugins-hdmicec'])
        if pathExists(resolveFilename(SCOPE_PLUGINS, 'SystemPlugins/KeymapManager')):
            self.packagelist.append(['KeymapManager', 'enigma2-plugin-systemplugins-keymapmanager'])
        if pathExists(resolveFilename(SCOPE_PLUGINS, 'SystemPlugins/MountManager')):
            self.packagelist.append(['MountManager', 'enigma2-plugin-systemplugins-mountmanager'])
        if pathExists(resolveFilename(SCOPE_PLUGINS, 'SystemPlugins/MultiTransCodingSetup')):
            self.packagelist.append(['MultiTransCodingSetup', 'enigma2-plugin-systemplugins-multitranscodingsetup'])
        if pathExists(resolveFilename(SCOPE_PLUGINS, 'SystemPlugins/OSD3DSetup')):
            self.packagelist.append(['OSD3DSetup', 'enigma2-plugin-systemplugins-osd3dsetup'])
        if pathExists(resolveFilename(SCOPE_PLUGINS, 'SystemPlugins/OSDPositionSetup')):
            self.packagelist.append(['OSDPositionSetup', 'enigma2-plugin-systemplugins-osdpositionsetup'])
        if pathExists(resolveFilename(SCOPE_PLUGINS, 'SystemPlugins/SatipClient')):
            self.packagelist.append(['SatipClient', 'enigma2-plugin-systemplugins-satipclient'])
        if pathExists(resolveFilename(SCOPE_PLUGINS, 'SystemPlugins/ServiceApp')):
            self.packagelist.append(['ServiceApp', 'enigma2-plugin-systemplugins-serviceapp'])
        if pathExists(resolveFilename(SCOPE_PLUGINS, 'SystemPlugins/SetPasswd')):
            self.packagelist.append(['SetPasswd', 'enigma2-plugin-systemplugins-setpasswd'])
        if pathExists(resolveFilename(SCOPE_PLUGINS, 'SystemPlugins/SH4BoosterControl')):
            self.packagelist.append(['SH4BoosterControl', 'enigma2-plugin-systemplugins-sh4boostercontrol'])
        if pathExists(resolveFilename(SCOPE_PLUGINS, 'SystemPlugins/SH4OSDAdjustment')):
            self.packagelist.append(['SH4OSDAdjustment', 'enigma2-plugin-systemplugins-sh4osdadjustment'])
        if pathExists(resolveFilename(SCOPE_PLUGINS, 'SystemPlugins/SparkUnionTunerType')):
            self.packagelist.append(['SparkUnionTunerType', 'enigma2-plugin-systemplugins-sparkuniontunertype'])
        if pathExists(resolveFilename(SCOPE_PLUGINS, 'SystemPlugins/SystemTime')):
            self.packagelist.append(['SystemTime', 'enigma2-plugin-systemplugins-systemtime'])
        if pathExists(resolveFilename(SCOPE_PLUGINS, 'SystemPlugins/VideoEnhancement')):
            self.packagelist.append(['VideoEnhancement', 'enigma2-plugin-systemplugins-videoenhancement'])
        if pathExists(resolveFilename(SCOPE_PLUGINS, 'SystemPlugins/TransCodingSetup')):
            self.packagelist.append(['TransCodingSetup', 'enigma2-plugin-systemplugins-transcodingsetup'])
        if pathExists(resolveFilename(SCOPE_PLUGINS, 'SystemPlugins/Vision')):
            self.packagelist.append(['Vision', 'openvision-core-plugin'])
        if pathExists(resolveFilename(SCOPE_PLUGINS, 'SystemPlugins/WeatherComponentHandler')):
            self.packagelist.append(['WeatherComponentHandler', 'enigma2-plugin-systemplugins-weathercomponenthandler'])
        if pathExists(resolveFilename(SCOPE_PLUGINS, 'SystemPlugins/xmlUpdate')):
            self.packagelist.append(['xmlUpdate', 'enigma2-plugin-systemplugins-xmlupdate'])
        self.packagelist.append(['                                        Locales', 'enigma2-locale-ar enigma2-locale-bg enigma2-locale-ca enigma2-locale-cs enigma2-locale-da enigma2-locale-de enigma2-locale-el enigma2-locale-es enigma2-locale-et enigma2-locale-fa enigma2-locale-fi enigma2-locale-fr enigma2-locale-fy enigma2-locale-gl enigma2-locale-he enigma2-locale-hr enigma2-locale-hu enigma2-locale-id enigma2-locale-is enigma2-locale-it enigma2-locale-ku enigma2-locale-lt enigma2-locale-lv enigma2-locale-mk enigma2-locale-nb enigma2-locale-nl enigma2-locale-nn enigma2-locale-pl enigma2-locale-pt enigma2-locale-pt-br enigma2-locale-ro enigma2-locale-ru enigma2-locale-sk enigma2-locale-sl enigma2-locale-sr enigma2-locale-sv enigma2-locale-th enigma2-locale-tr enigma2-locale-uk enigma2-locale-vi enigma2-locale-zh-cn enigma2-locale-zh-hk'])
        if pathExists('/usr/share/enigma2/po/ar'):
            self.packagelist.append(['locale-ar', 'enigma2-locale-ar'])
        if pathExists('/usr/share/enigma2/po/bg'):
            self.packagelist.append(['locale-bg', 'enigma2-locale-bg'])
        if pathExists('/usr/share/enigma2/po/ca'):
            self.packagelist.append(['locale-ca', 'enigma2-locale-ca'])
        if pathExists('/usr/share/enigma2/po/cs'):
            self.packagelist.append(['locale-cs', 'enigma2-locale-cs'])
        if pathExists('/usr/share/enigma2/po/da'):
            self.packagelist.append(['locale-da', 'enigma2-locale-da'])
        if pathExists('/usr/share/enigma2/po/de'):
            self.packagelist.append(['locale-de', 'enigma2-locale-de'])
        if pathExists('/usr/share/enigma2/po/el'):
            self.packagelist.append(['locale-el', 'enigma2-locale-el'])
        if pathExists('/usr/share/enigma2/po/es'):
            self.packagelist.append(['locale-es', 'enigma2-locale-es'])
        if pathExists('/usr/share/enigma2/po/et'):
            self.packagelist.append(['locale-et', 'enigma2-locale-et'])
        if pathExists('/usr/share/enigma2/po/fa'):
            self.packagelist.append(['locale-fa', 'enigma2-locale-fa'])
        if pathExists('/usr/share/enigma2/po/fi'):
            self.packagelist.append(['locale-fi', 'enigma2-locale-fi'])
        if pathExists('/usr/share/enigma2/po/fr'):
            self.packagelist.append(['locale-fr', 'enigma2-locale-fr'])
        if pathExists('/usr/share/enigma2/po/fy'):
            self.packagelist.append(['locale-fy', 'enigma2-locale-fy'])
        if pathExists('/usr/share/enigma2/po/gl'):
            self.packagelist.append(['locale-gl', 'enigma2-locale-gl'])
        if pathExists('/usr/share/enigma2/po/he'):
            self.packagelist.append(['locale-he', 'enigma2-locale-he'])
        if pathExists('/usr/share/enigma2/po/hr'):
            self.packagelist.append(['locale-hr', 'enigma2-locale-hr'])
        if pathExists('/usr/share/enigma2/po/hu'):
            self.packagelist.append(['locale-hu', 'enigma2-locale-hu'])
        if pathExists('/usr/share/enigma2/po/id'):
            self.packagelist.append(['locale-id', 'enigma2-locale-id'])
        if pathExists('/usr/share/enigma2/po/is'):
            self.packagelist.append(['locale-is', 'enigma2-locale-is'])
        if pathExists('/usr/share/enigma2/po/it'):
            self.packagelist.append(['locale-it', 'enigma2-locale-it'])
        if pathExists('/usr/share/enigma2/po/ku'):
            self.packagelist.append(['locale-ku', 'enigma2-locale-ku'])
        if pathExists('/usr/share/enigma2/po/lt'):
            self.packagelist.append(['locale-lt', 'enigma2-locale-lt'])
        if pathExists('/usr/share/enigma2/po/lv'):
            self.packagelist.append(['locale-lv', 'enigma2-locale-lv'])
        if pathExists('/usr/share/enigma2/po/mk'):
            self.packagelist.append(['locale-mk', 'enigma2-locale-mk'])
        if pathExists('/usr/share/enigma2/po/nb'):
            self.packagelist.append(['locale-nb', 'enigma2-locale-nb'])
        if pathExists('/usr/share/enigma2/po/nl'):
            self.packagelist.append(['locale-nl', 'enigma2-locale-nl'])
        if pathExists('/usr/share/enigma2/po/nn'):
            self.packagelist.append(['locale-nn', 'enigma2-locale-nn'])
        if pathExists('/usr/share/enigma2/po/pl'):
            self.packagelist.append(['locale-pl', 'enigma2-locale-pl'])
        if pathExists('/usr/share/enigma2/po/pt'):
            self.packagelist.append(['locale-pt', 'enigma2-locale-pt'])
        if pathExists('/usr/share/enigma2/po/pt_BR'):
            self.packagelist.append(['locale-pt-br', 'enigma2-locale-pt-br'])
        if pathExists('/usr/share/enigma2/po/ro'):
            self.packagelist.append(['locale-ro', 'enigma2-locale-ro'])
        if pathExists('/usr/share/enigma2/po/ru'):
            self.packagelist.append(['locale-ru', 'enigma2-locale-ru'])
        if pathExists('/usr/share/enigma2/po/sk'):
            self.packagelist.append(['locale-sk', 'enigma2-locale-sk'])
        if pathExists('/usr/share/enigma2/po/sl'):
            self.packagelist.append(['locale-sl', 'enigma2-locale-sl'])
        if pathExists('/usr/share/enigma2/po/sr'):
            self.packagelist.append(['locale-sr', 'enigma2-locale-sr'])
        if pathExists('/usr/share/enigma2/po/sv'):
            self.packagelist.append(['locale-sv', 'enigma2-locale-sv'])
        if pathExists('/usr/share/enigma2/po/th'):
            self.packagelist.append(['locale-th', 'enigma2-locale-th'])
        if pathExists('/usr/share/enigma2/po/tr'):
            self.packagelist.append(['locale-tr', 'enigma2-locale-tr'])
        if pathExists('/usr/share/enigma2/po/uk'):
            self.packagelist.append(['locale-uk', 'enigma2-locale-uk'])
        if pathExists('/usr/share/enigma2/po/vi'):
            self.packagelist.append(['locale-vi', 'enigma2-locale-vi'])
        if pathExists('/usr/share/enigma2/po/zh_CN'):
            self.packagelist.append(['locale-zh-cn', 'enigma2-locale-zh-cn'])
        if pathExists('/usr/share/enigma2/po/zh_HK'):
            self.packagelist.append(['locale-zh-hk', 'enigma2-locale-zh-hk'])
        self.packagelist.append(['                                        Skins', 'enigma2-plugin-skins-iflatfhd enigma2-plugin-skins-octetfhd enigma2-plugin-skins-pli-hd'])
        if fileExists('/usr/share/enigma2/iFlatFHD/skin.xml'):
            self.packagelist.append(['iFlatFHD', 'enigma2-plugin-skins-iflatfhd'])
        if fileExists('/usr/share/enigma2/OctEtFHD/skin.xml'):
            self.packagelist.append(['OctEtFHD', 'enigma2-plugin-skins-octetfhd'])
        if fileExists('/usr/share/enigma2/PLi-HD/skin.xml'):
            self.packagelist.append(['PLi-HD', 'enigma2-plugin-skins-pli-hd'])
        self.updateList()

    def cancel(self):
        self.close()

    def updateList(self):
        self.list = []
        for package in self.packagelist:
            item = NoSave(ConfigSelection(default='Installed', choices=[("Installed", _("Installed")), ("Remove", _("Remove"))]))
            res = getConfigListEntry(package[0], item)
            self.list.append(res)
        self['config'].list = self.list
        self['config'].l.setList(self.list)

    def saveList(self):
        self.mycmdlist = []
        for x in self['config'].list:
            if x[1].value == 'Remove':
                cmd = self.removePackages(x[0])
                self.mycmdlist.append(cmd)
        if len(self.mycmdlist) > 0:
            self.session.open(Console, title=_("PE Speed Up is working, please wait..."), cmdlist=self.mycmdlist, finishedCallback=self.allDone)
        else:
            PESpeedUp.instance = self.session.open(TryQuitMainloop, 3)

    def removePackages(self, name):
        cmd = ''
        for package in self.packagelist:
            if package[0] == name:
                cmd = 'opkg remove %s' % package[1]
        return cmd

    def allDone(self):
        mybox = self.session.openWithCallback(self.RestartGUI, MessageBox, _("WARNING! If you choose a section the entire section will be removed!\nPackage(s) removed!\nYou could install it(them) again from online feeds.\nYour STB will be restarted!\nPress OK to continue."), MessageBox.TYPE_INFO)
        mybox.setTitle('Info')

    def RestartGUI(self, answer):
        self.session.open(TryQuitMainloop, 3)


def main(session, **kwargs):
    session.open(PESpeedUp)


def Plugins(**kwargs):
    return PluginDescriptor(name=_("PE Speed Up"), description=_("Special version for Open Vision"), where=[PluginDescriptor.WHERE_EXTENSIONSMENU, PluginDescriptor.WHERE_PLUGINMENU], icon='pespeedup.png', fnc=main)

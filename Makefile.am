ACLOCAL_AMFLAGS = -I m4

SUBDIRS = \
	advancedmovieselection \
	advhdmi \
	aihdcontroler \
	antiscrollbar \
	ardmediathek \
	aspectratioswitch \
	audiorestart \
	audiosync \
	automaticcleanup \
	automaticvolumeadjustment \
	autoresolution \
	autotimerpli \
	babelzapper \
	birthdayreminder \
	bmediacenter \
	bonjour \
	cdinfo \
	channelselectionshorttitle \
	curlytx \
	dreamexplorer \
	dreamirc \
	dreammediathek \
	dvdbackup \
	easyinfo \
	easymedia \
	ecasa \
	eibox \
	emailclient \
	emission \
	eparted \
	epgrefresh \
	epgsearchpli \
	esame \
	eventlist \
	eventposition \
	fancontrol2 \
	filebrowser \
	flashexpander \
	fritzcall \
	fstabeditor \
	ftpbrowser \
	googlemaps \
	growlee \
	imdb \
	infobartunerstate \
	kiddytimer \
	letterbox \
	logomanager \
	mediadownloader \
	menusort \
	merlinepg \
	merlinepgcenter \
	merlinmusicplayer \
	mosaic \
	movielistpreview \
	movieretitle \
	moviesearch \
	movietagger \
	mphelp \
	multirc \
	mytube \
	ncidclient \
	netcaster \
	netzkino \
	ofdb \
	orfat \
	orfteletext \
	partnerbox \
	permanentclock \
	PESpeedUp \
	pipservicerelation \
	pluginhider \
	pluginsort \
	podcast \
	primetimemanager \
	pushservice \
	quickbutton \
	reconstructapsc \
	recordinfobar \
	reftopiconname \
	remotetimer \
	schiffe \
	seriesplugin \
	Series2Folder \
	setpasswd \
	shoutcast \
	showclock \
	simplerss \
	startuptostandby \
	subsdownloader2 \
	sudoku \
	svdrp \
	systemtime \
	tageditor \
	teletext \
	tetris \
	toolkit \
	transmission \
	tvcharts \
	unwetterinfo \
	valixdcontrol \
	vfdcontrol \
	videocolorspace \
	vierg \
	vlcplayer \
	weathercomponent \
	weathercomponenthandler \
	weatherplugin \
	webcamviewer \
	werbezapper \
	yttrailer \
	zaphistorybrowser \
	zapstatistic \
	zdfmediathek


metadir = $(datadir)/meta
meta_DATA = index-enigma2-plugins.xml
CLEANFILES = index-enigma2-plugins.xml

index-enigma2-plugins.xml: $(top_srcdir)/genmetaindex.py $(top_srcdir)/*/meta/plugin_*.xml
	$(AM_V_GEN)$(PYTHON) $^ > $@

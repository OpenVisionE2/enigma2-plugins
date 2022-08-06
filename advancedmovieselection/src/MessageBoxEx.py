# -*- coding: utf-8 -*-
from Screens.MessageBox import MessageBox


class MessageBox(MessageBox):
    def cancel(self):
        self.close(None)

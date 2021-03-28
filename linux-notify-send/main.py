

#!/usr/bin/env python
#-*- coding: utf-8 -*-

import subprocess

def sendmessage(message):
    subprocess.Popen(['notify-send', message])


sendmessage("bedir knk ubuntuya bildirim gönderebildiğini biliyormuydun")

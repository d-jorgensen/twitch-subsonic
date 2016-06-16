#!/usr/bin/env python
# encoding=utf8
from __future__ import unicode_literals

from urllib.request import urlopen
import sys
import xml.etree.ElementTree as ET
import datetime
import json

#import from settings
with open('settings.json') as settings_file:
    settings = json.load(settings_file)

# get XML
url = "http://" + settings["url"] + "/rest/getNowPlaying.view?u=" + settings["username"] + "&p=" + settings["password"] + "&v=1.11.0&c=android"
xml = urlopen(url)
content = xml.read()

encoding = xml.headers['content-type'].split('charset=')[-1]
ucontent = str(content, encoding)

# parse XML into an ElementTree
et = ET.fromstring(ucontent)
# Spin through the nowPlaying Elements

orig_stdout = sys.stdout
f = open('playing.php', encoding='utf-8', mode='w')
sys.stdout = f

for el in et[0]:
        print("<?php $command = escapeshellcmd('python3 " + settings["exportlocation"] + "nowplaying.py'); $output = shell_exec($command);"),
        print("echo $output; ?>"),
        print("╠ "),
        print(el.attrib["artist"]),
        print(" - "),
        print(el.attrib["title"]),
        print(" ╬ "),
        time = int(el.attrib["duration"])
        print(datetime.timedelta(seconds=time)),
        print(" ╣")
sys.stdout = orig_stdout
f.close()

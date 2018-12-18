#!/usr/bin/python

import xml.etree.ElementTree as ET
import base64

tree = ET.parse('shortcuts.plist')
root = tree.getroot()

irrelevantKeys = ['NSStatusItem Preferred Position Item-0', 'NSWindow Frame SUUpdateAlert', 'SUEnableAutomaticChecks', 'SUFeedURL', 'SUHasLaunchedBefore', 'SULastCheckTime', 'SUSendProfileInfo', 'use-canary-build', 'window-margin-size', 'window-margins', 'window-minimum-height', 'window-minimum-width', 'window-resize-step', 'display-current-layout']
irrelevantKeys = ['']
for i, child in enumerate(root[0]):
    if (child.text not in irrelevantKeys):
        data = str(child.text).strip()
        if (data[0:5] == "YnBsa"):
            key = str(root[0][i-1].text)
            data = base64.b64decode(data)
            with open("plists/"+key+".plist", 'w') as f:
                f.write(data)
#!/usr/bin/python
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import sys
import os
import json

if (sys.argv[2] == "German"):
    with open('keycodes_de.json') as f:
        keycodes = json.load(f)
else:
    with open('keycodes_en.json') as f:
        keycodes = json.load(f)

fName = os.path.basename(sys.argv[1])
fName = fName.split(".plist")[0]
tree = ET.parse(sys.argv[1])
root = tree.getroot()

maskCapsLock = 65536
maskShift = 131072
maskControl = 262144
maskOption = 524288
maskCommand = 1048576
maskFunction = 8388608

for i, child in enumerate(root[0][3][1]):
    if (i == 3):
        keyCode = int(child.text)
    elif (i == 5):
        hasShift = [u"shift down", u"⇧"] if (int(child.text) / maskShift) % 2 else ["", ""]
        hasControl = [u"control down", u"⌃"] if (int(child.text) / maskControl) % 2 else ["", ""]
        hasOption = [u"option down", u"⌥"] if (int(child.text) / maskOption) % 2 else ["", ""]
        hasCommand = [u"command down", u"⌘"] if (int(child.text) / maskCommand) % 2 else ["", ""]
        hasFunction = [u"function down", u"Fn"] if (int(child.text) / maskFunction) % 2 else ["", ""]
        modifier_applescript = [hasShift[0], hasControl[0], hasOption[0], hasCommand[0], hasFunction[0]]
        modifier_pretty = [hasShift[1], hasControl[1], hasOption[1], hasCommand[1], hasFunction[1]]

modifier_pretty = "".join(filter(None, modifier_pretty))
modifier_applescript = ", ".join(filter(None, modifier_applescript))

with open('settings.json', 'a') as f, open('controler.scpt', 'a') as scpt:
    if (fName == "cycle-layout-backward"):
    	j = {'title': 'Cycle Layout Backward', 'subtitle':u"{0} {1}".format(modifier_pretty, keycodes[str(keyCode)].upper()), 'arg': fName}
    	f.write("\"{0}\":{1},".format(fName, json.dumps(j)))
    	scpt.write("if q is \"{0}\" then\n\ttell application \"System Events\" to key code {1} using {{{2}}}\nelse ".format(fName, keyCode, modifier_applescript))
    elif (fName == "cycle-layout"):
    	j = {'title': 'Cycle Layout', 'subtitle':u"{0} {1}".format(modifier_pretty, keycodes[str(keyCode)].upper()), 'arg': fName}
    	f.write("\"{0}\":{1},".format(fName, json.dumps(j)))
    	scpt.write("if q is \"{0}\" then\n\ttell application \"System Events\" to key code {1} using {{{2}}}\nelse ".format(fName, keyCode, modifier_applescript))
    elif (fName == "decrease-main"):
    	j = {'title': 'Decrease main pane count', 'subtitle':u"{0} {1}".format(modifier_pretty, keycodes[str(keyCode)].upper()), 'arg': fName}
    	f.write("\"{0}\":{1},".format(fName, json.dumps(j)))
    	scpt.write("if q is \"{0}\" then\n\ttell application \"System Events\" to key code {1} using {{{2}}}\nelse ".format(fName, keyCode, modifier_applescript))
    elif (fName == "display-current-layout"):
    	j = {'title': 'Display current layout', 'subtitle':u"{0} {1}".format(modifier_pretty, keycodes[str(keyCode)].upper()), 'arg': fName}
    	f.write("\"{0}\":{1},".format(fName, json.dumps(j)))
    	scpt.write("if q is \"{0}\" then\n\ttell application \"System Events\" to key code {1} using {{{2}}}\nelse ".format(fName, keyCode, modifier_applescript))
    elif (fName == "expand-main"):
    	j = {'title': 'Expand main pane', 'subtitle':u"{0} {1}".format(modifier_pretty, keycodes[str(keyCode)].upper()), 'arg': fName}
    	f.write("\"{0}\":{1},".format(fName, json.dumps(j)))
    	scpt.write("if q is \"{0}\" then\n\ttell application \"System Events\" to key code {1} using {{{2}}}\nelse ".format(fName, keyCode, modifier_applescript))
    elif (fName == "focus-ccw"):
    	j = {'title': 'Move focus counter clockwise', 'subtitle':u"{0} {1}".format(modifier_pretty, keycodes[str(keyCode)].upper()), 'arg': fName}
    	f.write("\"{0}\":{1},".format(fName, json.dumps(j)))
    	scpt.write("if q is \"{0}\" then\n\ttell application \"System Events\" to key code {1} using {{{2}}}\nelse ".format(fName, keyCode, modifier_applescript))
    elif (fName == "focus-cw"):
    	j = {'title': 'Move focus clockwise', 'subtitle':u"{0} {1}".format(modifier_pretty, keycodes[str(keyCode)].upper()), 'arg': fName}
    	f.write("\"{0}\":{1},".format(fName, json.dumps(j)))
    	scpt.write("if q is \"{0}\" then\n\ttell application \"System Events\" to key code {1} using {{{2}}}\nelse ".format(fName, keyCode, modifier_applescript))
    elif (fName == "focus-screen-1"):
    	j = {'title': 'Throw focused window to space 1', 'subtitle':u"{0} {1}".format(modifier_pretty, keycodes[str(keyCode)].upper()), 'arg': fName}
    	f.write("\"{0}\":{1},".format(fName, json.dumps(j)))
    	scpt.write("if q is \"{0}\" then\n\ttell application \"System Events\" to key code {1} using {{{2}}}\nelse ".format(fName, keyCode, modifier_applescript))
    elif (fName == "focus-screen-2"):
    	j = {'title': 'Throw focused window to space 2', 'subtitle':u"{0} {1}".format(modifier_pretty, keycodes[str(keyCode)].upper()), 'arg': fName}
    	f.write("\"{0}\":{1},".format(fName, json.dumps(j)))
    	scpt.write("if q is \"{0}\" then\n\ttell application \"System Events\" to key code {1} using {{{2}}}\nelse ".format(fName, keyCode, modifier_applescript))
    elif (fName == "focus-screen-3"):
    	j = {'title': 'Throw focused window to space 3', 'subtitle':u"{0} {1}".format(modifier_pretty, keycodes[str(keyCode)].upper()), 'arg': fName}
    	f.write("\"{0}\":{1},".format(fName, json.dumps(j)))
    	scpt.write("if q is \"{0}\" then\n\ttell application \"System Events\" to key code {1} using {{{2}}}\nelse ".format(fName, keyCode, modifier_applescript))
    elif (fName == "focus-screen-4"):
    	j = {'title': 'Throw focused window to space 4', 'subtitle':u"{0} {1}".format(modifier_pretty, keycodes[str(keyCode)].upper()), 'arg': fName}
    	f.write("\"{0}\":{1},".format(fName, json.dumps(j)))
    	scpt.write("if q is \"{0}\" then\n\ttell application \"System Events\" to key code {1} using {{{2}}}\nelse ".format(fName, keyCode, modifier_applescript))
    elif (fName == "increase-main"):
    	j = {'title': 'Increase main pane count', 'subtitle':u"{0} {1}".format(modifier_pretty, keycodes[str(keyCode)].upper()), 'arg': fName}
    	f.write("\"{0}\":{1},".format(fName, json.dumps(j)))
    	scpt.write("if q is \"{0}\" then\n\ttell application \"System Events\" to key code {1} using {{{2}}}\nelse ".format(fName, keyCode, modifier_applescript))
    elif (fName == "reevaluate-windows"):
    	j = {'title': 'Force windows to be reevaluated', 'subtitle':u"{0} {1}".format(modifier_pretty, keycodes[str(keyCode)].upper()), 'arg': fName}
    	f.write("\"{0}\":{1},".format(fName, json.dumps(j)))
    	scpt.write("if q is \"{0}\" then\n\ttell application \"System Events\" to key code {1} using {{{2}}}\nelse ".format(fName, keyCode, modifier_applescript))
    elif (fName == "select-bsp-layout"):
    	j = {'title': 'Select bsp layout', 'subtitle':u"{0} {1}".format(modifier_pretty, keycodes[str(keyCode)].upper()), 'arg': fName}
    	f.write("\"{0}\":{1},".format(fName, json.dumps(j)))
    	scpt.write("if q is \"{0}\" then\n\ttell application \"System Events\" to key code {1} using {{{2}}}\nelse ".format(fName, keyCode, modifier_applescript))
    elif (fName == "select-column-layout"):
    	j = {'title': 'Select column layout', 'subtitle':u"{0} {1}".format(modifier_pretty, keycodes[str(keyCode)].upper()), 'arg': fName}
    	f.write("\"{0}\":{1},".format(fName, json.dumps(j)))
    	scpt.write("if q is \"{0}\" then\n\ttell application \"System Events\" to key code {1} using {{{2}}}\nelse ".format(fName, keyCode, modifier_applescript))
    elif (fName == "select-floating-layout"):
    	j = {'title': 'Select floating layout', 'subtitle':u"{0} {1}".format(modifier_pretty, keycodes[str(keyCode)].upper()), 'arg': fName}
    	f.write("\"{0}\":{1},".format(fName, json.dumps(j)))
    	scpt.write("if q is \"{0}\" then\n\ttell application \"System Events\" to key code {1} using {{{2}}}\nelse ".format(fName, keyCode, modifier_applescript))
    elif (fName == "select-fullscreen-layout"):
    	j = {'title': 'Select fullscreen layout', 'subtitle':u"{0} {1}".format(modifier_pretty, keycodes[str(keyCode)].upper()), 'arg': fName}
    	f.write("\"{0}\":{1},".format(fName, json.dumps(j)))
    	scpt.write("if q is \"{0}\" then\n\ttell application \"System Events\" to key code {1} using {{{2}}}\nelse ".format(fName, keyCode, modifier_applescript))
    elif (fName == "select-middle-wide-layout"):
    	j = {'title': 'Select middle-wide layout', 'subtitle':u"{0} {1}".format(modifier_pretty, keycodes[str(keyCode)].upper()), 'arg': fName}
    	f.write("\"{0}\":{1},".format(fName, json.dumps(j)))
    	scpt.write("if q is \"{0}\" then\n\ttell application \"System Events\" to key code {1} using {{{2}}}\nelse ".format(fName, keyCode, modifier_applescript))
    elif (fName == "select-row-layout"):
    	j = {'title': 'Select row layout', 'subtitle':u"{0} {1}".format(modifier_pretty, keycodes[str(keyCode)].upper()), 'arg': fName}
    	f.write("\"{0}\":{1},".format(fName, json.dumps(j)))
    	scpt.write("if q is \"{0}\" then\n\ttell application \"System Events\" to key code {1} using {{{2}}}\nelse ".format(fName, keyCode, modifier_applescript))
    elif (fName == "select-tall-layout"):
    	j = {'title': 'Select tall layout', 'subtitle':u"{0} {1}".format(modifier_pretty, keycodes[str(keyCode)].upper()), 'arg': fName}
    	f.write("\"{0}\":{1},".format(fName, json.dumps(j)))
    	scpt.write("if q is \"{0}\" then\n\ttell application \"System Events\" to key code {1} using {{{2}}}\nelse ".format(fName, keyCode, modifier_applescript))
    elif (fName == "select-tall-right-layout"):
    	j = {'title': 'Select tall-right layout', 'subtitle':u"{0} {1}".format(modifier_pretty, keycodes[str(keyCode)].upper()), 'arg': fName}
    	f.write("\"{0}\":{1},".format(fName, json.dumps(j)))
    	scpt.write("if q is \"{0}\" then\n\ttell application \"System Events\" to key code {1} using {{{2}}}\nelse ".format(fName, keyCode, modifier_applescript))
    elif (fName == "select-wide-layout"):
    	j = {'title': 'Select wide layout', 'subtitle':u"{0} {1}".format(modifier_pretty, keycodes[str(keyCode)].upper()), 'arg': fName}
    	f.write("\"{0}\":{1},".format(fName, json.dumps(j)))
    	scpt.write("if q is \"{0}\" then\n\ttell application \"System Events\" to key code {1} using {{{2}}}\nelse ".format(fName, keyCode, modifier_applescript))
    elif (fName == "select-widescreen-tall-layout"):
    	j = {'title': 'Select widescreen-tall layout', 'subtitle':u"{0} {1}".format(modifier_pretty, keycodes[str(keyCode)].upper()), 'arg': fName}
    	f.write("\"{0}\":{1},".format(fName, json.dumps(j)))
    	scpt.write("if q is \"{0}\" then\n\ttell application \"System Events\" to key code {1} using {{{2}}}\nelse ".format(fName, keyCode, modifier_applescript))
    elif (fName == "shrink-main"):
    	j = {'title': 'Shrink main pane', 'subtitle':u"{0} {1}".format(modifier_pretty, keycodes[str(keyCode)].upper()), 'arg': fName}
    	f.write("\"{0}\":{1},".format(fName, json.dumps(j)))
    	scpt.write("if q is \"{0}\" then\n\ttell application \"System Events\" to key code {1} using {{{2}}}\nelse ".format(fName, keyCode, modifier_applescript))
    elif (fName == "swap-ccw"):
    	j = {'title': 'Swap focused window counter clockwise', 'subtitle':u"{0} {1}".format(modifier_pretty, keycodes[str(keyCode)].upper()), 'arg': fName}
    	f.write("\"{0}\":{1},".format(fName, json.dumps(j)))
    	scpt.write("if q is \"{0}\" then\n\ttell application \"System Events\" to key code {1} using {{{2}}}\nelse ".format(fName, keyCode, modifier_applescript))
    elif (fName == "swap-cw"):
    	j = {'title': 'Swap focused window clockwise', 'subtitle':u"{0} {1}".format(modifier_pretty, keycodes[str(keyCode)].upper()), 'arg': fName}
    	f.write("\"{0}\":{1},".format(fName, json.dumps(j)))
    	scpt.write("if q is \"{0}\" then\n\ttell application \"System Events\" to key code {1} using {{{2}}}\nelse ".format(fName, keyCode, modifier_applescript))
    elif (fName == "swap-main"):
    	j = {'title': 'Swap focused window with main window', 'subtitle':u"{0} {1}".format(modifier_pretty, keycodes[str(keyCode)].upper()), 'arg': fName}
    	f.write("\"{0}\":{1},".format(fName, json.dumps(j)))
    	scpt.write("if q is \"{0}\" then\n\ttell application \"System Events\" to key code {1} using {{{2}}}\nelse ".format(fName, keyCode, modifier_applescript))
    elif (fName == "swap-screen-ccw"):
    	j = {'title': 'Swap focused window to counter clockwise screen', 'subtitle':u"{0} {1}".format(modifier_pretty, keycodes[str(keyCode)].upper()), 'arg': fName}
    	f.write("\"{0}\":{1},".format(fName, json.dumps(j)))
    	scpt.write("if q is \"{0}\" then\n\ttell application \"System Events\" to key code {1} using {{{2}}}\nelse ".format(fName, keyCode, modifier_applescript))
    elif (fName == "swap-screen-cw"):
    	j = {'title': 'Swap focused window to clockwise screen', 'subtitle':u"{0} {1}".format(modifier_pretty, keycodes[str(keyCode)].upper()), 'arg': fName}
    	f.write("\"{0}\":{1},".format(fName, json.dumps(j)))
    	scpt.write("if q is \"{0}\" then\n\ttell application \"System Events\" to key code {1} using {{{2}}}\nelse ".format(fName, keyCode, modifier_applescript))
    elif (fName == "throw-screen-1"):
    	j = {'title': 'Throw focused window to screen 1', 'subtitle':u"{0} {1}".format(modifier_pretty, keycodes[str(keyCode)].upper()), 'arg': fName}
    	f.write("\"{0}\":{1},".format(fName, json.dumps(j)))
    	scpt.write("if q is \"{0}\" then\n\ttell application \"System Events\" to key code {1} using {{{2}}}\nelse ".format(fName, keyCode, modifier_applescript))
    elif (fName == "throw-screen-2"):
    	j = {'title': 'Throw focused window to screen 2', 'subtitle':u"{0} {1}".format(modifier_pretty, keycodes[str(keyCode)].upper()), 'arg': fName}
    	f.write("\"{0}\":{1},".format(fName, json.dumps(j)))
    	scpt.write("if q is \"{0}\" then\n\ttell application \"System Events\" to key code {1} using {{{2}}}\nelse ".format(fName, keyCode, modifier_applescript))
    elif (fName == "throw-screen-3"):
    	j = {'title': 'Throw focused window to screen 3', 'subtitle':u"{0} {1}".format(modifier_pretty, keycodes[str(keyCode)].upper()), 'arg': fName}
    	f.write("\"{0}\":{1},".format(fName, json.dumps(j)))
    	scpt.write("if q is \"{0}\" then\n\ttell application \"System Events\" to key code {1} using {{{2}}}\nelse ".format(fName, keyCode, modifier_applescript))
    elif (fName == "throw-screen-4"):
    	j = {'title': 'Throw focused window to screen 4', 'subtitle':u"{0} {1}".format(modifier_pretty, keycodes[str(keyCode)].upper()), 'arg': fName}
    	f.write("\"{0}\":{1},".format(fName, json.dumps(j)))
    	scpt.write("if q is \"{0}\" then\n\ttell application \"System Events\" to key code {1} using {{{2}}}\nelse ".format(fName, keyCode, modifier_applescript))
    elif (fName == "throw-space-1"):
    	j = {'title': 'Throw focused window to space 1', 'subtitle':u"{0} {1}".format(modifier_pretty, keycodes[str(keyCode)].upper()), 'arg': fName}
    	f.write("\"{0}\":{1},".format(fName, json.dumps(j)))
    	scpt.write("if q is \"{0}\" then\n\ttell application \"System Events\" to key code {1} using {{{2}}}\nelse ".format(fName, keyCode, modifier_applescript))
    elif (fName == "throw-space-10"):
    	j = {'title': 'Throw focused window to space 10', 'subtitle':u"{0} {1}".format(modifier_pretty, keycodes[str(keyCode)].upper()), 'arg': fName}
    	f.write("\"{0}\":{1},".format(fName, json.dumps(j)))
    	scpt.write("if q is \"{0}\" then\n\ttell application \"System Events\" to key code {1} using {{{2}}}\nelse ".format(fName, keyCode, modifier_applescript))
    elif (fName == "throw-space-2"):
    	j = {'title': 'Throw focused window to space 2', 'subtitle':u"{0} {1}".format(modifier_pretty, keycodes[str(keyCode)].upper()), 'arg': fName}
    	f.write("\"{0}\":{1},".format(fName, json.dumps(j)))
    	scpt.write("if q is \"{0}\" then\n\ttell application \"System Events\" to key code {1} using {{{2}}}\nelse ".format(fName, keyCode, modifier_applescript))
    elif (fName == "throw-space-3"):
    	j = {'title': 'Throw focused window to space 3', 'subtitle':u"{0} {1}".format(modifier_pretty, keycodes[str(keyCode)].upper()), 'arg': fName}
    	f.write("\"{0}\":{1},".format(fName, json.dumps(j)))
    	scpt.write("if q is \"{0}\" then\n\ttell application \"System Events\" to key code {1} using {{{2}}}\nelse ".format(fName, keyCode, modifier_applescript))
    elif (fName == "throw-space-4"):
    	j = {'title': 'Throw focused window to space 4', 'subtitle':u"{0} {1}".format(modifier_pretty, keycodes[str(keyCode)].upper()), 'arg': fName}
    	f.write("\"{0}\":{1},".format(fName, json.dumps(j)))
    	scpt.write("if q is \"{0}\" then\n\ttell application \"System Events\" to key code {1} using {{{2}}}\nelse ".format(fName, keyCode, modifier_applescript))
    elif (fName == "throw-space-5"):
    	j = {'title': 'Throw focused window to space 5', 'subtitle':u"{0} {1}".format(modifier_pretty, keycodes[str(keyCode)].upper()), 'arg': fName}
    	f.write("\"{0}\":{1},".format(fName, json.dumps(j)))
    	scpt.write("if q is \"{0}\" then\n\ttell application \"System Events\" to key code {1} using {{{2}}}\nelse ".format(fName, keyCode, modifier_applescript))
    elif (fName == "throw-space-6"):
    	j = {'title': 'Throw focused window to space 6', 'subtitle':u"{0} {1}".format(modifier_pretty, keycodes[str(keyCode)].upper()), 'arg': fName}
    	f.write("\"{0}\":{1},".format(fName, json.dumps(j)))
    	scpt.write("if q is \"{0}\" then\n\ttell application \"System Events\" to key code {1} using {{{2}}}\nelse ".format(fName, keyCode, modifier_applescript))
    elif (fName == "throw-space-7"):
    	j = {'title': 'Throw focused window to space 7', 'subtitle':u"{0} {1}".format(modifier_pretty, keycodes[str(keyCode)].upper()), 'arg': fName}
    	f.write("\"{0}\":{1},".format(fName, json.dumps(j)))
    	scpt.write("if q is \"{0}\" then\n\ttell application \"System Events\" to key code {1} using {{{2}}}\nelse ".format(fName, keyCode, modifier_applescript))
    elif (fName == "throw-space-8"):
    	j = {'title': 'Throw focused window to space 8', 'subtitle':u"{0} {1}".format(modifier_pretty, keycodes[str(keyCode)].upper()), 'arg': fName}
    	f.write("\"{0}\":{1},".format(fName, json.dumps(j)))
    	scpt.write("if q is \"{0}\" then\n\ttell application \"System Events\" to key code {1} using {{{2}}}\nelse ".format(fName, keyCode, modifier_applescript))
    elif (fName == "throw-space-9"):
    	j = {'title': 'Throw focused window to space 9', 'subtitle':u"{0} {1}".format(modifier_pretty, keycodes[str(keyCode)].upper()), 'arg': fName}
    	f.write("\"{0}\":{1},".format(fName, json.dumps(j)))
    	scpt.write("if q is \"{0}\" then\n\ttell application \"System Events\" to key code {1} using {{{2}}}\nelse ".format(fName, keyCode, modifier_applescript))
    elif (fName == "throw-space-left"):
    	j = {'title': 'Throw focused window to space left', 'subtitle':u"{0} {1}".format(modifier_pretty, keycodes[str(keyCode)].upper()), 'arg': fName}
    	f.write("\"{0}\":{1},".format(fName, json.dumps(j)))
    	scpt.write("if q is \"{0}\" then\n\ttell application \"System Events\" to key code {1} using {{{2}}}\nelse ".format(fName, keyCode, modifier_applescript))
    elif (fName == "throw-space-right"):
    	j = {'title': 'Throw focused window to space right', 'subtitle':u"{0} {1}".format(modifier_pretty, keycodes[str(keyCode)].upper()), 'arg': fName}
    	f.write("\"{0}\":{1},".format(fName, json.dumps(j)))
    	scpt.write("if q is \"{0}\" then\n\ttell application \"System Events\" to key code {1} using {{{2}}}\nelse ".format(fName, keyCode, modifier_applescript))
    elif (fName == "toggle-float"):
    	j = {'title': 'Toggle float for focused window', 'subtitle':u"{0} {1}".format(modifier_pretty, keycodes[str(keyCode)].upper()), 'arg': fName}
    	f.write("\"{0}\":{1},".format(fName, json.dumps(j)))
    	scpt.write("if q is \"{0}\" then\n\ttell application \"System Events\" to key code {1} using {{{2}}}\nelse ".format(fName, keyCode, modifier_applescript))
    elif (fName == "toggle-focus-follows-mouse"):
    	j = {'title': 'Cycle Layout Backward', 'subtitle':u"{0} {1}".format(modifier_pretty, keycodes[str(keyCode)].upper()), 'arg': fName}
    	f.write("\"{0}\":{1},".format(fName, json.dumps(j)))
    	scpt.write("if q is \"{0}\" then\n\ttell application \"System Events\" to key code {1} using {{{2}}}\nelse ".format(fName, keyCode, modifier_applescript))
    elif (fName == "toggle-tiling"):
    	j = {'title': 'Toggle global tiling', 'subtitle':u"{0} {1}".format(modifier_pretty, keycodes[str(keyCode)].upper()), 'arg': fName}
    	f.write("\"{0}\":{1},".format(fName, json.dumps(j)))
    	scpt.write("if q is \"{0}\" then\n\ttell application \"System Events\" to key code {1} using {{{2}}}\nelse ".format(fName, keyCode, modifier_applescript))
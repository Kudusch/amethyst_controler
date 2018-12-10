#!/usr/bin/python
# -*- coding: UTF-8 -*-

from workflow import Workflow3
import string

wf = Workflow3()
args = wf.args
args = args[0].split(' ')
args = [i.strip(' ') for i in args]

itemListLayout = []
itemListLayout.append({'title':'Fullscreen', 'subtitle':'Choose layout', 'arg':'fullscreen', 'autocomplete':None, 'valid':True})
itemListLayout.append({'title':'Tall', 'subtitle':'Choose layout', 'arg':'tall', 'autocomplete':None, 'valid':True})
itemListLayout.append({'title':'Wide', 'subtitle':'Choose layout', 'arg':'wide', 'autocomplete':None, 'valid':True})
itemListLayout.append({'title':'Floating', 'subtitle':'Choose layout', 'arg':'floating', 'autocomplete':None, 'valid':True})

itemListShortcuts = []
itemListShortcuts.append({'title':'Make focused window main window', 'subtitle':'⌃⌥⇧↵', 'arg':'main', 'autocomplete':None, 'valid':True})
itemListShortcuts.append({'title':'Shrink main pane', 'subtitle':'⌃⌥⇧H', 'arg':'shrink', 'autocomplete':None, 'valid':True})
itemListShortcuts.append({'title':'Expand main pane', 'subtitle':'⌃⌥⇧L', 'arg':'expand', 'autocomplete':None, 'valid':True})
itemListShortcuts.append({'title':'Increase main pane count', 'subtitle':'⌃⌥⇧,', 'arg':'increase', 'autocomplete':None, 'valid':True})
itemListShortcuts.append({'title':'Decrease main pane count', 'subtitle':'⌃⌥⇧.', 'arg':'decrease', 'autocomplete':None, 'valid':True})
itemListShortcuts.append({'title':'Swap focused window counter clockwise', 'subtitle':'⌃⌥⇧←', 'arg':'ccw', 'autocomplete':None, 'valid':True})
itemListShortcuts.append({'title':'Swap focused window clockwise', 'subtitle':'⌃⌥⇧→', 'arg':'cw', 'autocomplete':None, 'valid':True})
itemListShortcuts.append({'title':'Force windows to be reevaluated', 'subtitle':'⌃⌥⇧Z', 'arg':'force', 'autocomplete':None, 'valid':True})
itemListShortcuts.append({'title':'Toggle float for focused window', 'subtitle':'⌃⌥⇧T', 'arg':'float', 'autocomplete':None, 'valid':True})

itemListMenu = []
itemListMenu.append({'title':'Layout', 'subtitle':'Choose layout', 'arg':None, 'autocomplete':'layout ', 'valid':False})
itemListMenu.append({'title':'Shortcut', 'subtitle':'Choose shortcut', 'arg':None, 'autocomplete':'shortcut ', 'valid':False})
if (args[0] == 'layout'):
    wf.add_item(title='←', subtitle='Back to the menu', arg=None, autocomplete='', valid='')
    for i in itemListLayout:
        if (args[-1].lower() == 'layout' or args[-1].lower() in i['title'].lower() and not args[-1].lower() == i['title'].lower()):
            wf.add_item(title=i['title'], subtitle=i['subtitle'], arg=i['arg'], autocomplete=i['autocomplete'], valid=i['valid'])
elif (args[0] == 'shortcut' ):
    wf.add_item(title='←', subtitle='Back to the menu', arg=None, autocomplete='', valid='')
    for i in itemListShortcuts:
        if (args[-1].lower() == 'shortcut' or args[-1].lower() in i['title'].lower() and not args[-1].lower() == i['title'].lower()):
            wf.add_item(title=i['title'], subtitle=i['subtitle'], arg=i['arg'], autocomplete=i['autocomplete'], valid=i['valid'])
else:
    for i in itemListMenu:
        wf.add_item(title=i['title'], subtitle=i['subtitle'], arg=i['arg'], autocomplete=i['autocomplete'], valid=i['valid'])

# Send feedback
wf.send_feedback()
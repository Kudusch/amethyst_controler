#!/usr/bin/python
# -*- coding: UTF-8 -*-

from workflow import Workflow3
import string
import json
import uuid

wf = Workflow3()
args = wf.args
args = args[0].split(' ')
args = [i.strip(' ') for i in args]

with open('settings.json') as f:
        settings = json.load(f)

layoutSettings = {k: v for k, v in settings.iteritems() if "select-" in k}
shortcutSettings = {k: v for k, v in settings.iteritems() if "select-" not in k and k != ""}

itemListLayout = []
for k, v in layoutSettings.iteritems():
    v['autocomplete'] = None
    v['valid'] = True
    v['uid'] = v['arg']
    v['uid'] = None
    itemListLayout.append(v)

itemListShortcut = []
for k, v in shortcutSettings.iteritems():
    v['autocomplete'] = None
    v['valid'] = True
    v['uid'] = v['arg']
    v['uid'] = None
    itemListShortcut.append(v)

itemListMenu = []
itemListMenu.append({'title':'Layout', 'subtitle':'Choose layout', 'arg':None, 'autocomplete':'layout ', 'valid':False})
itemListMenu.append({'title':'Shortcut', 'subtitle':'Choose shortcut', 'arg':None, 'autocomplete':'shortcut ', 'valid':False})
if (args[0] == 'layout'):
    wf.add_item(title='←', subtitle='Back to the menu', arg=None, autocomplete='', valid='', uid=None)
    for i in itemListLayout:
        if (args[-1].lower() == 'layout' or args[-1].lower() in i['title'].lower() and not args[-1].lower() == i['title'].lower()):
            wf.add_item(title=i['title'], subtitle=i['subtitle'], arg=i['arg'], autocomplete=i['autocomplete'], valid=i['valid'], uid=i['uid'])
elif (args[0] == 'shortcut' ):
    wf.add_item(title='←', subtitle='Back to the menu', arg=None, autocomplete='', valid='', uid=None)
    for i in itemListShortcut:
        if (args[-1].lower() == 'shortcut' or args[-1].lower() in i['title'].lower() and not args[-1].lower() == i['title'].lower()):
            wf.add_item(title=i['title'], subtitle=i['subtitle'], arg=i['arg'], autocomplete=i['autocomplete'], valid=i['valid'], uid=i['uid'])
else:
    for i in itemListMenu:
        wf.add_item(title=i['title'], subtitle=i['subtitle'], arg=i['arg'], autocomplete=i['autocomplete'], valid=i['valid'])

# Send feedback
wf.send_feedback()
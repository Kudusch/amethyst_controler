#!/bin/bash

cp ~/Library/Preferences/com.amethyst.Amethyst.plist shortcuts.plist
DIFF=$(diff old.plist shortcuts.plist) 
if [ "$DIFF" == "" ] 
then
    exit
fi
cp shortcuts.plist old.plist
plutil -convert xml1 shortcuts.plist
mkdir plists
python getShortcuts.py
plutil -convert xml1 plists/*.plist
rm shortcuts.plist

LANG=$(defaults read ~/Library/Preferences/com.apple.HIToolbox.plist AppleSelectedInputSources | egrep -w 'KeyboardLayout Name' | sed -E 's/^.+ = \"?([^\"]+)\"?;$/\1/')

echo "{" > settings.json
echo "on run argv\nset q to item 1 of argv\n" > controler.scpt

for file in plists/*; do
    DIFF=$(diff empty.plist $file) 
    if [ "$DIFF" == "" ] 
    then
        rm $file
    else
        python genSettings.py $file $LANG
    fi
done

echo "\"\":\"\"}" >> settings.json
echo "\n\treturn 0\nend if\nend run" >> controler.scpt

rm -r plists
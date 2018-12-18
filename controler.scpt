on run argv
set q to item 1 of argv

if q is "decrease-main" then
	tell application "System Events" to key code 47 using {shift down, control down, option down}
else if q is "expand-main" then
	tell application "System Events" to key code 37 using {shift down, control down, option down}
else if q is "increase-main" then
	tell application "System Events" to key code 43 using {shift down, control down, option down}
else if q is "reevaluate-windows" then
	tell application "System Events" to key code 16 using {shift down, control down, option down}
else if q is "select-floating-layout" then
	tell application "System Events" to key code 21 using {shift down, control down}
else if q is "select-fullscreen-layout" then
	tell application "System Events" to key code 20 using {shift down, control down}
else if q is "select-tall-layout" then
	tell application "System Events" to key code 18 using {shift down, control down}
else if q is "select-wide-layout" then
	tell application "System Events" to key code 19 using {shift down, control down}
else if q is "shrink-main" then
	tell application "System Events" to key code 4 using {shift down, control down, option down}
else if q is "swap-ccw" then
	tell application "System Events" to key code 123 using {shift down, control down, option down}
else if q is "swap-cw" then
	tell application "System Events" to key code 124 using {shift down, control down, option down}
else if q is "swap-main" then
	tell application "System Events" to key code 36 using {shift down, control down, option down}
else if q is "toggle-float" then
	tell application "System Events" to key code 17 using {shift down, control down, option down}
else if q is "toggle-focus-follows-mouse" then
	tell application "System Events" to key code 7 using {shift down, control down, option down}
else 
	return 0
end if
end run

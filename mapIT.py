#! python3 
#复制地址自动google map查询
# mapIT.py - Launches a map in the browser using an address from the command line or clipboard.
#技能包：webbrowser模块

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
	#Get address from command line.
	address = ' '.join(sys.argv[1:])
else:
	#Get address from clipboard.
	address = pyperclip.paste()
	
webbrowser.open('https://www.google.com/maps/place/' + address)

	

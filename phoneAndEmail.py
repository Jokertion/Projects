#!python3  电话号码和E-mail地址提取程序
#技能包：正则表达式
# phoneAndEmail.py = Finds phone numbers and email addresses on the clipboard.

import pyperclip,re

phoneRegex = re.compile(r'''(
	(\d{3}|\(\d{3}\))?				#area code
	(\s|-|\.)?						#separator
	(\d{3})							#first 3 digit
	(\s|-|\.)						#separator
	(\d{4})							#last 4 digit 
	(\s*(ext|x|ext.)\s*(\d{2,5}))?	#extension   groups[6]:整体 groups[7]:前 groups[8]:后 
	)''',re.VERBOSE)
	
#TODO: Create email regex.

#TODO: Find matches in clipboard text.

#TODO: Copy results to the clipboard.

#Create email regex.	
emailRegex = re.compile(r'''(
	[a-zA-Z0-9._%+-]+
	@
	[a-zA-Z0-9.-]+
	(\.[a-zA-Z]{2,4})
	)''',re.VERBOSE)
	
#TODO:Find matches in clipboard text.

#TODO: Copy results to the clipboard.

#Find matches in clipboard text.
text = str(pyperclip.paste())
matches=[]
for groups in phoneRegex.findall(text):
	phoneNum = '-'.join([groups[1],groups[3],groups[5]])
	if groups[8] !='':
		phoneNum += 'x' + groups[8]
	matches.append(phoneNum)
for groups in emailRegex.findall(text):
	matches.append(groups[0])
	
#TODO: Copy results to the clipboard.
	
#Copy results to the clipboard.
if len(matches) > 0:
	pyperclip.copy('n'.join(matches))
	print('Copied to clipboard:')
	print('\n'.join(matches))
else:
	print('No phone number or email addresses found.')
	

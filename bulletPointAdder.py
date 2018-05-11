#! python3  #把粘贴板的内容每一行前面添加星号
# bulletPoinAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.
#技能包： 1.pyperclip 2.列表的split<-->join 方法
import pyperclip
text = pyperclip.paste()

#Separate lines and add stars.
lines = text.split('\n')  #按换行分割文本，得到列表
for i in range(len(lines)):  #列表每个项是文本中的一行
	lines[i] = '* ' + lines[i]
text = '\n'.join(lines)  #还原回去
pyperclip.copy(text)
print('Has been added, it can be directly pasted.')

#! python3 
#pw.py - An insure password locker program.
#path：C:\
#技能包：1.建立bat批处理文件 2.pyperclip

PASSWORDS= {'sina':'f7MinlBDDuvmKJBbjshbsaccjJAksgnbbf8',
			'baidu':'gKCXkiajJJnvbCdDxfrgHujikGFEeHJMjmi8',
			'QQ':'12345'
			}
		
import sys,pyperclip
if len(sys.argv) < 2: #如果命令行输入参数少于两个，显示用法信息
	print('Usage: python pw.py [account] = copy account password')
	sys.exit()
	
account = sys.argv[1] #first command line arg is the account name

#字典中查找账户名，如果名称是字典中的键，取得其value，将它复制到剪贴板，然后打印一条信息；否则，告知没有这个账户名
if account in PASSWORDS: 
	pyperclip.copy(PASSWORDS[account])
	print ('Password for ' + account + ' copied to clipboard.')
else:
	print('There is no account named' + account)
	
'''
1.代码部分
2.将代码保存，以管理员身份运行记事本，建立一个bat批处理文件，内容：

@python.exe C:\pw.py %* 
@pause
保存为pw.bat文件，保存在‘C:\’中 
3、设置环境变量，将bat文件所在路径加入Path变量中

4、win + R 打开运行窗口，输入 “pw QQ”,点击“确定”，会跳出提示窗口，并将密码复制到剪贴板上

右键粘贴内容： 
12345
'''
#! python3
# pw.py - An insure password locker program.
# path：C:\
# 技能包：1.建立bat批处理文件 2.pyperclip

import sys, pyperclip


def password():
    PASSWORDS = {
        'sina': 'f7MinlBDDuvmKJBbjshbsaccjJAksgnbbf8',
        'baidu': 'gKCXkiajJJnvbCdDxfrgHujikGFEeHJMjmi8',
        'QQ': '12345',
    }
    return PASSWORDS


def judge_input():
    # 如果命令行输入参数少于两个，提示用法信息
    if len(sys.argv) < 2:
        print('Usage: python pw.py [account] = copy account password')
        sys.exit()

    account = sys.argv[1]
    code(account)


def code(account):
    PASSWORDS = password()
    # 字典中查找账户名，
    # 如果,是字典中的键，取得其value，
    # 复制到剪贴板，然后打印提示信息；
    # 否则，告知没有这个账户名
    if account in PASSWORDS:
        pyperclip.copy(PASSWORDS[account])
        print('Password for ' + account + ' copied to clipboard.')
    else:
        print('There is no account named' + account)


if __name__ == '__main__':
    judge_input()

'''
使用说明：

1.代码部分

2.建立bat批处理文件，输入内容：
@python.exe C:\pw.py %*
@pause
保存为pw.bat文件，和pw.py放一块 
保存在‘C:\’中

3、设置环境变量，将bat路径加入Path变量中

4、win + R 打开运行窗口，输入 “pw QQ”,
跳出提示窗口，QQ密码已经复制到剪贴板上

粘贴内容：
12345
'''

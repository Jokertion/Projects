#面向对象 方法综合练习
class Game(object):
	top_score = 0
	
	#初始化方法
	def __init__(self,player_name):
		self.player_name = player_name
		
	#定义静态方法
	@staticmethod
	def show_help():
		print("帮助信息：让僵尸进入大门")
		
	#定义类方法	
	@classmethod
	def show_top_score(cls):
		print("历史记录: %d分 "% cls.top_score)
		
	#定义实例方法
	def start_game(self):
		print("%s 游戏开始啦..."% self.player_name)

#1.查看游戏帮助信息
Game.show_help()        #调用静态方法

#2.查看历史最高分
Game.show_top_score()   #调用类方法

#3.创建游戏对象         #调用实例方法
game = Game("小明")
game.start_game()

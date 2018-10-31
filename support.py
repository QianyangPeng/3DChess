import os
import sys
import math
import 222
1
back masters
back master
import time
class Unit:
	"""
		one single unit on the chessboard
	"""
	def __init__(self,px=-1,py=-1,occupied=-1):
		self.__px,self.__py=px,py
		self.__occupied=occupied
		self.__base=False
		self.__land=-1
	def getLoc(self):
		return self.__px,self.__py
	def getState(self):
		return self.__occupied
	def changeState(self,val):
		self.__occupied=val
	def markBase(self):
		self.__base=True
	def getBase(self):
		return self.__base
	def markLand(self,team):
		self.__land=team
	def getLand(self):
		return self.__land
class Chessman:
	"""
		__team = -1(top)/1(bottom)
		(__px,__py) in [1,9]*[1*10]
	"""
	def __init__(self,px=-1,py=-1,team=-1,num=-1):
		self.__px,self.__py=px,py
		self.__team=team
		self.__num=num                 
	def getType(self):
		return ''
	def getLoc(self):
		return self.__px,self.__py
	def changeLoc(self,px,py):
                global winner
                if self.getType() == 'SHUAI' and px == -1 and py == -1:
                        winner = (self.getTeam()/2+1)%2*2
		self.__px=px
		self.__py=py
	def getTeam(self):
		return self.__team
	def getNum(self):
		return self.__num
	def move(self,absx,absy):
		return False
class Bing(Chessman):
	def __init__(self,px=-1,py=-1,team=-1,num=-1):
		global board,x,y
		board[(py-1)*x+px].changeState(team)
		Chessman.__init__(self,px,py,team,num)
	def getType(self):
		return 'BING'
	def move(self,unit):
		global board,x,y,dic,deserted
		absx,absy=unit.getLoc()
		occupied=unit.getState()
		team=self.getTeam()
		if team in [1,2]:
			alliance = [1,2]
		else:
			alliance = [0,3]
		ori_px,ori_py=self.getLoc()
		dx=absx-ori_px
		dy=absy-ori_py
		Bing_forbid = [(0,-1),(1,0),(0,1),(-1,0)]
		firstly_forbid = [[(1,0),(-1,0)],[(0,1),(0,-1)],[(1,0),(-1,0)],[(0,1),(0,-1)]]
		if occupied==-1:
			if (dx,dy) in [(1,0),(-1,0),(0,1),(0,-1)] and not (dx,dy) == Bing_forbid[team]:
                                if board[(ori_py-1)*x+ori_px].getLand()==team and (dx,dy)  in firstly_forbid[team]:
                                        return False
				board[(ori_py-1)*x+ori_px].changeState(-1) #get the current unit state to empty already done
				unit.changeState(team)
				self.changeLoc(absx,absy)
				return True
			else:
				return False
		elif not occupied in alliance:
			if (dx,dy) in [(1,0),(-1,0),(0,1),(0,-1)] and not (dx,dy) == Bing_forbid[team]:
				if (board[(ori_py-1)*x+ori_px].getLand()==team and (dx,dy)  in firstly_forbid[team]):
					return False
				board[(ori_py-1)*x+ori_px].changeState(-1) #get the current unit state to empty already done
				unit.changeState(team)
				dic[(absx,absy)].changeLoc(-1,-1)
				deserted.append(dic[(absx,absy)]) #get the covered one to be -1,-1 as dead _ to be done
				self.changeLoc(absx,absy)
				return True
			else:
				return False
		else:
			return False
class Shi(Chessman):
	def __init__(self,px=-1,py=-1,team=-1,num=-1):
		global board,x,y
		board[(py-1)*x+px].changeState(team)
		Chessman.__init__(self,px,py,team,num)
	def getType(self):
		return 'SHI'
	def move(self,unit):
		global board,x,y,dic,deserted
		absx,absy=unit.getLoc()
		occupied=unit.getState()
		team=self.getTeam()
		if team in [1,2]:
			alliance = [1,2]
		else:
			alliance = [0,3]
		ori_px,ori_py=self.getLoc()
		dx=absx-ori_px
		dy=absy-ori_py
		if occupied==-1:
			if (dx,dy) in [(1,1),(1,-1),(-1,1),(-1,-1)] and unit.getBase():
				board[(ori_py-1)*x+ori_px].changeState(-1) #get the current unit state to empty already done
				unit.changeState(team)
				self.changeLoc(absx,absy)
				return True
			else:
				return False
		elif not occupied in alliance:
			if (dx,dy) in [(1,1),(1,-1),(-1,1),(-1,-1)] and unit.getBase():
				board[(ori_py-1)*x+ori_px].changeState(-1) #get the current unit state to empty already done
				unit.changeState(team)
				dic[(absx,absy)].changeLoc(-1,-1)
				deserted.append(dic[(absx,absy)]) #get the covered one to be -1,-1 as dead _ to be done
				self.changeLoc(absx,absy)
				return True
			else:
				return False
		else:
			return False
class Xiang(Chessman):
	def __init__(self,px=-1,py=-1,team=-1,num=-1):
		global board,x,y
		board[(py-1)*x+px].changeState(team)
		Chessman.__init__(self,px,py,team,num)
	def getType(self):
		return 'XIANG'
	def move(self,unit):
		global board,x,y,dic,deserted
		absx,absy=unit.getLoc()
		occupied=unit.getState()
		team=self.getTeam()
		if team in [1,2]:
			alliance = [1,2]
		else:
			alliance = [0,3]
		ori_px,ori_py=self.getLoc()
		dx=absx-ori_px
		dy=absy-ori_py
		if occupied==-1:
			if (dx,dy) in [(2,2),(2,-2),(-2,-2),(-2,2)] and board[((absy+ori_py)/2-1)*x+(absx+ori_px)/2].getState()==-1 and unit.getLand()==team:
				board[(ori_py-1)*x+ori_px].changeState(-1) #get the current unit state to empty already done
				unit.changeState(team)
				self.changeLoc(absx,absy)
				return True
			else:
				return False
		elif not occupied in alliance:
			if (dx,dy) in [(2,2),(2,-2),(-2,-2),(-2,2)] and board[((absy+ori_py)/2-1)*x+(absx+ori_px)/2].getState()==-1 and unit.getLand()==team:
				board[(ori_py-1)*x+ori_px].changeState(-1) #get the current unit state to empty already done
				unit.changeState(team)
				dic[(absx,absy)].changeLoc(-1,-1)
				deserted.append(dic[(absx,absy)]) #get the covered one to be -1,-1 as dead _ to be done
				self.changeLoc(absx,absy)
				return True
			else:
				return False
		else:
			return False
class Ma(Chessman):
	def __init__(self,px=-1,py=-1,team=-1,num=-1):
		global board,x,y
		board[(py-1)*x+px].changeState(team)
		Chessman.__init__(self,px,py,team,num)
	def getType(self):
		return 'MA'
	def move(self,unit):
		global board,x,y,dic,deserted
		absx,absy=unit.getLoc()
		occupied=unit.getState()
		team=self.getTeam()
		if team in [1,2]:
			alliance = [1,2]
		else:
			alliance = [0,3]
		ori_px,ori_py=self.getLoc()
		dx=absx-ori_px
		dy=absy-ori_py
		if occupied==-1:
			if ((dx,dy) in [(1,2),(-1,2)] and board[ori_py*x+ori_px].getState()==-1) or ((dx,dy) in [(1,-2),(-1,-2)] and board[(ori_py-2)*x+ori_px].getState()==-1) or ((dx,dy) in [(2,1),(2,-1)] and board[(ori_py-1)*x+ori_px+1].getState()==-1) or ((dx,dy) in [(-2,1),(-2,-1)] and board[(ori_py-1)*x+ori_px-1].getState()==-1):
				board[(ori_py-1)*x+ori_px].changeState(-1) #get the current unit state to empty already done
				unit.changeState(team)
				self.changeLoc(absx,absy)
				return True
			else:
				return False
		elif not occupied in alliance:
			if ((dx,dy) in [(1,2),(-1,2)] and board[ori_py*x+ori_px].getState()==-1) or ((dx,dy) in [(1,-2),(-1,-2)] and board[(ori_py-2)*x+ori_px].getState()==-1) or ((dx,dy) in [(2,1),(2,-1)] and board[(ori_py-1)*x+ori_px+1].getState()==-1) or ((dx,dy) in [(-2,1),(-2,-1)] and board[(ori_py-1)*x+ori_px-1].getState()==-1):
				board[(ori_py-1)*x+ori_px].changeState(-1) #get the current unit state to empty already done
				unit.changeState(team)
				dic[(absx,absy)].changeLoc(-1,-1)
				deserted.append(dic[(absx,absy)]) #get the covered one to be -1,-1 as dead _ to be done
				self.changeLoc(absx,absy)
				return True
			else:
				return False
		else:
			return False
def check_Notblocked(x1,y1,x2,y2):
	global dic
	if not x1==x2:
		if not y1 == y2:
			return False
		else:
			for i in range(min(x1,x2)+1,max(x1,x2)):
				if dic.get((i,y1)):
					return False
			return True
	else:
		for i in range(min(y1,y2)+1,max(y1,y2)):
			if dic.get((x1,i)):
				return False
		return True
class Che(Chessman):
	def __init__(self,px=-1,py=-1,team=-1,num=-1):
		global board,x,y
		board[(py-1)*x+px].changeState(team)
		Chessman.__init__(self,px,py,team,num)
	def getType(self):
		return 'CHE'
	def move(self,unit):
		global board,x,y,dic,deserted
		absx,absy=unit.getLoc()
		occupied=unit.getState()
		team=self.getTeam()
		if team in [1,2]:
			alliance = [1,2]
		else:
			alliance = [0,3]
		ori_px,ori_py=self.getLoc()
		dx=absx-ori_px
		dy=absy-ori_py
		if occupied==-1:
			if check_Notblocked(ori_px,ori_py,absx,absy):
				board[(ori_py-1)*x+ori_px].changeState(-1) #get the current unit state to empty already done
				unit.changeState(team)
				self.changeLoc(absx,absy)
				return True
			else:
				return False
		elif not occupied in alliance:
			if check_Notblocked(ori_px,ori_py,absx,absy):
				board[(ori_py-1)*x+ori_px].changeState(-1) #get the current unit state to empty already done
				unit.changeState(team)
				dic[(absx,absy)].changeLoc(-1,-1)
				deserted.append(dic[(absx,absy)]) #get the covered one to be -1,-1 as dead _ to be done
				self.changeLoc(absx,absy)
				return True
			else:
				return False
		else:
			return False
def check_OneBetween(x1,y1,x2,y2):
	#print x1,y1,x2,y2

	global dic
	if not x1==x2:
		if not y1 == y2:
			return False
		else:
			flag = False
			for i in range(min(x1,x2)+1,max(x1,x2)):
				if dic.get((i,y1)):
					if flag:
						return False
					flag = True
			return flag
	else:
		flag = False
		for i in range(min(y1,y2)+1,max(y1,y2)):
			if dic.get((x1,i)):
				if flag:
					return False
				flag = True
		return flag
class Pao(Chessman):
	def __init__(self,px=-1,py=-1,team=-1,num=-1):
		global board,x,y
		board[(py-1)*x+px].changeState(team)
		Chessman.__init__(self,px,py,team,num)
	def getType(self):
		return 'PAO'
	def move(self,unit):
		global board,x,y,dic,deserted
		absx,absy=unit.getLoc()
		occupied=unit.getState()
		team=self.getTeam()
		if team in [1,2]:
			alliance = [1,2]
		else:
			alliance = [0,3]
		ori_px,ori_py=self.getLoc()
		dx=absx-ori_px
		dy=absy-ori_py
		if occupied==-1:
			if check_Notblocked(ori_px,ori_py,absx,absy):
				board[(ori_py-1)*x+ori_px].changeState(-1) #get the current unit state to empty already done
				unit.changeState(team)
				self.changeLoc(absx,absy)
				return True
			else:
				return False
		elif not occupied in alliance:
			if check_OneBetween(ori_px,ori_py,absx,absy):
				board[(ori_py-1)*x+ori_px].changeState(-1) #get the current unit state to empty already done
				unit.changeState(team)
				dic[(absx,absy)].changeLoc(-1,-1)
				deserted.append(dic[(absx,absy)]) #get the covered one to be -1,-1 as dead _ to be done
				self.changeLoc(absx,absy)
				return True
			else:
				return False
		else:
			return False
class Shuai(Chessman):
	def __init__(self,px=-1,py=-1,team=-1,num=-1):
		global board,x,y
		board[(py-1)*x+px].changeState(team)
		Chessman.__init__(self,px,py,team,num)
	def getType(self):
		return 'SHUAI'
	def move(self,unit):
		global board,x,y,dic,deserted
		absx,absy=unit.getLoc()
		occupied=unit.getState()
		team=self.getTeam()
		if team in [1,2]:
			alliance = [1,2]
		else:
			alliance = [0,3]
		ori_px,ori_py=self.getLoc()
		dx=absx-ori_px
		dy=absy-ori_py
		if occupied==-1:
			if (dx,dy) in [(0,1),(0,-1),(1,0),(-1,0)] and unit.getBase():
				board[(ori_py-1)*x+ori_px].changeState(-1) #get the current unit state to empty already done
				unit.changeState(team)
				self.changeLoc(absx,absy)
				return True
			else:
				return False
		elif not occupied in alliance:
			if ((dx,dy) in [(0,1),(0,-1),(1,0),(-1,0)] and unit.getBase()) or (dic[(absx,absy)].getType()=='SHUAI' and check_Notblocked(ori_px,ori_py,absx,absy)):
				board[(ori_py-1)*x+ori_px].changeState(-1) #get the current unit state to empty already done
				unit.changeState(team)
				dic[(absx,absy)].changeLoc(-1,-1)
				deserted.append(dic[(absx,absy)]) #get the covered one to be -1,-1 as dead _ to be done
				self.changeLoc(absx,absy)
				return True
			else:
				return False
		else:
			return False
def refreshChess(ori_px,ori_py,absx,absy):#move chess from (ori) to (abs), and delete ori 
	global dic
	dic[(absx,absy)] = dic[(ori_px,ori_py)]
	del dic[(ori_px,ori_py)]
def addLogst(stx,sty,edx,edy,exist):
	global logst
	ls = []
	if exist:
		ls.append(((edx,edy),(-1,-1)))
	ls.append(((stx,sty),(edx,edy)))
	logst.append(ls)
def Move(stx,sty,edx,edy):
	global dic,board,x,y
	if not dic.get((stx,sty)):
		return False
	exist = False
	if dic.get((edx,edy)):
		exist = True
	if dic[(stx,sty)].move(board[(edy-1)*x+edx]):
		addLogst(stx,sty,edx,edy,exist)
		return True
	else:
		return False
def getEachXY(px,py): # list []::(number,0)-putdown;(number,-1)-trashed;(number,1)-putup;(number,2,px,py)-move it to (px,py)
	global dic,state,memory,turn
	#print turn,state
	xturn = turn * 2
	if state:
		if dic.get((px,py)):
			if dic[(px,py)].getTeam() == xturn:
				state = False
				memory = (px,py)
				return [(dic[(px,py)].getNum(),1)] # 0: to down && 1 to up && -1 to disappear
			else:
				return []
		else:
			return []
	else:
		if dic.get((px,py)):
			#print 'dic exist'
			if dic[(px,py)].getTeam() == xturn:
				if dic[(px,py)].getNum() == dic[(memory[0],memory[1])].getNum():
					state = True
					return [(dic[(px,py)].getNum(),0)]
				else:
					(tmpx,tmpy) = memory
					memory = (px,py)
					return [(dic[(tmpx,tmpy)].getNum(),0),(dic[(px,py)].getNum(),1)]
			else:
				if Move(memory[0],memory[1],px,py):
					(tmpx,tmpy) = memory
					state = True
					turn = (turn + 1) % 2
					trash = dic[(px,py)].getNum()
					refreshChess(memory[0],memory[1],px,py)
					return [(trash,-1),(dic[(px,py)].getNum(),0),(dic[(px,py)].getNum(),2,px,py)]
				else:
					return []
		else:
			if Move(memory[0],memory[1],px,py):
				(tmpx,tmpy) = memory
				state = True
				turn = (turn + 1) % 2
				refreshChess(memory[0],memory[1],px,py)
				return [(dic[(px,py)].getNum(),0),(dic[(px,py)].getNum(),2,px,py)]
			else:
				state = True
				return [(dic[(memory[0],memory[1])].getNum(),0)]
def drawBoard():
	global x
	global y
	x = 9
	y = 10
	global board
	board=[Unit()]
	for i in range(1,y+1):
		for j in range(1,x+1):
			board.append(Unit(j,i,-1))
			if i <= 5:
				board[(i-1)*x+j].markLand(0)
			else:
				board[(i-1)*x+j].markLand(2)
	for i in range(4,7):
		for j in range(1,4):
			board[(j-1)*x+i].markBase()
		for j in range(8,11):
			board[(j-1)*x+i].markBase()
def drawChess():
	global dic,logst,deserted,state,memory,turn,regretTimes,winner
	dic = {}
	logst = []
	deserted = []
	state = True #marking : True for TaskDone || False for WaitingOrders-> check in reference.txt 
	memory = (-1,-1)
	turn = 0
	regretTimes=[5,5]
	winner = -1
	try:
		dic[(1,1)]=Che(1,1,0,2)
		dic[(2,1)]=Ma(2,1,0,4)
		dic[(3,1)]=Xiang(3,1,0,10)
		dic[(4,1)]=Shi(4,1,0,8)
		dic[(5,1)]=Shuai(5,1,0,1)
		dic[(6,1)]=Shi(6,1,0,9)
		dic[(7,1)]=Xiang(7,1,0,11)
		dic[(8,1)]=Ma(8,1,0,5)
		dic[(9,1)]=Che(9,1,0,3)
		dic[(2,3)]=Pao(2,3,0,6)
		dic[(8,3)]=Pao(8,3,0,7)
		for i in range(1,10,2):
			dic[(i,4)]=Bing(i,4,0,11+(i+1)/2)
			dic[(i,7)]=Bing(i,7,2,27+(i+1)/2)
		dic[(2,8)]=Pao(2,8,2,22)
		dic[(8,8)]=Pao(8,8,2,23)
		dic[(1,10)]=Che(1,10,2,18)
		dic[(2,10)]=Ma(2,10,2,20)
		dic[(3,10)]=Xiang(3,10,2,26)
		dic[(4,10)]=Shi(4,10,2,24)
		dic[(5,10)]=Shuai(5,10,2,17)
		dic[(6,10)]=Shi(6,10,2,25)
		dic[(7,10)]=Xiang(7,10,2,27)
		dic[(8,10)]=Ma(8,10,2,21)
		dic[(9,10)]=Che(9,10,2,19)
	except:
		print 'ERROR'
def test():
	global dic,logst,deserted
	global board
	Showit()
def CheckChess(ex,ey):
	global dic
	if dic.get((ex,ey)):
		return dic[(ex,ey)].getNum()
	else:
		return 0
def SaveToLocal(nm):
	path = 'save\\'+str(nm)
	for root,dirs,files in os.walk(path):
		for fi in files:
			p = os.path.join(path,fi)
			os.remove(p)
	global dic,logst,deserted,state,memory,turn,regretTimes
	TIMEFORMAT = '%Y-%m-%d-%H-%M-%S'
	filename = time.strftime(TIMEFORMAT,time.localtime(time.time()))
	#filename = '1.txt'
	path = os.path.join(path,filename)
	f = open(path,'w')
	ls = dic.keys()
	for i in ls:
		i = dic[i]
		f.write(str(i.getLoc()[0])+'\t'+str(i.getLoc()[1])+'\t'+str(i.getTeam())+'\t'+str(i.getNum())+'\t'+i.getType()+'\n')
	f.write('END'+'\n')
	for i in logst:
		for j in i:
			f.write(str(j[0][0])+'\t'+str(j[0][1])+'\t'+str(j[1][0])+'\t'+str(j[1][1])+'\t')
		f.write('\n')
	f.write('END'+'\n')
	for i in deserted:
		f.write(str(i.getLoc()[0])+'\t'+str(i.getLoc()[1])+'\t'+str(i.getTeam())+'\t'+str(i.getNum())+'\t'+i.getType()+'\n')
	f.write('END'+'\n')
	if state == True:
		state = 1
	if state == False:
		state = 0
	f.write(str(state)+'\t'+str(memory[0])+'\t'+str(memory[1])+'\t'+str(turn)+'\t'+str(regretTimes[0])+'\t'+str(regretTimes[1]))
	f.close()
	return filename
def DeleteAll():
	global dic,logst,deserted,state,memory,turn,regretTimes
	del dic
	del logst
	del deserted
	state = True
	memory = (-1,-1)
	turn = 0
	del regretTimes
def getLocalfiles():
	ls = []
	for root,dirs,files in os.walk('save'):
		for dr in dirs:
			path = os.path.join(root,dr)
			for rt,di,fi in os.walk(path):
				if len(fi)==0:
					ls.append('empty')
				else:
					ls.append(fi[0])
	return ls
def drawChessFromLocal(nm):
	global dic,logst,deserted,state,memory,turn,regretTimes
	dic = {}
	logst = []
	deserted = []
	state = True #marking : True for TaskDone || False for WaitingOrders-> check in reference.txt 
	memory = (-1,-1)
	turn = 0
	regretTimes=[]
	path = 'save\\'+str(nm)
	print nm
	print path,'a'
	for rt,dr,fl in os.walk(path):
		for f in fl:
			path = os.path.join(path,f)
	f = open(path)
	s = f.read()
	part = s.split('END')
	for line in part[0].split('\n'):
		if line == '':
			continue
		line = line.strip()
		ls = line.split('\t')
		if len(ls)<5:
			continue
		px,py,team,num,Ctype = int(ls[0]),int(ls[1]),int(ls[2]),int(ls[3]),ls[4]
		if Ctype == 'BING':
			dic[(px,py)] = Bing(px,py,team,num)
		elif Ctype == 'PAO':
			dic[(px,py)] = Pao(px,py,team,num)
		elif Ctype == 'CHE':
			dic[(px,py)] = Che(px,py,team,num)
		elif Ctype == 'MA':
			dic[(px,py)] = Ma(px,py,team,num)	
		elif Ctype == 'XIANG':
			dic[(px,py)] = Xiang(px,py,team,num)
		elif Ctype == 'SHI':
			dic[(px,py)] = Shi(px,py,team,num)
		elif Ctype == 'SHUAI':
			dic[(px,py)] = Shuai(px,py,team,num)
	for line in part[1].split('\n'):
		if line == '':
			continue
		line =line.strip()
		ls = line.split('\t')
		tmpl = []
		if len(ls)==4:
			x1,y1,x2,y2=int(ls[0]),int(ls[1]),int(ls[2]),int(ls[3])
			tmpl.append(((x1,y1),(x2,y2)))
		elif len(ls)==8:
			x1,y1,x2,y2=int(ls[0]),int(ls[1]),int(ls[2]),int(ls[3])
			tmpl.append(((x1,y1),(x2,y2)))
			x1,y1,x2,y2=int(ls[4]),int(ls[5]),int(ls[6]),int(ls[7])
			tmpl.append(((x1,y1),(x2,y2)))
		else:
			continue
		logst.append(tmpl)
	for line in part[2].split('\n'):
		if line == '':
			continue
		line = line.strip()
		ls = line.split('\t')
		if len(ls)<5:
			continue
		px,py,team,num,Ctype = int(ls[0]),int(ls[1]),int(ls[2]),int(ls[3]),ls[4]
		if Ctype == 'BING':
			deserted.append(Bing(px,py,team,num))
		elif Ctype == 'PAO':
			deserted.append(Pao(px,py,team,num))
		elif Ctype == 'CHE':
			deserted.append(Che(px,py,team,num))
		elif Ctype == 'MA':
			deserted.append(Ma(px,py,team,num))
		elif Ctype == 'XIANG':
			deserted.append(Xiang(px,py,team,num))
		elif Ctype == 'SHI':
			deserted.append(Shi(px,py,team,num))
		elif Ctype == 'SHUAI':
			deserted.append(Shuai(px,py,team,num))
	line = part[3].strip().split('\t')
	#state = int(line[0])
	#memory = (int(line[1]),int(line[2]))
	turn = int(line[3])
	regretTimes.append(int(line[4]))
	regretTimes.append(int(line[5]))
	ks = dic.keys()
	ls = []
	for i in ks:
		tmpx,tmpy = dic[i].getLoc()
		ls.append((dic[i].getNum(),2,tmpx,tmpy))
	print dic
	return ls

def SaveOrLoad(ap):
	ls = getLocalfiles()
	if ap[0]=='save':
		return SaveToLocal(ap[1])
	else:
		path = 'save\\'+str(ap[1])
		for rt,dr,fl in os.walk(path):
			if len(fl)==0:
				return False
		DeleteAll()
		drawBoard()
		return drawChessFromLocal(ap[1])

def regret():
	global dic,board,x,y,deserted,logst
	if len(logst)==0:
		return False,[]
	ls = logst.pop()
	if len(ls) > 1:
		tmplist = []
		dic[(ls[1][1][0],ls[1][1][1])].changeLoc(ls[1][0][0],ls[1][0][1])
		board[x*(ls[1][1][1]-1)+ls[1][1][0]].changeState(-1)
		board[x*(ls[1][0][1]-1)+ls[1][0][0]].changeState(dic[(ls[1][1][0],ls[1][1][1])].getTeam())
		num = dic[(ls[1][1][0],ls[1][1][1])].getNum()
		tmplist.append((num,2,ls[1][0][0],ls[1][0][1]))
		refreshChess(ls[1][1][0],ls[1][1][1],ls[1][0][0],ls[1][0][1])
		#if len(deserted)==0:
		#	return False,[]
		tmp=deserted.pop()
		num = tmp.getNum()
		tmplist.append((num,2,ls[0][0][0],ls[0][0][1]))
		board[(ls[0][0][1]-1)*x+ls[0][0][0]].changeState(tmp.getTeam())
		tmp.changeLoc(ls[0][0][0],ls[0][0][1])
		dic[(ls[0][0][0],ls[0][0][1])]=tmp
		return True,tmplist
	else:
		tmplist = []
		num = dic[(ls[0][1][0],ls[0][1][1])].getNum()
		tmplist.append((num,2,ls[0][0][0],ls[0][0][1]))
		dic[(ls[0][1][0],ls[0][1][1])].changeLoc(ls[0][0][0],ls[0][0][1])
		board[(ls[0][1][1]-1)*x+ls[0][1][0]].changeState(-1)
		board[(ls[0][0][1]-1)*x+ls[0][0][0]].changeState(dic[(ls[0][1][0],ls[0][1][1])].getTeam())
		refreshChess(ls[0][1][0],ls[0][1][1],ls[0][0][0],ls[0][0][1])
		return True,tmplist


def toPreState():
	global regretTimes,turn
	team = turn
	#if regretTimes[team]<=0:
	#	return []
	sta1=[]
	sta2=[]
	f,sta1 = regret()
	if f:
		turn=(turn+1)%2
	else:
		return []
	f,sta2 = regret()
	if f:
		turn=(turn+1)%2
	regretTimes[team]-=1
	return sta1+sta2
def getwinner():
        global winner
        return winner
def Showit():
	for i in range(10,0,-1):
		for j in range(1,10):
			if dic.get((j,i)):
				print str(dic[(j,i)].getType())[:2]+str(dic[(j,i)].getTeam()),'\t',
			else:
				print '   ','\t',
		print
#need a func to update chessboard & chess after each True move()

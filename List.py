class List(list):
	def __init__(self,ls = []):
		list.__init__([])
		self.extend(ls)

	def index(self,method = None):
		for i in range(len(self)):
			if method(self[i]):
				return i
		return -1

	def split(self,Separator = None,method = None,exclusive = False):

		compare = lambda x:x==Separator
		if method:
			compare = method

		def push(group,ls):
			if len(ls):group.append(ls)
			return group

		next = lambda x:x+1
		if exclusive == False:
			next = lambda x:x

		group = []
		pos =  0
		for i in range(len(self)):
			if compare(self[i]):
				group = push(group,self[pos:i])
				pos = next(i)

		return push(group,self[pos:])

	def group(self,method = None):
		legal = []
		ilegal = []
		judge = lambda x:True
		if method:
			judge = method
		for i in self:
			if judge(i):
				legal.append(i)
			else:
				ilegal.append(i)
		return legal,ilegal


if __name__ == '__main__':

  i = [1,2,6,3,1,4,1,5,1,6,7,1]
  ls = List(i)
  print i
  print ls.split(1)
  print ls.split(1,exclusive = True)
  print ls.split()
  print ls.split(method = lambda x: x%2)
  print ls.split(method = lambda x:x==6)
  print ls.group(lambda x:x>=4)

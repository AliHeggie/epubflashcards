import os
'''
generate a dict of topic:cards
open two "files", one for questions, one for answers
generata a list of unique random numbers and assign a pair to every
topic/file pair

for each topic:
	choose a random card in the dict
	assign that card an anchor pair from list of random numbers
	assemble the answer card from the title, question content, link and anchor
	assemble the solution card from the title, answer content, link and anchor
	write the answer card to the answer file
	write the solution card to the solution file

join the answer file to the solution file

convert to epuv


'''

#Card object
##method to read card and extract topics, question content and answer content

class card(object):
	def __init__(self,file=None):
		self.file = file
		self.topics = None
		self.question_content = None
		self.solution_content = None
		self.title = None		
	def parse(self):
		f = open(self.file,'r')
		lines = f.readlines()
		topics_idx = lines.index("%%%topics%%%\n")
		question_idx = lines.index("%%%question%%%\n")
		solution_idx = lines.index("%%%solution%%%\n")
		self.title = lines[0]
		self.topics= [str.strip(x) for x in lines[topics_idx+1:question_idx] 
		if x != "\n"]
		self.question_content= str.strip("".join(
			lines[question_idx+1:solution_idx]))
		self.solution_content= str.strip("".join(
			lines[solution_idx+1:len(lines)]))
		print "title:", self.title
		print "topics:", self.topics
		print "Question:", self.question_content
		print "Solution:", self.solution_content

path = "cards"
for filename in os.listdir(path):
	print filename
	a=card(file = os.path.join(path,filename))
	a.parse()
##method that assembles question card from title, content, link and anchor






#method to return a topic:files dict
#method that loops over topics



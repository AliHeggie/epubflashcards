import os
import subprocess

'''
generate a dict of topic:cards
open two "files", one for questions, one for answers
generata a list of unique random numbers and assign a pair to every
topic/file pair

for each topic:
	choose a random card in the dict
	assign that card an anchor pair from list of random numbers
	assemble the answer card from the title, question content, link and anchor
	assemble the answer card from the title, answer content, link and anchor
	write the answer card to the answer file
	write the answer card to the answer file

join the answer file to the answer file

convert to epuv


'''

#Card object
##method to read card and extract topics, question content and answer content

class card(object):
	def __init__(self,file=None):
		self.file = file
		self.topics = None
		self.question_content = None
		self.answer_content = None
		self.title = None		
	def parse(self,p = None):
		f = open(self.file,'r')
		lines = f.readlines()
		topics_idx = lines.index("%%%topics%%%\n")
		question_idx = lines.index("%%%question%%%\n")
		answer_idx = lines.index("%%%answer%%%\n")
		self.title = lines[0]
		self.topics= [str.strip(x) for x in lines[topics_idx+1:question_idx] 
		if x != "\n"]
		self.question_content= str.strip("".join(
			lines[question_idx+1:answer_idx]))
		self.answer_content= str.strip("".join(
			lines[answer_idx+1:len(lines)]))
		if p == True:
			print("title:", self.title)
			print("topics:", self.topics)
			print("Question:", self.question_content)
			print("answer:", self.answer_content)





path = "cards"
topics = set()
questions , answers = str(), str()
seedanchor =  99999


for filename in os.listdir(path):
	a=card(file = os.path.join(path,filename))
	a.parse()
	questionno = seedanchor+1
	answerno = seedanchor+2
	seedanchor = seedanchor+2

	
	topics.update(set(a.topics))
	title ="#" + a.title
	question_content=a.question_content+"\n\n"
	answer_content=a.answer_content+"\n\n"
	question_link = "[back to question](#question"+str(questionno)+")\n\n"
	answer_link = "[see answer](#answer"+str(answerno)+")\n\n"
	question_anchor = "#####question" + str(questionno) + "\n\n"
	answer_anchor = "#####answer" + str(answerno) + "\n\n"

	questions = (questions + title + question_content + 
		answer_link + question_anchor)
	answers = (answers + title + answer_content +
		question_link + answer_anchor)

header = "% My Flashcards\n% Alastair Heggie\n\n"
book = header + questions + answers
bookname = "flashcards"
bf =  open(bookname+".md","w")
bf.writelines(book)
bf.close()


args = ['pandoc', bookname+".md", '-o', bookname+".epub"]
subprocess.Popen(args)


##method that assembles question card from title, content, link and anchor






#method to return a topic:files dict
#method that loops over topics



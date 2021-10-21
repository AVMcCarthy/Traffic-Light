#!/usr/bin/env python

from Tkinter import *
import time

master = Tk()
frame = Frame(master)
frame.pack()
width = 256
height = 384
w = Canvas(master, width=width, height=height)
w.pack()

# class App:
# 	def __init__(self, master):
#
# 		frame = Frame(master)
# 		frame.pack()
# 		self.width = 256
# 		self.height = 384
# 		self.w = Canvas(master, width=self.width, height=self.height)
# 		self.w.pack()
# 		self.start = Button(
# 		    frame, text="Begin", fg="green", command=self.traffic
# 		    )
# 		self.start.pack(side=LEFT)
# 		# self.stop = Button(
# # 			frame, text = "End", fg = "red", command = self.end
# # 		)
# # 		self.stop.pack(side=LEFT)
# #
# 		self.phase = "red"
# #		self.contin = True
		
redLight = PhotoImage(file = "redLight.gif")
yellowLight = PhotoImage(file = "yellowLight.gif")
greenLight = PhotoImage(file = "greenLight.gif")
backImage = PhotoImage(file = "backImage.gif")

#w.create_image(width / 2, height / 2, image = backImage)
		
	# def end(self):
	# 	self.contin = False

def traffic():
	global phase
	#print "Beginning, phase = ", phase
	w.create_image(width / 2, height / 2, image = backImage)
	if(phase == "green"):
		w.create_image(width / 2, 276, image = greenLight)
		phase = "yellow"
	elif(phase == "yellow"):
		w.create_image(width / 2, 188, image = yellowLight)
		phase = "red"
	else:
		w.create_image(width / 2, 100, image = redLight)
		phase = "green"
	#print "Between phase = ", phase
	
	if(phase == "green"):
		time.sleep(7)
	elif(phase == "yellow"):
		time.sleep(30)
	else:
		time.sleep(35)
	
	#print "Post phase = ", phase
	master.update()

phase = "red"
		
# app = App(master)

while(True):
	traffic()

master.mainloop()
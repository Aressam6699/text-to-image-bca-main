from PIL import Image, ImageDraw
import pandas as pd

xls = pd.ExcelFile("samplequestion.xls")

sheetX = xls.parse(0) #2 is the sheet number+1 thus if the file has only 1 sheet write 0 in paranthesis

var1 = sheetX['Question']
var2 = sheetX['option A']
var3 = sheetX['option B']
var4 = sheetX['option C']
var5 = sheetX['option D']

#print(len(var1)) #1 is the row number.
#print(var1,"\t",var2,"\t",var3,"\t",var4,"\t",var5)
W, H = (400,300)

for i in range(len(var1)):
	
	msg = str(var1[i])
	im = Image.new("RGBA",(W,H),"white")
	draw = ImageDraw.Draw(im)
	w, h = draw.textsize(msg)
	draw.text(((W-w)/2,(H-h)/2), msg, fill="black")
	#im.save(str(i+1)+"Question."+str(i+1)+") "+str(var1[i])+".png", "PNG")
	im.save(str(i+1)+"_0Question.png","PNG")	
	msg = str(var2[i])
	im = Image.new("RGBA",(W,H),"white")
	draw = ImageDraw.Draw(im)
	w, h = draw.textsize(msg)
	draw.text(((W-w)/2,(H-h)/2), msg, fill="black")
	im.save(str(i+1)+"_1OptionA.png","PNG")
	#im.save(str(i+1)+"Question"+str(i+1)+" Answers/OptionA.png", "PNG")
	msg = str(var3[i])
	im = Image.new("RGBA",(W,H),"white")
	draw = ImageDraw.Draw(im)
	w, h = draw.textsize(msg)
	draw.text(((W-w)/2,(H-h)/2), msg, fill="black")
	im.save(str(i+1)+"_2OptionB.png","PNG")
	#im.save(str(i+1)+"Question"+str(i+1)+" Answers/OptionA.png", "PNG")
	msg = str(var4[i])
	im = Image.new("RGBA",(W,H),"white")
	draw = ImageDraw.Draw(im)
	w, h = draw.textsize(msg)
	draw.text(((W-w)/2,(H-h)/2), msg, fill="black")
	im.save(str(i+1)+"_3OptionC.png","PNG")
	#im.save(str(i+1)+"Question"+str(i+1)+" Answers/OptionA.png", "PNG")
	msg = str(var2[i])
	im = Image.new("RGBA",(W,H),"white")
	draw = ImageDraw.Draw(im)
	w, h = draw.textsize(msg)
	draw.text(((W-w)/2,(H-h)/2), msg, fill="black")
	im.save(str(i+1)+"_4OptionD.png","PNG")
	#im.save(str(i+1)+"Question"+str(i+1)+" Answers/OptionA.png", "PNG")

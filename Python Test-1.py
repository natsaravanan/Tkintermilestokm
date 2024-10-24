from tkinter import *
def convert(miles):
    km=1.609344*miles
    result="{} miles is {} kilometers".format(miles,km)
    resLabel.config(text=result,bg="#4285F4",font="Verdana 14")
root=Tk()
titlabel=Label(root,text="Miles to Kilometer Converter")
titlabel['bg']="#4285F4"
titlabel.config(fg="#FBBC2A",font="Verdana 24 bold")
titlabel.grid(row=0,column=0,columnspan=2)
milesLabel=Label(root,text="Enter Number of Miles Covered:")
milesLabel['bg']="#4285F4"
milesLabel.config(fg="#FBBC2A",font="Verdana 14")
milesLabel.grid(row=1,column=0)
milesinput=Entry(root,width=20)
milesinput.grid(row=1,column=1)
btn=Button(root,text="Convert to Km",bg="#FBBC2A",font="Verdana 14",
           command=lambda:convert(float(milesinput.get())))
btn.grid(row=2,column=0,columnspan=2)
resLabel=Label(root,text=" "*80)
resLabel.config(bg="#4285F4",font="Verdana 14")
resLabel.grid(row=3,column=0,columnspan=2)
root.title("Miles to Kilometer Converter")
root.minsize(width=400,height=200)
root.config(bg="#4285F4")
root.mainloop()

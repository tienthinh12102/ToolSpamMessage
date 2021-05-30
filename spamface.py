from tkinter import * #thư viên giao diện
import tkinter.messagebox
import re #thư viện tìm kiếm
import pyautogui, pyperclip, random, time

window = Tk() # tạo đối tượng 

window.wm_title("Tool Spam 1.0")
msg = Label(window, text = 'Nhập nội dung cần spam : ')
msg.config(font=("Helvetica", 10)) # font và size chữ
msg.grid(row = 0, column = 0)
txbmsg = Entry(window) # tạo textBox
txbmsg.grid(row = 0, column = 1)

n = Label(window, text = 'Nhập số lần Spam : ')
n.config(font=("Helvetica", 10)) # font và size chữ
n.grid(row = 1, column = 0)
txbn = Entry(window) # tạo textBox
txbn.grid(row = 1, column = 1)

def spamwold(a):
	pyperclip.copy(random.choice(a))
	pyautogui.hotkey("ctrl","v")
	pyautogui.press("enter")
	time.sleep(0.1) #Delay
#SPAM

def RunCommand():
	time.sleep(3)
	text2 = int(txbn.get())
	for i in range(text2):
		text1 = [txbmsg.get()]
		spamwold(text1)
	tkinter.messagebox.showinfo('Thông báo','Đã Xong')
	
btn=Button(window,text="OK", width=10, height=2, command=RunCommand) #Tạo btn
btn.grid(row = 3, column = 1)

window.mainloop()
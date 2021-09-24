import tkinter as tk

calculation = ""


def number(num):

    global calculation

    calculation = calculation + str(num)

    #the set method/function posts the numbers and operators in the entry box
    equation.set(calculation)

def equal():

    global calculation

    global total

    total = eval(calculation)

    equation.set(f"{calculation} = {total}")

def receipt():

    global calculation

    global total

    output_receipt.insert(tk.END, f"Receipt:\n{calculation} = {total}\n\n")

def clear():

    global calculation

    calculation = ""

    equation.set(calculation)


#window 
window = tk.Tk()
window.title("Calculator")
window.resizable(0,0)

#below are the output windows that show the calculations 
output_frame = tk.Frame(master = window, relief = tk.SUNKEN,borderwidth=5)
output_frame.grid(row=0,column=0, columnspan = 4)

output_frame_receipt= tk.Frame(master=window,relief = tk.RAISED, borderwidth = 5)
output_frame_receipt.grid(row=0,column=6, rowspan = 4)

#below are frames using the grid fuction on the frame object
frame_receipt= tk.Frame(master=window,relief = tk.RAISED, borderwidth=5)
frame_receipt.grid(row=4,column=4, columnspan = 4)

frame0= tk.Frame(master=window,relief = tk.RAISED, borderwidth=5)
frame0.grid(row=4,column=0)

frame1= tk.Frame(master=window,relief = tk.RAISED, borderwidth=5)
frame1.grid(row=1,column=0)
    
frame2 = tk.Frame(master = window, relief = tk.RAISED, borderwidth=5)
frame2.grid(row=1,column=1)

frame3 = tk.Frame(master = window, relief = tk.RAISED, borderwidth=5)
frame3.grid(row=1,column=2)

frame4 = tk.Frame(master = window, relief = tk.RAISED, borderwidth=5)
frame4.grid(row=2,column=0)

frame5 = tk.Frame(master = window, relief = tk.RAISED, borderwidth=5)
frame5.grid(row=2,column=1)

frame6 = tk.Frame(master = window, relief = tk.RAISED, borderwidth=5)
frame6.grid(row=2,column=2)

frame7= tk.Frame(master = window, relief = tk.RAISED, borderwidth=5)
frame7.grid(row=3,column=0)

frame8 = tk.Frame(master = window, relief = tk.RAISED, borderwidth=5)
frame8.grid(row=3,column=1)

frame9 = tk.Frame(master = window, relief = tk.RAISED, borderwidth=5)
frame9.grid(row=3,column=2)

frame_plus = tk.Frame(master = window, relief = tk.RAISED, borderwidth=5)
frame_plus.grid(row=1,column=3)

frame_minus = tk.Frame(master = window, relief = tk.RAISED, borderwidth=5)
frame_minus.grid(row=2,column=3)

frame_multiply = tk.Frame(master = window, relief = tk.RAISED, borderwidth=5)
frame_multiply.grid(row=3,column=3)

frame_divide = tk.Frame(master = window, relief = tk.RAISED, borderwidth=5)
frame_divide.grid(row=4,column=3)

frame_equal = tk.Frame(master = window, relief = tk.RAISED, borderwidth=5)
frame_equal.grid(row=4,column=1)
 
frame_clear = tk.Frame(master = window, relief =tk.RAISED, borderwidth=5)
frame_clear.grid(row = 4, column = 2)

#the equation variables that holds the entered equation as a string variable. 
equation = tk.StringVar()

#below are button/entry/text widgets whose masters are frames
output = tk.Entry(master=output_frame, textvariable = equation, bg = 'black', fg = 'white', font = ("Times New Roman",20))
output.grid(ipadx=110, ipady = 20)

output_receipt = tk.Text(master= output_frame_receipt, bg = 'black', fg = 'white')
output_receipt.grid()

button_receipt = tk.Button(master=frame_receipt, text = 'Receipt', bg = 'gray', fg = 'black', height = 5, width = 65)
button_receipt.grid()
button_receipt.bind('<Button-1>', lambda event: receipt())

button0 = tk.Button(master=frame0, text = '0', bg = 'gray', fg = 'black', height = 5, width = 10)
button0.grid()
button0.bind('<Button-1>', lambda event: number("0"))
 
button1 = tk.Button(master=frame1, text = '1', bg = 'gray', fg = 'black', height = 5, width = 10)
button1.grid()
button1.bind('<Button-1>', lambda event: number("1"))

button2 = tk.Button(master=frame2, text = '2', bg = 'gray', fg = 'black', height = 5, width = 10)
button2.grid()
button2.bind('<Button-1>', lambda event: number("2"))

button3 = tk.Button(master=frame3, text = '3', bg = 'gray', fg = 'black', height = 5, width = 10)
button3.grid()
button3.bind('<Button-1>', lambda event: number("3"))

button4 = tk.Button(master=frame4, text = '4', bg = 'gray', fg = 'black', height = 5, width = 10)
button4.grid()
button4.bind('<Button-1>', lambda event: number("4"))
 
button5 = tk.Button(master=frame5, text = '5', bg = 'gray', fg = 'black', height = 5, width = 10)
button5.grid()
button5.bind('<Button-1>', lambda event: number("5"))
    
button6 = tk.Button(master=frame6, text = '6', bg = 'gray', fg = 'black', height = 5, width = 10)
button6.grid()
button6.bind('<Button-1>', lambda event: number("6"))
    
button7 = tk.Button(master=frame7, text = '7', bg = 'gray', fg = 'black', height = 5, width = 10)
button7.grid()
button7.bind('<Button-1>', lambda event: number("7"))
    
button8 = tk.Button(master=frame8, text = '8', bg = 'gray', fg = 'black', height = 5, width = 10)
button8.grid()
button8.bind('<Button-1>', lambda event: number("8"))
    
button9 = tk.Button(master=frame9, text = '9', bg = 'gray', fg = 'black', height = 5, width = 10)
button9.grid()
button9.bind('<Button-1>', lambda event: number("9"))
    
button_plus = tk.Button(master=frame_plus, text = '+', bg = 'gray', fg = 'black', height = 5, width = 10)
button_plus.grid()
button_plus.bind('<Button-1>', lambda event: number("+"))

button_minus = tk.Button(master=frame_minus, text = '-', bg = 'gray', fg = 'black', height = 5, width = 10)
button_minus.grid()
button_minus.bind('<Button-1>', lambda event: number("-"))

button_multiply = tk.Button(master=frame_multiply, text = '*', bg = 'gray', fg = 'black', height = 5, width = 10)
button_multiply.grid()
button_multiply.bind('<Button-1>', lambda event: number("*"))

button_divide = tk.Button(master=frame_divide, text = '/', bg = 'gray', fg = 'black', height = 5, width = 10)
button_divide.grid()
button_divide.bind('<Button-1>', lambda event: number("/"))

button_equal = tk.Button(master=frame_equal, text = '=', bg = 'gray', fg = 'black', height = 5, width = 10)
button_equal.grid()
button_equal.bind('<Button-1>', lambda event: equal())

button_clear = tk.Button(master=frame_clear, text = 'Clear', bg = 'gray', fg = 'black', height = 5, width = 10)
button_clear.grid()
button_clear.bind('<Button-1>', lambda event: clear())

#runs application and keeps the window open
window.mainloop()











    

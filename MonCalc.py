from tkinter import *
from tkinter import messagebox

bills = [1000,500,200,100,50,20,10,5,2,1]

def sum_info():
    
    total_sum = Label(text=str(
                        float(label_1000_entry.get()) * 1000 * float(rates_head_e.get())
                        + float(label_500_entry.get()) * 500 * float(rates_head_e.get())
                        + float(label_200_entry.get()) * 200 * float(rates_head_e.get())
                        + float(label_100_entry.get()) * 100 * float(rates_head_e.get())
                        + float(label_50_entry.get()) * 50 * float(rates_head_e.get())
                        + float(label_20_entry.get()) * 20 * float(rates_head_e.get())
                        + float(label_10_entry.get()) * 10 * float(rates_head_e.get())
                        + float(label_5_entry.get()) * 5 * float(rates_head_e.get())
                        + float(label_2_entry.get()) * 2 * float(rates_head_e.get())
                        + float(label_1_entry.get()) * 1 * float(rates_head_e.get())))
    total_sum.grid(row=15,column=3,sticky="w")   
    
    sum1000 = Label(text=str(float(label_1000_entry.get()) * 1000 * float(rates_head_e.get())),height=2)
    sum1000.grid(row=5,column=3,sticky="w")
    sum500 = Label(text=str(float(label_500_entry.get()) * 500 * float(rates_head_e.get())),height=2)
    sum500.grid(row=6,column=3,sticky="w")
    sum200 = Label(text=str(float(label_200_entry.get()) * 200 * float(rates_head_e.get())),height=2)
    sum200.grid(row=7,column=3,sticky="w")
    sum100 = Label(text=str(float(label_100_entry.get()) * 100 * float(rates_head_e.get())),height=2)
    sum100.grid(row=8,column=3,sticky="w")
    sum50 = Label(text=str(float(label_50_entry.get()) * 50 * float(rates_head_e.get())),height=2)
    sum50.grid(row=9,column=3,sticky="w")
    sum20 = Label(text=str(float(label_20_entry.get()) * 20 * float(rates_head_e.get())),height=2)
    sum20.grid(row=10,column=3,sticky="w")
    sum10 = Label(text=str(float(label_10_entry.get()) * 10 * float(rates_head_e.get())),height=2)
    sum10.grid(row=11,column=3,sticky="w")
    sum5 = Label(text=str(float(label_5_entry.get()) * 5 * float(rates_head_e.get())),height=2)
    sum5.grid(row=12,column=3,sticky="w")
    sum2 = Label(text=str(float(label_2_entry.get()) * 2 * float(rates_head_e.get())),height=2)
    sum2.grid(row=13,column=3,sticky="w")
    sum1 = Label(text=str(float(label_1_entry.get()) * 1 * float(rates_head_e.get())),height=2)
    sum1.grid(row=14,column=3,sticky="w")

root = Tk()
root.geometry("600x470")
root.title("money calculator")

# заголовок 
bills_head = Label(text="bills",height=2,relief=GROOVE)
bills_head.grid(row=3,column=0,rowspan=3,sticky="n")
number_head = Label(text="number",height=2,relief=GROOVE)
number_head.grid(row=3,column=1,rowspan=3,sticky="n")
factor_head = Label(text="rate",height=2,relief=GROOVE)
factor_head.grid(row=3,column=2,rowspan=3,sticky="n")
rates_head_e = Entry(relief=GROOVE,width=7)
rates_head_e.grid(padx=5, pady=5,row=4,column=2,sticky="w")
rates_head_l = Label(text="sum",height=2,relief=GROOVE,width=6)
rates_head_l.grid(row=3,column=3,sticky="n")

rates_head_e.insert(0,1)

#Текстовая разметка номинала денег
label_1000 = Label(text="1000",height=2)
label_1000.grid(row=5,column=0,sticky="w")
label_500 = Label(text="500",height=2)
label_500.grid(row=6,column=0,sticky="w")
label_200 = Label(text="200",height=2)
label_200.grid(row=7,column=0,sticky="w")
label_100 = Label(text="100",height=2)
label_100.grid(row=8,column=0,sticky="w")
label_50 = Label(text="50",height=2)
label_50.grid(row=9,column=0,sticky="w")
label_20 = Label(text="20",height=2)
label_20.grid(row=10,column=0,sticky="w")
label_10 = Label(text="10",height=2)
label_10.grid(row=11,column=0,sticky="w")
label_5 = Label(text="5",height=2)
label_5.grid(row=12,column=0,sticky="w")
label_2 = Label(text="2",height=2)
label_2.grid(row=13,column=0,sticky="w")
label_1 = Label(text="1",height=2)
label_1.grid(row=14,column=0,sticky="w")

    
# Текстовая разметка для указания курса

for x in range(5,15):
    label_x = Label(text="=",height=2,width=5)
    label_x.grid(row=x,column=2,sticky="w")

label_1000_entry = Entry(width=7)
label_1000_entry.grid(row=5,column=1,sticky="e")
label_500_entry = Entry(width=7)
label_500_entry.grid(row=6,column=1,sticky="e")
label_200_entry = Entry(width=7)
label_200_entry.grid(row=7,column=1,sticky="e")
label_100_entry = Entry(width=7)
label_100_entry.grid(row=8,column=1,sticky="e")
label_50_entry = Entry(width=7)
label_50_entry.grid(row=9,column=1,sticky="e")
label_20_entry = Entry(width=7)
label_20_entry.grid(row=10,column=1,sticky="e")
label_10_entry = Entry(width=7)
label_10_entry.grid(row=11,column=1,sticky="e")
label_5_entry = Entry(width=7)
label_5_entry.grid(row=12,column=1,sticky="e")
label_2_entry = Entry(width=7)
label_2_entry.grid(row=13,column=1,sticky="e")
label_1_entry = Entry(width=7)
label_1_entry.grid(row=14,column=1,sticky="e")

#Устанавливаем в полях ввода кол-ва - 0
label_1000_entry.insert(0,0)
label_500_entry.insert(0,0)
label_200_entry.insert(0,0)
label_100_entry.insert(0,0)
label_50_entry.insert(0,0)
label_20_entry.insert(0,0)
label_10_entry.insert(0,0)
label_5_entry.insert(0,0)
label_2_entry.insert(0,0)
label_1_entry.insert(0,0)


# здесь будут кнопки
sum_btn = Button(text="Total",command=sum_info)
sum_btn.place(relx=.8, rely=.9, anchor="c", height=30, width=130, bordermode=OUTSIDE)

root.mainloop()

from tkinter import*

root =Tk()
root.title('999 pad')
root.geometry('250x300')

nums = [[9, 8, 7],
        [6, 5, 4],
        [3, 2, 1],
        ['#', 0, '*']]

for i in range(4):
  root.rowconfigure(i, weight=1, minsize=50)
  for j in range(3):
    root.columnconfigure(j, weight=1, minsize = 75)
    
    frame = Frame(master=root, relief=SUNKEN, borderwidth=1)
    frame.grid(row=i, column=j, padx=3, pady=3)

    btn = Button(master=frame, text=nums[i][j], width=5, height=2, bg="#d0efff")

    btn.pack(expand=True)

root.mainloop()

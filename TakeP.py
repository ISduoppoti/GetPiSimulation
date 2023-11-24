import customtkinter as ctk
import tkinter as tk
import threading as th
import random as r


root = ctk.CTk()
root.title('Take P')
root.geometry('550x300')
root.resizable(False, False)

class main():
    def __init__(self):
        self.frame_left = ctk.CTkFrame(root)
        self.frame_left.pack(fill = tk.Y, side = 'left')

        self.label_a = ctk.CTkLabel(self.frame_left, text='Lenght:', pady = 20) #value is 5
        self.label_a.grid(row = 0, column = 0)

        self.entry_a = ctk.CTkEntry(self.frame_left, width = 100)
        self.entry_a.grid(row = 0, column = 1)

        self.label_dott = ctk.CTkLabel(self.frame_left, text='Dott count:', pady = 20)
        self.label_dott.grid(row = 1, column = 0)

        self.entry_dott = ctk.CTkEntry(self.frame_left, width = 100)
        self.entry_dott.grid(row = 1, column = 1)


        self.label_in = ctk.CTkLabel(self.frame_left, text = 'In circle:', pady = 20)
        self.label_in.grid(row = 2, column = 0)

        self.label_in_info = ctk.CTkLabel(self.frame_left, text = '', fg_color = '#343638', width =100)
        self.label_in_info.grid(row = 2, column = 1)

        self.label_count_p = ctk.CTkLabel(self.frame_left, text = 'Num P:', width = 100, pady = 20)
        self.label_count_p.grid(row = 3, column = 0)

        self.label_count_p_info = ctk.CTkLabel(self.frame_left, text = '', fg_color = '#343638', width = 100)
        self.label_count_p_info.grid(row = 3, column = 1)


        self.btn_calculate = ctk.CTkButton(self.frame_left, text='Calculate', command = self.calculate)
        self.btn_calculate.grid(row = 4, columnspan = 2)

        self.canvas = ctk.CTkCanvas(root, width=250, height=250, bg='white')
        self.canvas.pack(expand = True)

        self.canvas.create_oval(2, 2, 251, 251, width=1, outline = 'red')

    def calculate(self):
        def main():
            r1 = int(self.entry_a.get()) / 2
            r2 = -r1

            count_in = 0

            count_repeat = int(self.entry_dott.get())

            for i in range(count_repeat):
                num1 = r.uniform(r2, r1)
                num2 = r.uniform(r2, r1)

                if num1**2 + num2**2 < r1**2:
                    count_in += 1
                else:
                    None

                self.canvas.create_oval(num1*100, num2*100, (num1)*100, (num2)*100, width = 1, outline = 'blue')

            self.label_in_info.configure(text=str(count_in))

            self.label_count_p_info.configure(text=str(4*count_in/count_repeat))
        
        th.Thread(target=main).start()

'''
p = 4K/N (K - count of dotts in circle)(N - count of all dott)
'''


main()

root.mainloop()

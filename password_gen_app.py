from tkinter import *
import customtkinter as ctk
from password_gen_oop import PasswordGenerator



class Layout(ctk.CTkFrame):
    def __init__(self, parent, pw, length, cap, lower, num, special, roll):
        super().__init__(parent, fg_color='#00F0F0')

        self.rowconfigure((0,1,2,3), uniform='a', weight=1)
        self.columnconfigure(0, weight=1)

        pwText = ctk.CTkLabel(self, textvariable=pw, font=('Arial-Bold', 32))
        pwText.grid(row=0, column=0, sticky='news')

        lengthSlider = ctk.CTkSlider(self, width=300, variable=length, from_=4, to=28)
        lengthSlider.grid(row=1, column=0, sticky='w', padx=50)

        sliderText = ctk.CTkLabel(self, textvariable=length, font=('Arial', 28))
        sliderText.grid(row=1, column=0, sticky='e', padx=100)

        optionFrame = ctk.CTkFrame(self)
        optionFrame.rowconfigure(0, weight=1)
        optionFrame.columnconfigure((0,1,2,3), weight=1, uniform='a')

        checkCap = ctk.CTkCheckBox(optionFrame, text='Capital Letters [A-Z]', onvalue=True, offvalue=False, variable=cap)
        checkCap.grid(row=0, column=0, sticky='news', padx=5)

        checkLower = ctk.CTkCheckBox(optionFrame, text='Lower Letters [a-z]', onvalue=True, offvalue=False, variable=lower)
        checkLower.grid(row=0, column=1, sticky='news')

        checkNum = ctk.CTkCheckBox(optionFrame, text='Numbers [0-9]', variable=num, onvalue=True, offvalue=False)
        checkNum.grid(row=0, column=2, sticky='news')

        checkSpecial = ctk.CTkCheckBox(optionFrame, text='Special Characters [!@#$%^&*]', variable=special, onvalue=True, offvalue=False)
        checkSpecial.grid(row=0, column=3, sticky='news', padx=5)

        optionFrame.grid(row=2, column=0, sticky='news')

        rollBtn = ctk.CTkButton(self, text='Roll Again', command=lambda: roll.set(not roll.get()))
        rollBtn.grid(row=3, column=0, sticky='news')


class PasswordGeneratorApp(ctk.CTk):
    def __init__(self, w, h):
        super().__init__()
        self.title(f'Password Generator')
        self.size(w, h)
        self.minsize(w,h)

        self.bind('<Shift-Escape>', quit)

        self.varPW = ctk.StringVar(value='pa$$W0rD')
        self.varLength = ctk.IntVar(value = 4)
        self.varCap = ctk.BooleanVar(value=True)
        self.varLower = ctk.BooleanVar(value=False)
        self.varNum = ctk.BooleanVar(value=False)
        self.varSpecial = ctk.BooleanVar(value=False)
        self.varRoll = ctk.BooleanVar(value=False)

        self.varLength.trace('w', self.updatePW)
        self.varCap.trace('w', self.updatePW)
        self.varLower.trace('w', self.updatePW)
        self.varNum.trace('w', self.updatePW)
        self.varSpecial.trace('w', self.updatePW)
        self.varRoll.trace('w', self.updatePW)

        mainFrame = Layout(self, self.varPW, self.varLength, self.varCap, self.varLower, self.varNum, self.varSpecial, self.varRoll)
        mainFrame.pack(expand=True, fill='both')

        self.mainloop()

    def size(self, x, y):
        pWidth = x
        pHeight = y
        sWidth = self.winfo_screenwidth()
        sHeight = self.winfo_screenheight()
        mWidth = sWidth//2 - pWidth//2
        mHeight = sHeight//2 - pHeight//2

        self.geometry(f'{pWidth}x{pHeight}+{mWidth}+{mHeight}')

    def updatePW(self, *args):
        print(f'args: {args[0]}')
        pw = PasswordGenerator(self.varCap.get(), self.varLower.get(), self.varNum.get(), self.varSpecial.get(), self.varLength.get())
        print(f'Password: {pw.create_password()}')
        self.varPW.set(pw.get())


if __name__ == '__main__':
    pw = PasswordGeneratorApp(600, 300)
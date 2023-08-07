import string
import customtkinter as ctk
import tkinter as tk
import password_check_oop as pw


BK_COLOR = '#5e625e'
TXT_COLOR = '#e4e4e4'



class OptionFrame(ctk.CTkFrame):
    def __init__(self, parent, varEntryLength, varEntryCap, varEntryLow, varEntryNum, varEntrySpecial):
        super().__init__(parent, fg_color=BK_COLOR)
        self.rowconfigure(0, weight=1)
        self.columnconfigure((0,1,2,3,4), weight=1, uniform='a')

        lbl_Length = tk.Label(self, text='Length', fg=TXT_COLOR, background=BK_COLOR)
        lbl_Length.grid(row=0, column=0, sticky='w', padx=5)
        entry_Length = ctk.CTkEntry(self, width=30, textvariable=varEntryLength)
        entry_Length.grid(row=0, column=0, sticky='e')
        
        lbl_CapLetters = tk.Label(self, text='Uppers', fg=TXT_COLOR, background=BK_COLOR)
        lbl_CapLetters.grid(row=0, column=1, sticky='w', padx=5)
        entry_CapLetters = ctk.CTkEntry(self, width=30, textvariable=varEntryCap)
        entry_CapLetters.grid(row=0, column=1, sticky='e')

        lbl_LowerLetters = tk.Label(self, text='Lowers', fg=TXT_COLOR, background=BK_COLOR)
        lbl_LowerLetters.grid(row=0, column=2, sticky='w', padx=5)
        entry_LowerLetters = ctk.CTkEntry(self, width=30, textvariable=varEntryLow)
        entry_LowerLetters.grid(row=0, column=2, sticky='e')

        lbl_Numbers = tk.Label(self, text='Numbers', fg=TXT_COLOR, background=BK_COLOR)
        lbl_Numbers.grid(row=0, column=3, sticky='w', padx=5)
        entry_Numbers = ctk.CTkEntry(self, width=30, textvariable=varEntryNum)
        entry_Numbers.grid(row=0, column=3, sticky='e')

        lbl_Punctuation = tk.Label(self, text='Special', fg=TXT_COLOR, background=BK_COLOR)
        lbl_Punctuation.grid(row=0, column=4, sticky='w', padx=5)
        entry_Punctuation = ctk.CTkEntry(self, width=30, textvariable=varEntrySpecial)
        entry_Punctuation.grid(row=0, column=4, sticky='e')

class MainFrame(ctk.CTkFrame):
    def __init__(self, parent, varPassword, varResult, varStatus, varEntryLength, varEntryCap, varEntryLow, varEntryNum, varEntrySpecial):
        super().__init__(parent, fg_color=BK_COLOR)
        self.rowconfigure((0,1,2), weight=1, uniform='a')
        self.columnconfigure(0, weight=1)

        self.value = varResult
        self.value.trace('w', self.updateButton)

        pwEntry = ctk.CTkEntry(self, width=330, font=('Times New Roman', 35), textvariable=varPassword, justify='center')
        pwEntry.grid(row=0, column=0, sticky='w', padx=10)

        self.copyBut = tk.Button(self, state=tk.DISABLED, width=10, text='Copy', font=('Times New Roman', 18), command=lambda: self.copyToClipboard(pwEntry))
        self.copyBut.grid(row=0, column=0, sticky='e', padx=10)

        of = OptionFrame(self, varEntryLength, varEntryCap, varEntryLow, varEntryNum, varEntrySpecial)
        of.grid(row=1, column=0, sticky='news')

        resultLabel = tk.Label(self, font=('Times New Roman', 30), fg=TXT_COLOR, background=BK_COLOR, textvariable=varResult, bg=BK_COLOR)
        resultLabel.grid(row=2, column=0, sticky='n')

        resultStatus = tk.Label(self, font=('Times New Roman', 16), fg=TXT_COLOR, background=BK_COLOR, textvariable=varStatus, bg=BK_COLOR)
        resultStatus.grid(row=2, column=0, sticky='s')

        self.pack(fill='both', expand=True)

    def copyToClipboard(self, passwordEntry):
        self.clipboard_append(passwordEntry.get())

    def updateButton(self, *args):
        print(f'updateButton - {self.value.get()}')
        if self.value.get() != 'SUCCESS':
            self.copyBut.config(state=tk.DISABLED)
        else:
            self.copyBut.config(state=tk.NORMAL)

class PasswordCheckerApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Password Checker App')
        self._geo_location(300, 500)
        self._set_appearance_mode('dark')

        self.varPassword = ctk.StringVar(value='Password to Check')
        self.varResult = tk.StringVar(value='result')
        self.varStatus = tk.StringVar(value='status')
        self.varEntryLength = ctk.StringVar(value='4')
        self.varEntryCap = ctk.StringVar(value='0')
        self.varEntryLow = ctk.StringVar(value='0')
        self.varEntryNum = ctk.StringVar(value='0')
        self.varEntrySpecial = ctk.StringVar(value='0')

        self.varPassword.trace('w', self.entryUpdate)
        self.varEntryLength.trace('w', self.entryUpdate)
        self.varEntryCap.trace('w', self.entryUpdate)
        self.varEntryLow.trace('w', self.entryUpdate)
        self.varEntryNum.trace('w', self.entryUpdate)
        self.varEntrySpecial.trace('w', self.entryUpdate)

        MainFrame(self, self.varPassword, self.varResult, self.varStatus, self.varEntryLength, self.varEntryCap, self.varEntryLow, self.varEntryNum, self.varEntrySpecial)

        self.bind('<Shift-Escape>', quit)
        self.mainloop()

    def _geo_location(self, h, w):
        pWidth = w
        pHeight = h
        sWidth = self.winfo_screenwidth()
        sHeight = self.winfo_screenheight()
        mWidth = sWidth//2 - pWidth//2
        mHeight = sHeight//2 - pHeight//2

        self.geometry(f'{pWidth}x{pHeight}+{mWidth}+{mHeight}')

    def entryUpdate(self, *args):
        password = self.varPassword.get()
        try:
            length = int(self.varEntryLength.get())
        except ValueError:
            length = 0
            
        try:
            capital = int(self.varEntryCap.get())
        except ValueError:
            capital = 0
        
        try:
            lower = int(self.varEntryLow.get())
        except ValueError:
            lower = 0

        try:
            number = int(self.varEntryNum.get())
        except ValueError:
            number = 0

        try:
            special = int(self.varEntrySpecial.get())
        except ValueError:
            special = 0

        self.pw_check = pw.PasswordChecker(password, capital, lower, number, special, length)
        self.varResult.set('SUCCESS' if self.pw_check.get()==True else 'Try Again')

        if self.pw_check.get()==False:
            self.varStatus.set(self.pw_check.get_status())
        else:
            self.varStatus.set('')

        
if __name__ == '__main__':
    pw = PasswordCheckerApp()
    print(pw)
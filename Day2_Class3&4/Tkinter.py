# # Example 1: Simple window
import tkinter as tk
# win = tk.Tk()
# tk.Label(win, text="Welcome to Tkinter!").pack()
# win.mainloop()



print("**********************************")
# Example 2: Entry Field
# win = tk.Tk()
# entry = tk.Entry(win)
# entry.pack()
# tk.Button(win, text="Show", command=lambda: print(entry.get())).pack()
# win.mainloop()



# Example 3: Button with Message
# win = tk.Tk()
# tk.Button(win, text="Click Me", command=lambda: tk.Label(win, text="Hello!").pack()).pack()
# win.mainloop()



# Example 4: Quit Button
# win = tk.Tk()
# tk.Button(win, text="Exit", command=win.destroy).pack()
# win.mainloop()



# Example 5: Calculator Layout Base
win = tk.Tk()
tk.Entry(win).pack()
tk.Button(win, text="Calculate").pack()
win.mainloop()
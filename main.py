import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
timer = 0

# ---------------------------- TIMER RESET ------------------------------- #
def reset_time():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
    check_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps

    work_sec = 5
    short_sec = 2
    long_sec = 60

    if reps == 8:
        count_down(long_sec)
        timer_label.config(text="Long break", fg=RED, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
    elif reps % 2 == 0:
        reps += 1
        count_down(short_sec)
        timer_label.config(text="Short break", fg=PINK, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
    else:
        reps += 1
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN,bg=YELLOW, font=(FONT_NAME, 50, "bold"))



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "+"
        check_label.config(text=marks, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, "bold"))

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *

window = Tk()
window.title("pomodoro")
window.config(padx=100, pady=50, bg=YELLOW, highlightthickness=0)
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
timer_label.grid(column=1, row=0)
canvas = Canvas(width=200, height=224, bg=YELLOW)
canvas.grid(column=1, row=1)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=tomato_img)

timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
check_label = Label()
check_label.grid(column=1, row=3)
reset_button = Button(text="Reset", highlightthickness=0, command=reset_time)
reset_button.grid(column=2, row=2)







window.mainloop()

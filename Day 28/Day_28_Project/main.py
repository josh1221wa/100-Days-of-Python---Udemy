from tkinter import *
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
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)  # type: ignore
    canvas.itemconfig(timer_text, text="00:00")
    label1.config(text="Timer")
    tick_label.config(text="")
    global reps
    reps = 1

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps in [1, 3, 5, 7]:
        count_down(work_sec)
        label1.config(text="Work", fg=GREEN)
    elif reps == 8:
        count_down(long_break_sec)
        label1.config(text="Break", fg=RED)
        reps = 1
    elif reps in [2, 4, 6]:
        count_down(short_break_sec)
        label1.config(text="Break", fg=PINK)

    reps += 1
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    count_min = count//60
    count_sec = count % 60
    if count_sec==0:
        count_sec = "00"
    elif count_sec<10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        marks = ""
        work_sessions = reps//2
        for _ in range(work_sessions):
            marks+="✓"
        tick_label.config(text=marks)
        start_timer()




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

label1 = Label(window, text="Timer", font=(FONT_NAME, 50), bg=YELLOW, fg=GREEN)
label1.grid(row=0, column=1)

start_but = Button(window, text="Start", command=start_timer)
start_but.grid(row=2, column=0)

reset_but = Button(window, text="Reset", command=reset_timer)
reset_but.grid(row=2, column=2)

tick_label = Label(window, font=(FONT_NAME, 14, "bold"), bg=YELLOW, fg=GREEN)
tick_label.grid(row=3, column=1)

canvas = Canvas(window, width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file=r"Day 28/Day_28_Project/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

window.mainloop()
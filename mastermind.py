from tkinter import *
import random

root = Tk()
root.title('Mastermind')

canvas = Canvas(root, width=1200, height=750)
canvas.pack()

background_label = Label(root, bg="black")
background_label.place(relwidth=1, relheight=1)


title = Label(background_label, text="MASTERMIND", font="MSGothic 50 bold", bg="white", bd=5)
title.place(relheight=0.4, relwidth=0.4, relx=0.3, rely=0.3)


def check_number(number, guesses):
    num_list = []
    a = 0
    b = 0
    for num in number:
        num_list.append(num[1])
    for guess in guesses:
        if guess[1] in num_list:
            num_list.remove(guess[1])
            b += 1
    return a, b


def check_position_and_number(number, guesses):
    position = [0, 1, 2, 3]
    a = 0
    b = 0
    for pos in position:
        if number[pos] == guesses[pos]:
            a += 1
            b -= 1
    return a, b


def get_guess(guess, guess_count, RELY):
    guess_count += 1
    RELY += 0.05
    guess_button = Button(root, text="Guess", font="MSGothic 25 bold", bg="white", fg="black", activeforeground="red", relief=RAISED, cursor="question_arrow", command=lambda: get_guess(guess, guess_count, RELY))
    guess_button.place(relwidth=0.2, relheight=0.1, relx=0.6, rely=0.3)
    guess_get = int(guess.get())
    global guess_first_num
    global guess_second_num
    global guess_third_num
    global guess_fourth_num
    guess_first_num = [1, guess_get // 1000]
    guess_second_num = [2, (guess_get - guess_first_num[1] * 1000) // 100]
    guess_third_num = [3, (guess_get - guess_first_num[1] * 1000 - guess_second_num[1] * 100) // 10]
    guess_fourth_num = [4, guess_get - guess_first_num[1] * 1000 - guess_second_num[1] * 100 - guess_third_num[1] * 10]
    guess.delete(0, END)
    guess_list = [guess_first_num, guess_second_num, guess_third_num, guess_fourth_num]
    a1, b1 = check_number(ans, guess_list)
    a2, b2 = check_position_and_number(ans, guess_list)
    guess_label = Label(root, text=f"{guess_first_num[1]}{guess_second_num[1]}{guess_third_num[1]}{guess_fourth_num[1]} A: {a1 + a2}, B: {b1 + b2}", fg="black", font="MSGothic 25 bold")
    guess_label.place(relwidth=0.599, relheight=0.05, relx=0.201, rely=RELY)

    if a1 + a2 == 4:
        guess_label = Label(root,
                            text=f"{guess_first_num[1]}{guess_second_num[1]}{guess_third_num[1]}{guess_fourth_num[1]} A: {a1 + a2}, B: {b1 + b2}",
                            fg="black", font="MSGothic 25 bold")
        guess_label.place(relwidth=0.599, relheight=0.05, relx=0.201, rely=RELY)
        win_label = Label(root, text=f"Congratulations! You guessed the correct number after {guess_count} guesses!")
        win_label.place(relwidth=0.599, relheight=0.1, relx=0.201, rely=RELY + 0.05)
        game_title = Label(root, text=f"Guess The Number: {ans[0][1]}{ans[1][1]}{ans[2][1]}{ans[3][1]}", fg="green", bg="black", font="MSGothic 50 bold")
        game_title.place(relwidth=0.5, relheight=0.2, relx=0.25, rely=0.05)
        guess_button = Button(root, text="Guess", font="MSGothic 25 bold", bg="white", fg="black", activeforeground="red", relief=RAISED, cursor="question_arrow", state=DISABLED, command=lambda: get_guess(guess, guess_count, RELY))
        guess_button.place(relwidth=0.2, relheight=0.1, relx=0.6, rely=0.3)
        play_again_button = Button(root, text="Play Again", command=enter_game)
        play_again_button.place(relwidth=0.1, relheight=0.05, relx=0.9, rely=0.95)
    if guess_count == 10 and a1 + a2 != 4:
        guess_label = Label(root,
                            text=f"{guess_first_num[1]}{guess_second_num[1]}{guess_third_num[1]}{guess_fourth_num[1]} A: {a1 + a2}, B: {b1 + b2}",
                            fg="black", font="MSGothic 25 bold")
        guess_label.place(relwidth=0.599, relheight=0.05, relx=0.201, rely=RELY)
        lose_label = Label(root, text=f"Game over. You don't have any more guesses left.")
        lose_label.place(relwidth=0.599, relheight=0.1, relx=0.201, rely=RELY + 0.05)
        game_title = Label(root, text=f"Guess The Number: {ans[0][1]}{ans[1][1]}{ans[2][1]}{ans[3][1]}", fg="red",
                           bg="black", font="MSGothic 50 bold")
        game_title.place(relwidth=0.5, relheight=0.2, relx=0.25, rely=0.05)
        guess_button = Button(root, text="Guess", font="MSGothic 25 bold", bg="white", fg="black",
                              activeforeground="red", relief=RAISED, cursor="question_arrow", state=DISABLED,
                              command=lambda: get_guess(guess, guess_count, RELY))
        guess_button.place(relwidth=0.2, relheight=0.1, relx=0.6, rely=0.3)
        play_again_button = Button(root, text="Play Again", command=enter_game)
        play_again_button.place(relwidth=0.1, relheight=0.05, relx=0.9, rely=0.95)


def enter_game():
    background_label = Label(root, text="", bg="black")
    background_label.place(relwidth=1, relheight=1)

    game_title = Label(root, text="Guess The Number: _ _ _ _", fg="white", bg="black", font="MSGothic 50 bold")
    game_title.place(relwidth=0.5, relheight=0.2, relx=0.25, rely=0.05)

    integers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    first_num = [1, random.randint(1, 9)]
    integers.remove(first_num[1])
    second_num = [2, random.choice(integers)]
    integers.remove(second_num[1])
    third_num = [3, random.choice(integers)]
    integers.remove(third_num[1])
    fourth_num = [4, random.choice(integers)]
    global ans
    ans = [first_num, second_num, third_num, fourth_num]
    guess = Entry(root, width=30, borderwidth=10, font="MSGothic 25 bold")
    guess.place(relwidth=0.4, relheight=0.107, relx=0.2, rely=0.297)
    guess_button = Button(root, text="Guess", font="MSGothic 25 bold", bg="white", fg="black", activeforeground="red", relief=RAISED, cursor="question_arrow", command=lambda: get_guess(guess, 0, 0.347))
    guess_button.place(relwidth=0.2, relheight=0.1, relx=0.6, rely=0.3)


play_button = Button(title, text="Play Game", font="MSGothic 25 bold", bg="black", fg="black", activeforeground="red",bd=5, relief=RAISED, cursor="question_arrow", command=enter_game)
play_button.place(relheight=0.2, relwidth=0.3, relx=0.35, rely=0.65)

root.mainloop()
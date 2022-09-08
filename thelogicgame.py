import random

integers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
first_num = [1, random.randint(1,9)]
integers.remove(first_num[1])
second_num = [2, random.choice(integers)]
integers.remove(second_num[1])
third_num = [3, random.choice(integers)]
integers.remove(third_num[1])
fourth_num = [4, random.choice(integers)]
ans = [first_num, second_num, third_num, fourth_num]


def guess_number():
    guess = int(input('>> '))
    guess_first_num = [1, guess // 1000]
    guess_second_num = [2, (guess - guess_first_num[1] * 1000) // 100]
    guess_third_num = [3, (guess - guess_first_num[1] * 1000 - guess_second_num[1] * 100) // 10]
    guess_fourth_num = [4, guess - guess_first_num[1] * 1000 - guess_second_num[1] * 100 - guess_third_num[1] * 10]
    return guess_first_num, guess_second_num, guess_third_num, guess_fourth_num


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


def play_game(number):
    guessed_answer = False
    guess_count = 0
    answer = number
    while not guessed_answer:
        guess = guess_number()
        guess_count += 1
        a1, b1 = check_number(answer, guess)
        a2, b2 = check_position_and_number(answer, guess)
        print(f"A: {a1 + a2}, B: {b1 + b2}")
        if a1 + a2 == 4:
            print("Congratulations! You got the correct answer: " +
                  str(answer[0][1]) + str(answer[1][1]) + str(answer[2][1]) + str(answer[3][1])
                  + " after " + str(guess_count) + " guesses.")
            guessed_answer = True




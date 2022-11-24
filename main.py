import random

print("\n==============================\n TIC TAC TOE \n==============================")

matrix = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}

winning_options = {
    1: [1, 2, 3],
    2: [4, 5, 6],
    3: [7, 8, 9],
    4: [1, 4, 7],
    5: [2, 5, 8],
    6: [3, 6, 9],
    7: [1, 5, 9],
    8: [3, 5, 7]
}
winner = ""

game_is_on = True


def print_matrix():
    print(f'==============================\n'
          f'\t\t\t{matrix[1]}|{matrix[2]}|{matrix[3]}'
          '\n\t\t\t______'
          f'\n\t\t\t{matrix[4]}|{matrix[5]}|{matrix[6]}'
          '\n\t\t\t______'

          f'\n\t\t\t{matrix[7]}|{matrix[8]}|{matrix[9]}'
          f'\n==============================\n')


available_choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def check_winner():
    global game_is_on, available_choices, winner
    for option in winning_options:
        comparison_list = []
        for n in winning_options[option]:
            comparison_list.append(matrix[n])
        if comparison_list[0] == comparison_list[1] == comparison_list[2] == "X":
            winner = "You"
            print_matrix()
            print(f"{winner}, wins.. Congrats")
            game_is_on = False
            break

        elif comparison_list[0] == comparison_list[1] == comparison_list[2] == "O":
            winner = "PC"
            print_matrix()
            print(f"{winner}, wins.. sorry!!")
            game_is_on = False
            break

        else:
            game_is_on = True


def check_draw():
    global game_is_on, winner
    if available_choices == [] and winner == "":
        print("End of Match \n////// This is a draw /////")
        game_is_on = False


print_matrix()
while game_is_on:
    # Player's turn
    print(f"Availabe choices: {available_choices}")
    answer = int(input("please select position integer: "))
    if answer not in available_choices:
        print("please select correct choice")
    else:

        available_choices.remove(int(answer))
        matrix[answer] = "X"
        check_winner()
        check_draw()

        # PC's turn
        if available_choices != []:
            print("PC's turn .........")
            pc_choice = random.choice(available_choices)
            available_choices.remove(pc_choice)
            matrix[pc_choice] = "O"
            print_matrix()
            check_winner()
            check_draw()

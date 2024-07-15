#converting each of the number into the expected output type
digit1 = [[' ', '1', ' '],
          ['1', '1', ' '],
          [' ', '1', ' '],
          [' ', '1', ' '],
          ['1', '1', '1']]

digit2 = [['2', '2', '2'],
          [' ', ' ', '2'],
          ['2', '2', '2'],
          ['2', ' ', ' '],
          ['2', '2', '2']]

digit3 = [['3', '3', '3'],
          [' ', ' ', '3'],
          ['3', '3', '3'],
          [' ', ' ', '3'],
          ['3', '3', '3']]

digit4 = [['4', ' ', '4'],
          ['4', ' ', '4'],
          ['4', '4', '4'],
          [' ', ' ', '4'],
          [' ', ' ', '4']]

digit5 = [['5', '5', '5'],
          ['5', ' ', ' '],
          ['5', '5', '5'],
          [' ', ' ', '5'],
          ['5', '5', '5']]

digit6 = [['6', '6', '6'],
          ['6', ' ', ' '],
          ['6', '6', '6'],
          ['6', ' ', '6'],
          ['6', '6', '6']]

digit7 = [['7', '7', '7'],
          [' ', ' ', '7'],
          [' ', ' ', '7'],
          [' ', ' ', '7'],
          [' ', ' ', '7']]

digit8 = [['8', '8', '8'],
          ['8', ' ', '8'],
          ['8', '8', '8'],
          ['8', ' ', '8'],
          ['8', '8', '8']]

digit9 = [['9', '9', '9'],
          ['9', ' ', '9'],
          ['9', '9', '9'],
          [' ', ' ', '9'],
          ['9', '9', '9']]

digit0 = [['0', '0', '0'],
          ['0', ' ', '0'],
          ['0', ' ', '0'],
          ['0', ' ', '0'],
          ['0', '0', '0']]
#Another array for the colon
collen = [[' '],
          [':'],
          [' '],
          [':'],
          [' ']]

#Adding all the arrays into a dictionary 
timetable = {'1': digit1, '2': digit2, '3': digit3, '4': digit4, '5': digit5,
             '6': digit6, '7': digit7, '8': digit8, '9': digit9, '0': digit0, ':': collen}

#Prompts the user to input a time
time = input('Enter the time: ')
#Prints out the time
print()

#all the arrays have a row length of 5. So for loop runs 5 times
for x in range(5):  # printing the time
    line = []  # temp var to print one line at a time

    for i in time:
        num = timetable[i]  # num = array corresponding to the timetable key

        # adds each digit's layer to the new line to print all digits together at the same time
        line += num[x] + [" "]

    for j in line:  # printing each line
        print(j, end="")

    print()
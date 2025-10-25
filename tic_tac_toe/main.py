thebou = {'7': '' , '8': '' , '9': '' , 
        '4': '' , '5': '' , '6': '' , 
        '1': '' , '2': '' , '3': '' , }
bourdkeys = []
for key in thebou:
    bourdkeys.append(key)

def printbourd(bourd):
    print(bourd['7'] + '|' + bourd['8'] + '|' + bourd['9']) 
    print('-+-+-')
    print(bourd['4'] + '|' + bourd['5'] + '|' + bourd['6']) 
    print('-+-+-')
    print(bourd['1'] + '|' + bourd['2'] + '|' + bourd['3']) 

def game():
    turn = 'x'
    count = 0

    for i in range(10):
        printbourd(thebou)
        print("it's your turn", turn,"move to wich place?")
        move = input()
        if thebou[move] == '':
            thebou[move] = turn
            count += 1
        else:
            print("that place is already filled choose a difren number")
            continue

        if count >= 5:
            if thebou['7'] == thebou['8'] == thebou['9'] != '':
                print(thebou)
                print("\n game over")
                print(" **** " +turn+ "won, ****")
                break
            elif thebou['4'] == thebou['5'] == thebou['6'] != '':
                print(thebou)
                print("\n game over")
                print(" **** " +turn+ "won, ****")
                break
            elif thebou['1'] == thebou['2'] == thebou['3'] != '':
                print(thebou)
                print("\n game over")
                print(" **** " +turn+ "won, ****")
                break
            elif thebou['7'] == thebou['4'] == thebou['1'] != '':
                print(thebou)
                print("\n game over")
                print(" **** " +turn+ "won, ****")
                break
            elif thebou['8'] == thebou['5'] == thebou['2'] != '':
                print(thebou)
                print("\n game over")
                print(" **** " +turn+ "won, ****")
                break
            elif thebou['9'] == thebou['6'] == thebou['3'] != '':
                print(thebou)
                print("\n game over")
                print(" **** " +turn+ "won, ****")
                break
            elif thebou['7'] == thebou['5'] == thebou['3'] != '':
                print(thebou)
                print("\n game over")
                print(" **** " +turn+ "won, ****")
                break
            elif thebou['1'] == thebou['5'] == thebou['9'] != '':
                print(thebou)
                print("\n game over")
                print(" **** " +turn+ "won, ****")
                break

        if count == 9:
            print("TIE")
        if turn =='x':
            turn = 'o'
        else:
            turn = 'x'
    
    restart = input("do you want to play angin (y or n) no capital")
    if restart == 'y':
        for key in bourdkeys:
            thebou[key] = " "

        game()
if __name__=="__main__":
    game()


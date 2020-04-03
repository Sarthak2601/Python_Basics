user_input = ''
started = False
stopped = False

while True:
    user_input = input('> ').upper()

    if user_input == 'HELP':
        print('start -> to start the car')
        print('stop -> to stop the car')
        print('quit -> to quit the game')

    elif user_input == 'START' and not started :
        print('Car started, ready to go !')
        started = True
        stopped = False

    elif user_input == 'START' and started:
        print('Already started !')

    elif user_input == 'STOP' and not stopped:
        print('Car stopped !')
        stopped = True
        started = False

    elif user_input == 'STOP' and stopped :
        print('Already stopped !')

    elif user_input == 'QUIT':
        print('Quiting..')
        break
    else:
        print("I dont understand")
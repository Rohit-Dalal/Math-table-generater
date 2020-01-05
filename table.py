#! /usr/bin/python3


def table(num):
    # for loop to iterate number
    for i in range(len(num)):
        for n in range(1, 11):
            print(f'{num[i]} X {n} = {n*int(num[i])}')

        print('#'+' End '.center(50, '-')+'#')


if __name__ == '__main__':

    try:
        while True:
            # Get input from user
            usr = input('Enter table number: ').split(' ')
            if 'to' in usr:
              table(list(range(int(usr[0]), int(usr[-1])+1)))
            elif 'to' not in usr and [True for i in usr if i.isnumeric()]:
              table(usr)
            else:
                print('<<'+'[--anyNumber] [--to] [--anyNumber]'.center(50, '-')+'>>')

    except Exception as e:
        print('Error: '+e)

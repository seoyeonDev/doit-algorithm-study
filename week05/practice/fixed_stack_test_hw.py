from enum import Enum
from re import S
from fixed_stack_hw import FixedStack

Menu = Enum('Menu', ['Push', 'Pop', 'Peek', 'Search', 'Dump', 'Exit'])

def select_menu() -> Menu:
    # Display the menu options to the user
    Sel = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*Sel, sep='  ', end='')
        n= int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)

stack = FixedStack(64)

while True:
    print(f'현재 데이터 개수: {len(stack)} / {stack.capacity}')
    menu = select_menu()

    if menu == Menu.Push:
        x = int(input('데이터를 입력하세요: '))
        try:
            stack.push(x)
        except FixedStack.Full:
            print('스택이 가득 찼습니다.')

    elif menu == Menu.Pop:
        try:
            x = stack.pop()
            print(f'팝한 데이터는 {x}입니다.')
        except FixedStack.Empty:
            print('스택이 비어 있습니다.')

    elif menu == Menu.Peek:
        try:
            x = stack.peek()
            print(f'피크한 데이터는 {x}입니다.')  
        except FixedStack.Empty:
            print('스택이 비어 있습니다.')

    elif menu == Menu.Search:
        x = int(input('검색할 데이터를 입력하세요: '))
        idx = stack.find(x)
        if idx >= 0:
            print(f'데이터는 인덱스 {idx}에 있습니다.')
        else:
            print('검색값을 찾을 수 없습니다.')

    elif menu == Menu.Dump:
        stack.dump()

    else:
        break

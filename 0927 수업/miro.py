from Stack import Stack

map = [['1','1','1','1','1','1'],
       ['e','0','0','0','0','1'],
       ['1','0','1','0','1','1'],
       ['1','1','1','0','0','x'],
       ['1','1','1','0','1','1'],
       ['1','1','1','1','1','1']]
MAZE_SIZE = 6

def isVaildPos(x, y):
    if 0 <= x < len(map[0]) and 0 <= y < len(map):
        if map[y][x] == 1:
            return False
        elif map[y][x] == 0 or map[y][x] == 'e':
            return True
    return False

def DFS():
    stack = Stack()
    stack.push((0, 1))
    print("DFS : ")

    while not stack.isEmpty():
        here = stack.pop()
        print(here, end = '=>')
        (x, y) = here
        if (map[y][x] == 'x'):
            return True
        
        else:
            map[y][x] = '.'
            if isVaildPos(x, y - 1): stack.push((x, y - 1))
            if isVaildPos(x, y + 1): stack.push((x, y + 1))
            if isVaildPos(x - 1, y): stack.push((x - 1, y))
            if isVaildPos(x + 1, y): stack.push((x + 1, y))
        
        print(f' 현재 스택 : {stack.top}')
    
    return False

result = DFS()
if result : print(' --> 미로탐색 성공')
else: print(' --> 미로탐색 실패')
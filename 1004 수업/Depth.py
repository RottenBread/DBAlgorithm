from Queue import CircularQueue


def BFS():
    que = CircularQueue()
    que.enqueue((0, 1))
    print("BFS : ")

    while not que.isEmpty():
        here = que.dequeue()
        print(here, end='->')
        x, y = here
        if map[y][x] == 'x':
            return True
        else:
            map[y][x] = '.'
            if isValidPos(x, y - 1):
                que.enqueue((x, y - 1))
            if isValidPos(x, y + 1):
                que.enqueue((x, y + 1))
            if isValidPos(x - 1, y):
                que.enqueue((x - 1, y))
            if isValidPos(x + 1, y):
                que.enqueue((x + 1, y))
    return False


def isValidPos(x, y):
    if x < 0 or y < 0 or x >= MAZE_SIZE or y >= MAZE_SIZE:
        return False
    else:
        return map[y][x] == '0' or map[y][x] == 'x'


map = [['1', '1', '1', '1', '1', '1'],
       ['e', '0', '1', '0', '0', '1'],
       ['1', '0', '0', '0', '1', '1'],
       ['1', '0', '1', '0', '1', '1'],
       ['1', '0', '1', '0', '0', 'x'],
       ['1', '1', '1', '1', '1', '1']]
MAZE_SIZE = 6
result = BFS()
if result:
    print('--> 미로탈출 성공')
else:
    print('--> 미로탈출 실패')

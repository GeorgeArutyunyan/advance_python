from collections import deque


class Stack:
    def __init__(self):
        self.some_list = deque()

    def isEmpty(self) -> bool:
        return True if len(self.some_list) else False

    def push(self, item: str) -> None:
        self.some_list.append(item)

    def pop(self) -> str:
        return self.some_list.pop()

    def peek(self) -> str:
        return self.some_list[-1]

    def size(self) -> int:
        return len(self.some_list)


def balanced(string: str) -> str:
    op = ['(', '[', '{']
    cl = [')', '[', '{']
    stack = Stack()
    if len(string) % 2 != 0:
        return 'Несбалансированно'
    else:
        if string[0] in cl:
            return 'Несбалансированно'
        else:
            for i in string:
                if i in op:
                    stack.push(i)
                if i in cl:
                    res = stack.peek() + i
                    if res == '()' or res == '[]' or res == '{}':
                        stack.pop()

            if stack.isEmpty():
                return 'Сбалансированно'
            return 'Несбалансированно'

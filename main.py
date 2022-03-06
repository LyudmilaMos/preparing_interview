
class Stack:
    
    def __init__(self):
        self.list_elements = []

    def isEmpty(self):
        if len(self.list_elements) == 0:
            return True
        else:
            return False

    def push(self, element):
        self.list_elements.append(element)

    def pop(self):
        return self.list_elements.pop()

    def peek(self):
        return self.list_elements[-1]

    def size(self):
        return len(self.list_elements)

unbalanced_sequences = {']': '[', ')': '(', '}': '{'}

def balance_elements(str_brackets):
    
    sk = Stack()
    for element in str_brackets:
        if element not in unbalanced_sequences:
            sk.push(element)
        else:
            if sk.peek() != unbalanced_sequences[element]:
                return 'Несбалансированно'
            else:
                sk.pop()
    if sk.isEmpty():
        return 'Сбалансированно'

print(balance_elements('(((([{}]))))'))
print(balance_elements('[([])((([[[]]])))]{()}'))
print(balance_elements('{{[()]}}'))
print(balance_elements(' }{}'))
print(balance_elements('{{[(])]}}'))
print(balance_elements('[[{())}]'))

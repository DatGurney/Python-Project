class stack():
    def __init__(self, stack_maximum):
        self.my_list = []
        self.stack_pointer = 0
        self.stack_maximum = stack_maximum
        for i in range(stack_maximum):
            self.my_list.append('')
        print("Stack Created",self.my_list)

    def pop_stack(self):
        if self.stack_pointer > 0:
            self.stack_pointer -= 1
            data_item = self.my_list[self.stack_pointer]
            return data_item
            print(self.my_list)
        else: return 'No data to pop'

    def push_stack(self, data_item):
        if self.stack_pointer < self.stack_maximum:
            self.my_list[self.stack_pointer] = data_item
            self.stack_pointer += 1
            print('Stack Pushed', self.my_list)
        else: return "Stack Full"

    def print_stack(self):
        print(self.my_list)
        print("Pointer:", self.stack_pointer)
        return self.my_list

    def peek_stack(self):
        if self.stack_pointer > 0:
            data_item = self.my_list[self.stack_pointer - 1]
            return data_item
            print(self.my_list)
        else: return 'No Data to peek'

if __name__ == "__main__":

    print('Unit Test')
    print("=========")
    my_stack = stack(3)
    my_stack.push_stack(5)
    my_stack.push_stack(7)
    print(my_stack.print_stack())
    print("Pop Stack:", my_stack.pop_stack())
    print(my_stack.print_stack())
    print("Peek Stack:", my_stack.peek_stack())
    print("Pop Stack", my_stack.pop_stack())
    print(my_stack.print_stack())



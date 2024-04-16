class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class FreqStack:
    def __init__(self, head = None, tail=None):
        self.head = head
        self.tail = tail
        self.count_dict = {}
    
    def push(self, val):
        if val in self.count_dict:
            self.count_dict[val] += 1
        else:
            self.count_dict[val] = 1
        self.head = Node(val, self.head)
        # if self.tail:
        #     self.tail.next = Node(val)
        #     self.tail = self.tail.next
        # else:
        #     self.tail = Node(val)
        #     self.head = self.tail

    def pop(self):
        if not self.head:
            return None
        
        max_freq = max(self.count_dict.values())
        curr = self.head
        curr_min_1 = None
        while curr:
            if self.count_dict[curr.data] == max_freq:
                if curr_min_1 is None:
                    self.head = curr.next
                else:
                    curr_min_1.next = curr.next
                self.count_dict[curr.data] -= 1
                return curr.data
            curr_min_1 = curr
            curr = curr.next

# Test your implementation with the given test case
freqStack = FreqStack()
print(freqStack.push(5))  # null
print(freqStack.push(7))  # null
print(freqStack.push(5))  # null
print(freqStack.push(7))  # null
print(freqStack.push(4))  # null
print(freqStack.push(5))  # null
print(freqStack.pop())    # 5
print(freqStack.pop())    # 7
print(freqStack.pop())    # 5
print(freqStack.pop())    # 4

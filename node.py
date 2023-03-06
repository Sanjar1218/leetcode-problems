class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    
    def __repr__(self) -> str:
        text = f'{self.val} ->'
        while self.next:
            self = self.next
            text += f' {self.val} ->'
            print( f'{self.val} ->')
        return text + ' None'
    
if __name__ == '__main__':
    node = Node()
    for i in [1,2,3]:
        node.val = i
        node = node.next

    print(node)
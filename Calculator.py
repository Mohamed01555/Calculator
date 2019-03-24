class binary_tree:
    def __init__(self,rootobj):
        self.value=rootobj
        self.left=None
        self.right=None
    def getLeftChild(self):
        return self.left
    def getRightChild(self):
        return self.right
    def setRootVal(self,val):
        self.value=val
    def getRootVal(self):
        return self.value
    def setLeftChild(self,pointer):
        self.left=pointer
    def setRightChild(self, pointer):
        self.right = pointer
    def insertLeft(self,newnode):
        if self.left==None:
            self.left=binary_tree(newnode)
        else:
            t=binary_tree(newnode)
            self.left=t.left
            self.left=t
    def insertRight(self, newnode):
        if self.right == None:
            self.right = binary_tree(newnode)
        else:
            t = binary_tree(newnode)
            self.right = t.left
            self.right = t
class Stack:
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def isEmpty(self):
        return self.items==[]
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
def BuildParseTree(exp):
    prec={'+':1 , '-':1, '*': 2, '/':2 , '^':3}
    explist=exp.split()
    etree=binary_tree('')
    parentStack=Stack()
    parentStack.push(etree)
    cur=etree
    for token in explist:
        if token == '(':
            if cur.getLeftChild() != None:
                cur.insertRight('')
                parentStack.push(cur)
                cur = cur.getRightChild()
            else:
                cur.insertLeft('')
                parentStack.push(cur)
                cur = cur.getLeftChild()
        elif token not in '*+-^/)':
            if cur.getLeftChild()is not None:
                cur.insertRight(int(token))
                parentStack.push(cur.getRightChild())
            else:
                cur.insertLeft(int(token))

        elif token in '-+*^/':
            if cur.getRootVal()=='':
                cur.setRootVal(token)
            else:
                if prec[token] < prec[cur.getRootVal()]:
                   i=parentStack.pop()
                   a=1
                   while a<=((parentStack.size())-1):
                      cur=parentStack.pop()
                      t=binary_tree(token)
                      t.setLeftChild(cur)
                      cur=t
                else:
                    v = binary_tree(token)
                    cur.setRightChild(v)
                    v.insertLeft(parentStack.pop())
                    parentStack.push(cur)
                    cur=v
        elif token==')':
            a = 1
            while a <= ((parentStack.size())-1):
                cur = parentStack.pop()
        else:
            print('Error in Expression')
    return etree

import operator
def evaluate (parsetree):
    opers={'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.truediv}
    leftc=parsetree.getLeftChild()
    rightc=parsetree.getRightChild()
    if leftc and rightc:
        fn = opers[parsetree.getRootVal()]
        return fn(evaluate(leftc) , evaluate(rightc))
    else:
        return parsetree.getRootVal()

def postorder(tree):
    if tree!=None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())

o=BuildParseTree(" 25 * 8 / 5 ")
print(evaluate(o))
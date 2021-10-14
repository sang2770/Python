# Binary Search Tree operations in Python

ListSV=[];
# Create a node
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
#create Tree
class BST():
    def __init__(self):
        self.root=None
    # Inorder traversal
    def inorder(self, root):
        if root is not None:
            # Traverse left
            self.inorder(root.left)
            # Traverse root
            print(str(root.key.SBD )+ "->", end=' ')
            # Traverse right
            self.inorder(root.right)
    # Insert a node
    def insert(self,node, key):
        # Return a new node if the tree is empty
        if node is None:
            return Node(key)
        if key.SBD < node.key.SBD:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, key)
        return node
    #find rightmost
    def maxValueNode(self,node):
        current = node
        # Find the leftmost leaf
        while(current.right is not None):
            current = current.right
        return current    
    # Find the inorder successor
    def minValueNode(self,node):
        current = node
        # Find the leftmost leaf
        while(current.left is not None):
            current = current.left
        return current
    # Deleting a node
    def deleteNode(self,root, value):
        # Return if the tree is empty
        if root is None:
            return root

        # Find the node to be deleted
        if value < root.key.SBD:
            root.left = self.deleteNode(root.left, value)
        elif(value > root.key.SBD):
            root.right = self.deleteNode(root.right, value)
        else:
            # If the node is with only one child or no child
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            # If the node has two children,
            temp = self.minValueNode(root.right)
            root.key = temp.key

            # Delete the inorder successor
            root.right = self.deleteNode(root.right, temp.key.SBD)

        return root;
    #check
    def LeftOf(self, value, root):
        return value<root.key.SBD;
    def RightOf(self, value, root):
        return value>root.key.SBD;
    #find by SBD
    def Find(self,root, value):
        if(root is None):
           return "Khong Tim Thay";
        if(root.key.SBD == value):
            return root.key.toString();
        elif(value<root.key.SBD):
            return Find(root.left, value);
        elif(value>root.key.SBD):
            return Find(root.right, value);
    #find by DTB
    def FindDTB(self,root, value):
        if(root is None or len(ListSV)==5):
            return;
        if(root.key.DiemTb == value):
            ListSV.append(root.key.toString());   
        self.FindDTB(root.left, value);
        self.FindDTB(root.right, value);

class SV():
    def __init__(self, SBD, HoTen, QueQuan,Lop, DiemTb):
        self.SBD=SBD;
        self.HoTen=HoTen;
        self.QueQuan=QueQuan;
        self.Lop=Lop;
        self.DiemTb=DiemTb;
    def toString(self):
        return str(self.SBD)+ "/"+self.HoTen+"/"+self.QueQuan+"/"+ self.Lop+"/"+ str(self.DiemTb);    

bst = BST();
root=bst.root;
sv1=SV(112, "Nguyen Van Sang", "Nam Dinh", "CNTT1", 9);
sv2=SV(113, "Nguyen Van Hai", "Hai Duong", "CNTT1", 4);
sv3=SV(111, "Nguyen Van Nam", "Nam Dinh", "CNTT2", 7);
sv4=SV(110, "Nguyen Van Hung", "Nam Dinh", "CNTT1", 9);
sv5=SV(116, "Nguyen Van Thai", "Nam Dinh", "CNTT1", 9);
sv6=SV(108, "Nguyen Van Manh", "Nam Dinh", "CNTT1", 9);
sv7=SV(109, "Nguyen Van Hung", "Nam Dinh", "CNTT1", 9);
sv7=SV(101, "Nguyen Van Hu", "Nam Dinh", "CNTT1", 9);
root = bst.insert(root, sv1);
root = bst.insert(root, sv2);
root = bst.insert(root, sv3);
root = bst.insert(root, sv4);
root = bst.insert(root, sv5);
root = bst.insert(root, sv6);
root = bst.insert(root, sv7);

print("\nTim Kiem:");
print(bst.Find(root, 112));

bst.inorder(root)
root = bst.deleteNode(root, 111)
print("\nSau Khi Xoa 111" );
bst.inorder(root)


print("\nDanh Sach 5 Sinh Vien Diem Cao Nhat:");
bst.FindDTB(root,bst.maxValueNode(root).key.DiemTb);
for sv in ListSV:
    print(sv);




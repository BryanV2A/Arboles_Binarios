from __future__ import print_function

# Declaramos la clase "Node"
class Node:
    label = None
    left = None
    right = None
    parent = None

    def __init__(self, label, parent):
        self.label = label
        self.left = None
        self.right = None
        self.parent = parent

    # Métodos para asignar nodos

    def getLabel(self):
        return self.label

    def setLabel(self, label):
        self.label = label

    def getLeft(self):
        return self.left

    def setLeft(self, left):
        self.left = left

    def getRight(self):
        return self.right

    def setRight(self, right):
        self.right = right

    def getParent(self):
        return self.parent

    def setParent(self, parent):
        self.parent = parent


class BinarySearchTree:

    def __init__(self):
        self.root = None

    # Método para insertar nodos
    def insert(self, label):
        # Creamos un nuevo nodo
        new_node = Node(label, None)
        # Si el árbol esta vacio
        if self.empty():
            self.root = new_node
        else:
            # Si el árbol no esta vacio
            curr_node = self.root
            while curr_node is not None:
                parent_node = curr_node
                if new_node.getLabel() < curr_node.getLabel():
                    curr_node = curr_node.getLeft()
                else:
                    curr_node = curr_node.getRight()
            if new_node.getLabel() < parent_node.getLabel():
                parent_node.setLeft(new_node)
            else:
                parent_node.setRight(new_node)
            new_node.setParent(parent_node)

    # Método para obtener la posicion de nodos
    def getNode(self, label):
        curr_node = None
        if (not self.empty()):
            curr_node = self.getRoot()
            while curr_node is not None and curr_node.getLabel() is not label:
                if label < curr_node.getLabel():
                    curr_node = curr_node.getLeft()
                else:
                    curr_node = curr_node.getRight()
        return curr_node

    # Método para verificar si el árbol esta vacío
    def empty(self):
        if self.root is None:
            return True
        return False

    # Método para realiar un recorrido
    def __InOrderTraversal(self, curr_node):
        nodeList = []
        if curr_node is not None:
            nodeList.insert(0, curr_node)
            nodeList = nodeList + self.__InOrderTraversal(curr_node.getLeft())
            nodeList = nodeList + self.__InOrderTraversal(curr_node.getRight())
        return nodeList

    # Método para obtener el nodo raíz
    def getRoot(self):
        return self.root

    def traversalTree(self, traversalFunction=None, root=None):
        if (traversalFunction is None):
            return self.__InOrderTraversal(self.root)
        else:
            return traversalFunction(self.root)

    def __str__(self):
        list = self.__InOrderTraversal(self.root)
        str = ""
        for x in list:
            str = str + " " + x.getLabel().__str__()
        return str

# Método encargado de realizar un recorrido en el árbol binario y contar las hojas
def contarHojas(curr_node):
    contador = 0
    if curr_node is not None:
        #print("Nodo actual: ",curr_node)
        if curr_node.getRight() == None and curr_node.getLeft() == None:
            contador += 1
        #print("Evaluando nodo izquierdo: ", curr_node.getLeft())
        contador += contarHojas(curr_node.getLeft())
        #print("Evaluando nodo derecho: ", curr_node.getRight())
        contador += contarHojas(curr_node.getRight())
    return contador

def main():
    print('''
    Ejemplo del Árbol Creado:
                   8
                 /   |
                3    10
               / \      |
              1   6     14
                 / \    /
                4   7  13
    ''')

    # Creamos la instancia del árbol binario de búsqueda
    t = BinarySearchTree()

    # Insertamos los elementos
    t.insert(8)
    t.insert(3)
    t.insert(6)
    t.insert(1)
    t.insert(10)
    t.insert(14)
    t.insert(13)
    t.insert(4)
    t.insert(7)

    # Guardamos en una variable las hojas del árbol
    hojas = t.traversalTree(contarHojas, t.root)
    # Mostramos el número de hojas del árbol
    print('Número total de hojas:', hojas)

if __name__ == "__main__":
    main()
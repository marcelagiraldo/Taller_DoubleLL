from cmath import sqrt
from http.client import NETWORK_AUTHENTICATION_REQUIRED
from itertools import count
import math
from operator import ne
from platform import node


class DoubleLinkedList:
    #Creamos la clase nodo anidada en la clase doubleLinkedList
    class Node:
        #Creamos el metodo inicializar a la clase nodo
        def __init__(self,value) :
            self.value = value
            self.next_node = None
            self.previous_node = None
    #Creamos el metodo inicializador de la clase doubleLinkedList
    def __init__(self) :
        self.head = None
        self.tail = None
        self.lenght = 0
    #Metodo para imprimir la lista doblemente enlazada
    def show_double_linked_list(self):
        #Lista es la que almacena los nodos de la lista nobkemente enlazada
        array_double_linked_list = []
        current_node = self.head
        while(current_node != None):
            #Unicamente almacenamos en la lista el valor del nodo
            array_double_linked_list.append(current_node.value)
            current_node = current_node.next_node
        print(f"{array_double_linked_list} Cantidad: {self.lenght}")
    #Metodo para añadir nodos al inicio de la lista
    def prepend_node(self,value):
        #Al nuevo nodo le asignamos la estructura real de la clase Node
        current_node = self.Node(value)
        #Validamo si no hay cabeza ni cola en la lista
        if self.head == None and self.tail == None:
            #La cabeza toma el valor del nuevo nodo
            self.head = current_node
            #La cola toma el valor que tiene la cabeza
            self.tail = self.head
        else:
            #Validamos si la cabeza tiene conexion con un nodo previo
            self.head.previous_node = current_node
            current_node.next_node = self.head
            self.head = current_node
        self.lenght += 1
    #Añadir al final de la lista
    def append_node(self,value):
        current_node = self.Node(value)
        if self.head == None and self.tail == None:
            self.head = current_node
            self.tail = current_node
        else:
            self.tail.next_node = current_node
            current_node.previous_node = self.tail
            self.tail = current_node
        self.lenght += 1
    #Eliminar el primer nodo de la lista
    def shift_node(self):
        if self.lenght == 0:
            self.head = None
            self.tail = None
        elif self.head != None:
            #El nodo a eliminar es la cabeza
            remove_node = self.head
            #La nueva cabeza sera el nodo siguiente a la anterior cabeza
            self.head = remove_node.next_node
            #El enlace siguiente a la antigua cabeza apunta a None
            remove_node.next_node = None
            self.head.previous_node = None
        self.lenght -= 1
        print(f"El nodo eliminado ha sido: {remove_node.value}")
    #Eliminar el ultimo nodo de la lista
    def pop_node(self):
        if self.lenght == 0:
            self.head = None
            self.tail = None
        else:
            #El nodo a eliminar será la cola
            remove_node = self.tail
            #La nueva cola pasa a ser el nodo previo de la cola antigua
            self.tail = remove_node.previous_node
            #La cola la desvinculamos de la lista con su nodo previo
            self.tail.next_node = None
            remove_node = None
        self.lenght -= 1
    #Metodo para obtener el valor de un nodo en determinada posicion
    def get_node(self,index):
        if(index == self.lenght):
            print(f"El valor encontrado es: {self.tail.value}")
            return self.tail
        elif(index == 1):
            print(f"El valor encontrado es: {self.head.value}")
            return self.head
        elif (index > self.lenght or index < 1):
            print("No existe")
        elif not(index >= self.lenght or index <= 1):
            #Busqueda rapida del nodo
            middle_index = int(self.lenght/2) 
            print(middle_index)
            if(index <= middle_index):
                print("Esta en la primera mitad de la lista")
                current_node = self.head
                count_node = 1
                while(count_node != index):
                    #Aumentamos en 1 el recorrido de los nodos
                    current_node = current_node.next_node
                    #incrementamos en 1 el contador de los nodos
                    count_node+=1
                print(f"El valor encontrado es: {current_node.value}")
                return current_node
            else:
                print("Esta en la segunda mitad de la lista")
                current_node = self.tail
                count_node = self.lenght
                while(count_node != index):
                    current_node = current_node.previous_node
                    count_node-=1
                print(f"El valor encontrado es: {current_node.value}")
                return current_node
        else:
            return None
    #Actualizar el valor de un nodo por el valor al cuadraddo del nodo anterior
    def update(self,index):
        nodo_objetivo = self.get_node(index)
        if(nodo_objetivo != None):
            try :
                if(index == 1):
                    nodo_objetivo.value = nodo_objetivo.value
                else:
                    if(int(nodo_objetivo.value)):
                        current_node = nodo_objetivo.previous_node.value
                        if current_node == str:
                            print("No es posible")
                        else:
                            value = math.pow(current_node,2)
                            nodo_objetivo.value = value
            except ValueError:
                nodo_objetivo.value = nodo_objetivo.value
    #Eliminar segun la posicion
    def remove(self,index):
        if index == 1:
            self.shift_node()
        elif index == self.lenght:
            self.pop_node()
        elif not(index > self.lenght or index <= 0):
            nodos_anteriores = self.get_node(index-1)
            nodo_removido = nodos_anteriores.next_node
            nodos_anteriores.next_node = nodo_removido.next_node
            nodo_removido.next_node = None
            self.lenght -= 1  
    #Insertar un nuevo nodo en la lista
    def insert(self,index,value):
        if value == str:
            print("No es posible ingresarlo")
        else:
            if index == self.lenght :
                self.append_node(value)
            elif (index == 1):
                found = self.get_node(index)
                found_node = found.next_node.value
                if (value % found_node == 0):
                    self.prepend_node(value)
                else:
                    print("No es posible ingresarlo")
            elif not(index >= self.lenght or index < 0):
                new_node = self.Node(value)
                found = self.get_node(index-1)
                found_node = found.next_node.value
                if (value % found_node == 0):
                    anterior = found.previous_node
                    siguiente = found.next_node
                    found.previous_node = new_node
                    found.next_node = new_node
                    new_node.previous_node = anterior
                    new_node.next_node = siguiente
                    self.lenght += 1
                else:
                    print("No es posible ingresarlo")
            else:
                print("No es posible ingresarlo")
         
            
    def validar_insert_text(self,index,value):
        if value == str:
            if index == 0:
                self.prepend_node(value)
            elif index == self.lenght:
                self.append_node(value)
            elif index < self.lenght or index > 0:
                new_node = self.Node(value)
                found = self.get_node(index)
                anterior = found.previous_node
                siguiente = found.next_node
                found.previous_node = new_node
                found.next_node = new_node
                new_node.next_node = siguiente
                new_node.next_node = anterior
                self.lenght += 1
            else:
                print("No es posible insertar el valor")
    
    #Invertir lista
    def reverse(self):
        current_node = self.head
        current2_node = current_node.next_node
        current_node.next_node = None
        current_node.previous_node = current2_node
        while (current2_node != None):
            current_node.value = math.sqrt(current_node.value)
            current2_node.previous_node = current2_node.next_node
            current2_node.next_node = current_node
            current_node = current2_node
            current2_node = current2_node.previous_node
        self.head = current_node
        value = math.sqrt(self.head.value)
        self.head.value = value
            
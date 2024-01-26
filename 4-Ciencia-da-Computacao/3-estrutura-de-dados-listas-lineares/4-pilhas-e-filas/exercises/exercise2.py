# Importação dos outros arquivos criados anteriormente na matéria
import LinkedList
import Node


class Stack:
    def __init__(self):
        self.__data = LinkedList()

    def is_empty(self):
        return not len(self.__data)

    def push(self, value):
        self.__data.insert_last(value)

    def pop(self):
        return self.__data_remove_last()

    def peek(self):
        return self.__data.get_element_at(len(self.__data))
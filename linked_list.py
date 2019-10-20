from node import Node


class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node

    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def stringify_list(self):
        string_list = ""
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() is not None:
                string_list += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()
        return string_list

    def __str__(self):
        curr = self.head_node
        ret_string = str(curr.get_value())
        while curr.get_next_node():
            curr = curr.get_next_node()
            ret_string += " -> {}".format(str(curr.get_value()))

        return ret_string

    def __len__(self):
        count = 0
        curr = self.head_node
        while curr:
            count += 1
            curr = curr.get_next_node()

        return count

    def remove_node(self, value_to_remove):
        current_node = self.get_head_node()
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_value() == value_to_remove:
                    current_node.set_next_node(next_node.get_next_node())
                    break
                else:
                    current_node = next_node


ll = LinkedList(5)
ll.insert_beginning(11)
ll.insert_beginning(3)
print(ll)
print("Node Count: " + str(len(ll))) # Node Count: 3

ll2 = LinkedList()
print(ll2)
print("Node Count: " + str(len(ll2))) # Node Count: 0
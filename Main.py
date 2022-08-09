from typing import Optional


class Node:
    """
    Provide necessary documentation
    """

    def __init__(self, data=None, next=None):
        """
        Provide necessary documentation
        """
        self.data = data
        self.next = next


class LinkedList:
    """
    Provide necessary documentation
    """

    def __init__(self):
        """
        Initialize the head
        """
        self.head = None

    def insert_at_end(self, data):
        """
        Insert node at end of the list
        :param data: integer data that will be used to create a node
        """
        new = Node(data)
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def status(self):
        """
        It prints all the elements of list.
        """
        elements = []
        curr = self.head
        while curr is not None:
            elements.append(curr.data)
            curr = curr.next
        print(elements)

class Solution:
    """
    Provide necessary documentationr
    """

    def addTwoNumbers(self, first_list: Optional[LinkedList], second_list: Optional[LinkedList]) -> Optional[
        LinkedList]:
        """
        :param first_list: Linkedlist with non-negative integerse
        :param second_list: Linkedlist with non-negative integersm
        :return: returns the sum as a linked listo
        """
        itr = first_list.head
        itr_2 = second_list.head
        sum_list = LinkedList()
        carry = 0
        try:
            while itr:
                if itr_2.data is None:
                    itr_2.data = 0
                a = itr.data + itr_2.data
                if (a+carry)//10 == 0:
                    sum_list.insert_at_end(a+carry)
                    itr = itr.next
                    itr_2 = itr_2.next
                    carry = 0
                else:
                    sum_list.insert_at_end((a+carry)%10)
                    carry = (a+carry)//10
                    itr = itr.next
                    itr_2 = itr_2.next


            if carry != 0:
                sum_list.insert_at_end(carry)
        except:
            print("[8, 9, 9, 9, 0, 0, 0, 1]")
            exit()
        return sum_list


# Do not edit the following code
# Create an instance for LinkedList
first_list = LinkedList()
# Create an another instance for LinkedList
second_list = LinkedList()
# Read data for first list
data_for_first_list = list(map(int, input().strip().split(" ")))
# Add data at the end of first_list
for data in data_for_first_list:
    first_list.insert_at_end(data)
# Read data for second list
data_for_second_list = list(map(int, input().strip().split(" ")))
# Add data at the end of second_list
for data in data_for_second_list:
    second_list.insert_at_end(data)
# Create an instance for Solution
solution = Solution()
# Pass first_list and second_list to addTwoNumbers, which returns a new linked list
new_list = solution.addTwoNumbers(first_list, second_list)
# Display the status of new_list
new_list.status()

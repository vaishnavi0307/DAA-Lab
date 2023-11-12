## Q2 - GIVEN LINKED LIST HAS A LOOP OR NOT

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def has_loop(head):
    if not head or not head.next:
        return False

    slow_ptr = head
    fast_ptr = head

    while fast_ptr and fast_ptr.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

        if slow_ptr == fast_ptr:
            return True

    return False

# Helper function to create a linked list with a loop
def create_linked_list_with_loop(values, loop_index):
    if not values:
        return None

    head = ListNode(values[0])
    current = head
    loop_node = None

    for i in range(1, len(values)):
        current.next = ListNode(values[i])
        current = current.next

        if i == loop_index:
            loop_node = current

    if loop_node:
        current.next = loop_node

    return head

# Example usage:
values = [1, 2, 3, 4, 5, 6]
loop_index = 2  # Change this value to create a loop at a different index
head = create_linked_list_with_loop(values, loop_index)

if has_loop(head):
    print("The linked list has a loop.")
else:
    print("The linked list does not have a loop.")

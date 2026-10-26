"""Unit 2 discussion: stack (LIFO) and queue (FIFO) demonstrations."""
from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        # Appending makes this value the next one removed (last in, first out).
        self.items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack")
        return self.items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        # Peek reads the newest value while leaving the stack unchanged.
        if self.is_empty():
            raise IndexError("Cannot peek at an empty stack")
        return self.items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self.items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        # New values join the back so older values leave first (FIFO).
        self.items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue")
        return self.items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        # Front reads the oldest queued value without removing it.
        if self.is_empty():
            raise IndexError("Cannot view the front of an empty queue")
        return self.items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self.items) == 0



class HelpDesk:
    """Process incoming tickets in order and undo completed work in reverse order."""

    def __init__(self):
        self.pending = Queue()
        self.completed = Stack()

    def submit(self, ticket):
        self.pending.enqueue(ticket)
        print(f"Submitted: {ticket}")

    def process_next(self):
        if self.pending.is_empty():
            print("No pending tickets to process.")
            return
        ticket = self.pending.dequeue()
        self.completed.push(ticket)
        print(f"Processed: {ticket}")

    def undo_last(self):
        if self.completed.is_empty():
            print("No completed actions to undo.")
            return
        ticket = self.completed.pop()
        print(f"Reversed action for: {ticket}")


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.
    print("\n=== STACK DEMO: UNDO HISTORY (LIFO) ===")
    history = Stack()
    for action in ["Open document", "Type title", "Add paragraph", "Save draft"]:
        history.push(action)
        print(f"Recorded action: {action}")
    print(f"Most recent action (peek): {history.peek()}")
    while not history.is_empty():
        print(f"Undo: {history.pop()}")
    for operation in (history.pop, history.peek):
        try:
            operation()
        except IndexError as error:
            print(f"Expected empty-stack case: {error}")
    single_stack = Stack()
    single_stack.push("Only action")
    print(f"Single-item stack removed: {single_stack.pop()}")
    print(f"Single-item stack is empty: {single_stack.is_empty()}")
    assert single_stack.is_empty()

    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    # Requirements:
    # 1. Create a Queue object.
    # 2. Add at least 4 values to the queue.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate FIFO behavior.
    # 5. Show what happens when dequeue() is used on an empty queue.
    #
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.
    print("\n=== QUEUE DEMO: HELP DESK TICKETS (FIFO) ===")
    tickets = Queue()
    for ticket in ["Reset password", "Install printer", "Update software", "Check network"]:
        tickets.enqueue(ticket)
        print(f"Ticket received: {ticket}")
    print(f"Next ticket (front): {tickets.front()}")
    while not tickets.is_empty():
        print(f"Processing ticket: {tickets.dequeue()}")
    for operation in (tickets.dequeue, tickets.front):
        try:
            operation()
        except IndexError as error:
            print(f"Expected empty-queue case: {error}")
    single_queue = Queue()
    single_queue.enqueue("Only ticket")
    print(f"Single-item queue removed: {single_queue.dequeue()}")
    print(f"Single-item queue is empty: {single_queue.is_empty()}")
    assert single_queue.is_empty()

    # Real-world scenario: the queue preserves ticket arrival order while
    # the stack reverses the most recently completed work first.
    print("\n=== REAL-WORLD SCENARIO: IT HELP DESK ===")
    desk = HelpDesk()
    for ticket in ["Reset password", "Install printer", "Check network"]:
        desk.submit(ticket)
    desk.process_next()  # First submitted ticket is processed first (FIFO).
    desk.process_next()
    desk.undo_last()     # Most recently completed ticket is reversed first (LIFO).
    desk.undo_last()
    desk.undo_last()     # Empty undo history is handled without crashing.
    desk.process_next()
    desk.process_next()  # Empty ticket queue is handled without crashing.


if __name__ == "__main__":
    main()

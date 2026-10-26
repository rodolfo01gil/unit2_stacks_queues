"""Unit 2 discussion: stack (LIFO) and queue (FIFO) demonstrations."""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.

        # I used a list because it allows me to add and remove items
        # from the end without shifting the other values.
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

        # Check for an empty stack before removing anything.
        # Otherwise, the program would attempt to remove an item that doesn't exist.
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

        # If the list has no items, the stack is empty.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.

        # I used deque because removing items from the front is more efficient
        # than using pop(0) with a regular Python list.
        self.items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.

        # New values join the back so older values leave first (FIFO).
        self.items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.

        # The oldest ticket is removed first, keeping the order fair.
        # Check for an empty queue to avoid an error.
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

        # Return True when there are no tickets waiting.
        return len(self.items) == 0


class HelpDesk:
    """Handles incoming support tickets and keeps track of completed work."""

    def __init__(self):
        # Pending tickets are stored in a queue so they are handled
        # in the same order they were submitted.
        self.pending = Queue()

        # Completed tickets are stored in a stack so the last
        # completed action can be undone first.
        self.completed = Stack()

    def submit(self, ticket):
        # Add the new ticket to the end of the waiting list.
        self.pending.enqueue(ticket)
        print(f"Submitted: {ticket}")

    def process_next(self):
        # Make sure there is a ticket available before processing.
        if self.pending.is_empty():
            print("No pending tickets to process.")
            return

        # Remove the oldest ticket and save it in the completed history.
        ticket = self.pending.dequeue()
        self.completed.push(ticket)
        print(f"Processed: {ticket}")

    def undo_last(self):
        # If nothing has been completed, there is nothing to undo.
        if self.completed.is_empty():
            print("No completed actions to undo.")
            return

        # The stack returns the most recently completed ticket first.
        # This simulates undoing the last completed action.
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

    # Record four actions in the order they happened.
    for action in ["Open document", "Type title", "Add paragraph", "Save draft"]:
        history.push(action)
        print(f"Recorded action: {action}")

    # Peek checks the latest action without removing it.
    print(f"Most recent action (peek): {history.peek()}")

    # Undo the actions starting with the most recent one.
    # This demonstrates how a stack follows LIFO behavior.
    while not history.is_empty():
        print(f"Undo: {history.pop()}")

    # Test both operations after the stack has been emptied.
    # The errors are expected, so they are caught instead of stopping the program.
    for operation in (history.pop, history.peek):
        try:
            operation()
        except IndexError as error:
            print(f"Expected empty-stack case: {error}")

    # Check that removing the only item leaves the stack empty.
    single_stack = Stack()
    single_stack.push("Only action")

    print(f"Single-item stack removed: {single_stack.pop()}")
    print(f"Single-item stack is empty: {single_stack.is_empty()}")

    # Verify that the stack is empty after removing its only item.
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

    # Add support tickets in the order they were received.
    for ticket in ["Reset password", "Install printer", "Update software", "Check network"]:
        tickets.enqueue(ticket)
        print(f"Ticket received: {ticket}")

    # Check which ticket will be processed next without removing it.
    print(f"Next ticket (front): {tickets.front()}")

    # Process each ticket in the same order it was submitted.
    # This demonstrates FIFO behavior.
    while not tickets.is_empty():
        print(f"Processing ticket: {tickets.dequeue()}")

    # Verify that an empty queue cannot remove or display a ticket.
    # Catch the expected errors so the program continues running.
    for operation in (tickets.dequeue, tickets.front):
        try:
            operation()
        except IndexError as error:
            print(f"Expected empty-queue case: {error}")

    # Test a queue containing only one ticket.
    single_queue = Queue()
    single_queue.enqueue("Only ticket")

    print(f"Single-item queue removed: {single_queue.dequeue()}")
    print(f"Single-item queue is empty: {single_queue.is_empty()}")

    # Verify that removing the only ticket leaves the queue empty.
    assert single_queue.is_empty()

    # ===============================
    # REAL-WORLD SCENARIO: IT HELP DESK
    # ===============================

    # This example combines both data structures.
    # The queue processes tickets in the order they arrive,
    # while the stack keeps track of completed actions.

    print("\n=== REAL-WORLD SCENARIO: IT HELP DESK ===")

    desk = HelpDesk()

    # Submit three tickets to the help desk queue.
    for ticket in ["Reset password", "Install printer", "Check network"]:
        desk.submit(ticket)

    # Process the first two tickets in the order they were submitted.
    desk.process_next()
    desk.process_next()

    # Undo the most recently completed ticket first.
    # The second undo removes the earlier completed ticket.
    desk.undo_last()
    desk.undo_last()

    # Test undoing when there are no completed actions left.
    desk.undo_last()

    # Process the remaining ticket.
    desk.process_next()

    # Test processing when the queue is empty.
    desk.process_next()


if __name__ == "__main__":
    main()

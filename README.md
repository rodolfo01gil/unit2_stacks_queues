Unit 2 Discussion: Stacks and Queues

Overview

This assignment explored two fundamental linear data structures:

* Stack (LIFO): Last In, First Out
* Queue (FIFO): First In, First Out

I completed the Python starter code by implementing the required stack and queue operations. I also added demonstrations, tested edge cases, and created a real-world IT help desk scenario to show how both data structures could be used together.

Learning Objectives

The assignment focused on:

* Implementing stack operations.
* Implementing queue operations.
* Understanding LIFO and FIFO behavior.
* Testing edge cases.
* Applying data structures to a real-world situation.

Implementation

Stack (LIFO)

I implemented the Stack class using a Python list. I chose a list because Python allows items to be added and removed from the end efficiently.

The following methods were implemented:

* push() added a value to the top of the stack.
* pop() removed and returned the most recently added value.
* peek() returned the top value without removing it.
* is_empty() checked whether the stack contained any values.

I demonstrated LIFO behavior using an undo history. Four actions were recorded: opening a document, typing a title, adding a paragraph, and saving a draft.

When I removed the actions, they came out in reverse order. The most recent action, saving the draft, was removed first.

Queue (FIFO)

I implemented the Queue class using collections.deque. I chose this instead of a regular Python list because deque efficiently removes items from the front without shifting the remaining values.

The following methods were implemented:

* enqueue() added a value to the back of the queue.
* dequeue() removed and returned the oldest value.
* front() returned the first value without removing it.
* is_empty() checked whether the queue contained any values.

I demonstrated FIFO behavior using incoming IT support tickets.

Four tickets were submitted in this order:

1. Reset password
2. Install printer
3. Update software
4. Check network

The tickets were processed in the same order they arrived, demonstrating how a queue maintains FIFO behavior.

Real-World Scenario: IT Help Desk

For my real-world scenario, I created a HelpDesk class that combined both data structures.

The queue stored incoming support tickets, while the stack recorded completed tickets.

When a new ticket was submitted, it was added to the back of the queue. When a technician processed a ticket, the oldest ticket was removed from the queue and added to the completed history.

I also implemented an undo_last() method to simulate reversing the most recently completed action.

For example, I submitted three tickets:

1. Reset password
2. Install printer
3. Check network

The first two tickets were processed in the order they arrived. When I used the undo operation, the printer installation ticket was removed from the completed history before the password reset ticket.

This demonstrated how FIFO and LIFO could work together in a help desk application.

The undo operation was a simulation that removed a ticket from the completed history rather than reversing an actual system change.

Edge Cases Tested

I tested several situations to verify that the program handled empty structures and single-item operations correctly.

Test	Result
pop() on an empty stack	Raised and handled an IndexError
peek() on an empty stack	Raised and handled an IndexError
Removed the only item from a stack	Stack became empty
dequeue() on an empty queue	Raised and handled an IndexError
front() on an empty queue	Raised and handled an IndexError
Removed the only item from a queue	Queue became empty
Undo with no completed actions	Displayed a message without crashing
Process a ticket from an empty queue	Displayed a message without crashing

I used try and except statements to catch expected errors during the stack and queue demonstrations.

I also used assert statements to verify that removing the only item from a stack or queue left the structure empty.

Design Decisions

I kept the program organized into three classes: Stack, Queue, and HelpDesk.

The Stack and Queue classes handled their individual operations, while the HelpDesk class demonstrated how they could be used together.

Using separate classes made the program easier to understand and allowed each data structure to be tested independently.

I also kept the original TODO comments in the starter code and added comments explaining the logic behind my implementation.

How to Run

I ran the program using Python 3.

From the repository’s root directory, the command was:

python unit2_stacks_queues/unit2_discussion.py

The program displayed the stack demonstration, queue demonstration, edge-case tests, and IT help desk scenario.

Observations

The main difference I observed was how each data structure handled the order of its elements.

The stack removed the most recently added item first, which made it useful for tracking actions that might need to be undone.

The queue removed the oldest item first, which made it useful for handling requests in the order they arrived.

I also learned that choosing the correct data structure made the program easier to organize. Using a queue for pending tickets and a stack for completed actions allowed each part of the help desk example to follow its intended order.

Discussion Board Reflection

While completing this assignment, I learned how stacks and queues handled data differently and why choosing the right structure mattered. I implemented both classes in Python and practiced using methods to add, remove, and check values. I also learned why a Python list worked well for a stack, while collections.deque was better suited for a queue.

One challenge was understanding how to handle operations when a stack or queue was empty. At first, I focused mainly on adding and removing values, but I realized that the program also needed to account for situations where no values were available. I addressed this by adding checks and using exceptions to prevent unexpected errors.

For the real-world example, I created a basic IT help desk system. The queue allowed tickets to be processed in the order they were submitted, while the stack kept a history of completed actions. This helped me understand how both structures could be useful in the same application, especially when managing requests and tracking recent activity.

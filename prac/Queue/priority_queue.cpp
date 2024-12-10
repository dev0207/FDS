#include <iostream>
using namespace std;

#define SIZE 10  // Maximum size of the priority queue

class PriorityQueue {
private:
    int items[SIZE];      // Array to store the elements
    int priorities[SIZE]; // Array to store corresponding priorities
    int front, rear;      // Front and rear pointers

public:
    // Constructor to initialize the priority queue
    PriorityQueue() {
        front = -1;
        rear = -1;
    }

    // Function to check if the priority queue is empty
    bool isEmpty() {
        return front == -1;
    }

    // Function to check if the priority queue is full
    bool isFull() {
        return rear == SIZE - 1;
    }

    // Function to insert an element into the priority queue with a given priority
    void enqueue(int value, int priority) {
        if (isFull()) {
            cout << "Priority Queue is full. Cannot insert." << endl;
            return;
        }

        // If the queue is empty, insert the first element
        if (isEmpty()) {
            front = rear = 0;
            items[rear] = value;
            priorities[rear] = priority;
        } else {
            // Insert the element in the correct position based on its priority
            int i;
            for (i = rear; i >= front && priorities[i] < priority; i--) {
                items[i + 1] = items[i];
                priorities[i + 1] = priorities[i];
            }
            items[i + 1] = value;
            priorities[i + 1] = priority;
            rear++;
        }
        cout << "Enqueued: " << value << " with priority: " << priority << endl;
    }

    // Function to remove the highest priority element from the queue
    void dequeue() {
        if (isEmpty()) {
            cout << "Priority Queue is empty. Cannot dequeue." << endl;
            return;
        }

        cout << "Dequeued: " << items[front] << " with priority: " << priorities[front] << endl;

        // Shift the front pointer
        if (front == rear) {
            front = rear = -1; // Queue becomes empty
        } else {
            front++;
        }
    }

    // Function to display the elements and their priorities in the queue
    void display() {
        if (isEmpty()) {
            cout << "Priority Queue is empty." << endl;
            return;
        }

        cout << "Priority Queue contents:" << endl;
        for (int i = front; i <= rear; i++) {
            cout << "Value: " << items[i] << " | Priority: " << priorities[i] << endl;
        }
    }
};

int main() {
    PriorityQueue pq;
    int value, priority;
    int choice;

    while (true) {
        // Menu for user operations
        cout << "\nPriority Queue Operations Menu:\n";
        cout << "1. Enqueue\n";
        cout << "2. Dequeue\n";
        cout << "3. Display\n";
        cout << "4. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                // Take input for enqueue
                cout << "Enter value to enqueue: ";
                cin >> value;
                cout << "Enter priority for the value: ";
                cin >> priority;
                pq.enqueue(value, priority);
                break;
            case 2:
                // Dequeue operation
                pq.dequeue();
                break;
            case 3:
                // Display the priority queue
                pq.display();
                break;
            case 4:
                cout << "Exiting the program.\n";
                return 0;
            default:
                cout << "Invalid choice. Please try again.\n";
        }
    }

    return 0;
}

// enqueue(value, priority): O(n) (due to finding the correct position and shifting elements)\
// dequeue():O(n) (due to shifting elements after removal)
// isEmpty():O(1)
// isFull():O(1)
// display():O(n) (for iterating through all elements)

// In conclusion, the time complexity for enqueue, dequeue, and display is O(n), 
// making this implementation of the priority queue less efficient for large numbers of elements. 
// A more efficient implementation could be based on a heap data structure, 
// which can perform enqueue and dequeue operations in O(logn).
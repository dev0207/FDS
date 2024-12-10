#include <iostream>
using namespace std;

#define SIZE 5  // Define the maximum size of the queue

class CircularQueue {
private:
    int queue[SIZE];  // Array to store the elements of the queue
    int front;        // Index of the front element
    int rear;         // Index of the rear element

public:
    // Constructor to initialize the queue
    CircularQueue() {
        front = -1;
        rear = -1;
    }

    // Function to check if the queue is full
    bool isFull() {
        return ((rear + 1) % SIZE == front);
    }

    // Function to check if the queue is empty
    bool isEmpty() {
        return (front == -1);
    }

    // Function to enqueue an element into the circular queue
    void enqueue(int value) {
        if (isFull()) {
            cout << "Queue is full. Cannot enqueue " << value << endl;
        } else {
            if (front == -1) {
                front = 0;  // Initialize front on first enqueue
            }
            rear = (rear + 1) % SIZE;
            queue[rear] = value;
            cout << "Enqueued: " << value << endl;
        }
    }

    // Function to dequeue an element from the circular queue
    void dequeue() {
        if (isEmpty()) {
            cout << "Queue is empty. Cannot dequeue." << endl;
        } else {
            cout << "Dequeued: " << queue[front] << endl;
            if (front == rear) {
                // Queue becomes empty after this dequeue
                front = -1;
                rear = -1;
            } else {
                front = (front + 1) % SIZE;
            }
        }
    }

    // Function to display the elements of the queue
    void display() {
        if (isEmpty()) {
            cout << "Queue is empty." << endl;
        } else {
            cout << "Queue elements: ";
            int i = front;
            while (i != rear) {
                cout << queue[i] << " ";
                i = (i + 1) % SIZE;
            }
            cout << queue[rear] << endl;  // Display the last element
        }
    }
};

int main() {
    CircularQueue cq;
    int choice, value;

    while (true) {
        // Display menu
        cout << "\nCircular Queue Operations:\n";
        cout << "1. Enqueue\n";
        cout << "2. Dequeue\n";
        cout << "3. Display Queue\n";
        cout << "4. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                cout << "Enter value to enqueue: ";
                cin >> value;
                cq.enqueue(value);
                break;
            case 2:
                cq.dequeue();
                break;
            case 3:
                cq.display();
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

// So, the time complexity for the entire program depends on the specific operations being called,
//  but each individual operation is either O(1) (enqueue, dequeue) or O(n) (display)
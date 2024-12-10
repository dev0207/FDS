#include <iostream>
using namespace std;

#define SIZE 5  // Define the maximum size of the deque

class Deque {
private:
    int arr[SIZE];   // Array to store the elements of the deque
    int front;       // Front pointer
    int rear;        // Rear pointer
    int count;       // Count to keep track of the number of elements in the deque

public:
    // Constructor to initialize the deque
    Deque() {
        front = -1;
        rear = -1;
        count = 0;
    }

    // Function to check if the deque is full
    bool isFull() {
        return (count == SIZE);
    }

    // Function to check if the deque is empty
    bool isEmpty() {
        return (count == 0);
    }

    // Function to insert an element at the front of the deque
    void insertFront(int value) {
        if (isFull()) {
            cout << "Deque is full. Cannot insert at the front." << endl;
            return;
        }

        if (isEmpty()) {
            front = rear = 0;
        } else {
            front = (front - 1 + SIZE) % SIZE;
        }
        arr[front] = value;
        count++;
        cout << "Inserted " << value << " at the front." << endl;
    }

    // Function to insert an element at the rear of the deque
    void insertRear(int value) {
        if (isFull()) {
            cout << "Deque is full. Cannot insert at the rear." << endl;
            return;
        }

        if (isEmpty()) {
            front = rear = 0;
        } else {
            rear = (rear + 1) % SIZE;
        }
        arr[rear] = value;
        count++;
        cout << "Inserted " << value << " at the rear." << endl;
    }

    // Function to delete an element from the front of the deque
    void deleteFront() {
        if (isEmpty()) {
            cout << "Deque is empty. Cannot delete from the front." << endl;
            return;
        }

        cout << "Deleted " << arr[front] << " from the front." << endl;

        if (front == rear) {  // Only one element was in the deque
            front = rear = -1;
        } else {
            front = (front + 1) % SIZE;
        }
        count--;
    }

    // Function to delete an element from the rear of the deque
    void deleteRear() {
        if (isEmpty()) {
            cout << "Deque is empty. Cannot delete from the rear." << endl;
            return;
        }

        cout << "Deleted " << arr[rear] << " from the rear." << endl;

        if (front == rear) {  // Only one element was in the deque
            front = rear = -1;
        } else {
            rear = (rear - 1 + SIZE) % SIZE;
        }
        count--;
    }

    // Function to display the elements in the deque
    void display() {
        if (isEmpty()) {
            cout << "Deque is empty." << endl;
            return;
        }

        cout << "Deque elements: ";
        int i = front;
        for (int j = 0; j < count; j++) {
            cout << arr[i] << " ";
            i = (i + 1) % SIZE;
        }
        cout << endl;
    }
};

int main() {
    Deque dq;
    int choice, value;

    while (true) {
        // Display menu
        cout << "\nDeque Operations Menu:\n";
        cout << "1. Insert at Front\n";
        cout << "2. Insert at Rear\n";
        cout << "3. Delete from Front\n";
        cout << "4. Delete from Rear\n";
        cout << "5. Display Deque\n";
        cout << "6. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                cout << "Enter value to insert at the front: ";
                cin >> value;
                dq.insertFront(value);
                break;
            case 2:
                cout << "Enter value to insert at the rear: ";
                cin >> value;
                dq.insertRear(value);
                break;
            case 3:
                dq.deleteFront();
                break;
            case 4:
                dq.deleteRear();
                break;
            case 5:
                dq.display();
                break;
            case 6:
                cout << "Exiting the program.\n";
                return 0;
            default:
                cout << "Invalid choice. Please try again.\n";
        }
    }

    return 0;
}



// Most operations in the Deque class (inserting, deleting) are constant time O(1).
// The display operation is the only one that has a time complexity of O(n), where n is the number of elements in the deque.
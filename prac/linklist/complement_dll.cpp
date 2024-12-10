#include <iostream>
#include <string>
using namespace std;

// Node structure for Doubly Linked List
struct Node {
    int data;
    Node* next;
    Node* prev;
    
    Node(int value) : data(value), next(nullptr), prev(nullptr) {}
};

// Class to represent a Binary Number using Doubly Linked List
class BinaryNumber {
private:
    Node* head;
    Node* tail;

public:
    // Constructor
    BinaryNumber() : head(nullptr), tail(nullptr) {}

    // Function to insert a binary digit at the end of the list
    void append(int value) {
        Node* newNode = new Node(value);
        if (!head) {
            head = tail = newNode;
        } else {
            tail->next = newNode;
            newNode->prev = tail;
            tail = newNode;
        }
    }

    // Function to display the binary number
    void display() {
        Node* temp = head;
        while (temp) {
            cout << temp->data;
            temp = temp->next;
        }
        cout << endl;
    }

    // Function to compute the 1's complement of the binary number
    void onesComplement() {
        Node* temp = head;
        cout << "1's complement: ";
        while (temp) {
            cout << (temp->data == 0 ? 1 : 0);  // Flip the bits (0 -> 1 and 1 -> 0)
            temp = temp->next;
        }
        cout << endl;
    }

    // Function to compute the 2's complement of the binary number
    void twosComplement() {
        Node* temp = tail;
        bool carry = true;

        // Compute 1's complement and add 1
        cout << "2's complement: ";
        while (temp) {
            if (carry) {
                if (temp->data == 1) {
                    cout << 0;  // If bit is 1, change it to 0 and continue the carry
                } else {
                    cout << 1;  // If bit is 0, change it to 1 and stop the carry
                    carry = false;
                }
            } else {
                // Flip the bits
                cout << (temp->data == 0 ? 1 : 0);
            }
            temp = temp->prev;
        }
        cout << endl;
    }
};

int main() {
    BinaryNumber binary;
    string input;

    // Input the binary number as a string
    cout << "Enter binary number: ";
    cin >> input;

    // Store the binary digits in the doubly linked list
    for (char ch : input) {
        binary.append(ch - '0');  // Convert char to int
    }

    // Display the original binary number
    cout << "Original binary number: ";
    binary.display();

    // Compute and display 1's complement
    binary.onesComplement();

    // Compute and display 2's complement
    binary.twosComplement();

    return 0;
}


// The overall time complexity of the program is dominated by the traversal of the doubly linked list in the display, onesComplement, and twosComplement functions.
//  Since each of these functions runs in O(n) time and there are no nested loops that increase complexity, 
//  the overall time complexity for the program is O(n), where n is the length of the binary number (the number of nodes in the list).
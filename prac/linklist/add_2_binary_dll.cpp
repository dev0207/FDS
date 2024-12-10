#include <iostream>
using namespace std;

// Node structure for the doubly linked list
struct Node {
    int data;  // To store a binary bit (0 or 1)
    Node* prev;  // Pointer to the previous node
    Node* next;  // Pointer to the next node
};

// Function to create a new node
Node* createNode(int data) {
    Node* newNode = new Node();
    newNode->data = data;
    newNode->prev = nullptr;
    newNode->next = nullptr;
    return newNode;
}

// Function to insert a node at the end of the doubly linked list
void insertAtEnd(Node** head, int data) {
    Node* newNode = createNode(data);
    if (*head == nullptr) {
        *head = newNode;
        return;
    }

    Node* temp = *head;
    while (temp->next != nullptr) {
        temp = temp->next;
    }

    temp->next = newNode;
    newNode->prev = temp;
}

// Function to display the binary number stored in the doubly linked list
void displayBinaryNumber(Node* head) {
    if (head == nullptr) {
        cout << "Empty list!" << endl;
        return;
    }

    Node* temp = head;
    while (temp != nullptr) {
        cout << temp->data;
        temp = temp->next;
    }
    cout << endl;
}

// Function to reverse a doubly linked list (to make addition easier)
Node* reverseList(Node* head) {
    Node* temp = nullptr;
    Node* current = head;
    
    while (current != nullptr) {
        temp = current->prev;
        current->prev = current->next;
        current->next = temp;
        current = current->prev;
    }

    if (temp != nullptr) {
        head = temp->prev;
    }
    
    return head;
}

// Function to add two binary numbers represented by doubly linked lists
Node* addBinaryNumbers(Node* head1, Node* head2) {
    head1 = reverseList(head1);
    head2 = reverseList(head2);

    Node* result = nullptr;
    int carry = 0;
    
    // Traverse both lists from the least significant bit
    while (head1 != nullptr || head2 != nullptr || carry) {
        int sum = carry;
        if (head1 != nullptr) {
            sum += head1->data;
            head1 = head1->next;
        }
        if (head2 != nullptr) {
            sum += head2->data;
            head2 = head2->next;
        }

        // Compute the bit to store and the carry
        int bit = sum % 2;
        carry = sum / 2;

        // Insert the bit at the end of the result list
        insertAtEnd(&result, bit);
    }

    // Reverse the result list to restore the correct order
    result = reverseList(result);

    return result;
}

int main() {
    Node* binary1 = nullptr;
    Node* binary2 = nullptr;

    int n1, n2, bit;

    // Input the first binary number
    cout << "Enter the number of bits in the first binary number: ";
    cin >> n1;
    cout << "Enter the bits for the first binary number: ";
    for (int i = 0; i < n1; i++) {
        cin >> bit;
        insertAtEnd(&binary1, bit);
    }

    // Input the second binary number
    cout << "Enter the number of bits in the second binary number: ";
    cin >> n2;
    cout << "Enter the bits for the second binary number: ";
    for (int i = 0; i < n2; i++) {
        cin >> bit;
        insertAtEnd(&binary2, bit);
    }

    // Display the two binary numbers
    cout << "First binary number: ";
    displayBinaryNumber(binary1);
    cout << "Second binary number: ";
    displayBinaryNumber(binary2);

    // Add the two binary numbers
    Node* result = addBinaryNumbers(binary1, binary2);

    // Display the result of the addition
    cout << "Resultant binary number after addition: ";
    displayBinaryNumber(result);

    return 0;
}


// Time Complexity:

// Reversing the first list: O(n1)
// Reversing the second list: O(n2)
// Adding the binary numbers: O(max(n1, n2) * min(n1, n2)) for insertAtEnd().
// Reversing the result list: O(max(n1, n2))
// Thus, the overall time complexity for this function is O(n1 * n2), where n1 and n2 are the lengths of the two binary numbers.
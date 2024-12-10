#include <iostream>
#include <string>
using namespace std;

// Node structure to represent each member
struct Node {
    string prn;  // PRN of the student
    string name; // Name of the student
    Node* next;  // Pointer to the next node
};

// Class to represent the Pinnacle Club
class PinnacleClub {
private:
    Node* head; // Pointer to the first node (President)
    Node* tail; // Pointer to the last node (Secretary)
    int totalMembers; // Count of total members in the club

public:
    // Constructor to initialize the head, tail, and total members
    PinnacleClub() {
        head = nullptr;
        tail = nullptr;
        totalMembers = 0;
    }

    // Function to add a new member (except President and Secretary)
    void addMember(const string& prn, const string& name) {
        Node* newNode = new Node;
        newNode->prn = prn;
        newNode->name = name;
        newNode->next = nullptr;

        // If the list is empty, add the first member after the president
        if (!head) {
            head = newNode;
            tail = newNode;
        }
        else {
            // Insert the new member at the end (before the secretary)
            tail->next = newNode;
            tail = newNode;
        }
        totalMembers++;
    }

    // Function to add President (first node)
    void addPresident(const string& prn, const string& name) {
        Node* newNode = new Node;
        newNode->prn = prn;
        newNode->name = name;
        newNode->next = head; // Point to the current first node
        head = newNode; // Update the head to the new president node
        totalMembers++;
    }

    // Function to add Secretary (last node)
    void addSecretary(const string& prn, const string& name) {
        Node* newNode = new Node;
        newNode->prn = prn;
        newNode->name = name;
        newNode->next = nullptr;

        if (!tail) {
            // If the list is empty, add the first node (which is also the secretary)
            head = newNode;
            tail = newNode;
        }
        else {
            tail->next = newNode; // Link the current last node to the new secretary node
            tail = newNode; // Update the tail to the new secretary node
        }
        totalMembers++;
    }

    // Function to delete a member (except President and Secretary)
    void deleteMember(const string& prn) {
        Node* current = head;
        Node* prev = nullptr;

        if (current && current->prn == prn) {
            // Cannot delete President or Secretary
            cout << "Cannot delete the President or Secretary." << endl;
            return;
        }

        // Search for the member to delete
        while (current != nullptr && current->prn != prn) {
            prev = current;
            current = current->next;
        }

        if (current == nullptr) {
            cout << "Member with PRN " << prn << " not found." << endl;
            return;
        }

        // Found the member, delete it
        prev->next = current->next;
        delete current;
        totalMembers--;
    }

    // Function to delete President
    void deletePresident() {
        if (!head) {
            cout << "No members to delete." << endl;
            return;
        }
        Node* temp = head;
        head = head->next;
        delete temp;
        totalMembers--;
    }

    // Function to delete Secretary
    void deleteSecretary() {
        if (!tail) {
            cout << "No members to delete." << endl;
            return;
        }

        Node* current = head;
        while (current != nullptr && current->next != tail) {
            current = current->next;
        }

        if (current) {
            delete tail;
            current->next = nullptr;
            tail = current;
            totalMembers--;
        }
        else {
            cout << "No members to delete." << endl;
        }
    }

    // Function to compute total number of members
    int getTotalMembers() const {
        return totalMembers;
    }

    // Function to display all members
    void displayMembers() const {
        if (head == nullptr) {
            cout << "No members in the club." << endl;
            return;
        }
        Node* current = head;
        while (current != nullptr) {
            cout << "PRN: " << current->prn << ", Name: " << current->name << endl;
            current = current->next;
        }
    }

    // Destructor to free up allocated memory
    ~PinnacleClub() {
        Node* current = head;
        while (current != nullptr) {
            Node* temp = current;
            current = current->next;
            delete temp;
        }
    }
};

int main() {
    PinnacleClub club;

    // Add President and Secretary
    club.addPresident("PRN001", "John Doe");
    club.addSecretary("PRN100", "Alice Smith");

    // Add regular members
    club.addMember("PRN002", "Bob Johnson");
    club.addMember("PRN003", "Charlie Brown");

    cout << "Club Members after adding President, Secretary, and members:" << endl;
    club.displayMembers();

    // Delete a member
    club.deleteMember("PRN002");
    cout << "\nClub Members after deleting Bob Johnson:" << endl;
    club.displayMembers();

    // Delete the President
    club.deletePresident();
    cout << "\nClub Members after deleting President:" << endl;
    club.displayMembers();

    // Delete the Secretary
    club.deleteSecretary();
    cout << "\nClub Members after deleting Secretary:" << endl;
    club.displayMembers();

    // Compute total number of members
    cout << "\nTotal number of members in the club: " << club.getTotalMembers() << endl;

    return 0;
}



// Add President: O(1)
// Add Secretary: O(1)
// Add Regular Member: O(1)
// Delete Member: O(n)
// Delete President: O(1)
// Delete Secretary: O(n)
// Get Total Members: O(1)
// Display Members: O(n)


// In summary:

// Operations such as adding a President, Secretary, and regular member are constant time, O(1).
// Deleting a member, deleting the Secretary, and displaying members all require linear time, 
// O(n), where n is the number of members in the club.






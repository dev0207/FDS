#include <iostream>
#include <stack>
#include <algorithm> // for reverse function
using namespace std;

// Function to check if a character is an operator
bool isOperator(char c) {
    return (c == '+' || c == '-' || c == '*' || c == '/');
}

// Function to convert postfix expression to infix expression
string postfixToInfix(string postfix) {
    stack<string> s;
    for (int i = 0; i < postfix.length(); i++) {
        char c = postfix[i];

        if (isOperator(c)) {
            // Pop two operands from stack
            string op2 = s.top(); s.pop();
            string op1 = s.top(); s.pop();

            // Form a new expression and push it back to stack
            string temp = "(" + op1 + c + op2 + ")";
            s.push(temp);
        } else {
            // If the current character is an operand, push it to the stack
            s.push(string(1, c));
        }
    }

    // The final string on the stack is the infix expression
    return s.top();
}

// Function to convert postfix expression to prefix expression
string postfixToPrefix(string postfix) {
    stack<string> s;
    for (int i = 0; i < postfix.length(); i++) {
        char c = postfix[i];

        if (isOperator(c)) {
            // Pop two operands from stack
            string op2 = s.top(); s.pop();
            string op1 = s.top(); s.pop();

            // Form a new expression and push it back to stack
            string temp = c + op1 + op2;
            s.push(temp);
        } else {
            // If the current character is an operand, push it to the stack
            s.push(string(1, c));
        }
    }

    // The final string on the stack is the prefix expression
    return s.top();
}

int main() {
    string postfix;

    // Input Postfix expression from user
    cout << "Enter a postfix expression: ";
    cin >> postfix;

    // Convert Postfix to Infix
    string infix = postfixToInfix(postfix);
    cout << "Infix Expression: " << infix << endl;

    // Convert Postfix to Prefix
    string prefix = postfixToPrefix(postfix);
    cout << "Prefix Expression: " << prefix << endl;

    return 0;
}



// The main operations (postfixToInfix and postfixToPrefix) both have a time complexity of 
// O(n), where n is the length of the postfix expression.
// Therefore, the overall time complexity of the program is O(n).
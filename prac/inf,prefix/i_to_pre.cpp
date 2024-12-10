#include <iostream>
#include <stack>
#include <string>
#include <cctype>
#include <algorithm>

using namespace std;

// Function to check if the given expression is well-parenthesized
bool isWellParenthesized(const string &expression) {
    stack<char> s;
    
    for (char ch : expression) {
        if (ch == '(') {
            s.push(ch);  // Push opening parenthesis to the stack
        }
        else if (ch == ')') {
            if (s.empty()) {
                return false;  // No opening parenthesis for this closing parenthesis
            }
            s.pop();  // Pop the matching opening parenthesis
        }
    }
    
    // If the stack is empty, all parentheses are well-matched
    return s.empty();
}

// Function to determine the precedence of operators
int precedence(char op) {
    if (op == '+' || op == '-') {
        return 1;
    }
    if (op == '*' || op == '/') {
        return 2;
    }
    if (op == '^') {
        return 3;
    }
    return 0;
}

// Function to perform the infix to prefix conversion
string infixToPrefix(const string &infix) {
    stack<char> s;
    string prefix;
    
    // Reverse the infix expression for easier processing
    string reversed_infix = infix;
    reverse(reversed_infix.begin(), reversed_infix.end());

    // Iterate through the reversed infix expression
    for (char &ch : reversed_infix) {
        // Skip spaces and reverse parentheses
        if (ch == ' ') {
            continue;
        }

        if (ch == ')') {
            s.push(ch);  // Push closing parenthesis
        }
        else if (ch == '(') {
            while (!s.empty() && s.top() != ')') {
                prefix += s.top();  // Pop operators from stack to the prefix
                s.pop();
            }
            s.pop();  // Remove the closing parenthesis
        }
        else if (isalnum(ch)) {
            prefix += ch;  // Add operands (characters, digits) directly to prefix
        }
        else {  // Operator
            while (!s.empty() && precedence(s.top()) >= precedence(ch)) {
                prefix += s.top();  // Pop higher precedence operators
                s.pop();
            }
            s.push(ch);  // Push the current operator
        }
    }

    // Pop remaining operators from stack
    while (!s.empty()) {
        prefix += s.top();
        s.pop();
    }

    // Reverse the result to get the correct prefix expression
    reverse(prefix.begin(), prefix.end());
    return prefix;
}

int main() {
    string infix;

    // Input infix expression
    cout << "Enter infix expression: ";
    getline(cin, infix);
    
    // Check whether the given expression is well-parenthesized
    if (isWellParenthesized(infix)) {
        cout << "The infix expression is well-parenthesized." << endl;
    }
    else {
        cout << "The infix expression is not well-parenthesized." << endl;
    }

    // Convert the infix expression to prefix
    string prefix = infixToPrefix(infix);
    cout << "Prefix expression: " << prefix << endl;

    return 0;
}

// The overall time complexity for checking if the expression is well-parenthesized 
// and converting the infix expression to prefix is 
// O(n), where n is the length of the input expression.







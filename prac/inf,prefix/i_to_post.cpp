#include <iostream>
#include <stack>
#include <string>
#include <cctype>

using namespace std;

// Function to determine the precedence of operators
int precedence(char op) {
    if (op == '+' || op == '-') {
        return 1;
    }
    if (op == '*' || op == '/') {
        return 2;
    }
    return 0;
}

// Function to check if a character is an operator
bool isOperator(char ch) {
    return (ch == '+' || ch == '-' || ch == '*' || ch == '/');
}

// Function to convert infix expression to postfix expression
string infixToPostfix(const string &infix) {
    stack<char> s;
    string postfix;

    for (char ch : infix) {
        // If the character is an operand (alphanumeric), add it to the postfix expression
        if (isalnum(ch)) {
            postfix += ch;
        }
        // If the character is '(', push it to the stack
        else if (ch == '(') {
            s.push(ch);
        }
        // If the character is ')', pop until '(' is encountered
        else if (ch == ')') {
            while (!s.empty() && s.top() != '(') {
                postfix += s.top();
                s.pop();
            }
            s.pop(); // Pop the '('
        }
        // If the character is an operator
        else if (isOperator(ch)) {
            while (!s.empty() && precedence(s.top()) >= precedence(ch)) {
                postfix += s.top();
                s.pop();
            }
            s.push(ch);
        }
    }

    // Pop all the operators from the stack
    while (!s.empty()) {
        postfix += s.top();
        s.pop();
    }

    return postfix;
}

// Function to evaluate a postfix expression
int evaluatePostfix(const string &postfix) {
    stack<int> s;

    for (char ch : postfix) {
        // If the character is an operand, push it to the stack (convert to integer)
        if (isdigit(ch)) {
            s.push(ch - '0'); // Convert character digit to integer
        }
        // If the character is an operator, pop two operands and perform the operation
        else if (isOperator(ch)) {
            int op2 = s.top(); s.pop();
            int op1 = s.top(); s.pop();
            int result;

            switch (ch) {
                case '+': result = op1 + op2; break;
                case '-': result = op1 - op2; break;
                case '*': result = op1 * op2; break;
                case '/': result = op1 / op2; break;
                default: throw invalid_argument("Unexpected operator");
            }

            s.push(result); // Push the result back to the stack
        }
    }

    // The final result will be at the top of the stack
    return s.top();
}

int main() {
    string infix, postfix;

    // Input the infix expression
    cout << "Enter infix expression (operands and operators must be single characters): ";
    getline(cin, infix);

    // Convert the infix expression to postfix
    postfix = infixToPostfix(infix);
    cout << "Postfix expression: " << postfix << endl;

    // Evaluate the postfix expression
    int result = evaluatePostfix(postfix);
    cout << "Result of postfix evaluation: " << result << endl;

    return 0;
}


// Time complexity: O(n), where n is the length of the expression
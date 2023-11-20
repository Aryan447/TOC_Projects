#include <iostream>
#include <stack>
#include <string>

class PDA {
private:
    std::stack<char> st;
    int currentState;

public:
    PDA() : currentState(0) {
        st.push('Z');
    }

    bool process(const std::string& input) {
        for (char c : input) {
            switch (currentState) {
                case 0:
                    if (c == 'a' && st.top() == 'Z') {
                        st.push('A');
                    } else if (c == 'a' && st.top() == 'A') {
                        st.push('A');
                    } else if (c == 'b' && st.top() == 'A') {
                        st.pop();
                        currentState = 1;
                    } else {
                        return false; // Invalid input
                    }
                    break;

                case 1:
                    if (c == 'b' && st.top() == 'A') {
                        st.pop();
                    } else {
                        return false; // Invalid input
                    }
                    break;

                default:
                    return false; // Invalid state
            }
        }
        return st.top() == 'Z'; // If we end with the initial stack symbol, the input is accepted.
    }
};

int main() {
    PDA pda;
    std::string input;

    std::cout << "Enter a string of 'a's and 'b's: ";
    std::cin >> input;

    if (pda.process(input)) {
        std::cout << "Accepted" << std::endl;
    } else {
        std::cout << "Rejected" << std::endl;
    }
 std::cout<<"Name :Aryan Singh\n";
    std::cout<<"Enrolment no: 0901AM211015\n";
    std::cout<<"Branch: AIML 3RD Year";
    return 0;
}

#include <iostream>
#include <string>

class CFG {
public:
    std::string derive(const std::string& input) {
        if (input == "E") {
            return "E + E"; // Derivation rule: E -> E + E
        } else if (input == "E + E") {
            return "E * E"; // Derivation rule: E + E -> E * E
        } else if (input == "E * E") {
            return "(E)"; // Derivation rule: E * E -> (E)
        } else if (input == "(E)") {
            return "a"; // Derivation rule: (E) -> a
        } else {
            return input;
        }
    }
};

int main() {
    CFG grammar;
    std::string currentString = "E";

    for (int i = 0; i < 5; ++i) { // Apply derivations for 5 steps
        std::cout << currentString << std::endl;
        currentString = grammar.derive(currentString);
    }
 std::cout<<"Name :Aryan Singh\n";
    std::cout<<"Enrolment no: 0901AM211015\n";
    std::cout<<"Branch: AIML 3RD Year";
    return 0;
}


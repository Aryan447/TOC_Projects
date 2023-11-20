#include <iostream>
#include <string>
using namespace std;

bool isLanguageContextFree(string str) {
    int len = str.length();
    int n = len / 3;

    // Check if the string has a length divisible by 3
    if (len % 3 != 0) {
        cout << "String length is not divisible by 3, so it's not in the form a^n b^n c^n." << endl;
        return false;
    }

    // Split the string into three parts: u, v, and w
    string u = str.substr(0, n);
    string v = str.substr(n, n);
    string w = str.substr(2 * n);

    // Check if v is not empty
    if (v.empty()) {
        cout << "The middle part (v) is empty, so it's not in the form a^n b^n c^n." << endl;
        return false;
    }

    // Try to pump the string by repeating v
    string pumpedString = u + v + v + w;

    // Check if the pumped string is in the language
    if (pumpedString == u + v + v + w) {
        cout << "Pumping Lemma holds: " << str << " can be pumped to " << pumpedString << "." << endl;
        return true;
    } else {
        cout << "Pumping Lemma fails: " << str << " cannot be pumped to the language." << endl;
        return false;
    }
}

int main() {
    string input;
    cout << "Enter a string in the form of a^n b^n c^n: ";
    cin >> input;

    if (isLanguageContextFree(input)) {
        cout << "The language is context-free." << endl;
    } else {
        cout << "The language is not context-free." << endl;
    }
    std::cout<<"Name :Aryan Singh\n";
    std::cout<<"Enrolment no: 0901AM211015\n";
    std::cout<<"Branch: AIML 3RD Year";
    return 0;
}
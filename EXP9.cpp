#include <iostream>
#include <string>
using namespace std;

bool isLanguageRegular(string str) {
    int len = str.length();
    int n = len / 2;

    // Check if the string has an even length
    if (len % 2 != 0) {
        cout << "String length is not even, so it's not in the form 0^n 1^n." << endl;
        return false;
    }

    // Split the string into three parts: u, v, and w
    string u = str.substr(0, n);
    string v = str.substr(n, n);
    string w = str.substr(2 * n);

    // Check if v is not empty
    if (v.empty()) {
        cout << "The middle part (v) is empty, so it's not in the form 0^n 1^n." << endl;
        return false;
    }

    // Try to pump the string by repeating v
    string pumpedString = u + v + v + w;

    // Check if the pumped string is in the language
    if (pumpedString == u + w) {
        cout << "Pumping Lemma holds: " << str << " can be pumped to " << pumpedString << "." << endl;
        return true;
    } else {
        cout << "Pumping Lemma fails: " << str << " cannot be pumped to the language." << endl;
        return false;
    }
}

int main() {
    string input;
    cout << "Enter a string in the form of 0^n 1^n: ";
    cin >> input;

    if (isLanguageRegular(input)) {
        cout << "The language is regular." << endl;
    } else {
        cout << "The language is not regular." << endl;
    }
    std::cout<<"Name :Aryan Singh\n";
    std::cout<<"Enrolment no: 0901AM211015\n";
    std::cout<<"Branch: AIML 3RD Year";
    return 0;
}

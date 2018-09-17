
#include <iostream>
#include <stdio.h>

using namespace std;

void reverse(char* str) {
    // Return if char array is null or empty
    if( !str ) return;
    // Init swapper variables
    char *start = str;
    char *end = str;
    // Go to the last character in the char array
    while( *end != '\0' ) {
        end++;
    }
    end--;
    // Loop front and back to middle and swap the respective values
    while( start < end ) {
        *start ^= *end;
        *end ^= *start;
        *start ^= *end;
        start++;
        end--;
    }
}

int main() {
    char *str = strdup("123456789");
    cout << str << endl;
    reverse(str);
    cout << str << endl;
}
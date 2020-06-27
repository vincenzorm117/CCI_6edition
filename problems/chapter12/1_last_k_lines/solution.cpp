
#include <iostream>
#include <fstream>

using namespace std;


void readLastKLines(int k, string filename) {
    char c;
    // Check if no filename provided
    if( filename.empty() ) {
        return;
    }
    // Initialize file and check if it exists
    ifstream file(filename, ifstream::binary);
    if(!file) {
        cout << "Unable to open file" << endl;
    }
    
    // Move file pointer to the beginning, grab the pointer to it and move the pointer to the end of the file
    file.seekg(0, ios::beg);
    ifstream::pos_type begin = file.tellg();
    file.seekg(0, ios::end);
    
    // Move the file pointer to the beginning of the k-th last line
    while( file.tellg() != begin ) {
        c = static_cast<char>(file.peek());
        if( c == '\n' ) {
            k--;
        }
        if( k <= 0 ) {
            file.seekg(1,ios::cur);
            break;
        }
        file.seekg(-1,ios::cur);
    }
    
    // Read the last k lines
    while( file.good() ) {
        file.read(&c, 1);
        cout << c;
    }
    cout << endl;
}



int main(int argc, const char * argv[]) {
    readLastKLines(5, "./example.txt");
}

#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    // Complete the code.
    int a, b;
    char num[][20] = {"one","two", "three", "four", "five", "six", "seven", "eight", "nine"};
    cin>>a>>b;
    for(int i = a; i <= b ; i++){
        if(i <= 9) cout<<num[i-1]<<endl;
        else if(i % 2 == 0) cout<<"even\n";
        else
          cout << "odd\n";
    }
    return 0;
}


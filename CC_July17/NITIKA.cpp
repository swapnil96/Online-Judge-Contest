#include <bits/stdc++.h>
using namespace std;

int main()
{
    int i, tt;
    scanf("%d", &tt);
    string str;
    string delimiter = " ";
    for (i = 0; i < tt; i++)
    {
        cin >> str;
        size_t pos = 0;
        string token;
        while ((pos = str.find(delimiter)) != string::npos) 
        {
            token = str.substr(0, pos);
            cout << token << endl;
            str.erase(0, pos + delimiter.length());
        }
        cout << "sdf" << endl;
    }
}
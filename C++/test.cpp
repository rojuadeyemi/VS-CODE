#include<iostream>

using namespace std;

int mersenne(int p)
{ 
    int result = 1;
    for (int i = 0; i < p; i++)
    {
        result *=2;
    }
    return result -1 ;
}
int main(int argc, char const *argv[])
{
    int p = mersenne(5); 
    if (p%2!=0)
    {
        cout <<p<<" is a prime mersenne number"<<endl;
        return 0;
    }
    else
    {
        cout<<"Try "<<p+2<<" Next time";
    };
    return 0;   
    
}
#include<iostream>
#include<cmath>
using namespace std;
int main()
{
    double a,b,c,d,e,f;
    cin>>a>>b>>c>>d>>e>>f;
    cout<<100000000*abs(a-0.5)*abs(b-0.6)*abs(c-0.7)*abs(d-0.8)*abs(e-0.9)*abs(f-0.1)+50*(abs(a-0.5)+abs(b-0.6)+abs(c-0.7)+abs(d-0.8)+abs(e-0.9)+abs(f-0.1));
    return 0;
}
         
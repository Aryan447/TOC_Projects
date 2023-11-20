#include<bits/stdc++.h> 
using namespace std;

 int main()
 {

int n; 
cout<<"Enter the no of Production Rules of CFG"; 

cin>>n; 
char s1; 
string s2; 
vector<pair<char,string>> v;

 cout<<"Please enter the Production rules of CFG \n";

  for(int i=0;i<n;i++)
    { cin>>s1>>s2;

      v.push_back(make_pair(s1,s2));}

cout<<"The Corresponding Production Rules For PDA are:-"<<endl; 


 cout<<"Rules For Non-Terminal Symbols are:- \n";

for(int i=0;i<n;i++){
 int flag=0; 
 cout<<"dl(q,null," <<v[i].first<<") --> ";

 string check=v[i].second;
 int si=check.size();

string ans="";
for(int i=0;i<si;i++){ char ch=check[i];

    if(ch == '|')
        { cout<<"dl(q,"<<ans<<") |";

              ans="";}

  else{ ans+=ch;}

  }

if(flag!=1) cout<<"dl(q,"<<ans<<")"<<endl;

}

cout<<"dl(q,0,0)--> dl(q,null)"<<endl; 
cout<<"dl(q,1,1) --> dl(q,null)"<<endl;
}

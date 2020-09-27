#include <iostream>
#include <cmath>
#include <fstream>
#include <string>
#include <map>
using namespace std;

typedef long long ll;

map<ll, ll> fact_cache;
ll fact(ll x){
    if(!fact_cache.count(x)){
        fact_cache[x] = x*fact(x-1);
    }
    return fact_cache[x];
}

ll C(int n, int k){
    ll res = 1;
    if(k>n-k){
        for(int i=n; i>=k+1; i--){
            res*=i;
        }
        res/=fact(n-k);
    }
    else{
        for(int i=n; i>=n-k+1; i--){
            res*=i;
        }
        res/=fact(k);
    }
    return res;
}

double P(ll x, int i, double p){
    return C(x+2*i, x+i)*pow((1-p)/2,x+i);
}

double W(double p_, ll x, int i){
    //cout << x << ' ' << i << ' ' << p_ << endl;
    return (x+2*i)*p_;
}

double Expect(int stop, ll x, double p){
    double res = 0;
    for(int i=0; i<=stop; i++){
        res+=W(P(x, i, p), x, i);
    }
    return res;
}

int main(){
    fact_cache[0] = 1;
    fact_cache[1] = 1;
    ll x = 5;
    double p = .6;
    //cout << Expect(65, x, p);
    cout << pow(2, 1023);
}
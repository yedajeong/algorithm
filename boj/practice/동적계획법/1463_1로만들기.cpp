#include <iostream>

using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    int N;
    cin >> N;
    int D[N+1]; // dp테이블[i]: 숫자 i를 1로 만드는 데 걸리는 최소 연산 횟수

    D[1] = 0;
    
    for(int i=2; i<=N; ++i){
        D[i] = D[i-1] + 1;
        if(i%2 == 0)
            D[i] = min(D[i], D[i/2] + 1);
        else if(i%3 == 0)
            D[i] = min(D[i], D[i/3] + 1);
    }

    cout << D[N];

    return 0;
}

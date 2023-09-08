#include <iostream>

using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    int N;
    cin >> N;

    // D[i][0]: i길이 가지는 이친수 중 0으로 끝나는 이친수 개수
    // D[i][1]: i길이 가지는 이친수 중 1로 끝나는 이친수 개수
    int D[N+1][2];
    D[1][1] = 1; // 1은 이친수
    D[1][0] = 0; // 0으로 시작하지 않음

    for(int i=2; i<=N; ++i){
        D[i][1] = D[i-1][0];
        D[i][0] = D[i-1][1] + D[i-1][0];
    }

    cout << D[N][0] + D[N][1];

    return 0;
}

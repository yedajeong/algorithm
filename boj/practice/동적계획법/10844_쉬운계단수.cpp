#include <iostream>

using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    int N;
    const int div = 1000000000;
    cin >> N;

    int D[N+1][10];
    D[1][0] = 0;
    for (int i=1; i<=9; ++i)
        D[1][i] = 1;

    for (int i=2; i<=N; ++i){
        D[i][0] = D[i-1][1];
        D[i][9] = D[i-1][8];
        for (int j=1; j<=8; ++j){
            D[i][j] = (D[i-1][j-1] + D[i-1][j+1]) % div;
        }
    }

    long result = 0;
    for (int i=0; i<=9; ++i)
        result += D[N][i];

    cout << result % div;

    return 0;
}

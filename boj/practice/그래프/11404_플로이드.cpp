#include <iostream>
using namespace std;

const int MAX = 0x3f3f3f3f;
int N, M;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    cin >> N;
    cin >> M;
    int D[N+1][N+1];

    for (int i=1; i<=N; ++i){
        for (int j=1; j<=N; ++j){
            if (i==j) D[i][j] = 0;
            else D[i][j] = MAX;
        }
    }

    int s, e, w;

    for (int i=0; i<M; ++i){
        cin >> s >> e >> w;
        D[s][e] = min(D[s][e], w);
    }

    for (int k=1; k<=N; ++k){
        for (int i=1; i<=N; ++i){
            for (int j=1; j<=N; ++j)
                D[i][j] = min(D[i][j], D[i][k] + D[k][j]);
        }
    }

    for (int i=1; i<=N; ++i){
        for (int j=1; j<=N; ++j){
            if (D[i][j] == MAX) cout << 0 << " ";
            else cout << D[i][j] << " ";
        }
        cout << "\n";
    }

    return 0;
}

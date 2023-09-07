#include <iostream>

using namespace std;

int N, M;
const int MAX = 0x3f3f3f3f;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    cin >> N >> M;
    int D[N+1][N+1];

    for(int i=1; i<=N; ++i){
        for(int j=1; j<=N; ++j){
            if(i==j) D[i][j] = 0;
            else D[i][j] = MAX;
        }
    }

    int s, e;
    for(int i=0; i<M; ++i){
        cin >> s >> e;
        D[s][e] = 1;
        D[e][s] = 1; // 무방향 그래프
    }

    for(int k=1; k<=N; ++k){
        for(int i=1; i<=N; ++i){
            for(int j=1; j<=N; ++j)
                D[i][j] = min(D[i][j], D[i][k] + D[k][j]);
        }
    }

    int dist = MAX;
    int result;
    for(int i=1; i<=N; ++i){
        int now = 0;
        for(int j=1; j<=N; ++j){
            now += D[i][j];
        }
        if (now < dist){
            dist = now;
            result = i;
        }
    }

    cout << result;

    return 0;
}

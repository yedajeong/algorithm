#include <iostream>
using namespace std;

int N;
const int MAX = 0x3f3f3f3f;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    cin >> N;

    // 인접행렬 초기화
    int D[N][N];

    for(int i=0; i<N; ++i){
        for(int j=0; j<N; ++j)
            D[i][j] = MAX;
    }

    // 그래프 정보 저장
    int w;
    for(int i=0; i<N; ++i){
        for(int j=0; j<N; ++j){
            cin >> w;
            if(w) D[i][j] = w;
        }
    }

    // 플로이드 워셜, 모든 노드 간 최단거리 계산
    for(int k=0; k<N; ++k){
        for(int i=0; i<N; ++i){
            for(int j=0; j<N; ++j){
                D[i][j] = min(D[i][k]+D[k][j], D[i][j]);
            }
        }
    }

    // 출력
    for(int i=0; i<N; ++i){
        for(int j=0; j<N; ++j){
            if(D[i][j] == MAX) cout << 0 << " ";
            else cout << 1 << " ";
        }
        cout << "\n";
    }

    return 0;
}

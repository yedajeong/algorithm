#include <iostream>
#include <vector>
#include <queue>
#include <climits>
using namespace std;

int N, M, s, e, w;

struct Edge{
    int s, e, w;
};

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    cin >> N >> M;

    vector<Edge> edges(M);
    long long D[N+1];


    for (int i=0; i<M; ++i){
        cin >> s >> e >> w;
        Edge tmp = {s, e, w};
        edges.push_back(tmp);
    }

    D[1] = 0;
    for (int i=2; i<=N; ++i)
        D[i] = INT_MAX;

    // 업데이트는 노드-1 번만 반복  (최단 거리 구해짐)
    for (int i=0; i<N-1; ++i){
        for (auto edge : edges){
            if (D[edge.s] < INT_MAX and D[edge.s]+edge.w < D[edge.e])
                D[edge.e] = D[edge.s] + edge.w;
        }
    }

    // 음수 사이클 존재 여부 확인 -> 마지막 한 번 더 모든 에지 확인
    bool nCycle = false;
    for (auto edge : edges){
        if (D[edge.s] < INT_MAX and D[edge.s]+edge.w < D[edge.e]){
            nCycle = true;
            break;
        }       
    }

    if (!nCycle){
        for (int i=2; i<=N; ++i){
            if (D[i] == INT_MAX)
                cout << -1 << '\n';
            else
                cout << D[i] << '\n';
        }
    }

    else
        cout << -1 << '\n';

    return 0;
}

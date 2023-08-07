#include <iostream>
#include <vector>
#include <climits>
using namespace std;

int N, M, S, E;
bool visited[50];
vector<pair<pair<int, int>, int>> edges;

bool dfs(int cur){
    if (cur == E) return true;

    visited[cur] = true;

    bool check = false;
    for (auto edge : edges){
        if (edge.first.first == cur && !visited[edge.first.second])
            check |= dfs(edge.first.second);
    }

    return check;
}   

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    cin >> N >> S >> E >> M;
    int money[N];
    long long D[N];

    int s, e, w;
    for (int i=0; i<M; ++i){
        cin >> s >> e >> w;
        edges.push_back(make_pair(make_pair(s, e), -1*w));
    }

    for (int i=0; i<N; ++i){
        D[i] = INT_MIN;
        cin >> money[i];
    }
        
    D[S] = money[S];

    // 업데이트는 노드-1 번만 반복
    for (int i=0; i<N-1; ++i){
        for (auto edge : edges){
            s = edge.first.first;
            e = edge.first.second;
            w = edge.second + money[e];
            if (D[s] > INT_MIN and D[s] + w > D[e]){
                D[e] = D[s] + w;
            }
        }
    }

    if (D[E] == INT_MIN)
        cout << "gg\n";
    else{
        // 양수 사이클 존재 여부 확인 -> 마지막 한 번 더 모든 에지 확인
        for (auto edge : edges){
            s = edge.first.first;
            e = edge.first.second;
            w = edge.second + money[e];
            if (D[s] > INT_MIN and D[s] + w > D[e]){
                // 양수 사이클에서 end까지 갈 수 있으면 Gee
                if (dfs(s)){
                    cout << "Gee\n";
                    return 0;
                }
            }
        }
        cout << D[E] << '\n';
    }
        

    return 0;
}

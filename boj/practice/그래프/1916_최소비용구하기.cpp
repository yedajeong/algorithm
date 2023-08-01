#include <iostream>
#include <vector>
#include <queue>
#include <climits>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    int N, M, A, B, s, e, w;

    cin >> N;
    cin >> M;

    vector<vector<pair<int, int>>> graph(N+1);
    int D[N+1], visited[N+1];
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

    for (int i=1; i<=N; ++i){
        D[i] = INT_MAX;
        visited[i] = 0;
    }
    for (int i=0; i<M; ++i){
        cin >> s >> e >> w;
        graph[s].push_back(make_pair(e, w));
    }

    cin >> s >> e;

    D[s] = 0;
    pq.push(make_pair(D[s], s));

    while(!pq.empty()){
        auto now = pq.top();
        pq.pop();

        if (visited[now.second])
            continue;
        visited[now.second] = 1;

        for (auto next : graph[now.second]){
            if (D[next.first] > (now.first + next.second)){
                D[next.first] = now.first + next.second;
                pq.push(make_pair(D[next.first], next.first));
            }
        }
    }

    cout << D[e];
    
    return 0;
}

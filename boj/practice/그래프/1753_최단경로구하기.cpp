#include <iostream>
#include <vector>
#include <queue>
#include <string.h>
#include <climits>

using namespace std;

int V, E, K;

/*
// 사용자 지정 우선순위
struct cmp{
    bool operator()(pair<int, int> &a, pair<int, int> &b) {
        if (a.first != b.first)
            return a.first > b.first;
        else 
            return a.second > b.second;
    }
};

priority_queue<pair<int,int>,vector<pair<int,int>>,cmp> pq;
*/

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    cin >> V >> E;
    cin >> K;

    int start, end, weight, D[V+1], visited[V+1];
    vector<vector<pair<int, int>>> graph(V+1);

    // memset(D, INT_MAX, sizeof(D));  -> memset은 0 or NULL로 초기화 시에만 사용하기
    memset(visited, 0, sizeof(visited));
    for (int i=1; i<=V; ++i)
        D[i] = INT_MAX;

    // 우선순위 큐 (#include <queue> 의 priority_queue 사용)
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

    for (int i=0; i<E; ++i){
        cin >> start >> end >> weight;
        graph[start].push_back(make_pair(end, weight));
    }

    D[K] = 0;
    pq.push(make_pair(D[K], K));

    while(!pq.empty()){
        auto now = pq.top();
        int distance = now.first;
        int node = now.second;
        pq.pop();

        if (visited[node])
            continue;
        visited[node] = 1;

        for (auto next : graph[node]){
            if (D[next.first] > distance + next.second){
                D[next.first] = distance + next.second;
                pq.push(make_pair(D[next.first], next.first));
            }
        }
    }

    for (int i=1; i<=V; ++i){
        if (visited[i])
            cout << D[i] << '\n';
        else
            cout << "INF\n";
    }
}

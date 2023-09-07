#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int V, E;
int parent[10001];

int find(int n){
    if(parent[n]==n)
        return n;
    else
        parent[n] = find(parent[n]); // 경로압축(필수!!) -> 재귀함수 빠져나오면서 제일 깊이 있는 부모 노드로 업데이트
        return parent[n];
}

void union_merge(int a, int b){
    a = find(a);
    b = find(b);

    if(a<b) parent[b] = a;
    else parent[a] = b;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
    // 가중치 기준 오름차순 정렬 -> pair<가중치, pair<시작, 도착>>
    priority_queue<pair<int, pair<int, int>>, vector<pair<int, pair<int, int>>>, greater<pair<int, pair<int, int>>>> pq;
    cin >> V >> E;
    int s, e, w, useEdge = 0, result = 0;

    for(int i=1; i<=V; ++i)
        parent[i] = i;

    for(int i=0; i<E; ++i){
        cin >> s >> e >> w;
        pq.push(make_pair(w, make_pair(s, e)));
    }

    while(useEdge < V-1){
        auto edge = pq.top();
        w = edge.first;
        s = edge.second.first;
        e = edge.second.second;
        pq.pop();

        if(find(s) != find(e)){
            union_merge(s, e);
            result += w;
            useEdge++;
        }
    }

    cout << result;

    return 0;
}

#include <iostream>
#include <vector>
#include <queue>
#include <climits>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    int N, M, K, s, e, w;

    cin >> N >> M >> K;

    vector<vector<pair<int, int>>> graph(N+1);
    priority_queue<int, vector<int>, less<int>> kth_pq[N+1];
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

    for (int i=0; i<M; ++i){
        cin >> s >> e >> w;
        graph[s].push_back(make_pair(e, w));
    }

    kth_pq[1].push(0);
    pq.push(make_pair(kth_pq[1].top(), 1));

    while(!pq.empty()){
        auto now = pq.top();
        pq.pop();

        int now_node = now.second;
        int now_min_path = now.first;

        for (auto next : graph[now.second]){
            int next_node = next.first;
            int next_path = now_min_path + next.second;

            if (kth_pq[next_node].size() < K){
                kth_pq[next_node].push(next_path);
                pq.push(make_pair(next_path, next_node));
            }

            else if (next_path < kth_pq[next_node].top()){
                kth_pq[next_node].pop();
                kth_pq[next_node].push(next_path);
                pq.push(make_pair(next_path, next_node));
            }

        }
    }

    for (int i=1; i<=N; ++i){
        if (kth_pq[i].size() < K)
            cout << -1 << "\n";
        else
            cout << kth_pq[i].top() << "\n";
    }

    return 0;
}

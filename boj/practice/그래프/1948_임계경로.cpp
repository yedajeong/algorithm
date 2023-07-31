#include <iostream>
#include <vector>
#include <queue>
#include <string.h>
using namespace std;

int N, M;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    cin >> N;
    cin >> M;

    int s, e, t, indegree[N+1], critical[N+1], visited[N+1][N+1];
    vector<vector<pair<int, int>>> graph(N+1);
    vector<vector<pair<int, int>>> reverse(N+1);

    memset(indegree, 0, sizeof(indegree));
    memset(critical, 0, sizeof(indegree));
    for (int i=0; i<=N; ++i)
        memset(visited[i], 0, sizeof(int)*(N+1));

    for (int i=0; i<M; ++i){
        cin >> s >> e >> t;
        graph[s].push_back(make_pair(e, t));
        reverse[e].push_back(make_pair(s, t));
        indegree[e]++;
    }

    cin >> s >> e;

    queue<pair<int, int>> myQue;

    // 1. 최장 경로(임계 경로) 찾기
    myQue.push(make_pair(s, critical[s]));
    while(!myQue.empty()){
        auto now = myQue.front();
        myQue.pop();
        
        for (auto next : graph[now.first]){
            indegree[next.first]--;
            critical[next.first] = max(critical[next.first], critical[now.first] + next.second);
            
            if (indegree[next.first]==0)
                myQue.push(next);
        }
    }

    // 2. 임계 경로에 포함되는 도로 찾기
    int ans = 0;
    myQue.push(make_pair(e, critical[e]));
    while(!myQue.empty()){
        auto now = myQue.front();
        myQue.pop();
        
        for (auto next : reverse[now.first]){
            if ((critical[next.first] + next.second) == critical[now.first]){
                if (visited[now.first][next.first] == 0){
                    visited[now.first][next.first] = 1;
                    myQue.push(next);
                    ans++;
                }
            }
        }
    }

    cout << critical[e] << "\n" << ans;
}

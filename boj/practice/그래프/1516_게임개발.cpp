#include <iostream>
#include <vector>
#include <stack>
using namespace std;

int N;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    cin >> N;

    int time, pre, indegree[N+1], wait_time[N+1], self_time[N+1];
    vector<vector<int>> graph(N+1);

    for (int i=1; i<=N; ++i){
        indegree[i] = 0;
    }

    for (int i=1; i<=N; ++i){
        cin >> time >> pre;
        wait_time[i] = 0;
        self_time[i] = time;
        while (pre != -1){
            graph[pre].push_back(i);
            indegree[i]++;
            cin >> pre;
        }
    }

    stack<int> s;
    for (int i=1; i<=N; ++i){
        if (indegree[i] == 0)
            s.push(i);
    }

    while(!s.empty()){
        int now = s.top();
        s.pop();
        
        for (int next : graph[now]){
            indegree[next]--;
            wait_time[next] = max(wait_time[next], wait_time[now] + self_time[now]);
            if (indegree[next]==0)
                s.push(next);
        }
    }

    for (int i=1; i<=N; ++i)
        cout << wait_time[i] + self_time[i] << "\n";
}

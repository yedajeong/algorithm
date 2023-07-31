#include <iostream>
#include <vector>
#include <stack>
using namespace std;

int N, M;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    cin >> N >> M;

    int a, b, indegree[N+1];
    vector<vector<int>> graph(N+1);

    for (int i=1; i<=N; ++i)
        indegree[i] = 0;

    for (int i=0; i<M; ++i){
        cin >> a >> b;
        graph[a].push_back(b);
        indegree[b]++;
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
            if (indegree[next]==0)
                s.push(next);
        }

        cout << now << " ";
    }
}

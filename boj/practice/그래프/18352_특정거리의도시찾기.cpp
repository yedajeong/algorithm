#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;

int n, m, k, x;
vector<int> visited;
vector<vector<int>> A;
vector<int> ans;

void BFS(int v){
    queue<int> myQue;
    myQue.push(v);
    visited[v]++;

    while(!myQue.empty()){
        int now = myQue.front();
        myQue.pop();
        for (int next : A[now]){
            if (visited[next] == -1){
                visited[next] = visited[now] + 1;
                myQue.push(next);
            }
        }
    }
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    cin >> n >> m >> k >> x;

    A.resize(n+1);
    visited.resize(n+1);

    for (int i=0; i<m; ++i){
        int start, end;
        cin >> start >> end;
        A[start].push_back(end);
    }

    for (int i=1; i<=n; ++i)
        visited[i] = -1;

    BFS(x);
    for (int i=1; i<=n; ++i){
        if (visited[i] == k)
            ans.push_back(i);
    }

    if (ans.empty())
        cout << -1;
    else{
        sort(ans.begin(), ans.end());
        for (int i : ans)
            cout << i << '\n';
    }

    return 0;
}

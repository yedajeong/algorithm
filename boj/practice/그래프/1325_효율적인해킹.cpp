#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

vector<vector<int>> A;
vector<int> visited;
vector<int> ans;
int n, m;

void BFS(int v){
    queue<int> myQue;
    myQue.push(v);
    visited[v] = 1;

    while(!myQue.empty()){
        int now = myQue.front();
        myQue.pop();

        for (int next : A[now]){
            if (!visited[next]){
                ans[next]++;
                myQue.push(next);
                visited[next] = 1;
            }
        }
    }
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    int a, b;
    cin >> n >> m; 

    A.resize(n+1);
    visited.resize(n+1);
    ans.resize(n+1);

    // 초기화
    for (int i = 1; i <= n; ++i){
        visited[i] = 0;
        ans[i] = 0;
    }
    
    // 그래프 구성
    for (int i = 0; i < m; ++i){
        cin >> a >> b;
        A[a].push_back(b);
    }

    // 그래프 탐색
    for (int i = 1; i <= n; ++i){
        fill(visited.begin(), visited.end(), 0);
        BFS(i);
    }

    // max value 찾기
    int maxVal = 0;
    for (int val : ans)
        maxVal = max(val, maxVal);
    
    for (int i = 1; i <= n; ++i){
        if (ans[i] == maxVal)
            cout << i << ' ';
    }


    return 0;
}

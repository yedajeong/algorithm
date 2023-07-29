#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

int k, v, e;

bool BFS(int v, vector<vector<int>> (&A), vector<int> (&visited)){
    queue<int> myQue;
    myQue.push(v);
    int color = 1;
    visited[v] = color;

    while(!myQue.empty()){
        int now = myQue.front();
        myQue.pop();
        color = visited[now] * -1;

        for (int next : A[now]){
            if (visited[next] == 0){
                myQue.push(next);
                visited[next] = color;
            }
            else if (visited[next] == visited[now])
                return false;
            
        }
    }

    return true;
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    int a, b;

    cin >> k;

    for (int test_case = 0; test_case < k; ++test_case){
        cin >> v >> e;

        vector<vector<int>> A(v+1);
        vector<int> visited(v+1);

        // 그래프 구성
        for (int i=0; i<e; ++i){
            cin >> a >> b;
            A[a].push_back(b);
            A[b].push_back(a);
        }

        bool result;
        for (int i=1; i<=v; ++i){
            if (!visited[i])
                result = BFS(i, A, visited);

            if (!result){
                cout << "NO\n";
                break;
            }
        }

        if (result)
            cout << "YES\n";
    }
    
    return 0;
}

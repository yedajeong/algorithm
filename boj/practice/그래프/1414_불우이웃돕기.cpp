#include <iostream>
#include <queue>
using namespace std;

int N;
int comp[51][51];
int parent[51];
const int MAX = 0x3f3f3f3f;

int find(int n){
    if(parent[n] == n)
        return n;
    else{
        parent[n] = find(parent[n]);
        return parent[n];
    }
}

void union_merge(int a, int b){
    a = find(a);
    b = find(b);

    if (a < b) parent[b] = a;
    else parent[a] = b;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    cin >> N;

    priority_queue<pair<int, pair<int, int>>, vector<pair<int, pair<int, int>>>, greater<pair<int, pair<int, int>>>> pq;
    int lan_total = 0;

    for(int i=1; i<=N; ++i){
        parent[i] = i;

        for(int j=1; j<=N; ++j){
            char tmpc = cin.get();
            if(tmpc == '\n') // 개행문자는 버리기
                tmpc = cin.get();
            
            int tmp = 0;
            if (tmpc >= 'a' && tmpc <= 'z' ){
                tmp = tmpc - 'a' + 1;
                lan_total += tmp;
                pq.push(make_pair(tmp, make_pair(i, j)));
            }
            else if (tmpc >= 'A' && tmpc <= 'Z'){
                tmp = tmpc - 'A' + 27;
                lan_total += tmp;
                pq.push(make_pair(tmp, make_pair(i, j)));
            }
            else if (tmpc == '0')
                tmp = MAX;
            
            comp[i][j] = tmp;
        }
        
    }

    // 예외처리1) 컴퓨터 1대, 랜선 없는 경우
    if (N==1 && pq.empty()){
        cout << 0;
        exit(0);
    }
    // 예외처리2) 랜선 없는 경우
    else if (pq.empty()){
        cout << -1;
        exit(0);
    }
    
    int useLan = 0, result = 0;
    while(useLan < N-1){
        // 예외처리3) 에지 다 썼는데 아직 모든 컴퓨터 연결 안됨
        if(useLan < N-1 && pq.empty()){
            cout << -1;
            exit(0);
        }

        int w = pq.top().first;
        int s = pq.top().second.first;
        int e = pq.top().second.second;
        pq.pop();

        if(find(s) != find(e)){
            union_merge(s, e);
            result += w;
            useLan++;
        }
    }

    cout << lan_total - result;

    return 0;
}

#include <iostream>
#include <queue>
#include <stack>
#include <string.h>
#include <vector>
using namespace std;

int N, M;
int visited[10][10];
int Map[10][10];
int dy[] = {-1, 1, 0, 0};
int dx[] = {0, 0, -1, 1};
int parent[7]; // 섬의 개수 2~6개
priority_queue<pair<int, pair<int,int>>, vector<pair<int, pair<int, int>>>, greater<pair<int, pair<int, int>>>> pq; // 가중치(first) 기준 오름차순
vector<pair<int, int>> land_info;

void mark_island(int y, int x, int num){
    // bfs
    queue<pair<int, int>> q;
    q.push(make_pair(y, x));
    visited[y][x] = 1;
    Map[y][x] = num;
    land_info.push_back(make_pair(y, x));

    while(!q.empty()){
        y = q.front().first;
        x = q.front().second;
        q.pop();

        for(int i=0; i<4; ++i){
            int next_y = y + dy[i];
            int next_x = x + dx[i];

            if(next_y > -1 && next_x > -1 && next_y < N && next_x < M){
                if(Map[next_y][next_x]==-1 && !visited[next_y][next_x]){
                    visited[next_y][next_x] = 1;
                    Map[next_y][next_x] = num;
                    q.push(make_pair(next_y, next_x));
                    land_info.push_back(make_pair(next_y, next_x));
                }
            }
        }
    }
}

void find_bridge(){
    for(auto land : land_info){
        int y = land.first;
        int x = land.second;
        int now_num = Map[y][x];

        for(int i=0; i<4; ++i){
            int dir_y = dy[i];
            int dir_x = dx[i];
            int next_y = y + dir_y;
            int next_x = x + dir_x;

            int bridge_len = 0;
            while(next_y > -1 && next_y < N && next_x > -1 && next_x < M){
                if(Map[next_y][next_x] == 0){
                    bridge_len++;
                    next_y += dir_y; // 일관된 방향으로
                    next_x += dir_x;
                }
                else if(Map[next_y][next_x] != now_num){
                    if(bridge_len>=2)
                        pq.push(make_pair(bridge_len, make_pair(now_num, Map[next_y][next_x])));
                    break;
                }
                    
                else if(Map[next_y][next_x] == now_num)
                    break;
            }
        }
    }
}

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
    if(a<b) parent[b] = a;
    else parent[a] = b;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    int item, land_num=0;

    cin >> N >> M;

    for(int i=0; i<N; ++i){
        for(int j=0; j<M; ++j){
            cin >> item;
            if(item) Map[i][j] = -1;
            else Map[i][j] = item;
        }
    }

    for(int i=0; i<N; ++i)
        memset(visited[i], 0, sizeof(visited[i]));

    // 노드 구하기 (노드 == 섬)
    for(int i=0; i<N; ++i){
        for(int j=0; j<M; ++j){
            if(Map[i][j] == -1){
                land_num++;
                mark_island(i, j, land_num);
            }
        }
    }

    // 가능한 에지 구하기 (에지 == 다리)
    find_bridge();

    // 최소신장트리 가중치 구하기 (크루스칼)
    for(int i=1; i<=land_num; ++i)
        parent[i] = i;
    
    // 예외처리1) 연결 가능한 에지 하나도 없을 때
    if(pq.empty()){
        cout << -1;
        exit(0);
    }

    int useEdge = 0, result = 0;
    while(useEdge < land_num-1){
        int w = pq.top().first;
        int s = pq.top().second.first;
        int e = pq.top().second.second;
        pq.pop();

        if(find(s) != find(e)){
            union_merge(s, e);
            result += w;
            useEdge++;
        }

        // 예외처리2) 에지 다 썼지만 모든 노드를 연결하지 못한 경우
        if(pq.empty() && useEdge != land_num-1){ 
            cout << -1;
            exit(0);
        }
    }

    cout << result;

    return 0;
}

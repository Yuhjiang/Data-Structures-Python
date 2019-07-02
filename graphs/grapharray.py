"""
邻接矩阵表示法

    A  B  C  D
 A  0  1  0  1
 B  1  0  0  1
 C  0  1  0  1
 D  0  1  1  0
"""
from queues.queues import Queue
INFINITY = 65535        # 在初始化图中，表示不连通的边


class GraphArray(object):
    def __init__(self):
        """
        初始化邻接矩阵图
        """
        self.nv = 0
        self.ne = 0
        self.graph = []
        self.visited = []

    def create_graph(self, nv, ne, edges):
        """
        创建图
        :param nv: 顶点数
        :param ne: 边数
        :param edges: [头顶点, 尾顶点, 权重]
        """
        self.nv = nv
        self.ne = ne

        # 设置初始图
        for i in range(self.nv):
            self.graph.append([INFINITY] * self.nv)
            self.graph[i][i] = 0
            self.visited.append(False)

        # 生成图
        for edge in edges:
            self.graph[edge[0]][edge[1]] = edge[2]

    def visit(self, v):
        print('Visit Node {}'.format(v))
        self.visited[v] = True

    def init_visit(self):
        for v in range(self.nv):
            self.visited[v] = False

    def is_edge(self, v, w):
        return self.graph[v][w] < INFINITY

    def insert_edge(self, edge):
        """
        插入一条边
        :param edge: [头顶点, 尾顶点, 权重]
        """
        self.graph[edge[0]][edge[1]] = edge[2]

    # 1. 广度优先遍历
    def deep_first_search(self, v):
        """
        :param v: 遍历起点
        """
        Q = Queue()

        self.visit(v)
        Q.enqueue(v)

        while not Q.is_empty():
            v = Q.dequeue()
            for w in range(self.nv):
                # 若w是v邻接点，且未被访问
                if self.is_edge(v, w) and not self.visited[w]:
                    self.visit(w)
                    Q.enqueue(w)

    # 2. 深度优先遍历
    def broad_first_search(self, v):
        """
        :param v: 遍历起点
        """
        self.visit(v)

        for w in range(self.nv):
            # w是v的邻接点，且未被访问
            if self.is_edge(v, w) and not self.visited[w]:
                self.broad_first_search(w)

    # 3. 无权图的单源最短路径算法
    def unweighted(self, dist, path, s):
        """
        :param dist: 保存v距离s的距离
        :param path: 保存上一一个点的位置
        :param s: 源点
        """
        Q = Queue()
        # 初始化路径和距离
        for _ in range(self.nv):
            dist.append(-1)
            path.append(-1)

        dist[s] = 0
        Q.enqueue(s)

        while not Q.is_empty():
            v = Q.dequeue()
            for w in range(self.nv):
                if dist[w] == -1 and self.is_edge(v, w):
                    dist[w] = dist[v] + 1
                    path[w] = v
                    Q.enqueue(w)

    # 4. 有权图的单源最短路径算法
    def find_min_dist(self, dist, collected):
        """
        返回未知节点中dist最小的节点
        :param dist: 距离
        :param collected: 节点被收录情况
        :return: dist最小的节点
        """
        min_v = 0
        min_dist = INFINITY

        for v in range(self.nv):
            if collected[v] is False and dist[v] < min_dist:
                min_dist = dist[v]
                min_v = v
        if min_dist < INFINITY:
            return min_v
        else:
            return False

    def dijkstra(self, dist, path, s):
        """
        :param dist: 保存v距离s的距离
        :param path: 保存上一一个点的位置
        :param s: 源点
        """
        collected = []
        for v in range(self.nv):
            collected.append(False)
            dist.append(self.graph[s][v])
            if dist[v] < INFINITY:
                path.append(s)
            else:
                path.append(-1)
            collected[v] = False

        collected[s] = True
        dist[s] = 0

        while True:
            v = self.find_min_dist(dist, collected)
            if v is False:
                break
            print(v)
            collected[v] = True     # 收录进已确定的点中
            for w in range(self.nv):
                # w是v的邻接点，且未被收录
                if not collected[w] and self.is_edge(v, w):
                    if dist[w] > dist[v] + self.graph[v][w]:
                        dist[w] = dist[v] + self.graph[v][w]
                        path[w] = v

    def floyd(self, dist, path):
        """
        多源最短路径算法
        :param dist: dist[i][j] i到j的最小长度
        :param path: 路径
        :return:
        """
        for i in range(self.nv):
            for j in range(self.nv):
                dist[i][j] = self.graph[i][j]
                path[i][j] = -1

        for k in range(self.nv):
            for i in range(self.nv):
                for j in range(self.nv):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        path[i][j] = k


if __name__ == '__main__':
    edges = [
        [1, 0, 1],
        [1, 3, 2],
        [1, 2, 3],
        [2, 4, 4],
        [3, 4, 4],
    ]

    g = GraphArray()
    g.create_graph(5, 5, edges)
    print(g.graph)

    g.deep_first_search(1)
    g.init_visit()
    print('--------------------------------')
    g.broad_first_search(1)
    print('----------------------------')
    dist = []
    path = []
    edges = [
        [0, 1, 2],
        [0, 3, 1],
        [1, 3, 3],
        [1, 4, 10],
        [2, 0, 4],
        [2, 5, 5],
        [3, 4, 2],
        [3, 5, 8],
        [3, 6, 4],
        [3, 2, 2],
        [4, 6, 6],
        [6, 5, 1]
    ]
    g = GraphArray()
    g.create_graph(7, 12, edges)
    g.unweighted(dist, path, 2)
    print(dist, path)
    print('---------------------------------------')
    dist = []
    path = []
    g.dijkstra(dist, path, 0)
    print(dist, path)
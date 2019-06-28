"""
图的邻接表表示法
A->B
B->C->D
C
D->A
"""
from queues.queues import Queue
INFINITY = 65535        # 在图中，表示不连通的边


class Edge(object):
    def __init__(self, v1, v2, weight):
        self.v1 = v1
        self.v2 = v2
        self.weight = weight


class Node(object):
    def __init__(self, v, weight, next=None):
        """
        图上顶点
        :param v: 点下标
        :param weight: 边权重
        :param next: 下一个邻接点
        """
        self.v = v
        self.weight = weight
        self.next = next


class Graph(object):
    def __init__(self):
        self.nv = 0
        self.ne = 0
        self.graph = []
        self.visited = []

    def insert_edge(self, edge):
        new_node = Node(edge[1], edge[2], self.graph[edge[0]])

        self.graph[edge[0]] = new_node

    def create_graph(self, nv, ne, edges):
        """
        创建图
        :param nv: 顶点数
        :param ne: 边数
        :param edges: [头顶点, 尾顶点, 权重]
        """
        self.nv = nv
        self.ne = ne

        # 初始化图
        for _ in range(ne):
            self.graph.append(None)
            self.visited.append(False)

        for edge in edges:
            self.insert_edge(edge)

    def visit(self, v):
        print('Visit Node {}'.format(v))
        self.visited[v] = True

    def init_visit(self):
        for v in range(self.nv):
            self.visited[v] = False

    # 1. 广度优先遍历
    def broad_first_search(self, v):
        Q = Queue()
        self.visit(v)
        Q.enqueue(v)

        while not Q.is_empty():
            v = Q.dequeue()
            w = self.graph[v]
            while w:
                # 如果w没有被访问过
                if not self.visited[w.v]:
                    self.visit(w.v)
                    Q.enqueue(w.v)
                w = w.next

    # 2. 深度优先遍历
    def deep_first_search(self, v):
        self.visit(v)

        w = self.graph[v]
        while w:
            # 如果w没有被访问过
            if not self.visited[w.v]:
                self.deep_first_search(w.v)
            w = w.next

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
            w = g.graph[v]
            while w:
                # dist可表示w是否被访问过
                if dist[w.v] == -1:
                    dist[w.v] = dist[v] + 1
                    path[w.v] = v
                    Q.enqueue(w.v)
                w = w.next

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
            if not collected[v] and dist[v] < min_dist:
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
            dist.append(INFINITY)
            path.append(-1)

        w: Node = self.graph[s]
        while w:
            dist[w.v] = w.weight
            path[w.v] = s
            w = w.next
        collected[s] = True
        dist[s] = 0

        while True:
            v = self.find_min_dist(dist, collected)
            print(v)
            if v is False:
                break
            collected[v] = True

            w = self.graph[v]
            while w:
                if not collected[w.v] and dist[w.v] > dist[v] + w.weight:
                    dist[w.v] = dist[v] + w.weight
                    path[w.v] = v
                w = w.next

    def __str__(self):
        s = []
        n = 0
        for v in self.graph:
            temp = str(n)
            while v is not None:
                temp += ' --{}--> {}'.format(v.weight, v.v)
                v = v.next
            n += 1
            s.append(temp)

        return '\n'.join(s)


if __name__ == '__main__':
    edges = [
        [1, 0, 1],
        [1, 3, 2],
        [1, 2, 3],
        [2, 4, 4],
        [3, 4, 4],
    ]

    g = Graph()
    g.create_graph(5, 5, edges)

    g.deep_first_search(1)
    g.init_visit()
    print('----------------------------')
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
    g = Graph()
    g.create_graph(7, 12, edges)
    g.unweighted(dist, path, 2)
    print(dist, path)
    print('----------------------------')
    dist = []
    path = []
    g.dijkstra(dist, path, 0)
    print(dist, path)
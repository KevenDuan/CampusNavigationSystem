def dijkstra(x, y):
    from queue import PriorityQueue
    node = ['电子信息实验楼', '电子工程学院', '历史文化研究中心', '信息技术中心', '向学楼', '竞秀楼', '学生宿舍管理中心', '学生一食堂', '旅游与国土资源学院', '万福超市']
    pq = PriorityQueue()
    path = [[(1, 200), (8, 300), (2, 200)],
            [(2, 200), (0, 200), (8, 350), (3, 400), (4, 500)],
            [(0, 200), (1, 200), (3, 300)],
            [(2, 200), (1, 400)],
            [(1, 500), (5, 100), (9, 500)],
            [(4, 100), (6, 150), (9, 550)],
            [(5, 150), (7, 100)],
            [(6, 100), (9, 300)],
            [(1, 350), (9, 200), (0, 300)],
            [(8, 200)], (7, 300), (4, 500), (5, 550)]
    sta = x
    n = len(node)
    r = [0x3f3f3f3f] * n
    record = [0] * n
    flag = [0] * n
    r[sta] = sta
    pq.put((r[sta], sta))
    while pq.qsize() != 0:
        d, v = pq.get()
        if flag[v]: continue
        flag[v] = 1 # 标记为最短路
        for Node, Distance in path[v]:
            if flag[Node]: continue
            if Distance + d < r[Node]:
                r[Node] = Distance+d
                record[Node] = v
            pq.put((r[Node], Node))

    Path = []
    end = y
    while True:
        Path.append(node[record[end]])
        end = record[end]
        if x == end: break
    Path.reverse()
    Path.append(node[y])
    Path = '->'.join(Path)
    print(Path)

dijkstra(3, 9)

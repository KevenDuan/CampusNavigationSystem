from PyQt5 import QtCore, QtGui, QtWidgets
from ui_mainwindow import Ui_MainWindow
import sys

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow
        self.setupUi(self)
        
    def check_wearth(self):
        import requests
        cityCode = 101240201

        r = requests.get("http://t.weather.sojson.com/api/weather/city/{}".format(cityCode))

        # print(r.json())

        if r.json().get('status') == 200:
            weatherMsg = '城市：{}\n日期：{}\n天气：{}\nPM 2.5：{} {}\n温度：{}\n湿度：{}\n风力：{}\n\n{}'.format(
                r.json()['cityInfo']['city'],
                r.json()['data']['forecast'][0]['ymd'],
                r.json()['data']['forecast'][0]['type'],
                int(r.json()['data']['pm25']),
                r.json()['data']['quality'],
                r.json()['data']['wendu'],
                r.json()['data']['shidu'],
                r.json()['data']['forecast'][0]['fl'],
                r.json()['data']['forecast'][0]['notice'],
            )
        else:
            weatherMsg = '天气查询失败，请稍后再试！'

        self.textBrowser_2.setText(weatherMsg)

    def dijkstra(self):
        self.textBrowser.clear()
        from queue import PriorityQueue
        node = ['电子信息实验楼', '电子工程学院', '历史文化研究中心', '信息技术中心', '向学楼', '竞秀楼', '学生宿舍管理中心', '学生一食堂', '旅游与国土资源学院', '万福超市']
        pq = PriorityQueue()
        path = [[(1, 200), (8, 300), (2, 200), (9, 600)],
                [(2, 200), (0, 200), (8, 350), (3, 400), (4, 500)],
                [(0, 200), (1, 200), (3, 300)],
                [(2, 350), (1, 400)],
                [(1, 500), (5, 100), (9, 500)],
                [(4, 100), (6, 150), (9, 550)],
                [(5, 150), (7, 100)],
                [(6, 100), (9, 300)],
                [(1, 350), (9, 200), (0, 300)],
                [(8, 200)], (7, 300), (4, 500), (5, 550)]
        sta = self.comboBox.currentIndex()
        n = len(node)
        r = [0x3f3f3f3f] * n
        record = [0] * n
        flag = [0] * n
        r[sta] = 0
        pq.put((r[sta], sta))
        while pq.qsize() != 0:
            d, v = pq.get()
            if flag[v]: continue
            flag[v] = 1  # 标记为最短路
            for Node, Distance in path[v]:
                if flag[Node]: continue
                if Distance + d < r[Node]:
                    r[Node] = Distance + d
                    record[Node] = v
                pq.put((r[Node], Node))

        Path = []
        end = self.comboBox_2.currentIndex()
        while True:
            Path.append(node[record[end]])
            end = record[end]
            if sta == end: break
        Path.reverse()
        Path.append(node[self.comboBox_2.currentIndex()])
        Path = '->'.join(Path)
        self.textBrowser.setText(Path + f'\ndistance:{r[self.comboBox_2.currentIndex()]}m')
        # print(Path)

    def car_dijkstra(self):
        self.textBrowser.clear()
        from queue import PriorityQueue
        node = ['电子信息实验楼', '电子工程学院', '历史文化研究中心', '信息技术中心', '向学楼', '竞秀楼', '学生宿舍管理中心', '学生一食堂', '旅游与国土资源学院', '万福超市']
        pq = PriorityQueue()
        path = [[(1, 200), (8, 300), (2, 200), (9, 600)],
                [(2, 200), (0, 200), (8, 350), (3, 400), (4, 500)],
                [(0, 200), (1, 200), (3, 300)],
                [(2, 300), (1, 700)],
                [(1, 500), (5, 100), (9, 500)],
                [(4, 100), (6, 150), (9, 550)],
                [(5, 150), (7, 100)],
                [(6, 100), (9, 300)],
                [(1, 350), (9, 200), (0, 300)],
                [(8, 200)], (7, 300), (4, 500), (5, 550)]
        sta = self.comboBox.currentIndex()
        n = len(node)
        r = [0x3f3f3f3f] * n
        record = [0] * n
        flag = [0] * n
        r[sta] = 0
        pq.put((r[sta], sta))
        while pq.qsize() != 0:
            d, v = pq.get()
            if flag[v]: continue
            flag[v] = 1  # 标记为最短路
            print(r)
            for Node, Distance in path[v]:
                if flag[Node]: continue
                if Distance + d < r[Node]:
                    r[Node] = Distance + d
                    record[Node] = v
                pq.put((r[Node], Node))

        Path = []
        end = self.comboBox_2.currentIndex()
        while True:
            Path.append(node[record[end]])
            end = record[end]
            if sta == end: break
        Path.reverse()
        Path.append(node[self.comboBox_2.currentIndex()])
        Path = '->'.join(Path)
        self.textBrowser.setText(Path + f'\ndistance:{r[self.comboBox_2.currentIndex()]}m')
        # print(Path)

    def floyd(self):
        node = ['电子信息实验楼', '电子工程学院', '历史文化研究中心', '信息技术中心', '向学楼', '竞秀楼', '学生宿舍管理中心', '学生一食堂', '旅游与国土资源学院', '万福超市']
        path = [[(1, 200), (8, 300), (2, 200), (9, 600)],
                [(2, 200), (0, 200), (8, 350), (3, 400), (4, 500)],
                [(0, 200), (1, 200), (3, 300)],
                [(2, 200), (1, 400)],
                [(1, 500), (5, 100), (9, 500)],
                [(4, 100), (6, 150), (9, 550)],
                [(5, 150), (7, 100)],
                [(6, 100), (9, 300)],
                [(1, 350), (9, 200), (0, 300)],
                [(8, 200)], (7, 300), (4, 500), (5, 550)]
        n = len(node)
        dp = [[0x3f3f3f3f] for _ in range(n)]
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
        sta = self.comboBox.currentIndex()
        record = []
        Path = []
        end = self.comboBox_2.currentIndex()
        while True:
            Path.append(node[record[end]])
            end = record[end]
            if sta == end: break
        Path.reverse()
        Path.append(node[self.comboBox_2.currentIndex()])
        Path = '->'.join(Path)
        self.textBrowser.setText(Path)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
        
    
    


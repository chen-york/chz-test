import tkinter as tk
import tkinter.messagebox
import webbrowser as wb



class player:
    def __init__(self):
        
        self.root = tk.Tk()  # 初始化窗口
        self.root.title('黄陈陈VIP视频播放器')  # 窗口名称
        self.root.geometry("500x500")  # 设置窗口大小
        # 设置窗口是否可变，宽不可变，高可变，默认为True
        self.root.resizable(width=True, height=True)
        self.menu = tk.Menu(self.root)
        self.helpmenu = tk.Menu(self.menu, tearoff=0)
        self.root.config(menu=self.menu)
        self.val = tk.StringVar(value='')
        self.label1 = tk.Label(self.root, text='视频播放通道')
        self.label1.place(x=20, y=20, width=100, height=20)
        self.Radio = tk.IntVar(value=1)
        self.Radio1 = tk.Radiobutton(self.root, variable=self.Radio, value=0, text='视频通道1')
        self.Radio1.place(x=200, y=20, width=100, height=20)
        self.val1 = tk.StringVar(value='')
        self.link = tk.Label(self.root, text='视频播放链接')
        self.link.place(x=20, y=60, width=100, height=20)
        self.movie = tk.Entry(self.root, textvariable=self.val1)
        self.movie.place(x=130, y=60, width=300, height=20)
        self.warn = tk.Label(self.root, text='将视频链接复制到框内，点击播放VIP视频')
        self.warn.place(x=50, y=90, width=400, height=20)
        self.val2 = tk.StringVar
        self.start = tk.Button(self.root, text='播放VIP视频', command=self.Button)
        self.start.place(x=220, y=140, width=80, height=30)
        self.start1 = tk.Button(self.root, text='爱奇艺', command=self.openaqy)
        self.start1.place(x=100, y=200, width=70, height=30)
        self.start2 = tk.Button(self.root, text='腾讯视频', command=self.opentx)
        self.start2.place(x=200, y=200, width=80, height=30)
        self.start3 = tk.Button(self.root, text='芒果TV', command=self.openyq)
        self.start3.place(x=300, y=200, width=80, height=30)
        self.b1=tk.Button(self.root,text='此播放器为黄陈陈专用，盗版必究！')
        self.b1.place(x=150,y=400,width=200,height=40,anchor='nw')
        self.root.mainloop()

    def Button(self):
        a = 'http://www.wmxz.wang/video.php?url='
        b = self.movie.get()
        wb.open(a + b)  # 打开浏览器进行播放


    def openaqy(self):
        wb.open('http://www.iqiyi.com')

    def opentx(self):
        wb.open('http://v.qq.com')

    def openyq(self):
        wb.open('https://www.mgtv.com/')




if __name__ == '__main__':
    player()

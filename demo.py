import tkinter as tk  # 使用Tkinter前需要先导入
import tkinter.messagebox
import cv2
import os
import time
import pymysql
import requests
import base64
import json

# 第1步，实例化object，建立窗口window
window = tk.Tk()

# 第2步，给窗口的可视化起名字
window.title('Wellcome to Hongwei Website')

# 第3步，设定窗口的大小(长 * 宽)
window.geometry('400x300')  # 这里的乘是小x

# 第4步，加载 wellcome image
canvas = tk.Canvas(window, width=400, height=135, bg='green')
image_file = tk.PhotoImage(file='D:\python_work\pic.gif')
image = canvas.create_image(200, 0, anchor='n', image=image_file)
canvas.pack(side='top')
tk.Label(window, text='Wellcome', font=('Arial', 16)).pack()

# 第5步，用户信息
tk.Label(window, text='User name:', font=('Arial', 14)).place(x=10, y=170)


# 第6步，用户登录输入框entry
# 用户名
var_usr_name = tk.StringVar()
entry_usr_name = tk.Entry(window, textvariable=var_usr_name, font=('Arial', 14))
entry_usr_name.place(x=120, y=175)

# 第8步，定义用户登录功能
def usr_login():
    # 这两行代码就是获取用户输入的usr_name和usr_pwd
    usr_name = var_usr_name.get()

    db = pymysql.connect("localhost", "root", "zsy...000", "users", charset='utf8')
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # 使用execute方法执行SQL语句
    cursor.execute("SELECT id FROM info")
    # 使用 fetchone() 方法获取一条数据
    datas = cursor.fetchall()

        # 如果用户名已经在我们的数据文件中，则提示Error, The user has already signed up!
    if (usr_name,) in datas:

        # 最后如果输入无以上错误，则将注册输入的信息记录到文件当中，并提示注册成功Welcome！,You have successfully signed up!，然后销毁窗口
        capture = cv2.VideoCapture(0)


        while True:
                # 读取每一帧的画面
            ret, image = capture.read()
                # 灰度处理

                # 显示图片
            cv2.imshow('she xiang tou ', image)

            if cv2.waitKey(5) & 0xFF == ord('o'):

                fileName =usr_name
                f = cv2.resize(image, (200, 200))
                cv2.imwrite('D:\python_work\me1' + os.sep + '%s.jpg' % fileName, f)  # 保存图片
                break

        capture.release()
        cv2.destroyAllWindows()
        f2 = open('D:\python_work\me1' + os.sep + '%s.jpg' % fileName, 'rb')
        img3 = base64.b64encode(f2.read())
        f2.close()
        os.remove('D:\python_work\me1' + os.sep + '%s.jpg' % fileName)
        access_token = '24.92dd696df735b3d3fb4ae2d42c5a7955.2592000.1561185546.282335-16316649'
        request_url = "https://aip.baidubce.com/rest/2.0/face/v3/search"
        headers2 = {
                'Content-Type': 'application/json'

        }
        params = {
                "image": img3,
                "image_type": "BASE64",
                "group_id_list": "1_zhang",
                "quality_control": "LOW",
                "liveness_control": "NORMAL"
            }

        request_url = request_url + "?access_token=" + access_token
        response1 = requests.post(request_url, headers=headers2, data=params)
        content1 = response1.content.decode()
        con = json.loads(content1)
        if not con['error_code']:
            if usr_name==con["result"]["user_list"][0]["user_id"]:
                tkinter.messagebox.showinfo(title='Welcome', message='How are you? ' + usr_name)
        else:
            tkinter.messagebox.showerror(message='Error, matching failure.')

    else:  # 如果发现用户名不存在
        is_sign_up = tkinter.messagebox.askyesno('Welcome！ ', 'You have not sign up yet. Sign up now?')
        # 提示需不需要注册新用户
        if is_sign_up:
            usr_sign_up()
# 第9步，定义用户注册功能
def usr_sign_up():
    def sign_to_Hongwei_Website():
        # 以下三行就是获取我们注册时所输入的信息
        nn = new_name.get()
        # 这里是打开我们记录数据的文件，将注册信息读出
        db = pymysql.connect("localhost", "root", "zsy...000", "users", charset='utf8')
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # 使用execute方法执行SQL语句
        cursor.execute("SELECT id FROM info")
        # 使用 fetchone() 方法获取一条数据
        datas = cursor.fetchall()
        # 如果用户名已经在我们的数据文件中，则提示Error, The user has already signed up!
        if (nn,) in datas:
            tkinter.messagebox.showerror('Error', 'The user has already signed up!')

        # 最后如果输入无以上错误，则将注册输入的信息记录到文件当中，并提示注册成功Welcome！,You have successfully signed up!，然后销毁窗口。
        else:
            cursor.execute("INSERT INTO info(id) VALUES('%s')" % (nn))
            db.commit()
            db.close()
            capture = cv2.VideoCapture(0)

            while True:
                # 读取每一帧的画面
                ret, image = capture.read()
                  # 显示图片
                cv2.imshow('she xiang tou ', image)
                if cv2.waitKey(5) & 0xFF == ord('q'):

                    fileName =nn
                    f = cv2.resize(image, (200, 200))
                    cv2.imwrite('D:\python_work\me' + os.sep + '%s.jpg' % fileName, f)# 保存图片
                    break
            capture.release()
            cv2.destroyAllWindows()
            f1 = open('D:\python_work\me' + os.sep + '%s.jpg' % fileName, 'rb')
            img2 = base64.b64encode(f1.read())
            f1.close()
            os.remove('D:\python_work\me' + os.sep + '%s.jpg' % fileName)

            access_token = '24.92dd696df735b3d3fb4ae2d42c5a7955.2592000.1561185546.282335-16316649'
            request_url = "https://aip.baidubce.com/rest/2.0/face/v3/faceset/user/add"
            headers2 = {
                    'Content-Type': 'application/json'

            }
            params = {
                    "image": img2,
                    "image_type": "BASE64",
                    "group_id": "1_zhang",
                    "user_id": nn, }

            request_url = request_url + "?access_token=" + access_token

            response1 = requests.post(request_url, headers=headers2, data=params)
            content1 = response1.content.decode()
            con=json.loads(content1)
            if not con['error_code']:
                tkinter.messagebox.showinfo('Welcome', 'You have successfully signed up!')
            window_sign_up.destroy()

            # 定义长在窗口上的窗口
    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry('300x200')
    window_sign_up.title('Sign up window')

    new_name = tk.StringVar()  # 将输入的注册名赋值给变量
    tk.Label(window_sign_up, text='User name: ').place(x=10, y=10)  # 将`User name:`放置在坐标（10,10）。
    entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)  # 创建一个注册名的`entry`，变量为`new_name`
    entry_new_name.place(x=130, y=10)  # `entry`放置在坐标（150,10）.

    # 下面的 sign_to_Hongwei_Website
    btn_comfirm_sign_up = tk.Button(window_sign_up, text='Sign up', command=sign_to_Hongwei_Website)
    btn_comfirm_sign_up.place(x=180, y=120)


# 第7步，login and sign up 按钮
btn_login = tk.Button(window, text='Login', command=usr_login)
btn_login.place(x=120, y=240)
btn_sign_up = tk.Button(window, text='Sign up', command=usr_sign_up)
btn_sign_up.place(x=200, y=240)

# 第10步，主窗口循环显示
window.mainloop()
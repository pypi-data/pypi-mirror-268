from apscheduler.schedulers.background import BackgroundScheduler
import requests

def scheduler_train_model(url='http://localhost:3000/train'):
    headers = {'Content-Type': 'application/json'}
    response = requests.put(url, headers=headers)
    if response.status_code == 200:
        print("模型训练任务调用成功")
    else:
        print("模型训练任务调用失败，状态码：", response.status_code)

# 假设你的Flask应用和训练接口运行在同一服务器上的3000端口
def scheduler(train_url='http://localhost:3000/train', hour = 4):
    # 初始化 BackgroundScheduler
    scheduler = BackgroundScheduler()
    # 添加定时任务，每天凌晨3点执行train_model函数，并传递train_url作为参数
    scheduler.add_job(scheduler_train_model, 'cron', args=[train_url], hour=hour)
    # 启动调度器
    scheduler.start()
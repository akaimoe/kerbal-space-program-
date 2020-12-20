"""import krpc
import time


conn=krpc.connect(name='test')
vessel=conn.space_center.active_vessel
vessel.auto_pilot.target_pitch_and_heading(90,90)
vessel.auto_pilot.engage()
vessel.control.throttle=1
time.sleep(10)
print('Launch')
vessel.control.activate_next_stage()
a=0
while a<2:
    while vessel.resoures.amount('SolidFuel') > 0:
        time.sleep(1)
    print('separation')
    vessel.control.activate_next_stage()
    a+1
return 0

"""
import PID
import time
import krpc
#import numpy as np

conn=krpc.connect(name='test')                  #建立连接
vessel = conn.space_center.active_vessel             #确认飞行器
vessel.auto_pilot.target_pitch_and_heading(90, 90)        #设置角度
#vessel.auto_pilot.engage()
pid=PID.PID(1,1,100)                          #写入P,I,D数值

#vessel.control.throttle = 0
vessel.control.activate_next_stage()        #启动引擎(按空格，在游戏里面设置好）
time.sleep(0.5)
while True:
    feedback = vessel.flight().mean_altitude  # 读取实时高度信息
    pid.setPoint = 100                 #设置目标高度
    firstdate = pid.update(feedback)      #输入实时高度信息，同时输出PID计算结果，并赋值给firstdate
    outdate = firstdate/100               #将PID输出值除以100，并赋值给outdate
    if(outdate>1):                        #当outdate超出阀值【0,1】时，取阀值 ，并赋值给findate（最终输出值）
        findate=1
    if(outdate<0):
        findate=0
    if(0<=outdate<=1):
        findate=outdate
    vessel.control.throttle = findate               #节流阀设置
    print("findate=%d,high=%d"%(firstdate,feedback))      #打印节流阀的输出值和实时高度
    #time.sleep(0.1)
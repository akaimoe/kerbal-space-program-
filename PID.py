import time

class PID:

    def __init__(self,P=1,I=1,D=0):
        self.Kp=P
        self.Ki=I
        self.Kd=D
        self.sample_time=0.0            #采样时间
        self.now_time=time.time()        #获取当前时间戳
        self.last_time=self.now_time
        self.clear()
    def clear(self):
        self.PTerm=0.0
        self.ITerm=0.0
        self.DTerm=0.0
        self.setPoint=0.0
        self.int_error=0.0
        self.last_error=0.0
        self.windup_guard=20.0
        self.outdate=0.0
    def update(self,return_value):
        error=self.setPoint-return_value
        self.now_time=time.time()
        delta_time=self.now_time-self.last_time
        delta_error=error-self.last_error
        #if(delta_time>self.sample_time):
        self.PTerm=error*self.Kp
        self.ITerm+=error*delta_time
        if(self.ITerm<-self.windup_guard):
            self.ITerm=-self.windup_guard
        if(self.ITerm>self.windup_guard):
            self.ITerm=self.windup_guard
        self.DTerm=0.0
        if(delta_time>0):
            self.DTerm=delta_error/delta_time
        self.now_time=self.last_time
        self.last_error=error
        self.outdate=self.PTerm+(self.Ki*self.ITerm)+(self.Kd*self.DTerm)
        return self.outdate
    def setKP(self,set_number_p):
        self.Kp=set_number_p
    def setKI(self,set_number_i):
        self.Ki=set_number_i
    def setKD(self,set_number_d):
        self.Kp=set_number_d
    def setwindup(self,set_number_windup):
        self.windup_guard=set_number_windup
    def setsample_time(self,set_number_sample_time):
        self.sample_time=set_number_sample_time




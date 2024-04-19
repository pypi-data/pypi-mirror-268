from concurrent.futures import ThreadPoolExecutor
import concurrent.futures as futures
import traceback
import time

class Singleton(type):
    '''单例元类'''
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class ThreadPools(ThreadPoolExecutor):
    '''多例'''
    def __init__(self,max_workers = 8) -> None:
        super().__init__(max_workers=max_workers)
        self.future_list=[]
        self.future_dic:dict[str,futures.Future]={}
        self.is_stop = False # 退出标记，线程中自行检查是否退出

        
    def set_max_workers(self, max_workers):
        self._max_workers = max_workers
        self._adjust_thread_count()
        print(f'set_max_workers:{self._max_workers}')

    def _add_workers(self, add_number):
        self._max_workers += add_number
        self.set_max_workers(self._max_workers)

    def add_task(self,name,task,*args, **kwargs)->futures.Future:
        '''
            # 增加一个多线程任务
            name在一轮多线程中需要唯一,便于找到自己的任务索引。\n
            name为None时,wait_finish不会等待这个任务的执行结果
        '''
        if self._max_workers - len(self._threads) < 4:
            self._add_workers(8)
            # 不建议动态扩容机制，这里主要是提醒作用。
            # 如果检测到这个字符串，那么最好的办法是,设计更大的线程池。
            print(f'Dynamic scaling waring')
        task = self.submit(task,*args, **kwargs)
        if name != None:
            self.future_dic[name]=task
        print(f'add thread task: {len(self._threads)}/{self._max_workers} now/max')
        return task

    def wait_finish(self, time_out=300) -> dict:
        '''等待执行结果，超过300秒就不等了'''
        if time_out==0:
            print('release thread hold without result , until the next wait')
            return
        rs_dic = {}
        start_time = time.time()
        print(f'wait_finish:{time_out}{self.is_stop}   {self.future_dic.keys()}')
        while time.time() - start_time < time_out and not self.is_stop:
            for future_name, future in self.future_dic.items():
                if future.running() or rs_dic.get(future_name,None):
                    continue
                rs_dic[future_name] = future.result()
            if len(rs_dic) == len(self.future_dic):
                break
            time.sleep(0.2)
        self.future_dic = {}
        return rs_dic
        

    def restart(self, wait: bool = ..., *, cancel_futures: bool = ...) -> None:
        super().shutdown(wait, cancel_futures=cancel_futures)
        self.future_list=[]
        super().__init__(max_workers=self._max_workers)
        return

class ThreadPool(ThreadPools,metaclass=Singleton):
    '''单例'''
    def __init__(self,max_workers = 8) -> None:
        self.future_list=[]
        self.future_dic:dict[str,futures.Future]={}
        self.in_running = True # 退出标记，线程中自行检查是否退出
        super().__init__(max_workers=max_workers)
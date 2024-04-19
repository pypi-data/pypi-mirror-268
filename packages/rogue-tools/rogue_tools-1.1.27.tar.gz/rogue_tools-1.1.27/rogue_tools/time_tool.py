import time
def time_stamp():
	'''
	超精准时间戳
	'''
	return int(round(time.time() * 1000000))

def check_time_stamp(ts=0,print_func=None):
	'''
	配合time_stamp使用,debug时候用的时间戳
	'''
	now = time_stamp()
	if ts>0:
		if print_func:
			print_func(f'{now - ts}')
		else:
			print(f'{now - ts}')
	return now

def time_stamp_s():
	'''
	秒级时间戳
	'''
	return int(round(time.time()))

def time_stamp_ms():
	'''
	超精准时间戳
	'''
	return int(round(time.time() * 1000))


def time_for_read(time_stamp = None,delay_stamp_ms=0):
	'''
	提供一种可读性好,且较为精准的时间戳
	精确到ms
	delay_stamp_ms为延迟后X毫秒后的时间戳
	'''
	if time_stamp == None:
		time_stamp = time.time()
	x = str(int(time_stamp * 1000) % 1000).rjust(3,'0')
	return time.strftime(f"%H-%M-%S-{x}", time.localtime(time_stamp+delay_stamp_ms/1000))
def time_for_read_away(t1,t2):
	'''
	辅助time_for_read进行差值计算,返回是ms
	'''
	tp1 = t1.split('-')
	tp2 = t2.split('-')
	return (int(tp2[0])-int(tp1[0]))*3600000+(int(tp2[1])-int(tp1[1]))*60000+(int(tp2[2])-int(tp1[2]))*1000+(int(tp2[3])-int(tp1[3]))
	


def get_now_ms(time_stamp = None,delay_stamp_ms=0):
	if time_stamp == None:
		time_stamp = time.time()
	x = str(int(time_stamp * 1000) % 1000).rjust(3,'0')
	return time.strftime(f"%Y-%m-%d_%H-%M-%S-{x}", time.localtime(time_stamp+delay_stamp_ms/1000))

def get_now_time():
	return time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
def get_now_date():
	return time.strftime("%Y-%m-%d", time.localtime())

def get_next_date(days=1):
	'''
	之前的时间，默认一天后,也可以负数呀
	'''
	return time.strftime("%Y-%m-%d", time.localtime(time.time()-86400*days))

def get_next_hour(hour=1):
	'''
	之前的时间，默认一小时前,也可以负数呀，还可以小数呀
	'''
	return time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime(time.time()-3600*hour))

def countdown(sleep_time):
	print(f'countdown:{sleep_time}/{sleep_time}')
	for i in range(1,sleep_time+1):
		time.sleep(1)
		print(f'countdown:{sleep_time-i}/{sleep_time}')

def calc_run_time(times,func,*arg,**args):
	'''计算一个方法的执行时间'''
	start_time = time.time()
	rs=None
	for _ in range(times):
		rs = func(*arg,**args)
	cost = time.time()-start_time
	avg_time = round(cost*1000/times,2)
	cost = round(cost*1000,2)
	print(f'总耗时:{cost}ms. avg cost:{avg_time}ms')
	return rs


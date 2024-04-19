

class BaseSignal(Exception):
	def __init__(self, info,message='') -> None:
		super().__init__(message)
		self.info = info
		self.message = message
	def __str__(self) -> str:
		return f'[SIGNAL] {self.__class__.__name__}:{self.info}{self.message}'

class RestartScript(BaseSignal):
    def __init__(self, message='') -> None:
        super().__init__('重启顶层循环。',message)

class RestartTask(BaseSignal):
    def __init__(self, message='') -> None:
        super().__init__('重启当前任务。',message)

class NextTask(BaseSignal):
    def __init__(self, message='') -> None:
        super().__init__('跳过当前任务。',message)
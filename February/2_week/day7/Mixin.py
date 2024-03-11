# 믹스인
class LoggerMixin:
    def log(self,message):
        print('Log : {}'.format(message))
class DataProcessor(LoggerMixin):
    def process(self,data):
        self.log(f'Processing {data}')

processor = DataProcessor()
processor.process("Pao Sell")
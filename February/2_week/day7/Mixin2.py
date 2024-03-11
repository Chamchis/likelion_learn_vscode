# 인터페이스 검증 믹스인
class interfaceMixin:
    def verify_interface(self):
        if not hasattr(self,'required_method'):
            raise NotImplementedError('Class에 required_method를 정의해야 합니다! ')
class Print(interfaceMixin):
    def doc_print(self):
        print('문서 인쇄가 잘되네요')
    def required_method(self):
        print('만들어 놓으셨네요')

hnc_print = Print()
hnc_print.verify_interface()

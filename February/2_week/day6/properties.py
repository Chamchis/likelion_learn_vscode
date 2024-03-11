# property
class Temperature:
    def __init__(self, celsius):
        self._celcius = celsius

    @property
    def celsius(self):
        return self.celsius * 1000
    @celsius.setter
    def celsius(self,value):
        if value < -273:
            raise ValueError('들어온 값에 대한 확인이 필요합니다.')
        self._celcius = value

temp = Temperature(6)
temp.celsius = -300
print(temp._celcius)
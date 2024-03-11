from googletrans import Translator

translator = Translator()

# sentence = '안녕하세요 후노레스입니다.'
sentence = input('글자를 입력하세요 : ')
dest = input('어떤 언어로 번역을 원하시나요?\n[en : 영어, ja : 일본어, fr : 프랑스어, de : 독일어, es : 스페인어] : ')

result = translator.translate(sentence,dest)
detected = translator.detect(sentence)

print('='*50)
print(detected.lang,':',sentence)
print(result.dest,':',result.text)
print('='*50)
import re

#abcd, book, desk
#ca?e
#-> care, cafe, case, cave..
#caae, cabe, cace...

p = re.compile("ca.e")
# . (<ex> ca.e) : 하나의 문자를 의미 > care, cafe, case (o) | caffe (x)
# ^ (<ex> ^de) : 문자열의 시작 > desk, destination (o) | fade (x)
# $ (<ex> se$) : 문자열의 끝 > case, base (o) | face (x)

def print_match(m):
    if m:
        print(m.group()) #매치되지 않으면 에러가 발생
    else:
        print("매칭되지 않음")

m = p.match("careless") # 주어진 문자열의 처음부터 일치하는지 확인
print_match(m)
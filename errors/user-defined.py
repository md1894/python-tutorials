# this is the way to define user defined exception
class TooYoung(Exception):

    def __init__(self,msg):
        self.msg = msg






i = int(input('enter age:'))
if i<18:
    try:
        raise TooYoung('kindly wait until 18yrs age')
    except TooYoung as msg:
        print(msg.__class__.__name__,":",msg)
else:
    print('yes you are valid')

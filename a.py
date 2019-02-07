def greeting():
    print('a.py')
    print(__name__)
    
if __name__=='__main__':
    greeting()
    print(__name__)
    print('직접 실행됨')
else:
	print('a.py가 import 되어 실행됨')
	
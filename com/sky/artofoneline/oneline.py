
print("Love...")
print('\n'.join([''.join([(u'ILoveChina爱'[(x-y)%11]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ')for x in range(-30,30)])for y in range(15,-15,-1)]))

print("Love...")
print('\n'.join([''.join([('Love'[(x-y) % len('Love')] if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<= 0else' ') for x in range(-30, 30)]) for y in range(30, -30, -1)]))

print("9*9 乘法表...")
print('\n'. join([' '. join([ "%2s x%2s = %2s"%(j,i,i*j) for j in range(1,i+1)]) for i in range(1,10)]))


'''
1. __import__ 就是我们在倒入模块的时候一直用的 import 关键字，这里是内置函数
2. .choice 里面的东西是2个斜杠，\u2571\u2572为unicode值，表示：╱╲
3. for循环50*24，随机输出斜杠，构造50*24的迷宫。
'''
print("迷宫...")
print(''.join(__import__('random').choice('\u2571\u2572') for i in range(50*24)))

print("小乌龟...")
print('\n'.join([''.join(['*' if abs((lambda a:lambda z,c,n:a(a,z,c,n))(lambda s,z,c,n:z if n==0 else s(s,z*z+c,c,n-1))(0,0.02*x+0.05j*y,40))<2 else' 'for x in range(-80,20)]) for y in range(-20,20)]))


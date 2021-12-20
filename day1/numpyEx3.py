import numpy as np
'''
arr1 = np.array([[2,4,1],[6,9,3]])

print(arr1,'\n')

arr2 = np.array([[True, False, True],[False, True, False]])

print(arr2,'\n')
print(arr1[arr2],'\n') #boolean 색인

arr3 = np.array([False, True])
#크기 다르면 행을 가져옴= false는 첫번째 행, true는 두 번째 행
print(arr1[arr3],'\n')

arr4 = np.array([True, False, True])
print(arr1[:, arr4])
'''

np.random.seed(12345)
names = np.array(['bob','joe','will','bob','will','joe','joe'])
print(names,'\n')
data = np.random.randn(7,4)
print(data,'\n') #정규분포에서 값 뽑아옴

print(names == 'bob','\n') #비교연산자

print(data[names == 'bob'],'\n')
print(data[names == 'bob',2:],'\n')
print(data[names == 'bob',3],'\n')
print(data[data < 0])


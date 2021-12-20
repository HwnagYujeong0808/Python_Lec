import numpy as np

'''
data1 = [6,7.7,8,0,1]  #리스트
print(data1)
# 배열의 특징
# 1.같은 type이므로 한 데이터 당 사이즈가 동일해야 한다(전체를 같은 type으로 만든다)
arr1= np.array(data1,dtype = np.int32)
print(arr1)
print(arr1.dtype)
print()
data2 = [[1,2,3],[4,5,6]]
#실제 2차원 배열 x
print(type(data2))
print(data2,'\n')


arr2=np.array(data2)
#실제 2차원 배열 o
print(arr2)
print(arr2.shape)
print(arr2.dtype,'\n')

arr3 = arr2.astype(dtype=np.float32)
print(arr3)
print(arr3.dtype)
print(type(arr3)) #2d 베열인지 아닌지 확인하고 싶을 때 type확인
'''

arr4 = np.arange(1,10,2)
print(arr4)
arr4 = np.arange(10)
print(arr4)
print(type(arr4),'\n')

arr5 = np.linspace(-3,3,10)
print(arr5,'\n')

arr6 = np.ones([3,4])
print(arr6,'\n')

arr7 = np.ones([3,4])
print(arr7,'\n')

#empty는 권장하지 않음 -> 가장 최근에 같은 크기가 있으면 인용해서 쓰겠다
arr8 = np.empty([3,4])
print(arr8,'\n')
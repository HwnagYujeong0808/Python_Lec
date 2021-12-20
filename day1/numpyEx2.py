import numpy as np

'''
arr1 = np.array([[2,6,1],[9,5,7]])
arr2 = np.array([[4,5,3],[8,6,2]])
print(arr1,'\n')
print(arr2,'\n')

print(arr1+arr2,'\n')
print(arr1*3,'\n')
print(1/arr1,'\n')
print(arr1>arr2)
'''

arr3 = np.array([5,2,9,8,1,3,7])
print(arr3)
print(arr3[2])
print(arr3[1:4]) #슬라이싱

arr3[1] = 3000
print(arr3,'\n')

arr4 = np.array([[4,1,9,2],[8,7,3,5],[33,11,77,54]])
print(arr4)
print(arr4[1,1]) #한번에 읽어옴
print(arr4[1][1],'\n') #1행을 읽고 1행에 대한 1열 가져옴

print(arr4[1:,2:]) #중요 : nd array에서는 콤마를 통해 정확하게 구분해줘야 정확한 값 가져올 수 있음
print(arr4[1:][2:])



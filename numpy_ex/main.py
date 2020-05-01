# 101 NumPy Exercises for Data Analysis (Python)

import numpy as np

# Exercise 4
# NumPy配列arrから奇数の要素のみを取り出し
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print("Exercise4 Ans: " + str(arr[arr % 2 == 1]))

# Exercise 5
# NumPy配列arr中の奇数の要素をすべて-1に書き換える
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr[arr % 2 == 1] = -1
print("Exercise5 Ans: " + str(arr))

# Exercise 8
# NumPy配列a,bを垂直方向に結合する
a = np.arange(10).reshape(2, -1)
b = np.repeat(1, 10).reshape(2, -1)
print("Exercise8 Ans")
# Method 1
print("Method 1:\n" + str(np.concatenate([a, b], 0)))
# Method 2
print("Method 2:\n" + str(np.vstack([a, b])))
# Method 3
print("Method 3:\n" + str(np.r_[a, b]))

# Exercise 14
# NumPy配列aの要素の中から5~10のものを抽出
a = np.array([2, 6, 1, 9, 10, 3, 27])
print("Exercise14 Ans")
# Method 1
index = np.where((a >= 5) & (a <= 10))
print("Method 1: " + str(a[index]))
# Method 2
index = np.where(np.logical_and(a >= 5, a <= 10))
print("Method 2: " + str(a[index]))
# Method 3
print("Method 3: " + str(a[(a >= 5) & (a <= 10)]))

# Exercise 15
# 引数がスカラーの関数に配列を入力できるようにする
def maxx(x, y):
    if x >= y:
        return x
    else:
        return y

pair_max = np.vectorize(maxx, otypes=[float])
a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])
print("Exercise15 Ans: " + str(pair_max(a, b)))

# Exercise 50
# 2次元NumPy配列の各配列を結合して1次元配列にまとめる
arr1 = np.arange(3)
arr2 = np.arange(3, 7)
arr3 = np.arange(7, 10)
array_of_arrays = np.array([arr1, arr2, arr3])
print("Exercise50 Ans")
# Solution 1
arr_2d = np.array([a for arr in array_of_arrays for a in arr])
print("Solution 1: " + str(arr_2d))
# Solution 2
arr_2d = np.concatenate(array_of_arrays)
print("Solution 2: " + str(arr_2d))

# Exercise 51
# NumPy配列の要素の値に対し，1->[1,0,0], 2->[0,1,0], 3->[0,0,1]のような変換を行う
np.random.seed(101)
arr = np.random.randint(1, 4, size=6)
print("Exercise51")
print("arr = " + str(arr))

def one_hot_encodings(arr):
    uniqs = np.unique(arr)
    out = np.zeros((arr.shape[0], uniqs.shape[0]))
    for i, k in enumerate(arr):
        out[i, k-1] = 1
    return out

print("Ans:")
print(one_hot_encodings(arr))

# Exercise 58
# 配列の要素を左から順に見ていき，初めて出てきた数にFalse，2回目以上の数にTrueを対応させた配列を作成する
np.random.seed(100)
a = np.random.randint(0, 5, 10)
print("Exercise58")
print("Array: ", a)
out = np.full(a.shape[0], True)
unique_position = np.unique(a, return_index=True)[1]
out[unique_position] = False
print("Ans: ", out)

# Exercise 61
# 配列中において要素がnanであるものを除く
a = np.array([1, 2, 3, np.nan, 5, 6, 7, np.nan])
out = a[~np.isnan(a)]
print("Exercise61 Ans: ", out)

# Exercise 62
# 2つの配列のユークリッド距離を求める
a = np.array([1, 2, 3, 4, 5])
b = np.array([4, 5, 6, 7, 8])
dist = np.linalg.norm(a - b)
print("Exercise62 Ans: dist = ", dist)

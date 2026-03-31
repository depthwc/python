#1

# nums = [2,7,11,15]
# target = 9
# outl = [i for i in nums if i < target]
# for i in outl:
#     for j in outl:
#         if i+j==target:
#             print([outl.inde ,j])
#             break


#2946

# mat = [[2,2],[2,2]]
# k = 3

# mat1 = [row[:] for row in mat]
# tf = True

# if k%2==0:
#     for i in range(len(mat1)):
#         for j in range(k):
#             mat1[i].append(mat1[i][0])
#             mat1[i].pop(0)

#             # print(mat[i])
#             # print(mat1[i])

#         if mat[i] != mat1[i]:
#             tf = False
#             break
# else:
#     for i in range(len(mat1)):
#         for j in range(k):
#             mat1[i].insert(0,mat1[i][-1])
#             mat1[i].pop(-1)

#             # print(mat[i])
#             # print(mat1[i])

#         if mat[i] != mat1[i]:
#             tf = False
#             break
# # print(tf)


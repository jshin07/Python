# # Odd/Even
#
# def odd_even ():
#     for i in range (1, 2001):
#         if i % 2 !=0:
#             print "Number is" , i ,". This is an odd number."
#         if i % 2 ==0:
#             print "Number is", i,". This is an even number."
#
# odd_even()
#
# # Mulitply

def mulitply (arr, mult):
    for i in range (0, len(arr)):
        arr[i] = arr[i] * mult
    print arr
# mulitply([2,4,10,16], 5)

# Hacker Challenge
# def layered_multiples(arr):
#     print arr
#     new_array = []
#     for x in arr:
#         val_arr = []
#         for i in range(0,x):
#             val_arr.append(1)
#         new_array.append(val_arr)
#     return new_array
#
# x = layered_multiples(multiply([2,4,5],3))
# print x
#



def layered_multiples(arr, mult):
    multiply(arr, mult)


layered_multiples([2,4,5],3)

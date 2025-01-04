# # __add__ method 
# class Test:
    
#     def __init__(self, a ,b):
#         self.a = a
#         self.b = b
        
#     def __add__(self):
#         return f"Adding a and b values : {Test(self.a, self.b)}"
#     def __str__(self):
#         return f"m str Method Test({self.a}, {self.b})"
    
# t1 = Test(20,30)
# print(t1)
# print(t1.__add__())
# t2= Test(4,5)
# print(t2)


# print("adding this line to commit from account1!")
# print("Adding this line to commit from account1 and lakshmi and Test branch")

# # Input=[1, 2, 3, 4, 5, 6]
# # Output: [1, 4, 2, 5, 3, 6]


# from collections import deque
# queue=[1,2,3,4,5,6]
# queue = deque(queue)
# mid = len(queue)//2
# print(mid)

# first_half=deque([])
# for i in range(mid):
#     first_half.append(queue.popleft())
    
# while first_half:    
#     for i in range(mid):
#         queue.append(first_half.popleft())
#         queue.append(queue.popleft())
    
#     print(queue)

# class Stack:
#     def __init__(self):
#         self.l=list()
#     def push(self,element):
#         self.l.append(element)
#     def pop(self):
#         return self.l.pop()
#     def seek(self):
#         print(self.l)

# stack = Stack()
# stack.push(1)
# stack.push(4)
# stack.push(5)
# stack.seek()
# stack.pop()
# stack.seek()      

# d= {1:100,2:200,3:300}
# d1={4:400,5:500}
# d.update(d1)
# # print(d)
# list1 = [1, 2, 3, 4]
# list2 = [3, 4, 5, 6]

# final_elements = set()
# for e1 , e2 in zip(list1,list2):
#     if e1 in list2:
#         final_elements.add(e1)
#     if e2 in list1:
#         final_elements.add(e2)
# print(final_elements) 

# list1 = [1, 2, 2, 3, 4, 4]
# # print(set(list1))
# for i in list1[:]:
#     if list1.count(i) >1:
#         list1.remove(i)

# print(list1)
        
# s= 'hello'
# print(s[::-1])
# s=s.replace('l','lll')
# print(s)

# def longest_word(st):
#     maxx=0
#     for i in st.split():
#         if maxx <len(i):
#              maxx, word = len(i), i
             
#     return maxx, word
# print(longest_word("The fox jumpsinto over the lazy dog"))  # jumps

# print(first_non_repeating_char("nxtwave"))  # n

# def first_non_repeating_char(st):
#     char_dict ={}
#     for i in st:
#         char_dict[i]= char_dict.get(i,0)+1
        
#     print(char_dict)
    
# st= 'nxtwavenx'
# print(first_non_repeating_char(st))

# def count_uppercase(st):
    
#     return len([i for i in st if i.isupper()])
# print(count_uppercase("NxtwaveW"))  # 1

# def flatten(nested_list,flat_list=[]):
#     print(flat_list)
 
#     for i in nested_list:
#         if type(i) == list:
#             flatten(i,flat_list)
#         else:
#             flat_list.append(i)
#             print(flat_list)
       
#     return flat_list



# l=[1, [2, [3, 4], [7,8,[9,10]], 5], 6]
# print(l)
# print(flatten(l,[]))  # [1, 2, 3, 4, 5, 6]


# def binary_search(l,k):
#     left, right = 0, len(l)-1
    
#     while left <right:
#         # print(left,right)
#         mid = (left+right)//2
#         # print(mid)
    
#         if l[mid] <k:
#             left= mid +1
#         elif l[mid]>k:
#             right = mid-1
#         else:
#             return mid
#     return 0
        
    
# print(binary_search([1, 2, 3, 4, 5], 2))  # 2
# Input: arr = [2, 1, 5, 1, 3, 2], k = 3
# Output: 9
# Explanation: Subarray [5, 1, 3] has the maximum sum of 9.
# # 
# def maxx_sum(arr, k):
#     maxtotal=0
#     for i in range(len(arr)-k+1):
#         maxsum = sum(arr[i:i+k])
#         maxtotal = max(maxtotal,maxsum)
    
#     return maxtotal

# arr = [2, 1, 5, 1, 3, 2]; k = 3
# print(maxx_sum(arr,k))
    
# arr = [2, 1, 5, 2, 3, 2]; s = 10

# def maxx_sum(arr, s, k=2):
    
#     for i in range(len(arr)-k+1):
#         maxsum = sum(arr[i:i+k])
#         # print(maxsum,arr[i:i+k])
#         if maxsum >=s:
#             return arr[i:i+k]
    
#     if k <len(arr):
    
#         return maxx_sum(arr,s,k+1)
    

# print(maxx_sum(arr,s,2))

# def count_anagrams(s,p):
#     cnt=0
#     # s = "cbaebabacd";p = "abc"
#     for i in range(len(s)-len(p)+1):
#         st = s[i:i+len(p)]
#         if sorted(st) == sorted(p):
#             cnt+=1
    
#     if cnt>0:
#         return cnt
    
#     return 0
        
    
# s = "cbaebabacd";p = "aba"
# print(count_anagrams(s,p))

# s = "abcdabcbb"
# subs=''
# max_length=0
# for i in s:
#     if i not in subs:
#         subs+=i
#         max_length = max(max_length,len(subs))
             
#     else:
#         # print(subs)
#         subs = subs[subs.index(i)+1:]+i
        

# print(max_length)

# import requests
# import json

# # get_response = requests.get("https://api.restful-api.dev/objects/2")

# # https://api.restful-api.dev/objects
# # print(get_response.status_code, get_response.json())
# # making a post request:
# payload = json.dumps({
#    "name": "Narayana Cool lakshmi",
#    "data": {
#       "year": 2019,
#       "price": 1849.99,
#       "CPU model": "Intel Core i9",
#       "Hard disk size": "1 TB"
#    }
# })
# headers = {"content-type": "application/json"}
# url = "https://api.restful-api.dev/objects"
# response = requests.post(url=url, data=payload, headers=headers)
# print(response.status_code, response.json())
# coding 'utf-8'

# import threading


# a = [['a','b','c','d','e'],['f','g','h','i']]

# the_str = 'asdfaf'

# for x in range(len(the_str)):
#    new = the_str + str(x)
#    print(new)

# def pack(*all_arguments):
#     print(type(all_arguments))  # tuple
#     print(all_arguments)

# def pack_1(**all_arguments):
#     print(type(all_arguments))  # dict
#     print(all_arguments)


# pack(1,2,5)
# pack(1,2,4,6,7)

# pack_1(a = 1,c = 3,e = 5)
# pack_1(e = 5,k = 12,z = 55,i = 13)

# 斐波纳契数列
'''
a,b = 1,1
print(a,b)
for index in range(1,15):
    print(a+b)
    a = b
    b = a + b
'''

# 键入 及转化
'''
s = float(input('input sonmething:'))
h = int(input('input another:'))
print(s+h)
'''

# 画图
'''
#from turtle import *
#speed(1)
#fd(100)
#lt(150)
#fd(100)
'''

# 文件IO
'''
#index = 1
#mystr = "'this is some text txt file'"
#mystr_1 = '123'
#
#f = open('text.txt','a+',encoding='utf-8')
#while index < 4:
#    f.write(mystr+'\t'+mystr_1+'\n')
#    index += 1
#f.close
'''

'''
# repr()  repr(obj)   转化为供解释器读取的形式
# x = 10 * 3.25
# y = 200 * 233
# s = 'The value '+ repr(x) +' and '+ repr(y) + ' is '+ repr(x*y) +' ...'
# print(s)
'''

'''
for x in range(2, 11):
# print(repr(x).rjust(2), repr(x*x).rjust(3),end=' ')
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
# Note use of 'end' on previous line      
# print(repr(x*x*x).rjust(4))
    print( repr(x*x*x).rjust(4))

======一种get tag的方法======
from urllib.request import *
from bs4 import BeautifulSoup as bs

header = {'User-Agent':''}
Html = urlopen('http://jwc.hut.edu.cn/')
html = bs(Html,'lxml')
# print(html)

for tag_a in html.find('select', {'onchange': 'javascript:window.open(this.options[this.selectedIndex].value)'}).option.next_siblings:
    print(tag_a)
'''

# 爬取导航网站网址
'''
import urllib
from bs4 import BeautifulSoup
html = input('ここへ、Please input a website：')
if (html[0:6] != 'https://') | (html[0:6] != 'http://'):
   html = 'https://' + html + '/'
#html = 'https://www.msn.cn/zh-cn'
header = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'}#代理
web = urllib.request.urlopen(html)
content = BeautifulSoup(web,'html.parser')
href = content.find_all('a',attrs = {'target':'_blank'})
ss = []
for tag in href:
    s = []
    url_name = tag.text
    url = tag['href']
    s.append(url_name)
    s.append(url)
    ss.append(s) 
f = open('url.csv','wb')
f.close
f = open('url.csv','ab+')
for in_url in ss:
#    print(type(in_url))
#    print(type(in_url[0]))
    print('\n＊＊＊＊＊＊＊＊＊＊＊')
    for var in in_url:
        print(var)
        #以中文编码写入
        f.write(bytes(var + '\n',encoding = 'GBK'))
f.close
print('==========================================\nできだ、すごいいぞ！！！')
'''



'''
def fun_1():
    x = 2
    return x

def fun(x):
    print(x)

fun()
'''


# 九九乘法表
'''
for a in range(1,10):
    
    for b in range(1,a+1):
        print(a*b)
    print('---------')
'''

# 死循环
'''
while(1):
    print('yes')
'''

# 使用【字典】编写的studentinformation代码
'''
stuInfo = {
        'grade':{
                 'D1':{
                        'Class1':{
                                'STU':{
                                        1:'name1', 
                                        2:'name2', 
                                        3:'name3'
                                        }
                                },
                        'Class2':{
                                'STU':{
                                        1:'name1',
                                        2:'name2',
                                        3:'name3'
                                        }
                                }, 
                        }, 
                'D2':{
                        'Class1':{
                                'STU':{
                                        1:'name1', 
                                        2:'name2', 
                                        3:'name3'
                                        }
                                }, 
                        'Class2':{
                                'STU':{
                                        1:'name1', 
                                        2:'name2', 
                                        3:'name3'
                                        }
                                }, 
                        }, 
                'D3':{
                        'Class1':{
                                'STU':{
                                        1:'name1', 
                                        2:'name2', 
                                        3:'name3'
                                        }
                                }, 
                        'Class2':{
                                'STU':{
                                        1:'name1', 
                                        2:'name2', 
                                        3:'name3'
                                        }
                                }, 
                        }, 
                'D4':{
                        'Class1':{
                                'STU':{
                                        1:'name1', 
                                        2:'name2', 
                                        3:'name3'
                                        }
                                }, 
                        'Class2':{
                                'STU':{
                                        1:'name1', 
                                        2:'name2', 
                                        3:'name3'
                                        }
                                }, 
                        }, 
                'Y':{
                        'Class1':{
                                'STU':{
                                        1:'name1', 
                                        2:'name2', 
                                        3:'name3'
                                        }
                                }, 
                        'Class2':{
                                'STU':{
                                        1:'name1', 
                                        2:'name2', 
                                        3:'name3'
                                        }
                                }, 
                        }
                },
          }
'''

'''
print('grade\tclass\tname')
print(dict_1['grade'], '\t' + dict_1['class'], '\t' + dict_1['STU']['01'])
print(stuInfo['grade']['D1'].keys())
'''

'''
name = []
sex  = []
xid  = []
sid  = []
eveStuInfo = {'stuXid': xid, 'stuName': name, 'stuSex': sex, 'stuSid': sid}
allStuInfo = {}
def wSTUInfo():
    # 写入班级信息
#    打开文件
    f = open('info.txt','r',encoding = 'utf-8')
#    读取每行
    tmp = f.readlines()
#    print(tmp, '\n')
    for line in tmp:
#        print(line)
        l = line.split('\n')[0].split('\t')
        xid.append(l[0])
        name.append(l[1])
        sex.append(l[2])
        sid.append(l[3])
#    print(name, '\n')0
    for index1 in range(1,5):
        eveStuInfo['stuXid']  = xid[index1]
        eveStuInfo['stuName'] = name[index1]
        eveStuInfo['stuSex']  = sex[index1]
        eveStuInfo['stuSid']  = sid[index1]
    allStuInfo[index] = eveStuInfo
#    print(eveStuInfo)
wSTUInfo()
'''


# 装饰器









# 时间
'''
import time

print(time.time())

Time = time.localtime(time.time())
print(Time)

for var in Time:
        print(var)
'''


#for var in range(5):
#    print(var)



# =============================================================================
# trasUrlDic = {
# # 有道翻译
# 'youdao': 'http://www.youdao.com/',
# # google翻译
# 'google': 'https://translate.google.cn/',
# # 百度翻译
# 'baidu': 'https://fanyi.baidu.com/',
# # 爱词霸
# 'iciba': 'http://fy.iciba.com/',
# }
# =============================================================================


# 将字典的key(value)以列表的形式返回
'''
print(len(trasUrlDic))
list_ = trasUrlDic.keys()
value_ = trasUrlDic.values()
print(list_)
print(value_)
'''


# 短信息处理      Example: A -> a
# var = input()
# print(var.lower())


# 往字典中添加key:Value
'''
dic1 = trasUrlDic
dic2 = trasUrlDic
keyName = 'sougou'
valueUrl = 'https://fanyi.sougou.com'
dic1.update( keyName = valueUrl)
dic2 .update({keyName: valueUrl})
print(dic1)
print(dic2)
'''


# MD5加密
'''
import hashlib

mystr = '这是待加密信息'

# 创建一个MD5对象
md = hashlib.md5()

# Tips
# 此处必须声明encode
# 若写法为hl.update(str)  报错为： Unicode-objects must be encoded before hashing
md.update(mystr.encode(encoding='utf-8'))

print('MD5加密前为 ：' + mystr)
print('MD5加密后为 ：' + md.hexdigest())
'''


"""
装饰器

#第一种：
def wrapper(func):
    print(1)
    func()
@wrapper
def det():
    print('def')


"""

"""
# 文件IO(使用with打开文件操作)
filepath = "test1.txt"
text = 'this is a test'
with open(filepath, 'w+', encoding= 'utf-8') as file:
    index = 1
    while index <= 4:
        file.writelines(text + '\n')
        index += 1
"""

"""
filepath = 'test.txt'
with open(filepath, 'r', encoding= 'utf-8') as f:
    lines = f.readlines()
    print(type(lines[0]))
    DicList = []
    for line in lines:
        DicList.append(eval(line))
    print(type(DicList[0]))
"""

"""    
    
    Dic = {
        'pr':'adobe pro',
        'ae':'adobe after effect',
        'au':'adobe audition',
        'ps':'adobe photo shop',
        'me':'adobe media encode'
    }
    import string
    
    def Replace(Str, Old, New):
        for index in range(len(Old)):
            Str = Str.replace(Old[index], New[index])
        return Str
    '''
    filepath = 'adobe product.txt'
    with open(filepath, 'w+', encoding= 'utf-8') as f:
        f.writelines(str(Dic))
        f.write('\n')
    OldList = ['{', '}', ', ', ':', '\'']
    NewList = ['', '', '\n', '\t==>\t', '']
    with open(filepath, 'r+', encoding= 'utf-8') as f:
        Str = f.readlines()
        # result = Replace(Str[0], ',', '\n')
        # result = Str[0].replace('{', '')
        # result = result.replace('}', '')
        # result = result.replace(', ', '\n')
        Str = Replace(Str[0], OldList, NewList)
        f.writelines(Str)
    '''
    
    '''
    import pickle
    filepath = 'test.txt'
    Str = str(Dic)
    with open(filepath, 'wb+') as f:
        pickle.dump(Str, f)
    '''
    
    '''
    filepath = '6000常用密码字典.txt'
    OldList = [', ', '\\n', '[', ']', '\'', '\'']
    NewList = ['\n', '', '', '', '', '']
    with open(filepath, 'r') as f:
        Str = str(f.readlines())
        List = Replace(Str, OldList, NewList)
    print(List)
    # print(Str)
    with open('password.txt', 'w') as f:
        file = f.write(List)
    with open('password.txt', 'r') as f:
        line = f.readline()
        print('\n{}'.format(line))
    '''
    
    def rangematrix(matrix, code):
        var = []
        if code == 1:
            for i in range(len(matrix_a)):
                matrixlist = []
                for j in range(len(matrix_a[i])):
                    matrixlist.append(matrix_a[i][j])
                var.append(matrixlist)
        if code == 2:
            for j in range(len(matrix_a)):
                matrixlist = []
                for i in range(len(matrix_a[j])):
                    matrixlist.append(matrix[i][j])
                var.append(matrixlist)
        if code == 3:
            pass
    
        return var
    matrix_a = [
        [1, 2, 3],
        [5, 7, 34],
        [23, 35, 11]
    ]
    matrix_b = [
        [4, 4, 3],
        [23, -23, 45],
        [0, 24, 12]
    ]
    
    element1 = rangematrix(matrix_a, 1)
    element2 = rangematrix(matrix_b, 2)
    # print('{0}\n{1}'.format(element1, element2))
    print(rangematrix(matrix_a, 1))

"""

"""
    #矩阵的逆
    A = [
        [1, -1, 1],
        [1, 1, 1],
        [2, 1, 1]
    ]
        #算法
            #1.求 |A| 或 A*
    for i in range(len(A) - 1):
        for j in range(len(a[i])):
            pass
"""


#矩阵乘以矩阵
A = [[4, 4, -1],
    [-1, 12, 3],
    [-1, -1, 2]
]
B = [[1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]
# det ==> 行列式(determinant)
class matrix:
    """
    矩阵的运算
    """
    def __int__(self):
        pass

    def sum(self, A, B):
        """
        矩阵 与 矩阵的加法
        :param A: 矩阵
        :param B: 矩阵
        :return: C(矩阵)
        """
        C = []
        for i in range(len(A)):
            c = []
            for j in range(len(A[i])):
                var = 2 * A[i][j] - 13 * B[j][i]
                c.append(var)
            C.append(c)
        return C


    def mutiply(self, A, B):
        """
        矩阵与矩阵的乘法 和 矩阵的数乘运算
        :param A: 矩阵 或 数字
        :param B: 矩阵
        :return: 返回矩阵C
        """
        if type(A) in (type(1), type(1.0)):
            C = []
            for i in range(len(B)):
                c = []
                for j in range(len(B[i])):
                    var = A * B[i][j]
                    c.append(var)
                C.append(c)
        elif type(A) is type(B):
            C = []
            for i in range(len(A)):
                c = []
                b = 0
                index = 0
                for j in range(len(A[i])):
                    while index < len(A[i]):
                        a = A[i][j] * B[index][i]
                        b += a
                        index += 1
                        c.append(b)
                C.append(c)
        elif ((type(A) in (type(1), type(1.0))) and (type(A) is type(B))) is False:
            print('Type Error\n')
            print("\n" + "="*5 + "Error请输入一个矩阵或是数字作为A" + "="*5 + "\n")
        return C

    def Ni(self, A):
        C = []
        for i in range(len(A)-1):
            c = []
            for j in range(len(A[i])-1):
                var = A[i+1][j+1]
                c.append(var)
            C.append(c)
        return C
# NI = matrix()
# print(NI.Ni(A))
# thesum = matrix()
# print(thesum.sum(A, B))
# thesum = matrix()
multiply = matrix()
print(multiply.mutiply(A, B))

# 求矩阵的伴随矩阵
def add(A):
    var3 = []
    for i in range(len(A)):
        for j in range(len(A[i])):
            var2 = []
            for a in range(len(A)):
                var1 = []
                for b in range(len(A[a])):
                    if a != i & b != j:
                        var1.append(A[a][b])
                var2.append(var1)
            var3.append(var2)
    return var3

file = ('number')
with open(file, 'w+') as f:
    f.writelines(str(add(A)))















































































































































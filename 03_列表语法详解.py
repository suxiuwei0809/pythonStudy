# Python 列表（List）语法详解

# ==================== 1. 列表的基本概念 ====================

print("=== 列表的基本概念 ===")

# 列表是 Python 中最常用的数据类型之一
# 列表是有序、可变的集合，可以存储任意类型的元素
# 列表用方括号 [] 表示，元素之间用逗号分隔

# 基本列表定义
numbers = [1, 2, 3, 4, 5]
fruits = ['苹果', '香蕉', '橙子']
mixed = [1, 'hello', 3.14, True]  # 混合类型列表

print(f"数字列表: {numbers}")
print(f"水果列表: {fruits}")
print(f"混合列表: {mixed}")


# ==================== 2. 列表的创建和初始化 ====================

print("\n=== 列表的创建和初始化 ===")

# 直接创建
list1 = [1, 2, 3, 4, 5]
print(f"直接创建: {list1}")

# 使用 list() 函数
list2 = list([1, 2, 3, 4, 5])
print(f"使用list()函数: {list2}")

# 创建空列表
empty_list = []
empty_list2 = list()
print(f"空列表1: {empty_list}")
print(f"空列表2: {empty_list2}")

# 使用 range() 创建数字列表
list3 = list(range(10))
print(f"使用range创建: {list3}")

# 列表推导式创建
list4 = [x**2 for x in range(10)]
print(f"列表推导式: {list4}")

# 创建重复元素的列表
list5 = [0] * 5
print(f"重复元素: {list5}")


# ==================== 3. 列表的访问和切片 ====================

print("\n=== 列表的访问和切片 ===")

fruits = ['苹果', '香蕉', '橙子', '葡萄', '西瓜']

# 访问单个元素（索引从0开始）
print(f"第一个元素: {fruits[0]}")  # 苹果
print(f"第二个元素: {fruits[1]}")  # 香蕉
print(f"最后一个元素: {fruits[-1]}")  # 西瓜
print(f"倒数第二个元素: {fruits[-2]}")  # 葡萄

# 切片操作
print(f"前3个元素: {fruits[0:3]}")  # ['苹果', '香蕉', '橙子']
print(f"从第2个开始: {fruits[1:]}")  # ['香蕉', '橙子', '葡萄', '西瓜']
print(f"前3个元素: {fruits[:3]}")  # ['苹果', '香蕉', '橙子']
print(f"每隔一个元素: {fruits[::2]}")  # ['苹果', '橙子', '西瓜']
print(f"反转列表: {fruits[::-1]}")  # ['西瓜', '葡萄', '橙子', '香蕉', '苹果']

# 切片赋值
fruits_copy = fruits.copy()
fruits_copy[1:3] = ['樱桃', '桃子']
print(f"切片赋值: {fruits_copy}")


# ==================== 4. 列表的修改操作 ====================

print("\n=== 列表的修改操作 ===")

numbers = [1, 2, 3, 4, 5]
print(f"原始列表: {numbers}")

# 修改元素
numbers[0] = 10
print(f"修改第一个元素: {numbers}")

# 修改多个元素
numbers[1:3] = [20, 30]
print(f"修改多个元素: {numbers}")

# 添加元素到末尾
numbers.append(6)
print(f"添加元素到末尾: {numbers}")

# 在指定位置插入元素
numbers.insert(2, 25)
print(f"在位置2插入元素: {numbers}")

# 扩展列表（添加另一个列表的所有元素）
numbers.extend([7, 8, 9])
print(f"扩展列表: {numbers}")

# 删除指定位置的元素
del numbers[0]
print(f"删除第一个元素: {numbers}")

# 删除指定值的元素（只删除第一个匹配的）
numbers.remove(20)
print(f"删除值为20的元素: {numbers}")

# 删除并返回最后一个元素
last = numbers.pop()
print(f"删除最后一个元素: {last}")
print(f"删除后的列表: {numbers}")

# 清空列表
numbers.clear()
print(f"清空列表: {numbers}")


# ==================== 5. 列表的常用方法 ====================

print("\n=== 列表的常用方法 ===")

fruits = ['苹果', '香蕉', '橙子', '苹果', '葡萄']
print(f"原始列表: {fruits}")

# 统计元素出现次数
apple_count = fruits.count('苹果')
print(f"'苹果'出现次数: {apple_count}")

# 查找元素索引
index = fruits.index('橙子')
print(f"'橙子'的索引: {index}")

# 列表排序
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort()
print(f"升序排序: {numbers}")

numbers.sort(reverse=True)
print(f"降序排序: {numbers}")

# 反转列表
fruits.reverse()
print(f"反转列表: {fruits}")

# 获取列表长度
print(f"列表长度: {len(fruits)}")

# 获取列表最大值和最小值
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"最大值: {max(numbers)}")
print(f"最小值: {min(numbers)}")

# 计算列表元素总和
print(f"总和: {sum(numbers)}")


# ==================== 6. 列表的遍历 ====================

print("\n=== 列表的遍历 ===")

fruits = ['苹果', '香蕉', '橙子', '葡萄']

# 使用 for 循环遍历
print("使用for循环遍历:")
for fruit in fruits:
    print(f"  - {fruit}")

# 使用索引遍历
print("使用索引遍历:")
for i in range(len(fruits)):
    print(f"  索引{i}: {fruits[i]}")

# 使用 enumerate() 同时获取索引和值
print("使用enumerate遍历:")
for index, fruit in enumerate(fruits):
    print(f"  索引{index}: {fruit}")

# 使用 while 循环遍历
print("使用while循环遍历:")
i = 0
while i < len(fruits):
    print(f"  - {fruits[i]}")
    i += 1


# ==================== 7. 列表推导式 ====================

print("\n=== 列表推导式 ===")

# 基本列表推导式
squares = [x**2 for x in range(10)]
print(f"平方数: {squares}")

# 带条件的列表推导式
even_numbers = [x for x in range(20) if x % 2 == 0]
print(f"偶数: {even_numbers}")

# 带多个条件的列表推导式
numbers = [x for x in range(100) if x % 3 == 0 and x % 5 == 0]
print(f"3和5的倍数: {numbers}")

# 复杂表达式
words = ['hello', 'world', 'python']
uppercase_words = [word.upper() for word in words]
print(f"大写单词: {uppercase_words}")

# 嵌套列表推导式
matrix = [[i*j for j in range(3)] for i in range(3)]
print(f"乘法表: {matrix}")

# 使用函数的列表推导式
def process_item(item):
    return item * 2

processed = [process_item(x) for x in range(5)]
print(f"函数处理: {processed}")

# 同时满足多个条件
numbers = [x for x in range(100) if x % 3 == 0 and x % 5 == 0]
# 结果: [0, 15, 30, 45, 60, 75, 90]
print(f"满足条件的数字: {numbers}")


# 生成乘法表
matrix = [[i*j for j in range(3)] for i in range(3)]
# 结果: [[0, 0, 0], [0, 1, 2], [0, 2, 4]]

# 传统写法
matrix = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(i*j)
    matrix.append(row)
print(f"乘法表: {matrix}")

# 生成乘法表
matrix = [[i*j for j in range(3)] for i in range(3)]
# 结果: [[0, 0, 0], [0, 1, 2], [0, 2, 4]]

# 传统写法
matrix = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(i*j)
    matrix.append(row)
print(f"乘法表: {matrix}")

# 处理学生成绩
students = [('张三', 85), ('李四', 92), ('王五', 78)]
passed = [f"{name}通过" for name, score in students if score >= 60]
# 结果: ['张三通过', '李四通过', '王五通过']
print(f"及格学生: {passed}")


# 去除空值和空字符串
raw_data = [1, 2, None, 3, '', 4, None, 5]
cleaned = [x for x in raw_data if x is not None and x != '']
# 结果: [1, 2, 3, 4, 5]
print(f"清理后的数据: {cleaned}")


# 温度转换
celsius = [0, 10, 20, 30, 40]
fahrenheit = [(c * 9/5) + 32 for c in celsius]
# 结果: [32.0, 50.0, 68.0, 86.0, 104.0]
print(f"华氏温度: {fahrenheit}")



# 读取文件并处理行
lines = ['hello world', 'python programming', 'data analysis']
processed = [line.strip().upper() for line in lines]
# 结果: ['HELLO WORLD', 'PYTHON PROGRAMMING', 'DATA ANALYSIS']
print(f"处理后的行: {processed}")



# ==================== 8. 列表的排序 ====================

print("\n=== 列表的排序 ===")

# sort() 方法（原地排序）
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort()
print(f"原地排序: {numbers}")

# sorted() 函数（返回新列表）
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_numbers = sorted(numbers)
print(f"原列表: {numbers}")
print(f"新排序列表: {sorted_numbers}")

# 降序排序
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort(reverse=True)
print(f"降序排序: {numbers}")

# 按绝对值排序
numbers = [-3, 1, -4, 1, 5, -9, 2, 6]
numbers.sort(key=abs)
print(f"按绝对值排序: {numbers}")

# 按字符串长度排序
words = ['apple', 'banana', 'cherry', 'date']
words.sort(key=len)
print(f"按长度排序: {words}")

# 自定义排序规则
students = [('张三', 90), ('李四', 85), ('王五', 95)]
students.sort(key=lambda x: x[1], reverse=True)
print(f"按分数排序: {students}")


# ==================== 9. 列表的复制 ====================

print("\n=== 列表的复制 ===")

original = [1, 2, 3, 4, 5]

# 浅拷贝（推荐）
copy1 = original.copy()
copy2 = original[:]
copy3 = list(original)

print(f"原列表: {original}")
print(f"拷贝1: {copy1}")
print(f"拷贝2: {copy2}")
print(f"拷贝3: {copy3}")

# 修改拷贝不影响原列表
copy1[0] = 100
print(f"修改拷贝1后: {copy1}")
print(f"原列表: {original}")

# 深拷贝（用于嵌套列表）
import copy
nested_list = [[1, 2], [3, 4], [5, 6]]
shallow_copy = nested_list.copy()
deep_copy = copy.deepcopy(nested_list)

shallow_copy[0][0] = 100
deep_copy[1][0] = 200

print(f"原嵌套列表: {nested_list}")
print(f"浅拷贝: {shallow_copy}")
print(f"深拷贝: {deep_copy}")


# ==================== 10. 列表的高级操作 ====================

print("\n=== 列表的高级操作 ===")

# 列表拼接
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(f"列表拼接: {combined}")

# 列表重复
repeated = [1, 2, 3] * 3
print(f"列表重复: {repeated}")

# 列表成员检查
fruits = ['苹果', '香蕉', '橙子']
print(f"'苹果'在列表中: {'苹果' in fruits}")
print(f"'葡萄'在列表中: {'葡萄' in fruits}")

# 列表比较
list_a = [1, 2, 3]
list_b = [1, 2, 3]
list_c = [1, 2, 4]
print(f"list_a == list_b: {list_a == list_b}")
print(f"list_a == list_c: {list_a == list_c}")

# 列表解包
numbers = [1, 2, 3]
a, b, c = numbers
print(f"解包结果: a={a}, b={b}, c={c}")

# 列表作为函数参数
def process_list(lst):
    return [x * 2 for x in lst]

result = process_list([1, 2, 3, 4, 5])
print(f"函数处理结果: {result}")


# ==================== 11. 实用示例 ====================

print("\n=== 实用示例 ===")

# 示例1：学生成绩管理
def manage_student_scores():
    """学生成绩管理系统"""
    students = [
        {'name': '张三', 'score': 85},
        {'name': '李四', 'score': 92},
        {'name': '王五', 'score': 78},
        {'name': '赵六', 'score': 95}
    ]
    
    # 计算平均分
    avg_score = sum(student['score'] for student in students) / len(students)
    print(f"平均分: {avg_score:.1f}")
    
    # 找出最高分学生
    top_student = max(students, key=lambda x: x['score'])
    print(f"最高分学生: {top_student['name']} - {top_student['score']}分")
    
    # 筛选及格学生
    passed_students = [s for s in students if s['score'] >= 60]
    print(f"及格人数: {len(passed_students)}")
    
    # 按分数排序
    sorted_students = sorted(students, key=lambda x: x['score'], reverse=True)
    print("排名:")
    for i, student in enumerate(sorted_students, 1):
        print(f"  {i}. {student['name']}: {student['score']}分")

manage_student_scores()


# 示例2：数据清洗
def clean_data(raw_data):
    """数据清洗函数"""
    # 去除空值
    cleaned = [item for item in raw_data if item is not None and item != '']
    
    # 去除重复
    cleaned = list(set(cleaned))
    
    # 排序
    cleaned.sort()
    
    return cleaned

raw_data = [1, 2, None, 3, '', 2, 4, None, 5, '']
cleaned_data = clean_data(raw_data)
print(f"原始数据: {raw_data}")
print(f"清洗后数据: {cleaned_data}")


# 示例3：数据分组
def group_data(data, key_func):
    """数据分组函数"""
    groups = {}
    for item in data:
        key = key_func(item)
        if key not in groups:
            groups[key] = []
        groups[key].append(item)
    return groups

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
grouped = group_data(numbers, lambda x: '偶数' if x % 2 == 0 else '奇数')
print(f"数据分组: {grouped}")


# 示例4：列表去重（保持顺序）
def remove_duplicates_preserve_order(lst):
    """去重并保持原始顺序"""
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

numbers = [1, 2, 2, 3, 4, 4, 5, 1, 6]
unique_numbers = remove_duplicates_preserve_order(numbers)
print(f"原始列表: {numbers}")
print(f"去重后: {unique_numbers}")


# 示例5：列表分块
def chunk_list(lst, chunk_size):
    """将列表分成指定大小的块"""
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]

large_list = list(range(1, 21))
chunks = chunk_list(large_list, 5)
print(f"原始列表: {large_list}")
print(f"分块结果: {chunks}")


# 示例6：列表交集、并集、差集
def list_operations(list1, list2):
    """列表集合操作"""
    # 交集
    intersection = list(set(list1) & set(list2))
    
    # 并集
    union = list(set(list1) | set(list2))
    
    # 差集
    difference = list(set(list1) - set(list2))
    
    return {
        '交集': intersection,
        '并集': union,
        '差集': difference
    }

list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]
operations = list_operations(list_a, list_b)
print(f"列表A: {list_a}")
print(f"列表B: {list_b}")
for op_name, result in operations.items():
    print(f"{op_name}: {result}")


print("\n=== Python 列表语法详解完成 ===")


# 基本语法：lambda 参数: 表达式
square = lambda x: x ** 2
print(square(5))  # 25

# 多个参数
add = lambda x, y: x + y
print(add(3, 4))  # 7

# 与高阶函数结合
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"平方数: {squared}")

# 基本装饰器
def my_decorator(func):
    def wrapper():
        print("函数执行前")
        func()
        print("函数执行后")
    return wrapper

@my_decorator
def say_hello():
    print("Hello, World!")

say_hello()

# 带参数的装饰器
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"调用函数：{func.__name__}")
        result = func(*args, **kwargs)
        print(f"返回值：{result}")
        return result
    return wrapper

@log_decorator
def add_numbers(a, b):
    return a + b

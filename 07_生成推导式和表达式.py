# Python 生成推导式和表达式详解

# ==================== 1. 列表推导式 ====================

print("=== 列表推导式 ===")

# 基本语法：[表达式 for 变量 in 可迭代对象 if 条件]


# 基本列表推导式
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(f"原始列表：{numbers}")
print(f"平方列表：{squares}")

# 带条件的列表推导式
even_numbers = [x for x in range(20) if x % 2 == 0]
print(f"1-19的偶数：{even_numbers}")

# 多个条件的列表推导式
numbers = list(range(100))
multiple_of_3_and_5 = [x for x in numbers if x % 3 == 0 and x % 5 == 0]
print(f"3和5的倍数：{multiple_of_3_and_5}")

# 嵌套列表推导式
matrix = [[i*j for j in range(3)] for i in range(3)]
print(f"乘法表：{matrix}")

# 带函数的列表推导式
words = ['hello', 'world', 'python']
uppercase_words = [word.upper() for word in words]
print(f"大写单词：{uppercase_words}")

# 带复杂表达式的列表推导式
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
processed = [x**2 if x % 2 == 0 else x**3 for x in numbers]
print(f"偶数平方，奇数立方：{processed}")

# ==================== 2. 字典推导式 ====================

print("\n=== 字典推导式 ===")

# 基本语法：{键表达式: 值表达式 for 变量 in 可迭代对象 if 条件}

# 基本字典推导式
words = ['apple', 'banana', 'cherry']
word_lengths = {word: len(word) for word in words}
print(f"单词长度：{word_lengths}")

# 带条件的字典推导式
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = {num: num**2 for num in numbers if num % 2 == 0}
print(f"偶数平方：{even_squares}")

# 从两个列表创建字典
keys = ['name', 'age', 'city']
values = ['张三', 25, '北京']
person_dict = {k: v for k, v in zip(keys, values)}
print(f"个人信息：{person_dict}")

# 交换字典的键和值
original_dict = {'a': 1, 'b': 2, 'c': 3}
swapped_dict = {v: k for k, v in original_dict.items()}
print(f"交换键值：{swapped_dict}")

# 带复杂表达式的字典推导式
words = ['hello', 'world', 'python', 'programming']
word_info = {
    word: {
        'length': len(word),
        'first_char': word[0],
        'last_char': word[-1],
        'uppercase': word.upper()
    }
    for word in words
}
print(f"单词信息：{word_info}")

# ==================== 3. 集合推导式 ====================

print("\n=== 集合推导式 ===")

# 基本语法：{表达式 for 变量 in 可迭代对象 if 条件}

# 基本集合推导式
numbers = [1, 2, 3, 4, 5, 4, 3, 2, 1]
unique_numbers = {x for x in numbers}
print(f"唯一数字：{unique_numbers}")

# 带条件的集合推导式
numbers = list(range(20))
even_numbers = {x for x in numbers if x % 2 == 0}
print(f"偶数集合：{even_numbers}")

# 字符串处理
sentence = "hello world python programming"
unique_chars = {char for char in sentence if char.isalpha()}
print(f"唯一字母：{unique_chars}")

# 带函数的集合推导式
words = ['hello', 'world', 'hello', 'python']
unique_words = {word.upper() for word in words}
print(f"唯一单词（大写）：{unique_words}")

# ==================== 4. 生成器表达式 ====================

print("\n=== 生成器表达式 ===")

# 基本语法：(表达式 for 变量 in 可迭代对象 if 条件)

# 基本生成器表达式
gen_exp = (x**2 for x in range(10))
print(f"生成器表达式类型：{type(gen_exp)}")
print(f"生成器值：{list(gen_exp)}")

# 带条件的生成器表达式
even_gen = (x for x in range(20) if x % 2 == 0)
print(f"偶数生成器：{list(even_gen)}")

# 生成器表达式的优势
print("生成器表达式的优势：")
print("1. 内存效率高（惰性求值）")
print("2. 可以处理无限序列")
print("3. 适用于大数据处理")

# 对比列表推导式和生成器表达式
import sys

# 列表推导式（立即求值）
list_comp = [x**2 for x in range(1000000)]
print(f"列表推导式内存使用：{sys.getsizeof(list_comp)} 字节")

# 生成器表达式（惰性求值）
gen_comp = (x**2 for x in range(1000000))
print(f"生成器表达式内存使用：{sys.getsizeof(gen_comp)} 字节")

# ==================== 5. 条件表达式 ====================

print("\n=== 条件表达式 ===")

# 基本语法：值1 if 条件 else 值2

# 基本条件表达式
age = 25
status = "成年" if age >= 18 else "未成年"
print(f"年龄{age}：{status}")

# 嵌套条件表达式
score = 85
grade = (
    "优秀" if score >= 90 else
    "良好" if score >= 80 else
    "及格" if score >= 60 else
    "不及格"
)
print(f"分数{score}：{grade}")

# 在列表推导式中使用条件表达式
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
processed = [
    "偶数" if x % 2 == 0 else "奇数"
    for x in numbers
]
print(f"数字分类：{processed}")

# 在字典推导式中使用条件表达式
words = ['hello', 'world', 'python', 'programming']
word_classification = {
    word: (
        "短单词" if len(word) <= 5 else
        "中等单词" if len(word) <= 8 else
        "长单词"
    )
    for word in words
}
print(f"单词分类：{word_classification}")

# ==================== 6. Lambda 表达式 ====================

print("\n=== Lambda 表达式 ===")

# 基本语法：lambda 参数: 表达式

# 基本 lambda 表达式
square = lambda x: x**2
print(f"5的平方：{square(5)}")

# 多个参数的 lambda 表达式
add = lambda x, y: x + y
print(f"3 + 4 = {add(3, 4)}")

# 带默认参数的 lambda 表达式
power = lambda x, p=2: x**p
print(f"2的3次方：{power(2, 3)}")
print(f"3的2次方：{power(3)}")

# lambda 与高阶函数结合
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(f"平方列表：{squared}")

# lambda 与 filter 结合
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"偶数列表：{even_numbers}")

# lambda 与 sorted 结合
students = [('张三', 85), ('李四', 92), ('王五', 78)]
students_sorted = sorted(students, key=lambda x: x[1], reverse=True)
print(f"按分数排序：{students_sorted}")

# ==================== 7. 正则表达式 ====================

print("\n=== 正则表达式 ===")

import re

# 基本正则表达式匹配
pattern = r'hello'
text = "hello world"
match = re.search(pattern, text)
print(f"匹配结果：{match.group() if match else '未匹配'}")

# 邮箱验证（你看到的例子）
def validate_email(email):
    """验证邮箱格式
    
    正则表达式解析：
    ^[a-zA-Z0-9._%+-]+  - 用户名部分：字母、数字、点、下划线、百分号、加号、减号
    @                        - @ 符号
    [a-zA-Z0-9.-]+       - 域名部分：字母、数字、点、减号
    \.                      - 点号
    [a-zA-Z]{2,}          - 顶级域名：至少2个字母
    $                        - 字符串结束
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return bool(re.match(pattern, email))

print(f"'user@example.com' 有效：{validate_email('user@example.com')}")
print(f"'invalid-email' 有效：{validate_email('invalid-email')}")
print(f"'test.user@domain.co.uk' 有效：{validate_email('test.user@domain.co.uk')}")

# 手机号验证
def validate_phone(phone):
    """验证中国手机号"""
    pattern = r'^1[3-9]\d{9}
    return bool(re.match(pattern, phone))

print(f"'13812345678' 有效：{validate_phone('13812345678')")
print(f"'12345678901' 有效：{validate_phone('12345678901')}")

# 身份证号验证
def validate_id_card(id_card):
    """验证中国身份证号（简单版本）"""
    pattern = r'^\d{17}[\dXx]
    return bool(re.match(pattern, id_card))

print(f"'110101199001011234' 有效：{validate_id_card('110101199001011234')}")
print(f"'123456789012345' 有效：{validate_id_card('123456789012345')}")

# URL 验证
def validate_url(url):
    """验证 URL 格式"""
    pattern = r'^https?://(?:www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(?:/\S*)?
    return bool(re.match(pattern, url))

print(f"'https://www.example.com' 有效：{validate_url('https://www.example.com')}")
print(f"'http://example.com/path' 有效：{validate_url('http://example.com/path')}")

# 正则表达式常用模式
print("\n正则表达式常用模式：")
print("r'\d+' - 匹配一个或多个数字")
print("r'[a-z]+' - 匹配一个或多个小写字母")
print("r'^hello' - 匹配以 hello 开头的字符串")
print("r'world - 匹配以 world 结尾的字符串")
print("r'hello|world' - 匹配 hello 或 world")
print("r'[A-Z][a-z]+' - 匹配首字母大写，其余小写的单词")

# 正则表达式替换
text = "Hello World, Hello Python"
replaced = re.sub(r'Hello', 'Hi', text)
print(f"替换结果：{replaced}")

# 正则表达式分割
text = "apple,banana;cherry|orange"
split_result = re.split(r'[,;|]', text)
print(f"分割结果：{split_result}")

# 正则表达式查找所有匹配
text = "apple123banana456cherry789"
numbers = re.findall(r'\d+', text)
print(f"找到的数字：{numbers}")

# ==================== 8. 复杂表达式组合 ====================

print("\n=== 复杂表达式组合 ===")

# 列表推导式 + 条件表达式 + 函数
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
complex_list = [
    (
        "偶数平方" if x % 2 == 0 else
        "奇数立方" if x % 2 == 1 else
        "零"
    )
    for x in numbers
]
print(f"复杂处理：{complex_list}")

# 字典推导式 + lambda 表达式
words = ['hello', 'world', 'python', 'programming']
word_stats = {
    word: {
        'length': len(word),
        'type': (
            "短单词" if len(word) <= 5 else
            "中等单词" if len(word) <= 8 else
            "长单词"
        ),
        'vowels': sum(1 for char in word if char in 'aeiou')
    }
    for word in words
}
print(f"单词统计：{word_stats}")

# 生成器表达式 + filter + map
numbers = list(range(100))
filtered_squared = (
    x**2  # map 操作：平方
    for x in numbers
    if x % 2 == 0  # filter 操作：只处理偶数
    if x < 20  # 额外条件：只处理小于20的数
)
print(f"过滤并平方：{list(filtered_squared)}")

# 正则表达式 + 列表推导式
text = "apple123 banana456 cherry789 date123"
words_with_numbers = [
    word
    for word in text.split()
    if re.search(r'\d+', word)  # 使用正则表达式检查是否包含数字
]
print(f"包含数字的单词：{words_with_numbers}")

# ==================== 9. 实用表达式示例 ====================

print("\n=== 实用表达式示例 ===")

# 示例1：数据清洗
def clean_data(raw_data):
    """数据清洗函数"""
    # 使用列表推导式去除空值
    cleaned = [item for item in raw_data if item is not None and item != '']
    
    # 使用集合推导式去重
    unique = list(set(cleaned))
    
    # 使用列表推导式转换类型
    converted = [int(item) if isinstance(item, str) and item.isdigit() else item for item in unique]
    
    return converted

raw_data = [1, 2, None, '3', '', 2, 4, None, '5', '6']
cleaned_data = clean_data(raw_data)
print(f"原始数据：{raw_data}")
print(f"清洗后数据：{cleaned_data}")

# 示例2：文本处理
def process_text(text):
    """文本处理函数"""
    # 使用正则表达式分割单词
    words = re.findall(r'\b\w+\b', text)
    
    # 使用字典推导式统计词频
    word_count = {word: words.count(word) for word in set(words)}
    
    # 使用列表推导式过滤长单词
    long_words = [word for word in words if len(word) > 5]
    
    return {
        'words': words,
        'word_count': word_count,
        'long_words': long_words
    }

text = "hello world hello python world programming"
result = process_text(text)
print(f"文本处理结果：{result}")

# 示例3：数据转换
def convert_temperature(temperatures, scale='c'):
    """温度转换函数"""
    if scale.lower() == 'c':
        # 摄氏度转华氏度
        return [temp * 9/5 + 32 for temp in temperatures]
    elif scale.lower() == 'f':
        # 华氏度转摄氏度
        return [(temp - 32) * 5/9 for temp in temperatures]
    else:
        return temperatures

celsius_temps = [0, 10, 20, 30, 40]
fahrenheit_temps = convert_temperature(celsius_temps, 'c')
print(f"摄氏度：{celsius_temps}")
print(f"华氏度：{[round(temp, 1) for temp in fahrenheit_temps]}")

# 示例4：复杂数据结构处理
def process_students(students):
    """处理学生数据"""
    # 使用字典推导式创建学生档案
    student_profiles = {
        student['name']: {
            'age': student['age'],
            'score': student['score'],
            'grade': (
                'A' if student['score'] >= 90 else
                'B' if student['score'] >= 80 else
                'C' if student['score'] >= 70 else
                'D'
            ),
            'passed': student['score'] >= 60
        }
        for student in students
    }
    
    # 使用列表推导式筛选优秀学生
    top_students = [
        name for name, info in student_profiles.items()
        if info['grade'] == 'A'
    ]
    
    return {
        'profiles': student_profiles,
        'top_students': top_students
    }

students = [
    {'name': '张三', 'age': 20, 'score': 95},
    {'name': '李四', 'age': 21, 'score': 88},
    {'name': '王五', 'age': 19, 'score': 92},
    {'name': '赵六', 'age': 22, 'score': 78}
]

result = process_students(students)
print(f"学生档案：{result['profiles']}")
print(f"优秀学生：{result['top_students']}")

# 示例5：正则表达式批量处理
def batch_process_text(texts, pattern, replacement):
    """批量文本处理"""
    return [
        re.sub(pattern, replacement, text)
        for text in texts
    ]

texts = [
    "Hello World",
    "Hello Python",
    "Hello Programming"
]

processed = batch_process_text(texts, r'Hello', 'Hi')
print(f"批量处理结果：{processed}")

# ==================== 10. 性能对比 ====================

print("\n=== 性能对比 ===")

import time

# 列表推导式 vs 传统循环
data = list(range(10000))

# 列表推导式
start = time.time()
squares_list_comp = [x**2 for x in data]
list_comp_time = time.time() - start

# 传统循环
start = time.time()
squares_loop = []
for x in data:
    squares_loop.append(x**2)
loop_time = time.time() - start

print(f"列表推导式时间：{list_comp_time:.6f}秒")
print(f"传统循环时间：{loop_time:.6f}秒")
print(f"性能提升：{(loop_time - list_comp_time) / loop_time * 100:.1f}%")

# 生成器表达式 vs 列表推导式
print("\n内存使用对比：")

# 列表推导式（占用更多内存）
list_comp = [x**2 for x in range(100000)]
print(f"列表推导式内存：{sys.getsizeof(list_comp)} 字节")

# 生成器表达式（占用更少内存）
gen_comp = (x**2 for x in range(100000))
print(f"生成器表达式内存：{sys.getsizeof(gen_comp)} 字节")

# ==================== 11. 最佳实践 ====================

print("\n=== 最佳实践 ===")

print("1. 列表推导式：")
print("   - 适合简单到中等复杂度的逻辑")
print("   - 避免嵌套过深（一般不超过2层）")
print("   - 考虑使用生成器处理大数据")

print("\n2. 字典推导式：")
print("   - 确保键的唯一性")
print("   - 使用有意义的键名")
print("   - 复杂值使用嵌套字典")

print("\n3. 生成器表达式：")
print("   - 处理大数据时优先使用")
print("   - 注意只能迭代一次")
print("   - 适合管道式处理")

print("\n4. Lambda 表达式：")
print("   - 适合简单单行表达式")
print("   - 避免过于复杂的逻辑")
print("   - 与高阶函数结合使用")

print("\n5. 正则表达式：")
print("   - 使用原始字符串 r''")
print("   - 预编译常用模式")
print("   - 注意贪婪和非贪婪匹配")
print("   - 测试边界条件")

print("\n6. 性能考虑：")
print("   - 列表推导式通常比循环快")
print("   - 生成器表达式节省内存")
print("   - 复杂表达式考虑可读性")
print("   - 预编译正则表达式提升性能")

print("\n=== Python 生成推导式和表达式详解完成 ===")
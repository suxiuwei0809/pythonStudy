# Python 函数编程详解

# ==================== 1. 函数的基本概念 ====================

print("=== 函数的基本概念 ===")

# 函数是组织代码的基本单位，用于封装可重用的代码块
# 函数可以提高代码的可读性、可维护性和重用性


# 基本语法
def greet():
    """这是一个简单的问候函数"""
    print("Hello, World!")

# 调用函数
greet()

# 函数的优点
print("\n函数的优点：")
print("1. 代码重用")
print("2. 提高可读性")
print("3. 便于维护")
print("4. 模块化设计")


# ==================== 2. 函数的定义和调用 ====================

print("\n=== 函数的定义和调用 ===")

# 基本函数定义
def say_hello():
    """打印问候语"""
    print("你好，Python！")

say_hello()

# 带参数的函数
def greet_person(name):
    """向指定的人问候"""
    print(f"你好，{name}！")

greet_person("张三")
greet_person("李四")

# 带多个参数的函数
def introduce(name, age, city):
    """介绍个人信息"""
    print(f"我叫{name}，今年{age}岁，来自{city}")

introduce("王五", 25, "北京")

# 带默认参数的函数
def greet_with_default(name="朋友"):
    """使用默认参数问候"""
    print(f"你好，{name}！")

greet_with_default()  # 使用默认值
greet_with_default("赵六")  # 使用传入的值


# ==================== 3. 函数的参数类型 ====================

print("\n=== 函数的参数类型 ===")

# 位置参数
def add(a, b):
    """两个数相加"""
    return a + b


result = add(3, 5)
print(f"3 + 5 = {result}")

# 关键字参数
def describe_pet(animal_type, pet_name):
    """描述宠物"""
    print(f"我有一只{animal_type}，名字叫{pet_name}")

describe_pet(animal_type="狗", pet_name="旺财")
describe_pet(pet_name="咪咪", animal_type="猫")

# 默认参数
def make_pizza(topping="芝士"):
    """制作披萨"""
    print(f"制作一个{topping}披萨")

make_pizza()
make_pizza("意大利香肠")

# 可变参数（*args）
def sum_all(*numbers):
    """计算所有数字的总和"""
    total = 0
    for num in numbers:
        total += num
    return total


print(f"1+2+3+4+5 = {sum_all(1, 2, 3, 4, 5)}")
print(f"10+20+30 = {sum_all(10, 20, 30)}")

# 关键字可变参数（**kwargs）
def build_profile(first, last, **user_info):
    """构建用户资料"""
    profile = {'first_name': first, 'last_name': last}
    profile.update(user_info)
    return profile


user_profile = build_profile("张", "三", age=25, city="北京", job="工程师")
print(f"用户资料：{user_profile}")

# 参数组合使用
def complex_function(a, b, c=10, *args, **kwargs):
    """演示各种参数的组合使用"""
    print(f"位置参数：a={a}, b={b}")
    print(f"默认参数：c={c}")
    print(f"可变位置参数：{args}")
    print(f"可变关键字参数：{kwargs}")

complex_function(1, 2, 3, 4, 5, 6, name="张三", age=25)


# ==================== 4. 函数的返回值 ====================

print("\n=== 函数的返回值 ===")

# 返回单个值
def add_numbers(a, b):
    """返回两个数的和"""
    return a + b


result = add_numbers(10, 20)
print(f"10 + 20 = {result}")

# 返回多个值（元组）
def get_name_and_age():
    """返回姓名和年龄"""
    return "张三", 25


name, age = get_name_and_age()
print(f"姓名：{name}，年龄：{age}")

# 返回列表
def get_even_numbers(start, end):
    """返回指定范围内的偶数列表"""
    return [num for num in range(start, end + 1) if num % 2 == 0]

evens = get_even_numbers(1, 10)
print(f"1-10的偶数：{evens}")

# 返回字典
def create_person(name, age, city):
    """创建个人信息字典"""
    return {
        'name': name,
        'age': age,
        'city': city
    }

person = create_person("李四", 30, "上海")
print(f"个人信息：{person}")

# 提前返回
def check_positive(number):
    """检查数字是否为正数"""
    if number > 0:
        return True
    elif number < 0:
        return False
    else:
        return "零"

print(f"5是正数：{check_positive(5)}")
print(f"-3是正数：{check_positive(-3)}")
print(f"0是正数：{check_positive(0)}")

# 无返回值（返回None）
def print_message(message):
    """打印消息，无返回值"""
    print(f"消息：{message}")

result = print_message("Hello")
print(f"返回值：{result}")

# ==================== 5. 函数的文档字符串 ====================

print("\n=== 函数的文档字符串 ===")

def calculate_area(radius):
    """
    计算圆的面积
    
    Args:
        radius (float): 圆的半径
    
    Returns:
        float: 圆的面积
    
    Example:
        >>> calculate_area(5)
        78.539816
    """
    import math
    return math.pi * radius ** 2

area = calculate_area(5)
print(f"半径为5的圆面积：{area:.2f}")

# 访问文档字符串
print(f"函数文档：{calculate_area.__doc__}")

# ==================== 6. 函数的作用域 ====================

print("\n=== 函数的作用域 ===")

# 全局变量
global_var = 100

def access_global():
    """访问全局变量"""
    print(f"函数内访问全局变量：{global_var}")

access_global()

# 修改全局变量
def modify_global():
    """修改全局变量（需要使用global关键字）"""
    global global_var
    global_var = 200
    print(f"函数内修改全局变量：{global_var}")

modify_global()
print(f"函数外全局变量：{global_var}")

# 局部变量
def local_variable_demo():
    """演示局部变量"""
    local_var = 50
    print(f"函数内局部变量：{local_var}")

local_variable_demo()
# print(local_var)  # 这会报错，局部变量在函数外不可访问

# 变量查找规则（LEGB规则）
# L (Local) - 局部作用域
# E (Enclosing) - 嵌套函数的外层函数作用域
# G (Global) - 全局作用域
# B (Built-in) - 内置作用域

def outer_function():
    outer_var = "外层函数变量"
    
    def inner_function():
        inner_var = "内层函数变量"
        print(f"内层访问外层：{outer_var}")
        print(f"内层访问自身：{inner_var}")
    
    inner_function()
    # print(inner_var)  # 这会报错


outer_function()


# ==================== 7. 高阶函数 ====================

print("\n=== 高阶函数 ===")

# 函数作为参数
def apply_operation(func, x, y):
    """应用指定的函数到两个数上"""
    return func(x, y)

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

result1 = apply_operation(add, 5, 3)
result2 = apply_operation(multiply, 5, 3)
print(f"5 + 3 = {result1}")
print(f"5 * 3 = {result2}")

# 函数作为返回值
def get_operation(operator):
    """根据操作符返回对应的函数"""
    if operator == '+':
        return add
    elif operator == '*':
        return multiply
    else:
        return lambda x, y: x - y

add_func = get_operation('+')
multiply_func = get_operation('*')
subtract_func = get_operation('-')

print(f"使用返回的加法函数：{add_func(10, 5)}")
print(f"使用返回的乘法函数：{multiply_func(10, 5)}")
print(f"使用返回的减法函数：{subtract_func(10, 5)}")

# map 函数
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(f"平方：{squared}")

# filter 函数
even_numbers = list(filter(lambda x: x % 2 == 0, range(1, 11)))
print(f"偶数：{even_numbers}")

# reduce 函数
from functools import reduce
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)
print(f"总和：{total}")

# ==================== 8. Lambda 函数 ====================

print("\n=== Lambda 函数 ===")

# 基本语法：lambda 参数: 表达式
square = lambda x: x ** 2
print(f"5的平方：{square(5)}")

# 多个参数
add = lambda x, y: x + y
print(f"3 + 4 = {add(3, 4)}")

# 带条件的lambda
is_even = lambda x: x % 2 == 0
print(f"4是偶数：{is_even(4)}")
print(f"3是偶数：{is_even(3)}")

# lambda 与高阶函数结合
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 过滤偶数并平方
evens_squared = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))
print(f"偶数的平方：{evens_squared}")

# 排序
students = [('张三', 85), ('李四', 92), ('王五', 78)]
students_sorted = sorted(students, key=lambda x: x[1], reverse=True)
print(f"按分数排序：{students_sorted}")

# lambda 的局限性
# lambda 只能包含一个表达式
# 不能包含语句（如 if、for、while）
# 不适合复杂的逻辑

# ==================== 9. 装饰器 ====================

print("\n=== 装饰器 ===")

# 基本装饰器
def my_decorator(func):
    """简单的装饰器
    
    装饰器是一个接受函数作为参数并返回新函数的函数。
    它可以在不修改原函数代码的情况下，为函数添加额外的功能。
    
    Args:
        func: 被装饰的函数对象
    
    Returns:
        wrapper: 包装后的新函数
    
    Example:
        >>> @my_decorator
        >>> def say_hello():
        >>>     print("Hello!")
        >>> say_hello()
        函数执行前
        Hello!
        函数执行后
    """
    # 定义内部函数 wrapper（包装函数）
    # 这个函数将替代原始函数被调用
    # 它可以在调用原始函数前后添加额外的逻辑
    def wrapper():
        # 在原始函数执行前添加的功能
        # 这里可以添加前置处理逻辑，如参数验证、日志记录等
        print("函数执行前")
        
        # 调用被装饰的原始函数
        # func 是传入的原始函数对象
        # 这里执行原始函数的主要逻辑
        func()
        
        # 在原始函数执行后添加的功能
        # 这里可以添加后置处理逻辑，如结果处理、清理工作等
        print("函数执行后")
    
    # 返回包装函数
    # 装饰器必须返回一个函数对象
    # 这个返回的函数将替代原始函数被调用
    return wrapper


# 使用装饰器语法
# @my_decorator 等价于 say_hello = my_decorator(say_hello)
# Python 会在函数定义后立即应用装饰器
@my_decorator
def say_hello():
    """被装饰的函数
    
    这个函数被 my_decorator 装饰后，
    每次调用 say_hello() 时，实际执行的是 wrapper() 函数。
    """
    print("Hello, World!")

say_hello()

# 带参数的装饰器
def log_decorator(func):
    """日志装饰器"""
    def wrapper(*args, **kwargs):
        print(f"调用函数：{func.__name__}")
        print(f"参数：args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"返回值：{result}")
        return result
    return wrapper

@log_decorator
def add_numbers(a, b):
    """加法函数"""
    return a + b

result = add_numbers(10, 20)

# 带返回值的装饰器
def measure_time(func):
    """测量函数执行时间的装饰器"""
    import time
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"函数 {func.__name__} 执行时间：{end_time - start_time:.4f}秒")
        return result
    return wrapper

@measure_time
def slow_function():
    """模拟耗时函数"""
    import time
    time.sleep(0.1)
    return "完成"

result = slow_function()

# 多个装饰器
def decorator1(func):
    def wrapper():
        print("装饰器1 - 前")
        func()
        print("装饰器1 - 后")
    return wrapper

def decorator2(func):
    def wrapper():
        print("装饰器2 - 前")
        func()
        print("装饰器2 - 后")
    return wrapper

@decorator1
@decorator2
def decorated_function():
    print("被装饰的函数")

decorated_function()

# ==================== 10. 生成器函数 ====================

print("\n=== 生成器函数 ===")

# 基本生成器
def simple_generator():
    """简单的生成器"""
    yield 1
    yield 2
    yield 3


for value in simple_generator():
    print(f"生成器值：{value}")

# 生成器表达式
gen_exp = (x**2 for x in range(5))
for value in gen_exp:
    print(f"生成器表达式值：{value}")

# 无限生成器
def infinite_counter():
    """无限计数器"""
    count = 0
    while True:
        yield count
        count += 1

# 只取前5个值
print("无限生成器前5个值：")
counter = infinite_counter()
for i in range(5):
    print(f"  {next(counter)}")

# 生成器的优势
print("生成器的优势：")
print("1. 内存效率高（惰性求值）")
print("2. 可以处理无限序列")
print("3. 适用于大数据处理")

# ==================== 11. 递归函数 ====================

print("\n=== 递归函数 ===")

# 阶乘计算
def factorial(n):
    """计算阶乘"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(f"5的阶乘：{factorial(5)}")
print(f"10的阶乘：{factorial(10)}")

# 斐波那契数列
def fibonacci(n):
    """斐波那契数列"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("斐波那契数列前10项：")
for i in range(10):
    print(f"  F({i}) = {fibonacci(i)}")

# 递归的注意事项
print("递归的注意事项：")
print("1. 必须有终止条件")
print("2. 注意递归深度限制")
print("3. 可能导致栈溢出")
print("4. 某些情况下效率较低")

# ==================== 12. 实用函数示例 ====================

print("\n=== 实用函数示例 ===")

# 数据验证函数
def validate_email(email):
    """验证邮箱格式"""
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}
    return bool(re.match(pattern, email))

print(f"'user@example.com' 有效：{validate_email('user@example.com')}")
print(f"'invalid-email' 有效：{validate_email('invalid-email')}")

# 数据转换函数
def celsius_to_fahrenheit(celsius):
    """摄氏度转华氏度"""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """华氏度转摄氏度"""
    return (fahrenheit - 32) * 5/9


celsius = 25
print(f"{celsius}°C = {celsius_to_fahrenheit(celsius):.1f}°F")
print(f"77°F = {fahrenheit_to_celsius(77):.1f}°C")

# 数据处理函数
def clean_data(data):
    """清理数据：去除空值和重复"""
    cleaned = [item for item in data if item is not None and item != '']
    return list(set(cleaned))

raw_data = [1, 2, None, 3, '', 2, 4, None, 5]
cleaned_data = clean_data(raw_data)
print(f"原始数据：{raw_data}")
print(f"清理后数据：{cleaned_data}")

# 缓存装饰器
def cache_decorator(func):
    """缓存装饰器，避免重复计算"""
    cache = {}
    
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    
    return wrapper

@cache_decorator
def expensive_function(n):
    """模拟耗时函数"""
    import time
    time.sleep(0.1)  # 模拟耗时操作
    return n ** 2

print("测试缓存装饰器：")
print(f"第一次调用：{expensive_function(5)}")
print(f"第二次调用（使用缓存）：{expensive_function(5)}")

# 重试装饰器
def retry_decorator(max_retries=3, delay=1):
    """重试装饰器"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            import time
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_retries - 1:
                        raise e
                    print(f"第{attempt + 1}次尝试失败，{delay}秒后重试...")
                    time.sleep(delay)
        return wrapper
    return decorator

@retry_decorator(max_retries=3, delay=0.5)
def unstable_function():
    """不稳定的函数，可能失败"""
    import random
    if random.random() < 0.7:  # 70%概率失败
        raise Exception("随机失败")
    return "成功"

try:
    result = unstable_function()
    print(f"函数执行结果：{result}")
except Exception as e:
    print(f"函数最终失败：{e}")

# ==================== 13. 函数式编程特性 ====================

print("\n=== 函数式编程特性 ===")

# 纯函数（无副作用）
def pure_add(a, b):
    """纯函数：相同的输入总是产生相同的输出"""
    return a + b

# 不可变数据
numbers = [1, 2, 3, 4, 5]

# 不修改原列表，返回新列表
doubled = list(map(lambda x: x * 2, numbers))
print(f"原列表：{numbers}")
print(f"新列表：{doubled}")

# 函数组合
def compose(f, g):
    """函数组合：返回 f(g(x))"""
    return lambda x: f(g(x))

def double(x):
    return x * 2

def square(x):
    return x ** 2

# 先平方再翻倍
double_square = compose(double, square)
print(f"先平方再翻倍：{double_square(5)}")  # (5^2) * 2 = 50

# 柯里化（Currying）
def multiply(a, b):
    return a * b

def curried_multiply(a):
    """柯里化：将多参数函数转换为单参数函数链"""
    return lambda b: a * b

multiply_by_5 = curried_multiply(5)
print(f"5 * 3 = {multiply_by_5(3)}")
print(f"5 * 10 = {multiply_by_5(10)}")

# ==================== 14. 最佳实践 ====================

print("\n=== 函数编程最佳实践 ===")

print("1. 函数命名：")
print("   - 使用动词或动词短语")
print("   - 遵循PEP8命名规范")
print("   - 名称要能描述函数功能")

print("\n2. 函数设计：")
print("   - 单一职责原则")
print("   - 避免过多参数（一般不超过5个）")
print("   - 使用默认参数提高灵活性")

print("\n3. 文档字符串：")
print("   - 为所有函数添加文档字符串")
print("   - 说明参数、返回值、使用示例")

print("   - 遵循Google或NumPy风格")

print("\n4. 错误处理：")
print("   - 预期可能的异常")
print("   - 提供有意义的错误信息")
print("   - 考虑使用装饰器统一处理")

print("\n5. 性能考虑：")
print("   - 避免不必要的计算")
print("   - 使用生成器处理大数据")
print("   - 考虑使用缓存")

print("\n6. 测试：")
print("   - 编写单元测试")
print("   - 测试边界条件")
print("   - 测试异常情况")

print("\n=== Python 函数编程详解完成 ===")
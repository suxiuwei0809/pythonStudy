# Python 字符串语法详解

# ==================== 1. 字符串定义 ====================

# 单引号字符串
str1 = 'Hello, World!'
print(f"单引号字符串: {str1}")

# 双引号字符串
str2 = "Hello, Python!"
print(f"双引号字符串: {str2}")

# 三引号字符串（可以跨行）
str3 = '''这是一个
多行字符串
使用三引号'''
print(f"三引号字符串:\n{str3}")

# 三引号字符串（双引号）
str4 = """这是另一个
多行字符串
使用双引号"""
print(f"双引号三引号字符串:\n{str4}")


# ==================== 2. 字符串转义字符 ====================

# 转义字符示例
escape_str1 = "He said: \"Hello!\""
print(f"转义双引号: {escape_str1}")

escape_str2 = 'It\'s a beautiful day'
print(f"转义单引号: {escape_str2}")

escape_str3 = "第一行\n第二行"
print(f"换行符:\n{escape_str3}")

escape_str4 = "Hello\tWorld"
print(f"制表符: {escape_str4}")

escape_str5 = "路径: C:\\Users\\Documents"
print(f"反斜杠: {escape_str5}")

# 原始字符串（不转义）
raw_str = r"C:\Users\Documents\file.txt"
print(f"原始字符串: {raw_str}")


# ==================== 3. 字符串访问和切片 ====================

text = "Python Programming"

# 访问单个字符
print(f"第一个字符: {text[0]}")  # P
print(f"最后一个字符: {text[-1]}")  # g

# 切片操作
print(f"前6个字符: {text[0:6]}")  # Python
print(f"从第7个字符开始: {text[7:]}")  # Programming
print(f"每隔一个字符: {text[::2]}")  # Pto rgamn
print(f"反转字符串: {text[::-1]}")  # gnimmargorP nohtyP


# ==================== 4. 字符串拼接 ====================

# 使用 + 运算符
str_a = "Hello"
str_b = "World"
result1 = str_a + " " + str_b
print(f"拼接结果: {result1}")

# 使用 * 运算符重复
str_repeat = "Python " * 3
print(f"重复字符串: {str_repeat}")

# 使用 join() 方法
words = ["Hello", "World", "Python"]
result2 = " ".join(words)
print(f"join拼接: {result2}")


# ==================== 5. 字符串格式化 ====================

# 使用 f-string（推荐）
name = "张三"
age = 25
formatted1 = f"姓名: {name}, 年龄: {age}"
print(f"f-string格式化: {formatted1}")

# 使用 format() 方法
formatted2 = "姓名: {}, 年龄: {}".format(name, age)
print(f"format方法: {formatted2}")

# 使用 % 格式化（旧方法）
formatted3 = "姓名: %s, 年龄: %d" % (name, age)
print(f"%格式化: {formatted3}")

# 格式化数字
pi = 3.1415926
formatted4 = f"圆周率: {pi:.2f}"  # 保留两位小数
print(f"数字格式化: {formatted4}")


# ==================== 6. 常用字符串方法 ====================

text_sample = "  Hello, Python World!  "

# 大小写转换
print(f"大写: {text_sample.upper()}")
print(f"小写: {text_sample.lower()}")
print(f"首字母大写: {text_sample.capitalize()}")
print(f"每个单词首字母大写: {text_sample.title()}")

# 去除空白
print(f"去除首尾空白: '{text_sample.strip()}'")
print(f"去除左边空白: '{text_sample.lstrip()}'")
print(f"去除右边空白: '{text_sample.rstrip()}'")

# 查找和替换
print(f"查找'Python'位置: {text_sample.find('Python')}")
print(f"替换'Python'为'Java': {text_sample.replace('Python', 'Java')}")

# 分割和连接
words_list = text_sample.split()
print(f"分割字符串: {words_list}")
print(f"重新连接: {'-'.join(words_list)}")

# 检查字符串
test_str = "Python123"
print(f"是否全是字母: {test_str.isalpha()}")
print(f"是否全是数字: {test_str.isdigit()}")
print(f"是否全是字母或数字: {test_str.isalnum()}")
print(f"是否全是空白: {text_sample.isspace()}")


# ==================== 7. 字符串长度和计数 ====================

sample_text = "Hello, Python!"

# 字符串长度
print(f"字符串长度: {len(sample_text)}")

# 字符计数
print(f"'o'出现次数: {sample_text.count('o')}")
print(f"'l'出现次数: {sample_text.count('l')}")


# ==================== 8. 字符串检查方法 ====================

check_str = "Python Programming"

# 检查开头和结尾
print(f"是否以'Python'开头: {check_str.startswith('Python')}")
print(f"是否以'ing'结尾: {check_str.endswith('ing')}")

# 检查包含
print(f"是否包含'Program': {'Program' in check_str}")


# ==================== 9. 字符串对齐 ====================

align_str = "Python"

# 左对齐、右对齐、居中
print(f"左对齐: '{align_str.ljust(10, '-')}'")
print(f"右对齐: '{align_str.rjust(10, '-')}'")
print(f"居中: '{align_str.center(10, '-')}'")


# ==================== 10. 字符串编码和解码 ====================

# 编码
original_str = "你好，Python"
encoded_str = original_str.encode('utf-8')
print(f"编码结果: {encoded_str}")

# 解码
decoded_str = encoded_str.decode('utf-8')
print(f"解码结果: {decoded_str}")


# ==================== 11. 字符串高级操作 ====================

# 字符串模板
from string import Template
template = Template('Hello, $name! Welcome to $language.')
result = template.substitute(name='张三', language='Python')
print(f"字符串模板: {result}")

# 字符串分割（保留分隔符）
import re
complex_str = "apple,banana;orange|grape"
result_list = re.split(r'[,;|]', complex_str)
print(f"复杂分割: {result_list}")


# ==================== 12. 实用示例 ====================

def clean_string(text):
    """清理字符串：去除空白、统一大小写"""
    return text.strip().lower().replace(' ', '_')

dirty_str = "  Hello World  "
cleaned = clean_string(dirty_str)
print(f"清理前: '{dirty_str}'")
print(f"清理后: '{cleaned}'")


def validate_email(email):
    """简单邮箱验证"""
    if '@' in email and '.' in email:
        return True
    return False

email1 = "user@example.com"
email2 = "invalid-email"
print(f"邮箱1有效: {validate_email(email1)}")
print(f"邮箱2有效: {validate_email(email2)}")


def mask_sensitive_info(text, mask_char='*', show_first=2, show_last=2):
    """敏感信息脱敏函数
    
    该函数用于对敏感信息进行脱敏处理，保留前几位和后几位字符，
    中间部分用指定的字符替换。常用于手机号、身份证号、银行卡号等敏感信息的处理。
    
    Args:
        text (str): 需要脱敏的原始文本，如手机号、身份证号等
        mask_char (str): 用于脱敏的替换字符，默认为 '*'
        show_first (int): 保留前几位字符，默认为 2
        show_last (int): 保留后几位字符，默认为 2
    
    Returns:
        str: 脱敏后的字符串，如果文本长度小于等于需要显示的字符数，则返回原文
    
    Example:
        >>> mask_sensitive_info("13812345678")
        '13******78'
        
        >>> mask_sensitive_info("13812345678", mask_char='#')
        '13######78'
        
        >>> mask_sensitive_info("13812345678", show_first=3, show_last=4)
        '138****5678'
        
        >>> mask_sensitive_info("1234567890123456", show_first=4, show_last=4)
        '1234********3456'
    """
    # 检查文本长度是否小于等于需要显示的字符数
    # 如果文本太短，不需要脱敏，直接返回原文
    if len(text) <= show_first + show_last:
        return text
    
    # 构建脱敏字符串：
    # 1. text[:show_first] - 获取前 show_first 个字符
    # 2. mask_char * (len(text) - show_first - show_last) - 生成中间的脱敏字符
    # 3. text[-show_last:] - 获取后 show_last 个字符
    # 4. 使用 + 运算符将三部分拼接起来
    masked = text[:show_first] + mask_char * (len(text) - show_first - show_last) + text[-show_last:]
    
    # 返回脱敏后的字符串
    return masked

phone = "13812345678"
masked_phone = mask_sensitive_info(phone)
print(f"手机号脱敏: {masked_phone}")
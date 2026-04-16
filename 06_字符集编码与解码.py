# Python 字符集编码与解码详解

# ==================== 1. 字符编码的基本概念 ====================

print("=== 字符编码的基本概念 ===")

# 字符编码是将字符转换为字节的过程
# 字符解码是将字节转换回字符的过程
# 常见的编码格式：ASCII、UTF-8、GBK、GB2312 等

print("\n常见编码格式：")
print("ASCII - 美国信息交换标准码（7位）")
print("UTF-8 - 8位Unicode转换格式（推荐）")
print("GBK - 中文编码（中国国家标准）")
print("GB2312 - 简体中文编码")
print("ISO-8859-1 - 西欧语言编码")

# ==================== 2. 字符串编码 ====================

print("\n=== 字符串编码 ===")

# 基本编码操作
text = "Hello, 世界！"

# 编码为 UTF-8（推荐）
utf8_bytes = text.encode('utf-8')
print(f"原始文本：{text}")
print(f"UTF-8 编码结果：{utf8_bytes}")
print(f"编码类型：{type(utf8_bytes)}")

# 编码为 GBK
try:
    gbk_bytes = text.encode('gbk')
    print(f"GBK 编码结果：{gbk_bytes}")
except UnicodeEncodeError as e:
    print(f"GBK 编码错误：{e}")

# 编码为 ASCII（仅支持英文字符）
ascii_text = "Hello, World!"
ascii_bytes = ascii_text.encode('ascii')
print(f"ASCII 文本：{ascii_text}")
print(f"ASCII 编码结果：{ascii_bytes}")

# 尝试用 ASCII 编码中文（会失败）
try:
    chinese_text = "你好世界"
    chinese_bytes = chinese_text.encode('ascii')
except UnicodeEncodeError as e:
    print(f"ASCII 无法编码中文：{e}")

# ==================== 3. 字节解码 ====================

print("\n=== 字节解码 ===")

# 基本解码操作
utf8_bytes = b'Hello, \xe4\xb8\x96\xe7\x95\x8c\xef\xbc\x81'

# 从 UTF-8 解码
decoded_text = utf8_bytes.decode('utf-8')
print(f"字节内容：{utf8_bytes}")
print(f"解码后的文本：{decoded_text}")

# 从 GBK 解码
gbk_bytes = b'Hello, \xc4\xe3\xba\xc3\xca\xbd\xc1\xa1\xbc\x81'
try:
    gbk_decoded = gbk_bytes.decode('gbk')
    print(f"GBK 解码结果：{gbk_decoded}")
except UnicodeDecodeError as e:
    print(f"GBK 解码错误：{e}")

# 错误的编码方式会导致解码失败
try:
    # 用错误的编码方式解码
    wrong_decoded = utf8_bytes.decode('gbk')
except UnicodeDecodeError as e:
    print(f"用 GBK 解码 UTF-8 字节失败：{e}")

# ==================== 4. 常见编码格式对比 ====================

print("\n=== 常见编码格式对比 ===")

# UTF-8 编码
text = "Hello, 你好！世界！"
utf8_encoded = text.encode('utf-8')
print(f"原始文本：{text}")
print(f"UTF-8 编码：{utf8_encoded}")
print(f"UTF-8 字节数：{len(utf8_encoded)}")

# GBK 编码
try:
    gbk_encoded = text.encode('gbk')
    print(f"GBK 编码：{gbk_encoded}")
    print(f"GBK 字节数：{len(gbk_encoded)}")
except UnicodeEncodeError as e:
    print(f"GBK 编码错误：{e}")

# ASCII 编码（仅英文）
ascii_text = "Hello, World!"
ascii_encoded = ascii_text.encode('ascii')
print(f"ASCII 文本：{ascii_text}")
print(f"ASCII 编码：{ascii_encoded}")
print(f"ASCII 字节数：{len(ascii_encoded)}")

# ==================== 5. 编码错误处理 ====================

print("\n=== 编码错误处理 ===")

# 编码时忽略错误
text_with_special = "Hello, 世界！\ud83d\ude00"  # 包含 emoji
try:
    # 使用 errors 参数处理编码错误
    encoded_ignore = text_with_special.encode('gbk', errors='ignore')
    print(f"忽略错误编码：{encoded_ignore}")
    
    encoded_replace = text_with_special.encode('gbk', errors='replace')
    print(f"替换错误编码：{encoded_replace}")
    
    encoded_xmlcharref = text_with_special.encode('gbk', errors='xmlcharrefreplace')
    print(f"XML字符引用编码：{encoded_xmlcharref}")
    
except Exception as e:
    print(f"编码处理错误：{e}")

# 解码时忽略错误
invalid_utf8 = b'Hello, \xff\xfe\x80\x81'
try:
    decoded_ignore = invalid_utf8.decode('utf-8', errors='ignore')
    print(f"忽略错误解码：{decoded_ignore}")
    
    decoded_replace = invalid_utf8.decode('utf-8', errors='replace')
    print(f"替换错误解码：{decoded_replace}")
    
except Exception as e:
    print(f"解码处理错误：{e}")

# ==================== 6. 文件编码操作 ====================

print("\n=== 文件编码操作 ===")

# 写入 UTF-8 编码的文件
with open('utf8_file.txt', 'w', encoding='utf-8') as f:
    f.write('Hello, 世界！\n')
    f.write('这是 UTF-8 编码的文件\n')

print("UTF-8 文件已创建")

# 读取 UTF-8 编码的文件
with open('utf8_file.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(f"UTF-8 文件内容：{content}")

# 写入 GBK 编码的文件
try:
    with open('gbk_file.txt', 'w', encoding='gbk') as f:
        f.write('Hello, 世界！\n')
        f.write('这是 GBK 编码的文件\n')
    print("GBK 文件已创建")
    
    # 读取 GBK 编码的文件
    with open('gbk_file.txt', 'r', encoding='gbk') as f:
        content = f.read()
        print(f"GBK 文件内容：{content}")
except Exception as e:
    print(f"GBK 文件操作错误：{e}")

# 错误的编码方式会导致读取失败
try:
    with open('utf8_file.txt', 'r', encoding='gbk') as f:
        content = f.read()
except UnicodeDecodeError as e:
    print(f"用 GBK 读取 UTF-8 文件失败：{e}")

# ==================== 7. 网络数据编码 ====================

print("\n=== 网络数据编码 ===")

# 模拟网络请求的数据
import urllib.request

# 获取网页内容（自动处理编码）
try:
    # 使用简单的 HTTP 请求
    url = 'https://www.example.com'
    print(f"正在请求：{url}")
    # 注意：实际使用时需要处理网络请求
    # 这里只是演示编码处理
    print("网络请求需要处理编码问题")
except Exception as e:
    print(f"网络请求错误：{e}")

# 模拟网络数据处理
network_data = b'Hello, \xe4\xb8\x96\xe7\x95\x8c\xef\xbc\x81'

# 检测编码
def detect_encoding(data):
    """简单的编码检测"""
    try:
        data.decode('utf-8')
        return 'utf-8'
    except UnicodeDecodeError:
        try:
            data.decode('gbk')
            return 'gbk'
        except UnicodeDecodeError:
            try:
                data.decode('ascii')
                return 'ascii'
            except UnicodeDecodeError:
                return 'unknown'

detected = detect_encoding(network_data)
print(f"检测到的编码：{detected}")

# 根据检测的编码解码
if detected != 'unknown':
    decoded_content = network_data.decode(detected)
    print(f"解码后的内容：{decoded_content}")

# ==================== 8. 编码转换 ====================

print("\n=== 编码转换 ===")

# UTF-8 转 GBK
text = "Hello, 世界！"
utf8_bytes = text.encode('utf-8')
try:
    gbk_bytes = utf8_bytes.decode('utf-8').encode('gbk')
    print(f"UTF-8 转 GBK：{gbk_bytes}")
except Exception as e:
    print(f"编码转换错误：{e}")

# GBK 转 UTF-8
gbk_text = "你好，世界！"
gbk_bytes = gbk_text.encode('gbk')
utf8_bytes = gbk_bytes.decode('gbk').encode('utf-8')
print(f"GBK 转 UTF-8：{utf8_bytes}")

# 批量编码转换
def convert_encoding(text, from_encoding, to_encoding):
    """编码转换函数"""
    try:
        # 先解码为 Unicode
        unicode_text = text.encode(from_encoding).decode(from_encoding)
        # 再编码为目标格式
        converted_bytes = unicode_text.encode(to_encoding)
        return converted_bytes
    except Exception as e:
        print(f"编码转换错误：{e}")
        return None

result = convert_encoding("Hello, 世界！", 'utf-8', 'gbk')
if result:
    print(f"编码转换结果：{result}")

# ==================== 9. Unicode 处理 ====================

print("\n=== Unicode 处理 ===")

# Unicode 字符串
unicode_text = "Hello, 世界！🌍"
print(f"Unicode 文本：{unicode_text}")
print(f"文本长度：{len(unicode_text)}")

# 访问 Unicode 码点
for char in unicode_text:
    code_point = ord(char)
    print(f"字符：{char}，码点：U+{code_point:04X}")

# Unicode 字符分类
import unicodedata
for char in unicode_text:
    category = unicodedata.category(char)
    name = unicodedata.name(char, 'UNKNOWN')
    print(f"字符：{char}，类别：{category}，名称：{name}")

# Unicode 归一化
import unicodedata

text_with_accents = "café, naïve, résumé"
normalized = unicodedata.normalize('NFC', text_with_accents)
print(f"原始文本：{text_with_accents}")
print(f"归一化后：{normalized}")

# ==================== 10. 实用编码函数 ====================

print("\n=== 实用编码函数 ===")

def safe_encode(text, encoding='utf-8', errors='ignore'):
    """安全编码函数"""
    try:
        return text.encode(encoding, errors=errors)
    except Exception as e:
        print(f"编码错误：{e}")
        return None

def safe_decode(data, encoding='utf-8', errors='ignore'):
    """安全解码函数"""
    try:
        return data.decode(encoding, errors=errors)
    except Exception as e:
        print(f"解码错误：{e}")
        return None

def convert_text_encoding(text, from_enc, to_enc):
    """文本编码转换"""
    try:
        # 编码为源格式
        bytes_data = text.encode(from_enc)
        # 解码为 Unicode
        unicode_text = bytes_data.decode(from_enc)
        # 编码为目标格式
        return unicode_text.encode(to_enc)
    except Exception as e:
        print(f"编码转换错误：{e}")
        return None

def detect_file_encoding(file_path):
    """检测文件编码（简单版本）"""
    encodings = ['utf-8', 'gbk', 'gb2312', 'ascii', 'latin-1']
    
    with open(file_path, 'rb') as f:
        raw_data = f.read(1024)  # 读取前 1024 字节
    
    for encoding in encodings:
        try:
            raw_data.decode(encoding)
            return encoding
        except UnicodeDecodeError:
            continue
    
    return 'unknown'

# 测试实用函数
test_text = "Hello, 世界！测试文本！"

# 测试安全编码
encoded = safe_encode(test_text, 'utf-8')
if encoded:
    print(f"安全编码结果：{encoded}")

# 测试安全解码
decoded = safe_decode(encoded, 'utf-8')
if decoded:
    print(f"安全解码结果：{decoded}")

# 测试编码转换
converted = convert_text_encoding(test_text, 'utf-8', 'gbk')
if converted:
    print(f"编码转换结果：{converted}")

# 测试文件编码检测
with open('utf8_file.txt', 'r', encoding='utf-8') as f:
    f.write(test_text)

detected_encoding = detect_file_encoding('utf8_file.txt')
print(f"检测到的文件编码：{detected_encoding}")

# ==================== 11. 实际应用场景 ====================

print("\n=== 实际应用场景 ===")

# 场景1：处理不同编码的文件
def process_files_with_different_encodings(file_list):
    """处理不同编码的文件"""
    results = []
    
    for file_path in file_list:
        # 检测文件编码
        encoding = detect_file_encoding(file_path)
        
        if encoding == 'unknown':
            print(f"无法检测文件编码：{file_path}")
            continue
        
        try:
            # 读取文件
            with open(file_path, 'r', encoding=encoding) as f:
                content = f.read()
            
            # 转换为 UTF-8
            utf8_content = content.encode(encoding).decode(encoding)
            results.append({
                'file': file_path,
                'original_encoding': encoding,
                'content': utf8_content
            })
            
        except Exception as e:
            print(f"处理文件错误：{file_path}, {e}")
    
    return results

# 创建测试文件
with open('test_utf8.txt', 'w', encoding='utf-8') as f:
    f.write('这是 UTF-8 文件')

try:
    with open('test_gbk.txt', 'w', encoding='gbk') as f:
        f.write('这是 GBK 文件')
    
    # 处理不同编码的文件
    files_to_process = ['test_utf8.txt', 'test_gbk.txt']
    processed = process_files_with_different_encodings(files_to_process)
    
    for result in processed:
        print(f"文件：{result['file']}")
        print(f"原始编码：{result['original_encoding']}")
        print(f"内容：{result['content']}")
        
except Exception as e:
    print(f"GBK 文件操作错误：{e}")

# 场景2：数据库编码处理
def handle_database_encoding(data, target_encoding='utf-8'):
    """处理数据库编码问题"""
    processed_data = []
    
    for item in data:
        if isinstance(item, str):
            try:
                # 尝试编码为目标格式
                encoded = item.encode(target_encoding)
                decoded = encoded.decode(target_encoding)
                processed_data.append(decoded)
            except UnicodeEncodeError:
                # 编码失败，尝试忽略错误
                encoded = item.encode(target_encoding, errors='ignore')
                decoded = encoded.decode(target_encoding, errors='ignore')
                processed_data.append(decoded)
        else:
            processed_data.append(item)
    
    return processed_data

# 测试数据库编码处理
db_data = ["Hello", "世界", "测试", "数据", 123, True]
processed_db_data = handle_database_encoding(db_data)
print(f"数据库数据处理结果：{processed_db_data}")

# 场景3：Web 表单编码处理
def handle_form_submission(form_data, encoding='utf-8'):
    """处理 Web 表单提交的编码问题"""
    cleaned_data = {}
    
    for key, value in form_data.items():
        if isinstance(value, str):
            try:
                # 确保数据是 UTF-8 编码
                encoded = value.encode(encoding)
                decoded = encoded.decode(encoding)
                cleaned_data[key] = decoded
            except UnicodeDecodeError:
                # 解码失败，使用错误处理
                cleaned_data[key] = value.encode(encoding, errors='replace').decode(encoding, errors='replace')
        else:
            cleaned_data[key] = value
    
    return cleaned_data

# 测试表单编码处理
form_data = {
    'username': '张三',
    'email': 'zhangsan@example.com',
    'message': '你好，世界！'
}
processed_form = handle_form_submission(form_data)
print(f"表单数据处理结果：{processed_form}")

# ==================== 12. 编码最佳实践 ====================

print("\n=== 编码最佳实践 ===")

print("1. 统一使用 UTF-8：")
print("   - 新项目优先使用 UTF-8")
print("   - 数据库连接指定 UTF-8")
print("   - Web 应用使用 UTF-8")

print("\n2. 文件操作明确编码：")
print("   - 始终指定 encoding 参数")
print("   - 读取和写入使用相同编码")
print("   - 处理编码异常")

print("\n3. 错误处理策略：")
print("   - errors='ignore'：忽略错误")
print("   - errors='replace'：替换为 ?")
print("   - errors='xmlcharrefreplace'：XML 实体引用")

print("\n4. 编码检测：")
print("   - 使用 chardet 库进行准确检测")
print("   - 提供编码选择选项")
print("   - 记录检测到的编码")

print("\n5. 数据库编码：")
print("   - 连接字符串指定编码")
print("   - 表字段使用合适的字符集")
print("   - 存储前验证编码")

print("\n6. Web 开发：")
print("   - HTML 头指定 charset")
print("   - HTTP 头指定编码")
print("   - 表单处理编码转换")

# ==================== 13. 清理测试文件 ====================

print("\n=== 清理测试文件 ===")

import os

# 要删除的文件列表
files_to_remove = [
    'utf8_file.txt',
    'gbk_file.txt',
    'test_utf8.txt',
    'test_gbk.txt'
]

# 删除文件
for file_path in files_to_remove:
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"已删除：{file_path}")

print("测试文件清理完成")

print("\n=== Python 字符集编码与解码详解完成 ===")
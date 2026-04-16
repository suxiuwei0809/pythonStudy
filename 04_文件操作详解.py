# Python 文件操作详解

# ==================== 1. 文件的基本概念 ====================

print("=== 文件的基本概念 ===")

# 文件操作是编程中非常重要的一部分
# Python 使用 open() 函数来打开文件
# 基本语法：open(文件名, 模式, 编码)

# 文件打开模式：
# 'r' - 只读模式（默认）
# 'w' - 写入模式（会覆盖原有内容）
# 'a' - 追加模式（在文件末尾添加内容）
# 'r+' - 读写模式
# 'b' - 二进制模式（与以上模式组合使用，如 'rb', 'wb'）

print("文件操作模式：")
print("'r' - 只读模式")
print("'w' - 写入模式（覆盖）")
print("'a' - 追加模式")
print("'r+' - 读写模式")
print("'b' - 二进制模式")


# ==================== 2. 文件的打开和关闭 ====================

print("\n=== 文件的打开和关闭 ===")

# 创建一个测试文件
with open('test.txt', 'w', encoding='utf-8') as f:
    f.write('Hello, World!\n')
    f.write('Python 文件操作示例\n')
    f.write('第三行内容\n')

print("测试文件已创建")

# 传统方式打开和关闭文件
file = open('test.txt', 'r', encoding='utf-8')
content = file.read()
print(f"文件内容：\n{content}")
file.close()

# 推荐方式：使用 with 语句（自动关闭文件）
with open('test.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(f"使用with语句读取：\n{content}")

print("with语句的优点：自动关闭文件，即使发生异常")


# ==================== 3. 文件的读取操作 ====================

print("\n=== 文件的读取操作 ===")

# 读取整个文件
with open('test.txt', 'r', encoding='utf-8') as f:
    all_content = f.read()
    print(f"读取整个文件：\n{all_content}")

# 读取指定字符数
with open('test.txt', 'r', encoding='utf-8') as f:
    first_chars = f.read(10)
    print(f"读取前10个字符：{first_chars}")

# 读取一行
with open('test.txt', 'r', encoding='utf-8') as f:
    first_line = f.readline()
    print(f"读取第一行：{first_line.strip()}")

# 读取所有行（返回列表）
with open('test.txt', 'r', encoding='utf-8') as f:
    all_lines = f.readlines()
    print(f"读取所有行（列表）：{all_lines}")

# 逐行读取（推荐用于大文件）
print("逐行读取：")
with open('test.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(f"  行内容：{line.strip()}")


# ==================== 4. 文件的写入操作 ====================

print("\n=== 文件的写入操作 ===")

# 写入字符串（覆盖模式）
with open('write_test.txt', 'w', encoding='utf-8') as f:
    f.write('这是写入测试文件\n')
    f.write('第二行内容\n')
    f.write('第三行内容\n')

print("写入测试文件已创建")

# 写入多行
lines_to_write = ['第一行\n', '第二行\n', '第三行\n']
with open('write_test.txt', 'w', encoding='utf-8') as f:
    f.writelines(lines_to_write)

print("多行内容已写入")

# 读取验证
with open('write_test.txt', 'r', encoding='utf-8') as f:
    print(f"写入的内容：\n{f.read()}")


# ==================== 5. 文件的追加操作 ====================

print("\n=== 文件的追加操作 ===")

# 创建初始文件
with open('append_test.txt', 'w', encoding='utf-8') as f:
    f.write('初始内容\n')

print("初始文件已创建")

# 追加内容
with open('append_test.txt', 'a', encoding='utf-8') as f:
    f.write('追加的第一行\n')
    f.write('追加的第二行\n')

print("内容已追加")

# 读取验证
with open('append_test.txt', 'r', encoding='utf-8') as f:
    print(f"追加后的内容：\n{f.read()}")


# ==================== 6. 文件指针操作 ====================

print("\n=== 文件指针操作 ===")

# 创建测试文件
with open('pointer_test.txt', 'w', encoding='utf-8') as f:
    f.write('0123456789\n')
    f.write('ABCDEFGHIJ\n')
    f.write('abcdefghij\n')

# 文件指针操作
with open('pointer_test.txt', 'r', encoding='utf-8') as f:
    # 获取当前指针位置
    print(f"初始指针位置：{f.tell()}")
    
    # 移动指针到指定位置
    f.seek(5)
    print(f"移动到位置5后的字符：{f.read(1)}")
    
    # 读取一行
    f.seek(0)
    print(f"回到开头读取一行：{f.readline().strip()}")
    
    # 移动到文件末尾
    f.seek(0, 2)  # 0表示偏移量，2表示从文件末尾开始
    print(f"文件末尾指针位置：{f.tell()}")


# ==================== 7. 文件和目录操作 ====================

print("\n=== 文件和目录操作 ===")

import os
import shutil

# 获取当前工作目录
print(f"当前工作目录：{os.getcwd()}")

# 创建目录
if not os.path.exists('test_dir'):
    os.makedirs('test_dir')
    print("测试目录已创建")

# 创建文件
with open('test_dir/test_file.txt', 'w', encoding='utf-8') as f:
    f.write('测试文件内容')
print("测试文件已创建")

# 检查文件是否存在
print(f"测试文件是否存在：{os.path.exists('test_dir/test_file.txt')}")

# 获取文件信息
file_path = 'test_dir/test_file.txt'
print(f"文件大小：{os.path.getsize(file_path)} 字节")
print(f"是否为文件：{os.path.isfile(file_path)}")
print(f"是否为目录：{os.path.isdir('test_dir')}")

# 重命名文件
if os.path.exists('test_dir/test_file.txt'):
    os.rename('test_dir/test_file.txt', 'test_dir/renamed_file.txt')
    print("文件已重命名")

# 复制文件
if os.path.exists('test_dir/renamed_file.txt'):
    shutil.copy('test_dir/renamed_file.txt', 'test_dir/copied_file.txt')
    print("文件已复制")

# 列出目录内容
print("目录内容：")
for item in os.listdir('test_dir'):
    print(f"  - {item}")

# ==================== 8. 文件异常处理 ====================

print("\n=== 文件异常处理 ===")

# 基本的异常处理
try:
    with open('nonexistent_file.txt', 'r', encoding='utf-8') as f:
        content = f.read()
except FileNotFoundError:
    print("文件不存在错误")
except PermissionError:
    print("权限不足错误")
except Exception as e:
    print(f"其他错误：{e}")

# 完整的异常处理示例ile_path = 'safe_read_test.txt'
try:
    # 尝试打开文件
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        print(f"成功读取文件：{content}")
        
except FileNotFoundError:
    print(f"错误：文件 '{file_path}' 不存在")
    # 创建文件
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write('这是新创建的文件')
    print(f"已创建新文件：{file_path}")
    
except PermissionError:
    print(f"错误：没有权限访问文件 '{file_path}'")
    
except UnicodeDecodeError:
    print(f"错误：文件 '{file_path}' 编码格式不正确")
    
except Exception as e:
    print(f"未知错误：{e}")

# ==================== 9. 二进制文件操作 ====================

print("\n=== 二进制文件操作 ======")

# 写入二进制文件
data = b'Hello, Binary World!'
with open('binary_test.bin', 'wb') as f:
    f.write(data)
print("二进制文件已创建")

# 读取二进制文件
with open('binary_test.bin', 'rb') as f:
    binary_content = f.read()
    print(f"二进制内容：{binary_content}")
    print(f"解码后的内容：{binary_content.decode('utf-8')}")

# 图片文件复制（二进制操作）
# 注意：这里只是示例，实际使用时需要确保有图片文件
try:
    # 模拟图片文件操作
    image_data = b'\x89PNG\r\n\x1a\n'  # 简化的PNG文件头
    with open('fake_image.png', 'wb') as f:
        f.write(image_data)
    print("模拟图片文件已创建")
except Exception as e:
    print(f"图片文件操作错误：{e}")


# ==================== 10. 实用文件操作函数 ====================

print("\n=== 实用文件操作函数 ===")

def read_file_safely(file_path, encoding='utf-8'):
    """安全读取文件，带异常处理"""
    try:
        with open(file_path, 'r', encoding=encoding) as f:
            return f.read()
    except FileNotFoundError:
        print(f"文件不存在：{file_path}")
        return None
    except Exception as e:
        print(f"读取文件错误：{e}")
        return None

def write_file_safely(file_path, content, encoding='utf-8'):
    """安全写入文件，带异常处理"""
    try:
        with open(file_path, 'w', encoding=encoding) as f:
            f.write(content)
        return True
    except Exception as e:
        print(f"写入文件错误：{e}")
        return False

def append_file_safely(file_path, content, encoding='utf-8'):
    """安全追加内容到文件，带异常处理"""
    try:
        with open(file_path, 'a', encoding=encoding) as f:
            f.write(content)
        return True
    except Exception as e:
        print(f"追加文件错误：{e}")
        return False

def count_lines(file_path, encoding='utf-8'):
    """统计文件行数"""
    try:
        with open(file_path, 'r', encoding=encoding) as f:
            return sum(1 for _ in f)
    except Exception as e:
        print(f"统计行数错误：{e}")
        return 0

def search_in_file(file_path, keyword, encoding='utf-8'):
    """在文件中搜索关键词"""
    try:
        with open(file_path, 'r', encoding=encoding) as f:
            for line_num, line in enumerate(f, 1):
                if keyword in line:
                    print(f"找到关键词 '{keyword}' 在第 {line_num} 行")
                    return True
        print(f"未找到关键词 '{keyword}'")
        return False
    except Exception as e:
        print(f"搜索文件错误：{e}")
        return False

# 测试实用函数
print("测试实用文件操作函数：")

# 测试安全读取
content = read_file_safely('test.txt')
if content:
    print(f"安全读取成功，内容长度：{len(content)} 字符")

# 测试安全写入
write_file_safely('safe_write_test.txt', '这是安全写入的内容\n第二行')
print("安全写入测试完成")

# 测试安全追加
append_file_safely('safe_write_test.txt', '\n追加的内容')
print("安全追加测试完成")

# 测试行数统计
line_count = count_lines('test.txt')
print(f"文件行数：{line_count}")

# 测试文件搜索
search_in_file('test.txt', 'Python')


# ==================== 11. 实际应用示例 ====================

print("\n=== 实际应用示例 ===")

# 示例1：日志文件处理
def process_log_file(log_file):
    """处理日志文件，统计错误信息"""
    error_count = 0
    warning_count = 0
    info_count = 0
    
    try:
        with open(log_file, 'r', encoding='utf-8') as f:
            for line in f:
                if 'ERROR' in line:
                    error_count += 1
                elif 'WARNING' in line:
                    warning_count += 1
                elif 'INFO' in line:
                    info_count += 1
                    
        print(f"日志统计：")
        print(f"  错误：{error_count} 条")
        print(f"  警告：{warning_count} 条")
        print(f"  信息：{info_count} 条")
        
    except FileNotFoundError:
        print(f"日志文件不存在：{log_file}")
    except Exception as e:
        print(f"处理日志文件错误：{e}")

# 创建测试日志文件
log_content = '''2024-01-01 10:00:00 INFO 系统启动
2024-01-01 10:05:00 WARNING 内存使用率高
2024-01-01 10:10:00 ERROR 数据库连接失败
2024-01-01 10:15:00 INFO 重试连接成功
2024-01-01 10:20:00 ERROR 文件写入失败
'''

with open('test.log', 'w', encoding='utf-8') as f:
    f.write(log_content)

process_log_file('test.log')

# 示例2：配置文件处理
def read_config(config_file):
    """读取配置文件"""
    config = {}
    try:
        with open(config_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):  # 跳过空行和注释
                    if '=' in line:
                        key, value = line.split('=', 1)
                        config[key.strip()] = value.strip()
        return config
    except FileNotFoundError:
        print(f"配置文件不存在：{config_file}")
        return {}
    except Exception as e:
        print(f"读取配置文件错误：{e}")
        return {}

# 创建测试配置文件
config_content = '''# 应用配置文件
app_name=MyApplication
version=1.0.0
debug_mode=true
max_connections=100
'''

with open('config.ini', 'w', encoding='utf-8') as f:
    f.write(config_content)

config = read_config('config.ini')
print(f"配置内容：{config}")

# 示例3：数据文件处理
def process_data_file(input_file, output_file):
    """处理数据文件：读取、转换、写入"""
    try:
        # 读取输入文件
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # 处理数据
        processed_lines = []
        for line in lines:
            line = line.strip()
            if line:  # 跳过空行
                # 简单处理：转换为大写并添加行号
                processed_line = f"{len(processed_lines) + 1}. {line.upper()}"
                processed_lines.append(processed_line)
        
        # 写入输出文件
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(processed_lines))
        
        print(f"数据处理完成：{len(processed_lines)} 行")
        return True
        
    except FileNotFoundError:
        print(f"输入文件不存在：{input_file}")
        return False
    except Exception as e:
        print(f"数据处理错误：{e}")
        return False

# 创建测试数据文件
data_content = '''apple
banana
orange
grape
watermelon
'''

with open('input_data.txt', 'w', encoding='utf-8') as f:
    f.write(data_content)

process_data_file('input_data.txt', 'output_data.txt')

# 读取处理结果
with open('output_data.txt', 'r', encoding='utf-8') as f:
    print(f"处理后的数据：\n{f.read()}")

# ==================== 12. 清理测试文件 ====================

print("\n=== 清理测试文件 ===")

import os
import shutil

# 要删除的文件列表
files_to_remove = [
    'test.txt',
    'write_test.txt', 
    'append_test.txt',
    'pointer_test.txt',
    'binary_test.bin',
    'fake_image.png',
    'safe_write_test.txt',
    'test.log',
    'config.ini',
    'input_data.txt',
    'output_data.txt'
]

# 删除文件
for file_path in files_to_remove:
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"已删除：{file_path}")

# 删除目录
if os.path.exists('test_dir'):
    shutil.rmtree('test_dir')
    print("已删除目录：test_dir")

print("测试文件清理完成")

print("\n=== Python 文件操作详解完成 ===")# Python 文件操作详解
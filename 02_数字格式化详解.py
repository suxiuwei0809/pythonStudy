# f-string 数字格式化详解

# ==================== 基本示例 ====================

pi = 3.1415926
formatted4 = f"圆周率: {pi:.2f}"  # 保留两位小数
print(f"数字格式化: {formatted4}")


# ==================== 1. 小数位数控制 ====================

print("\n=== 小数位数控制 ===")

pi = 3.1415926

# 保留2位小数
print(f"保留2位小数: {pi:.2f}")  # 3.14

# 保留4位小数
print(f"保留4位小数: {pi:.4f}")  # 3.1416

# 不保留小数
print(f"不保留小数: {pi:.0f}")  # 3

# 保留1位小数
print(f"保留1位小数: {pi:.1f}")  # 3.1


# ==================== 2. 宽度控制 ====================

print("\n=== 宽度控制 ===")

num = 42

# 固定宽度，右对齐
print(f"固定宽度右对齐: '{num:10}'")  # '        42'

# 固定宽度，左对齐
print(f"固定宽度左对齐: '{num:<10}'")  # '42        '

# 固定宽度，居中
print(f"固定宽度居中: '{num:^10}'")  # '    42    '

# 填充字符
print(f"星号填充: '{num:*>10}'")  # '********42'
print(f"井号填充: '{num:#>10}'")  # '########42'
print(f"零填充: '{num:0>10}'")  # '0000000042'


# ==================== 3. 千位分隔符 ====================

print("\n=== 千位分隔符 ===")

big_num = 1234567890

# 使用逗号作为千位分隔符
print(f"千位分隔符: {big_num:,}")  # 1,234,567,890

# 保留小数并添加千位分隔符
print(f"带小数的千位分隔符: {big_num:,.2f}")  # 1,234,567,890.00

# 下划线作为千位分隔符（Python 3.6+）
print(f"下划线分隔符: {big_num:_}")  # 1_234_567_890


# ==================== 4. 百分比格式 ====================

print("\n=== 百分比格式 ===")

ratio = 0.1234

# 转换为百分比，保留2位小数
print(f"百分比(2位小数): {ratio:.2%}")  # 12.34%

# 转换为百分比，保留1位小数
print(f"百分比(1位小数): {ratio:.1%}")  # 12.3%

# 转换为百分比，保留3位小数
print(f"百分比(3位小数): {ratio:.3%}")  # 12.340%

# 不同比例
print(f"50%: {0.5:.0%}")  # 50%
print(f"100%: {1.0:.0%}")  # 100%


# ==================== 5. 科学计数法 ====================

print("\n=== 科学计数法 ===")

big_num = 1234567890
small_num = 0.000123456

# 科学计数法，保留2位小数
print(f"大数科学计数法: {big_num:.2e}")  # 1.23e+09

# 科学计数法，保留4位小数
print(f"大数科学计数法(4位): {big_num:.4e}")  # 1.2346e+09

# 小数的科学计数法
print(f"小数科学计数法: {small_num:.2e}")  # 1.23e-04

# 科学计数法，保留1位小数
print(f"科学计数法(1位): {big_num:.1e}")  # 1.2e+09


# ==================== 6. 正负号显示 ====================

print("\n=== 正负号显示 ===")

num1 = 42
num2 = -42
num3 = 0

# 总是显示符号
print(f"正数带符号: {num1:+}")  # +42
print(f"负数带符号: {num2:+}")  # -42
print(f"零带符号: {num3:+}")  # +0

# 正数显示空格，负数显示符号
print(f"正数空格: '{num1: }'")  # ' 42'
print(f"负数符号: '{num2: }'")  # '-42'
print(f"零空格: '{num3: }'")  # ' 0'

# 不显示符号（默认）
print(f"正数无符号: {num1}")  # 42
print(f"负数无符号: {num2}")  # -42


# ==================== 7. 实用示例 ====================

print("\n=== 实用示例 ===")

# 货币格式化
price = 1234.5678
print(f"人民币价格: ¥{price:,.2f}")  # 人民币价格: ¥1,234.57
print(f"美元价格: ${price:,.2f}")  # 美元价格: $1,234.57

# 进度显示
progress = 0.6789
print(f"下载进度: {progress:.1%}")  # 下载进度: 67.9%
print(f"完成度: {progress:.0%}")  # 完成度: 68%

# 对齐表格
name = "张三"
score = 95.5
rank = 1

print(f"{name:10s} | {score:6.1f} | {rank:4d}")
# 输出: 张三        |   95.5 |    1

name2 = "李四"
score2 = 88.0
rank2 = 3
print(f"{name2:10s} | {score2:6.1f} | {rank2:4d}")
# 输出: 李四        |   88.0 |    3

# 时间格式化
seconds = 3661
hours = seconds / 3600
print(f"时间: {hours:.2f} 小时")  # 时间: 1.02 小时

days = 7.5
print(f"天数: {days:.1f} 天")  # 天数: 7.5 天

# 分数显示
numerator = 3
denominator = 7
ratio = numerator / denominator
print(f"分数: {numerator}/{denominator} = {ratio:.3f}")  # 分数: 3/7 = 0.429

# 温度显示
temp_celsius = 25.678
temp_fahrenheit = temp_celsius * 9/5 + 32
print(f"摄氏温度: {temp_celsius:.1f}°C")  # 摄氏温度: 25.7°C
print(f"华氏温度: {temp_fahrenheit:.1f}°F")  # 华氏温度: 78.2°F

# 速度显示
speed_kmh = 120.456
speed_ms = speed_kmh / 3.6
print(f"速度: {speed_kmh:.1f} km/h")  # 速度: 120.5 km/h
print(f"速度: {speed_ms:.2f} m/s")  # 速度: 33.46 m/s


# ==================== 8. 组合格式化 ====================

print("\n=== 组合格式化 ===")

# 宽度 + 小数位数 + 千位分隔符
large_number = 1234567.8912
print(f"组合格式: {large_number:>15,.2f}")  # '  1,234,567.89'

# 填充 + 居中 + 小数位数
value = 3.14159
print(f"居中填充: {value:^10.2f}")  # '   3.14   '

# 符号 + 宽度 + 小数位数
positive = 123.456
negative = -123.456
print(f"正数组合: {positive:+10.2f}")  # '   +123.46'
print(f"负数组合: {negative:+10.2f}")  # '   -123.46'


# ==================== 9. 数据类型格式化 ====================

print("\n=== 数据类型格式化 ===")

# 整数格式化
integer = 42
print(f"整数: {integer:d}")  # 42
print(f"二进制: {integer:b}")  # 101010
print(f"八进制: {integer:o}")  # 52
print(f"十六进制: {integer:x}")  # 2a
print(f"十六进制(大写): {integer:X}")  # 2A

# 浮点数格式化
float_num = 123.456
print(f"浮点数: {float_num:f}")  # 123.456000
print(f"科学计数法: {float_num:e}")  # 1.234560e+02
print(f"通用格式: {float_num:g}")  # 123.456


# ==================== 10. 实际应用场景 ====================

print("\n=== 实际应用场景 ===")

def format_report_data(data):
    """格式化报表数据"""
    print("\n报表数据:")
    print(f"{'姓名':<10} {'分数':>8} {'排名':>6}")
    print("-" * 26)
    for name, score, rank in data:
        print(f"{name:<10} {score:>8.1f} {rank:>6d}")

# 学生成绩数据
students = [
    ("张三", 95.5, 1),
    ("李四", 88.0, 3),
    ("王五", 92.3, 2),
    ("赵六", 85.7, 4)
]

format_report_data(students)


def format_financial_summary(income, expense, balance):
    """格式化财务摘要"""
    print("\n财务摘要:")
    print(f"收入: ¥{income:,.2f}")
    print(f"支出: ¥{expense:,.2f}")
    print(f"余额: ¥{balance:,.2f}")
    print(f"结余率: {(balance/income):.1%}")

# 财务数据
format_financial_summary(50000.50, 32000.75, 17999.75)


def format_progress_bars(tasks):
    """格式化进度条"""
    print("\n任务进度:")
    for task, progress in tasks:
        bar_length = 30
        filled = int(bar_length * progress)
        bar = "█" * filled + "░" * (bar_length - filled)
        print(f"{task:<20} [{bar}] {progress:.0%}")

# 任务进度数据
tasks = [
    ("数据分析", 0.75),
    ("报告编写", 0.45),
    ("代码优化", 0.90),
    ("测试验证", 0.30)
]

format_progress_bars(tasks)


print("\n=== f-string 数字格式化示例完成 ===")



# 货币格式化
price = 1234.5678
print(f"人民币价格: ¥{price:,.2f}")  # 人民币价格: ¥1,234.57

# 进度显示
progress = 0.6789
print(f"下载进度: {progress:.1%}")  # 下载进度: 67.9%



# 学生成绩报表
def format_report_data(data):
    print(f"{'姓名':<10} {'分数':>8} {'排名':>6}")
    for name, score, rank in data:
        print(f"{name:<10} {score:>8.1f} {rank:>6d}")

# 财务摘要
def format_financial_summary(income, expense, balance):
    print(f"收入: ¥{income:,.2f}")
    print(f"支出: ¥{expense:,.2f}")
    print(f"余额: ¥{balance:,.2f}")

# 进度条显示
def format_progress_bars(tasks):
    for task, progress in tasks:
        bar = "█" * int(30 * progress) + "░" * (30 - int(30 * progress))
        print(f"{task:<20} [{bar}] {progress:.0%}")





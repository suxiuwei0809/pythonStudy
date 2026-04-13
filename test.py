import sys
import argparse


def example_basic_variables():
    """示例1：基本变量定义和打印操作"""
    print("\n=== 示例1：基本变量定义和打印操作 ===")
    
    # 定义整数变量 a，值为 10
    a = 10
    # 定义字符串变量 b，值为 "Hello, World!"
    b = "Hello, World!"
    
    # 打印整数变量 a 的值
    print(a)    
    # 打印字符串变量 b 的值
    print(b)  
    # print(a+b)会报错，因为 a 是整数，b 是字符串，不能直接相加   
    # 使用逗号分隔打印 a 和 b，自动添加空格
    print(a, b)  
    # 使用 f-string 格式化打印变量 a 的值
    print(f"{a}")
    print(f"{a}{b}")


def example_two_parameters(a, b):
    """示例2：接受两个参数并打印它们的值
    
    该函数演示了 Python 函数参数的基本使用方法，
    接收两个任意类型的参数并将它们的值格式化输出。
    
    Args:
        a: 第一个参数，可以是任意类型（int, str, float, list, dict 等）
        b: 第二个参数，可以是任意类型（int, str, float, list, dict 等）
    
    Returns:
        None: 函数不返回任何值，仅打印参数值
    
    Example:
        >>> example_two_parameters(10, "Hello")
        参数 a: 10
        参数 b: Hello
        
        >>> example_two_parameters("Python", 3.14)
        参数 a: Python
        参数 b: 3.14
    """
    print("\n=== 示例2：接受两个参数并打印它们的值 ===")
    
    # 使用 f-string 格式化输出第一个参数 a 的值
    # f-string 是 Python 3.6+ 引入的字符串格式化方法
    # {a} 会被替换为参数 a 的实际值
    print(f"参数 a: {a}")
    
    # 使用 f-string 格式化输出第二个参数 b 的值
    # {b} 会被替换为参数 b 的实际值
    print(f"参数 b: {b}")


def example_default_parameters(a=10, b="默认值"):
    """示例3：带默认参数值的函数
    
    该函数演示了 Python 函数默认参数的使用方法，
    调用时不传递参数时使用默认值，传递参数时覆盖默认值。
    
    Args:
        a (int): 第一个参数，默认值为 10
        b (str): 第二个参数，默认值为 "默认值"
    
    Returns:
        None: 函数不返回任何值，仅打印参数
    """
    print("\n=== 示例3：带默认参数值的函数 ===")
    
    # 使用 f-string 格式化打印参数 a 的值
    print(f"参数 a: {a}")
    
    # 使用 f-string 格式化打印参数 b 的值
    print(f"参数 b: {b}")


def example_sys_argv():
    """示例4：使用 sys.argv 处理命令行参数
    
    该函数演示了如何使用 sys.argv 获取命令行参数。
    sys.argv 是一个列表，包含了命令行传递的所有参数。
    
    Args:
        无参数，从命令行获取输入
    
    Returns:
        None: 函数不返回任何值，仅打印命令行参数
    
    Example:
        在命令行运行：python test.py arg1 arg2 arg3
        输出：命令行参数: ['arg1', 'arg2', 'arg3']
    """
    print("\n=== 示例4：使用 sys.argv 处理命令行参数 ===")
    
    # sys.argv 是一个列表，包含命令行参数
    # sys.argv[0] 是脚本文件名（如 test.py）
    # sys.argv[1:] 是除脚本名外的所有命令行参数（从索引1开始到末尾）
    # 使用切片 [1:] 获取所有命令行参数，排除脚本文件名
    args = sys.argv[1:]
    
    # 使用 f-string 格式化输出获取到的命令行参数列表
    print(f"命令行参数: {args}")


def example_argparse():
    """示例5：使用 argparse 解析命令行参数
    
    该函数演示了如何使用 Python 的 argparse 模块来解析命令行参数。
    argparse 是 Python 标准库中用于解析命令行参数的强大工具，
    可以自动生成帮助信息、处理参数类型转换和验证。
    
    Args:
        无参数，从命令行获取输入
    
    Returns:
        None: 函数不返回任何值，仅打印解析结果
    
    Example:
        在命令行运行：python test.py 123 hello
        输出：
            数字参数: 123
            文本参数: hello
        
        查看帮助信息：python test.py --help
    """
    print("\n=== 示例5：使用 argparse 解析命令行参数 ===")
    
    # 创建 ArgumentParser 对象，用于解析命令行参数
    # description 参数会在帮助信息中显示，用于描述程序的功能
    parser = argparse.ArgumentParser(description="示例程序")
    
    # 添加第一个位置参数 "number"
    # 位置参数是必须提供的，按顺序传递
    # type=int 会自动将输入转换为整数类型，如果转换失败会报错
    # help 参数会在帮助信息中显示该参数的说明
    parser.add_argument("number", type=int, help="一个整数参数")
    
    # 添加第二个位置参数 "text"
    # 位置参数是必须提供的，按顺序传递
    # type=str 会自动将输入转换为字符串类型
    # help 参数会在帮助信息中显示该参数的说明
    parser.add_argument("text", type=str, help="一个字符串参数")
    
    # 解析命令行参数
    # parse_args() 会自动从 sys.argv 中读取命令行参数
    # 返回一个命名空间对象，包含解析后的参数值
    # 可以通过 args.number 和 args.text 访问对应的参数值
    args = parser.parse_args()
    
    # 使用 f-string 格式化输出解析得到的数字参数值
    # args.number 访问第一个位置参数的值，类型为整数
    print(f"数字参数: {args.number}")
    
    # 使用 f-string 格式化输出解析得到的文本参数值
    # args.text 访问第二个位置参数的值，类型为字符串
    print(f"文本参数: {args.text}")


def main():
    """主函数，运行所有示例
    
    该函数依次调用所有示例函数，展示不同的 Python 编程概念。
    每个示例都演示了特定的功能和技术。
    """
    print("=" * 50)
    print("Python 编程示例集合")
    print("=" * 50)
    
    # 运行示例1：基本变量定义和打印操作
    example_basic_variables()
    
    # 运行示例2：接受两个参数并打印它们的值
    example_two_parameters(10, "Hello")
    
    # 运行示例3：带默认参数值的函数
    example_default_parameters()
    example_default_parameters(20, "自定义值")
    
    # 运行示例4：使用 sys.argv 处理命令行参数
    example_sys_argv()
    
    # 注意：示例5 需要命令行参数，如果在 IDE 中运行可能会出错
    # 可以在命令行中运行：python test.py 123 hello
    try:
        example_argparse()
    except SystemExit:
        print("\n注意：示例5 需要命令行参数，请在命令行中运行：")
        print("python test.py 123 hello")
    
    print("\n" + "=" * 50)
    print("所有示例运行完成！")
    print("=" * 50)


if __name__ == "__main__":
    main()
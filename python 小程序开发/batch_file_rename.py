"""
这将批量重命名给定目录中的一组文件，
一旦您通过了当前和新的扩展名
"""
__author__ = 'iByte'
__version__ = '1.0'

import argparse
import os


def batch_rename(work_dir, old_ext, new_ext):
    """
    这将批量重命名给定目录中的一组文件，
     一旦您通过了当前和新的扩展名
    """
    # files = os.listdir(work_dir)
    for filename in os.listdir(work_dir):
        # 获取文件扩展名
        split_file = os.path.splitext(filename)
        file_ext = split_file[1]
        # 如果old_ext = file_ext，则开始检查文件扩展名的逻辑
        if old_ext == file_ext:
            # 返回具有新扩展名的文件的更改名称
            newfile = split_file[0] + new_ext

            # 写文件
            os.rename(
                os.path.join(work_dir, filename),
                os.path.join(work_dir, newfile)
            )
    print("rename is done!")
    print(os.listdir(work_dir))


def get_parser():
    parser = argparse.ArgumentParser(description='change extension of files in a working directory')
    parser.add_argument('work_dir', metavar='WORK_DIR', type=str, nargs=1,
                        help='the directory where to change extension')
    parser.add_argument('old_ext', metavar='OLD_EXT', type=str, nargs=1, help='old extension')
    parser.add_argument('new_ext', metavar='NEW_EXT', type=str, nargs=1, help='new extension')
    return parser


def main():
    """
    如果直接调用脚本，则将调用此方法。
    """
    # 添加命令行参数
    parser = get_parser()
    args = vars(parser.parse_args())

    # 使用传递的第一个参数设置变量work_dir
    work_dir = args['work_dir'][0]
    # 设置变量old_ext并传递第二个参数
    old_ext = args['old_ext'][0]
    if old_ext[0] != '.':
        old_ext = '.' + old_ext
    # 设置变量new_ext并传递第三个参数
    new_ext = args['new_ext'][0]
    if new_ext[0] != '.':
        new_ext = '.' + new_ext

    batch_rename(work_dir, old_ext, new_ext)


if __name__ == '__main__':
    main()

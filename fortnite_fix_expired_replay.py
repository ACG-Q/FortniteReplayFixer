import argparse
import shutil
import os

def backup_file(file_path):
    """
    备份文件，创建一个副本，文件名为原始文件名加上 .bak 后缀。
    """
    backup_path = f"{file_path}.bak"
    try:
        shutil.copy(file_path, backup_path)
        print(f"[INFO] 已创建备份文件：{backup_path}")
        return backup_path
    except Exception as e:
        print(f"[ERROR] 备份文件失败：{e}")
        raise

def copy_bytes(source_file, target_file, byte_range=(0, 1024)):
    """
    将源文件中的指定字节范围复制到目标文件。
    """
    start, end = byte_range

    # 参数验证
    if start < 0 or end <= start:
        raise ValueError(f"无效的字节范围：{byte_range}")

    try:

        # 读取源文件中的指定字节范围
        with open(source_file, 'rb') as src:
            src.seek(start)
            data_to_copy = src.read(end - start)

        # 读取目标文件并替换指定范围的字节
        with open(target_file, 'r+b') as tgt:
            tgt.seek(start)
            tgt.write(data_to_copy)

        print(f"[INFO] 成功将 {source_file} 的字节范围 {byte_range} 替换到 {target_file} 中。")
    except FileNotFoundError as e:
        print(f"[ERROR] 文件未找到：{e}")
    except PermissionError as e:
        print(f"[ERROR] 文件访问权限不足：{e}")
    except Exception as e:
        print(f"[ERROR] 操作失败：{e}")

def main():
    parser = argparse.ArgumentParser(description="修复堡垒之夜过期回放文件的工具。")
    parser.add_argument("source_file", type=str, help="路径到有效的回放文件。")
    parser.add_argument("target_file", type=str, help="路径到需要修复的回放文件。")
    parser.add_argument("--start", type=int, default=0, help="复制的起始字节位置（默认：0）。")
    parser.add_argument("--end", type=int, default=48, help="复制的结束字节位置（默认：48）。")
    parser.add_argument("--skip-backup", action="store_true", help="跳过备份目标文件。")

    args = parser.parse_args()

    # 检查文件路径是否存在
    if not os.path.exists(args.source_file):
        print(f"[ERROR] 源文件不存在：{args.source_file}")
        return

    if not os.path.exists(args.target_file):
        print(f"[ERROR] 目标文件不存在：{args.target_file}")
        return

    try:
        # 是否跳过备份
        if not args.skip_backup:
            backup_file(args.target_file)
        copy_bytes(args.source_file, args.target_file, (args.start, args.end))
    except Exception as e:
        print(f"[ERROR] 修复失败：{e}")

if __name__ == "__main__":
    main()

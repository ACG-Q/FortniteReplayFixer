# 修复堡垒之夜过期回放文件工具

该工具用于修复堡垒之夜过期的回放文件，支持将指定字节范围从源文件复制到目标文件。

## 功能

1. **备份目标文件**：可以选择是否备份目标文件，以防止意外操作。
2. **复制字节范围**：从源文件指定的字节范围复制内容到目标文件。
3. **支持命令行参数**：通过命令行输入路径和参数，自定义操作。

## 使用方法

### 命令行参数说明

```bash
python fix_replay.py <source_file> <target_file> [--start <start_byte>] [--end <end_byte>] [--skip-backup]
```

- `source_file`: 源文件路径（有效的回放文件）。
- `target_file`: 目标文件路径（需要修复的回放文件）。
- `--start`: 复制的起始字节位置（默认：0）。
- `--end`: 复制的结束字节位置（默认：48）。
- `--skip-backup`: 跳过备份目标文件的操作。

### 示例

1. 备份并修复回放文件：

```bash
python fix_replay.py source_file.replay target_file.replay
```

2. 跳过备份并修复特定字节范围：

```bash
python fix_replay.py source_file.replay target_file.replay --start 100 --end 150 --skip-backup
```

## 注意事项

- 请确保源文件和目标文件路径正确，并具有足够的权限。
- 建议在操作前备份重要文件。
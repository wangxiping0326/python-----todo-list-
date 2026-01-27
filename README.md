# python-----todo-list-
这是gap期间自学Python使用的仓库。致谢deepseek的规划与帮助。

# 个人待办事项管理工具 (Personal Todo List Manager)

一个使用Python命令行实现的简易待办事项管理器，是用来练手的实践项目。

## ✨ 功能特性
- **增删改查**：可以添加、查看、标记完成和删除任务。
- **数据持久化**：任务数据保存在本地JSON文件中。【待更新】
- **清晰的交互界面**：使用符号（[ ]/[✓]）直观展示任务状态。

## 🚀 如何运行
1.  确保你安装了 **Python 3.8+**。
2.  克隆本项目到本地：
    ```bash
    git clone https://github.com/wangxiping0326/python-----todo-list-.git
    ```
3.  进入项目目录并运行主程序：
    ```bash
    cd python-----todo-list-
    python todo.py
    ```

## 📁 项目结构
python-----todo-list-/
├── todo.py # 主程序文件，包含所有核心逻辑
├── tasks.json # 任务数据存储文件（运行后自动生成）
└── README.md # 本说明文件

## 🖥️ 使用示例
启动程序后，你会看到如下菜单：
🌟 简易待办事项管理器
==============================
请选择操作:

1.添加任务

2.查看任务

3.标记任务完成

4.删除任务

5.退出

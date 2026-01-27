#todo.py - 版本0.1：最基础的待办事项
#简单功能:
#--1--:增加待办事项
#--2--:查看待办事项
#--3--:删除待办事项
from pydoc import describe

tasks = []#定义一个空列表来存放代办事项

def add_task():
    print("添加待办事项")
    description = input("请输入任务描述:\n ").strip()
    task ={
        'id':len(tasks)+1,
        'description':description,
        'done':False
    }
    tasks.append(task)
    print(f"✅任务：{description}添加！")
    print(f"当前共有{len(tasks)}个任务！")

def show_tasks(tasks_list):
    if not tasks:
        print("📭 还没有任务，快去添加一个吧！")
        return

    print('\n📋 你的待办事项')
    for task in tasks:
        if task['done']:
            status = "[✓]"  # 已完成
        else:
            status = "[ ]"  # 未完成
        print(f'{task["id"]}: {status} {task["description"]}')

def mark_task_done():
    if not tasks:
        print("📭 还没有任务，快去添加一个吧！")
        return

    # 先显示当前任务
    show_tasks(tasks)
    # 获取用户输入

    done_choice = input("请输入要完结的任务序号").strip()
    target_id = int(done_choice)
    #特别注意，在输入过程中输入返回的是字符串

    for task in tasks:
        if target_id == task['id']:
            if task['done']:
                print("已经是完成状态！")
            task['done'] = True
            print(f'{task["id"]}: {task["description"]}已标记完成')
            return

        print("📭 还没有任务，快去添加一个吧！")

def delete_task():
    if not tasks:
        print("📭 还没有任务，快去添加一个吧！")
        return

    # 先显示当前任务
    show_tasks(tasks)
    # 获取用户输入

    delete_choice= input("请输入要删除的任务序号").strip()
    target_del_id = int(delete_choice)

    for i,task in enumerate(tasks):
        if task['id'] == target_del_id:
            conform = input(f'请确认要删除任务{task["description"]}?y/n').strip().lower()
            if conform == 'y':
                removed_task = tasks.pop(i)
                print(f'已删除任务{task["id"]}: {task["description"]}')
                renumber_tasks()
                return

def renumber_tasks():
    for j,task in enumerate(tasks, start=1):
        task['id'] = j




def main():
    #tasks = []#定义一个空列表来存放代办事项
    """主程序"""
    print("🌟 简易待办事项管理器")
    print("=" * 30)

    while True:
        print("\n请选择操作:")
        print("1. 添加任务")
        print("2. 查看任务")
        print("3. 标记任务完成")  # 新增选项
        print("4. 删除任务")
        print("5. 退出")

        choice = input("请输入选项(1-5)")
        if choice == "1":
            add_task()
            pass
        elif choice == "2":
            show_tasks(tasks)
            pass
        elif choice == "3":
            mark_task_done()
            pass
        elif choice == "4":
            delete_task()
            pass
        elif choice == "5":
            break
        else:
            print("无效选项，请重新输入")
            break
#   print("欢迎使用个人数据管理工具")

if __name__ == "__main__":
    main()
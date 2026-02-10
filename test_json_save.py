from core import Todo_list

def test_save_function():
    """1.测试保存功能"""
    print("🧪 开始测试JSON保存功能")
    print("=" * 50)


###1.创建实例
    todo = Todo_list("test_tasks.json")#新建一个名为test_tasks的json文件

    # 2. 添加一些测试任务
    print("\n1. 添加测试任务")
    todo.add_task("学习Python面向对象")
    todo.add_task("实现Json保存功能")
    todo.add_task("测试数据持久化")


    # 标记第一个任务为完成
    print("\n标记第一个任务为完成")
    todo.tasks[0].mark_status()

    # 3. 显示当前任务
    print("\n2.当前任务列表：")
    todo.print_all()

    # 4. 保存到JSON
    print("\n3. 保存任务到JSON文件")
    success = todo.save_data_to_json()
    if success:
        print("\n✅ 保存成功！")

        #5.读取并且显示保存的内容
        print("\n4. 查看保存的任务")
        try:
            import json
            with open("test_tasks.json","r",encoding="utf-8") as f:
                saved_data = json.load(f)
            print("保存的数据内容：")
            print(json.dumps(saved_data,indent = 2,ensure_ascii=False))

            #验证保存的数据
            print("\n验证开始")
            print(f"保存的任务数量：{len(saved_data['tasks'])}")
            print(f"下一个id:{saved_data['next_id']}")
            print(f"第一个任务状态：{saved_data['tasks'][0]['status']}")

        except Exception as e:
            print(f"❌ 读取保存文件失败: {e}")

    #6.清理测试文件
    print("\n5. 清理测试文件")
    import os
    if os.path.exists("test_tasks.json"):
        os.remove("test_tasks.json")
        print("✅ 测试文件已清理")

        print("\n" + "=" * 50)
        print("🎉 测试完成！")

if __name__ == "__main__":
    test_save_function()
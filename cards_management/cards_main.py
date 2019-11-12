# 用列表存储所有的用户信息，单个用户信息用字典
# 所有名片相关操作都需要使用列表，所以需要定义在程序的顶部
# 程序刚运行时，没有数据，所以是空列表
# 程序就是用来处理数据的，而变量就是用来存储数据的。

# 在程序的第一行利用shebang符号"#!"，可以在终端中直接执行python代码，而不需要启动编译器

import cards_tools

while True:  # 无限循环，由用户决定什么时候退出系统；

    # 显示功能菜单

    cards_tools.show_menu()

    action_str = input("Please choose the next step: ")
    print("Your choice is 【%s】" % action_str)

    # 如果用户输入123，针对名片的操作
    if action_str in ["1","2","3"]:

        # 新增名片处理
        if action_str=="1":
            # pass
            cards_tools.new_card()
        # 显示全部
        elif action_str=="2":
            # pass
            cards_tools.show_all()
        # 查询名片
        elif action_str=="3":
            # pass
            cards_tools.search_card()
    # 输入0，退出系统
    elif action_str=="0":
        print("!!!Welcome next time!!!")
        break
        # pass关键字是占位符，保障程序结构正确，不希望立即编写程序内部代码；
        # pass

    # 其他内容，提示用户输入错误
    else:
        print("Wrong! Please input your choice again.")

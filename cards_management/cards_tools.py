# 记录所有的名片字典
card_list=[]

def show_menu():

    """显示菜单"""
    print("*"*50)
    print("Welcome to Cards_Management System V1.0")
    print("")
    print("1. Add a new card")
    print("2. Show all cards")
    print("3. Search a card")
    print("")
    print("0. Exit the system")
    print("*"*50)




def new_card():

    """新增名片处理"""

    # 先用"-"提示要新增名片
    print("-"*50)
    print("Create a new card")

    # 1. 接收用户输入信息
    name_str = input("Please input your name: ")
    tel_str = input("Please input your tel: ")
    email_str = input("Please input your email: ")

    # 2. 建立名片字典
    card_dict={
        "Name":name_str,
        "Tel":tel_str,
        "Email":email_str
    }

    # 3. 将新建的名片追加到名片管理系统列表中
    card_list.append(card_dict)

    # 4. 提示用户名片创建成功
    print("%s , your card is successfully created!"%name_str)



def show_all():

    """显示所有名片"""
    print("-"*50)
    print("Show all cards.")

    # 判断是否存在名片记录，如果没有，提示用户并返回
    if len(card_list)==0:
        print("No cards record")

        # return可以返回一个函数的执行结果
        # return下方的代码不会被执行
        # 如果return后面没有任何结果，就返回到调用函数的位置，并且不返回任何内容
        return

    # 打印表头
    for i in ["name","Tel","Email"]:
        print(i,end="\t\t")  # 为了保障输出的结果格式美观，每个输出之间用两个\t；

    print("")

    # 打印分割线
    print("="*50)

    # 遍历名片依次输出用户信息
    for  card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t"%(
                                    card_dict["Name"],
                                    card_dict["Tel"],
                                    card_dict["Email"]
        ))

    print("="*50)



def search_card():

    """搜索名片"""
    print("-"*50)
    print("Search card.")

    # 1。 提示用户输入要查找的用户姓名
    find_name = input("Please input the name: ")

    # 2. 查找是否再列表中，如果没有找到，需要提示用户；
    for card_dict in card_list:
        if card_dict["Name"] == find_name:
            print("Name\t\tTel\t\tEmail\t\t",end=" ")
            # 由于上面代码中，需要在结束后，补充一个print("")，否则不会换行
            print("")
            print("="*50)
            print("%s\t\t%s\t\t%s\t\t" % (
                                            card_dict["Name"],
                                            card_dict["Tel"],
                                            card_dict["Email"]
            ))

            # 针对找到的名片记录执行修改和删除的操作
            deal_card(card_dict)

            break

    # 这里时使用的for--else的用法，只有for循环体内部所有遍历而不得，才会执行else语句
    else:
            print("Can't find %s, please reconfirm the name" % find_name)



def deal_card(find_dict):

    """处理查找到的名片

    :param find_dict:查找的名片
    """
    print(find_dict)

    action_str=input('Please choose what to do: [1] Modify [2] Delete [0] Go Back')

    if action_str=='1':
        find_dict['Name']=input_card_info(find_dict['Name'],'Name: ')
        find_dict['Tel']=input_card_info(find_dict['Tel'],'Tel: ')
        find_dict['Email']=input_card_info(find_dict['Email'],'Email:')
        print('modify card successfully!')

    elif action_str=='2':
        card_list.remove(find_dict)
        print('delete card')


def input_card_info(dict_value,tip_message):
    """输入名片信息

    :param dict_value: 字典中原有的值
    :param tip_message: 输入的提示文字
    :return: 如果用户输入了内容，就返回内容，否则就返回字典中原有的值
    """
    # 1. 提示用户输入内容
    result_str=input(tip_message)
    # 2. 针对用户输入进行判断，如果用户输入了内容，直接返回结果
    if len(result_str)>0:
        return result_str
    # 3. 如果用户没有输入内容，返回字典原有的值
    else:
        return dict_value

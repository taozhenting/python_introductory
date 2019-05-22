#!/usr/bin/python
# -*- coding: utf-8 -*-

def file_handle(backend_data,new_ret=None,type='fetch'):
    if type == 'fetch':
        with open('haproxy.conf','r') as read_f:
            ret = []
            tag = False
            for read_line in read_f:
                if read_line.strip() == backend_data:
                    tag = True
                    continue
                if tag and read_line.startswith('backend'):
                        break
                if tag:
                    print('\033[1;45m%s\033[0m' %read_line,end='')
                    ret.append(read_line)
        return ret

    if type == 'change':
        with open('haproxy.conf', 'r') as read_f, open('haproxy_new.conf', 'w') as write_f:
            tag = False
            has_wirte = False
            for read_line in read_f:
                if read_line.strip() == backend_data:
                    tag = True
                    continue
                if tag and read_line.startswith('backend'):
                    tag = False
                if not tag:
                    write_f.write(read_line)
                else:
                    if not has_wirte:
                        for record in new_ret:
                            write_f.write(record)
                        has_wirte = True

def fetch(data):
    print('这是查询功能')
    print('用户数据是',data)
    backend_data = 'backend %s' %data
    return file_handle(backend_data)

def add():
    pass

def change(data):
    new_ret = []
    old_server_record = fetch(data)
    with open('data.txt', 'r') as new_server_record:
        new_ret.append('backend %s \n' %data)
        for read_line in new_server_record:
            new_ret.append(read_line)
    backend_data = 'backend %s' %data
    print("这是修改功能")
    print('用户旧数据是', old_server_record)
    print('用户新数据是', new_ret)
    file_handle(backend_data,new_ret=new_ret,type='change')

def delete():
    pass

if __name__ == '__main__':
    msg = '''
    1:查询
    2:添加
    3:修改
    4:删除
    5:退出
    '''

    msg_dic = {
        '1':fetch,
        '2':add,
        '3':change,
        '4':delete,
    }

    while True:
        print(msg)
        choice = input('请输入你的选项: ').strip()
        if not choice:continue
        if choice == '5':break

        data = input('请输入你的数据: ').strip()

        # if choice != '1':
        #     data = eval(data)

        res = msg_dic[choice](data)
        print(res)

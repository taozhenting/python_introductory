#函数写法
#编写两个函数，第一个函数将负责处理打印设计的工作，而第二个将概述打印了哪些设计
def print_models(unprinted_designs,completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其移到列表completed_models中
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        #模拟根据设计制作3D打印模型的过程
        print(
            "Printing model: " +
            current_design
        )
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
unprinted_designs = ['iphone case','robot pendant','dodecahedron']
completed_models = []
print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)

#函数列表副本，防止列表被修改，使用方式：unprinted_designs[:] 这是unprinted_designs列表的副本，不会修改unprinted_designs列表
#但除非有充分理由需要传递副本，因为让函数使用现成列表避免花时间和内存创建副本，从而提高效率。
#在处理大型列表时尤其如此。
print_models(unprinted_designs[:],completed_models)
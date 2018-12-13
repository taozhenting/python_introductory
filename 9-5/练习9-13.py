from collections import OrderedDict
tao=OrderedDict()
tao['first_name']='tao'
tao['last_name']='zhenting'
tao['age']='36'
tao['city']='shanghai'
for name,info in tao.items():
    print(
        name +
        ": " +
        info
    )
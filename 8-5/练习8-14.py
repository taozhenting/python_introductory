def make_car(manufacturer,model,**car_info):
    """汽车信息存储在一个字典中"""
    profile={}
    profile['manufacturer'] = manufacturer
    profile['model'] = model
    for key, value in car_info.items():
        profile[key] = value
    return profile

car = make_car('subaru','outback',color='bule',tow_package=True)
print(car)
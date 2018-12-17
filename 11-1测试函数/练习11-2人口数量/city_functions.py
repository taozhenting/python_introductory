def get_city_country(city,country,population=''):
    """生成城市名和国家名"""
    fullname = city + ', ' + country + population
    return fullname.title()

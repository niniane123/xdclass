# 字典类型  key:value 键值对，这玩意不就是map吗  {key1:value1,key2:value2,key3:value3}
# map中key是不能重复的，如果是重复的key,那么后者会覆盖前者。
info = {"name": "zrc", "birth": "1223", "hobby": "rap"}
print(type(info))

# 增
info.update({"lover": "niniane"})
print(info)

# 删
# 删除整个字典
del info
# 删除某个key
del info["name"]

# 改
info["name"] = "zhangrenchao"
print(info)

# 查
# 查看map的长度
print(len(info))
# 取某一个key的值
print(info.get("lover"))

# 覆盖演示实例
info.update({"name": "zrc_last_name"})
print(info)

# 字典中的key必须要是不可变的，即要求保证对象的不变性




immutable_var = 1,"вафля", 9>1
print (immutable_var)
print (type(immutable_var))
# immutable_var[0] = 200 - кортеж дает возможность работать с разными типами данных, но не дает возможность их изменить
# данные можно изменить при условии что в кортеже будет использоваться список, пример: immutable_var = 1,"вафля",[2, стол],9>1 - в таком случае можно изменить только "2 и стол"
mutable_list = ["карандаш","степлер","бумага"]
print (mutable_list)
mutable_list[0] = "ручка"
mutable_list[1] = mutable_list[2]
print (mutable_list)
name= "waqas"
age=26
height=5.5
print(type(name))
print(type(age))
print(type(height))
customer_value=10
print(customer_value)
age+=5
customer_info=(" Tim kate is a prime customer he lives in california")
print(type(customer_info))
print(len(customer_info))
for c in customer_info:
    print(c)
    customer_list=["tim cate" ,54,6.12, "abc inc", True]
print(customer_list[1])
print(customer_list[3])
print(type(customer_list[1]))
print(type(customer_list[3]))
customer_list.append(30000)
print(customer_list)
customer_list.insert(1,"lahore")
print(customer_list)
customer_list.remove(54)
print(customer_list)
customer_list.pop(0)
print(customer_list)
print(len(customer_list))
for x in customer_list:
    print(x)
customer_list[0]= "karachi"
print(customer_list)
customer_tuple=("tim cate" ,54,6.12, "abc inc", True)
print(customer_tuple)
print(type(customer_tuple))
print(len(customer_tuple))
for g in customer_tuple:
    print(g)
print(customer_tuple[0])
print(customer_tuple[3])
customer_set={"tim cate" ,54,6.12, "abc inc", True}
print(customer_set)
print(type(customer_set))
print(len(customer_set))
for x in customer_set:
    print(x)
customer_dict={"name":"waqas","age":26,"height": 5.5,"companies":"abc Inc","status":True}
print(customer_dict)
print(type(customer_dict))
customer_dict["Name"]="ali"
print(customer_dict["name"])
print(len(customer_dict))
for x in customer_dict:
    print(x)
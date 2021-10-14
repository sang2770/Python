from copy import deepcopy
person = {
    'name': 'Vũ Thanh Tài',
    'age': 22,
    'male': True,
    'status': 'single',
    2:1
    }
#Access
print(person["name"])
print(person[2])
#change
person[2]="test"
print(person[2])
#delete
del person[2];
print(person)
#Xoa het
person.clear()
#Lồng nhau
person = {
    'name': 'Vũ Thanh Tài',
    'option': {
                'age': 22,
                'male': True,
                'status': 'alone'
            }        
    }

print(person['option']['age'])
# 22
print('Tạo từ điển từ list');
items=[("name", "Sang"), ("Xuan","Sang"),("array", [1,2,4])];
dic=dict(items);
print(dic);
##print(dic.has_key("name"));
##print(dic.items());

##Copy vs deepcopy
dic_copy=dic.copy();
print(dic_copy);
dic_copy["name"]="Xuan";
dic_copy["array"][0]=3;

print("Dic goc:",dic);
print("Dic Copy:",dic_copy);
print("===Deep===");
dic_Deep=deepcopy(dic);
print(dic_Deep);

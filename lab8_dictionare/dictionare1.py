
dict1 = {
    'Key1': 1,
    'Key2': {
        'key1': 1,
        'key2': ['element1', 'element2']
    }
    }

dict_nou = dict1['Key2']
print(dict1['Key2']['key2'][0]) #ca sa trec dintr un dict in altul, fac o noua var cu al doilea dict, iar atunci pot parcurge dict.

dict1['Key1'] = 2
print(dict1['Key1']) # Schimb valoarea

dict1['Key3'] = set()
print(dict1)   #asa adaug un element in dict

del dict1['Key2']
print(dict1) #asa sterg din dictionar.



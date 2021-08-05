import os
path_folder = os.path.join(os.getcwd(), 'ДЗ')
#print(path_folder)
list_doc = os.listdir(path_folder)
#print(list_doc)
document_length = dict()
for doc in list_doc:
    path_file = os.path.join(os.getcwd(), 'ДЗ', doc)
    with open(path_file, encoding='utf-8') as file:
        a = file.read().split('\n')
        document_length[doc] = [len(a), a]
sorted_doc = {}
sorted_keys = sorted(document_length, key=document_length.get)
for w in sorted_keys:
    sorted_doc[w] = document_length[w]
with open('result.txt', 'w', encoding='utf-8') as file:
    for key, value in sorted_doc.items():
        file.write(key + '\n')
        file.write(str(value[0]) + '\n')
        for v in value[1]:
            file.write(v + '\n')



#with open('result.txt', 'w', encoding='utf-8') as file:
    #for key, value in sorted_doc:



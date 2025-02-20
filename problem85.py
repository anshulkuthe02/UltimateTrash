name = ["Anne","Robert","Steven","Davidson","McLaren","David","Devon"]
n_ner = []
for i in name:
    if i.endswith('n') or i.endswith('N'):
        n_ner.append(i)
print(n_ner)
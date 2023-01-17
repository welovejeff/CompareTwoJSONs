import json

def compare_json(file1, file2, new_file):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        data1 = json.load(f1)
        data2 = json.load(f2)
        differences = {}
        for key in data1.keys():
            if data1[key] != data2.get(key):
                differences[key] = data2[key]
        with open(new_file, 'w') as f:
            for key in differences.keys():
                f.write('# ' + key + ': ' + json.dumps(differences[key]) + '\n')
            for key in data1.keys():
                if key not in differences.keys():
                    f.write(key + ': ' + json.dumps(data1[key]) + '\n')

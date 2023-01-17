import json

def compare_json(file1, file2, output_file):
    # load the two JSON files
    with open(file1, 'r') as f1:
        data1 = json.load(f1)
    with open(file2, 'r') as f2:
        data2 = json.load(f2)

    # compare the two JSON files
    differences = {}
    for key in data1:
        if key not in data2:
            differences[key] = data1[key]
        elif data1[key] != data2[key]:
            differences[key] = data1[key]

    for key in data2:
        if key not in data1:
            differences[key] = data2[key]

    # write the differences to the output file
    with open(output_file, 'w') as f:
        for key in differences:
            f.write('# ' + key + ': ' + str(differences[key]) + '\n')


compare_json('file1.json', 'file2.json', 'differences.json')

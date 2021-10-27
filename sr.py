lang_list_filename = 'rtype_list.csv'
people_output_filename = 'test_out.csv'
people_output_processed_filename = 'date_people_processed.csv'


lang_dict = {}
with open(lang_list_filename, 'r') as f:
    lines = f.readlines()
    for line in lines[1:]:
        tokens = line[:-1].split(',')
        id = tokens[0]
        lang = tokens[1]
        lang_dict[lang] = id

people_output = []
with open(people_output_filename, 'r') as f:
    lines = f.readlines()
    people_output.append(lines[0][:-1])
    for line in lines[1:]:
        tokens = line[:-1].split(',')
        tokens = [lang_dict[t] if len(t) > 0 else t for t in tokens]
        csv_tokens = ','.join(tokens)
        people_output.append(csv_tokens)

with open(people_output_processed_filename, 'w') as f:
    print('\n'.join(people_output), file=f)

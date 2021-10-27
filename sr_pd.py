import pandas as pd

lang_list_filename = 'Language_List.csv'
people_output_filename = 'people_output.csv'
people_output_processed_filename = 'people_output_processed.csv'

df_lang_list = pd.read_csv(lang_list_filename)
lang_to_id = dict(df_lang_list.to_numpy()[:, [1, 0]])
# print(df_lang_list.set_index('name').transpose().to_dict('str'))
# def get_id(name): return df_lang_list[df_lang_list['name'] == name].id.to_numpy()[0]

df_people_output = pd.read_csv(people_output_filename)
cols = df_people_output.columns.to_numpy()
replace_dict = dict(zip(cols, [lang_to_id for _ in range(len(cols))]))
print(df_people_output.replace(replace_dict))


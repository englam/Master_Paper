import json



with open("engalm2.json") as json_data:
    d = json.load(json_data)


print(d['bug_titls_list']['100'])
print(d['bug_content_list']['100'])
print(d['feedback_author_list']['100'])
print(d['feedback_content_list']['100'])
print(d['model_name_list']['100'])
print(d['price_list']['100'])
print(d['wireless_type_list']['100'])
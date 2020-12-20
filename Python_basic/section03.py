import json as simplejson

test_dict = {'1': 95, '4': 77, '3':65, '5':100, '2':88}

print(simplejson.dumps(test_dict, sort_keys=True, indent=4 * ' '))
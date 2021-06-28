Dict = [{'make':'Toyota', 'model':2575, 'color':'Grey'}, {'make':'Mi Max', 'model':'2', 'color':'Gold'}, {'make':'Samsung', 'model': 7, 'color':'Blue'}]

print("Orignal dictionary: \n", Dict , "\n")
sorted_dict = sorted(Dict, key = lambda x: x['color'])

print("sorted dictionary: \n", sorted_dict)
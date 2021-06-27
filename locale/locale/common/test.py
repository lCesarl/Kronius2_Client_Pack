import re
def load_blend():
	data = []
	with open("blend.txt", "r+") as file:
		lines = file.readlines()
	for i, line in enumerate(lines):
		if "section" in line:
			data.append([])	
		elif "item_vnum" in line or "apply_type" in line:
			data[len(data)-1].append(line.split()[1])
		elif "apply_value" in line:
			attr_value = []
			for value in line.split()[1:]:
				attr_value.append(value)
			data[len(data)-1].append(attr_value)
		elif "apply_duration" in line:
			times_in_seconds = []
			for time in line.split()[1:]:
				times_in_seconds.append(time)
			data[len(data)-1].append(times_in_seconds)
	return data
for d in load_blend():
	print(d)
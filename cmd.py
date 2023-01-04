
clss = "element_cell text_level_semantics"

l = "img area map embed object param source iframe canvas track* audio video device"

li = l.split(' ')

result = ""
for i in li:
	connect = f'<td><button class="{clss}">{i}</button></td>'

	result = result + "\n" + connect

print(result)
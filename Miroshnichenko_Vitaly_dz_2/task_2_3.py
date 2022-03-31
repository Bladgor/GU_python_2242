info_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
final_text = ''

for element in info_list[:]:
    if element.startswith('+'):
        info_list.extend(('"', f'+{int(element):02d}', '"'))
    elif element.isdigit() or element[-1].isdigit():
        info_list.extend(('"', f'{int(element):02d}', '"'))
    else:
        info_list.append(element)
    info_list.pop(0)

for elem in info_list:
    if elem == '"' or elem[-1].isdigit():
        final_text += elem
    else:
        final_text += f' {elem} '

final_text = (' '.join(final_text.split()))

print(info_list)
print(final_text)

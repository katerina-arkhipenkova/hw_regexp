import re
import csv

if __name__ == '__main__':
    with open("phonebook_raw.csv") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    for item in contacts_list:
        # имена и фамилии
        res = re.split(' ', item[0])
        if len(res) == 3:
            item[0] = res[0]
            item[1] = res[1]
            item[2] = res[2]
        if len(res) == 2:
            item[0] = res[0]
            item[1] = res[1]
        res = re.split(' ', item[1])
        if len(res) == 2:
            item[1] = res[0]
            item[2] = res[1]
        # телефоны
        pattern1 = r"(\+7|8)\s*\(?(\d{3})\)?(\s*|-)(\d{3})(\s*|-)(\d{2})(\s*|-)(\d{2})(\s\(?((?:доб\.)?)\s)?((?:\d{4})?)?\)?"
        pattern2 = r"+7(\2)\4-\6-\8 \g<10>\g<11>"
        item[5] = re.sub(pattern1, pattern2, item[5])
    # удаление совпадений
    i = 1
    for item in contacts_list:
        for itm in contacts_list[i:]:
            if item[0] == itm[0] and item[1] == itm[1]:
                for index in range(2, 7):
                    if item[index] == '':
                        item[index] = itm[index]
                contacts_list.remove(itm)
        i += 1
        print(item)

    with open("phonebook.csv", "w") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(contacts_list)

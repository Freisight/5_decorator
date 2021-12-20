import main3
import re
from pprint import pprint
import csv
import os

dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(dir)


with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

###### Поправить ФИО

fix_name = []
for item in contacts_list:
    # сначала все части ФИО соединяем в одно и потом делаим на части в списке
    full_name = ' '.join(item[:3]).split(' ')

    # теперь делаем новый список и на первые 3 позиции ставим части ФИО из списка, а на остальные позиции ставим остаточные данные из начальных данных.
    result = [full_name[0], full_name[1], full_name[2], item[3], item[4], item[5], item[6]]
    fix_name.append(result)


# print(fix_name[0])
# print(fix_name[5])


###### корректировка телефона
def fix_format_phonenumbers(contacts_list):
    PHONE_PATTERN = r'(8|\+7)?\s*(\(*)(\d{3})(\)*)(\s*|-)(\d{3})(\s*|-)(\d{2})(\s*|-)(\d{2})\s*(\(*)(\w\w\w\.)*\s*(\d{4})*(\))*'
    PHONE_SUB = r'+7(\3)\6-\8-\10 \12\13'

    for item in contacts_list:
        item[5] = re.sub(PHONE_PATTERN, PHONE_SUB, item[5])


fix_format_phonenumbers(fix_name)


###### удаление дубликатов и соединение информации
@main3.param_decorator('/Users/sergejpetrov/desktop/1')
def delete_duplicates_contact(new_contacts_list):
    phone_book = dict()
    for contact in new_contacts_list:
        if contact[0] in phone_book:
            contact_value = phone_book[contact[0]]
            for i in range(len(contact_value)):
                if contact[i]:
                    contact_value[i] = contact[i]
        else:
            phone_book[contact[0]] = contact
    return list(phone_book.values())


end_list = delete_duplicates_contact(fix_name)

with open("phonebook.csv", "w",encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(end_list)
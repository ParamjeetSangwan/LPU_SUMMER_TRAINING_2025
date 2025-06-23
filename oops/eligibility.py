from MyExceptions.custom_exception import AgelimitError



per_name=input('Name : ')
per_age=int(input('Age : '))

try:
    if per_age < 18:
        raise AgelimitError('Not Eligible')
except AgelimitError as ale:
    print(ale)
else:
     print('Eligible !!')
finally:
    print('Finally !!')
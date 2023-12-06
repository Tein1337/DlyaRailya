from django.shortcuts import render


def index(request):
    header = 'Данные пользователя'
    langs = ['C', 'C++', 'Python', 'Java', 'JavaScript', 'Pascal']
    user = {'name': 'Vasilii', 'surname': 'Pupkin'}
    address = ('Mira', 12, 147)
    text = '<h4>My Text</h4>'

    data = {'header': header, 'langs': langs, 'user': user, 'address': address, 'text': text}
    return render(request, 'shop/index.html', context=data)

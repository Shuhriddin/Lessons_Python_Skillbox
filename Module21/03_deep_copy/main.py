site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}

# TODO здесь писать код

def deep_copy(struct):
    if isinstance(struct, dict):
        new_struct = {}
        for key, value in struct.items():
            new_struct[key] = deep_copy(value)
        return new_struct
    else:
        return struct

num_sites = int(input('Сколько сайтов: '))
sites = []

for i in range(num_sites):
    product_name = input('Введите название продукта для нового сайта: ')
    new_site = deep_copy(site)
    new_site['html']['head']['title'] = f'Куплю/продам {product_name} недорого'
    new_site['html']['body']['h2'] = f'У нас самая низкая цена на {product_name}'
    sites.append(new_site)

    print(f'Сайт для {product_name}:')
    print(new_site)
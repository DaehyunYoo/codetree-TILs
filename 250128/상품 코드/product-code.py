class result:
    def __init__(self, name='codetree', code=50):
        self.name = name
        self.code = code

result1 = result()
print(f'product {result1.code} is {result1.name}')

new_name, new_code = input().split()
result2 = result(new_name, new_code)
print(f'product {result2.code} is {result2.name}')
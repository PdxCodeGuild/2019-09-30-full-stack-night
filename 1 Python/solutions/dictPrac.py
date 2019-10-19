# practice problem: 1
def combine_lists(list_1, list_2):
    # combined = {}
    # for i in range(len(list_1)):
    #     combined.update({list_1[i]: list_2[i]})
    # return combined

    # or, as a comprehension:
    return {list_1[i]: list_2[i] for i in range(len(list_1))}

fruits = ['apple', 'banana', 'pear']
prices = [1.2, 3.3, 2.1]

print(combine_lists(fruits, prices))


# practice problem: 1 using zip()
def combine_lists_zip(list_1, list_2):
    return dict(zip(fruits, prices))

print(combine_lists_zip(fruits, prices))



# practice problem: 2
item_price_dict = combine_lists(fruits, prices)

def calc_avg_price(a_dict):
    avg_price = 0
    prices = a_dict.values()
    for price in prices:
        avg_price += price / len(prices)
    return round(avg_price, 2)

print(calc_avg_price(item_price_dict))


# # practice problem 3
import string  

d = {'a1':5, 'a2':2, 'a3':3, 'b1':10, 'b2':1, 'b3':1, 'c1':4, 'c2':5, 'c3':6, 'm1':7, 'm2': 7, 'm3': 5}

def unify(a_dict):
    results = {}
    for letter in string.ascii_lowercase:
        count = 0
        total = 0
        for key in a_dict:
            if not key.startswith(letter):
                continue
            count += 1
            total += a_dict[key]
            results.update({letter: round(total / count)})
    return results

print(unify(d))
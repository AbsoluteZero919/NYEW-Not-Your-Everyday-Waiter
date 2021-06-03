import pandas as pd
from apyori import apriori
# from utilities.convert_list_to_string import listToString

def apriori_algorithm(str_item):
    dataset = pd.read_csv('datasets/Recommendations_menu.csv', header=None)
    basket = []
    # Outer for loop to iterate through no. of rows, inner for loop to iterate through no. of cols
    for i in range(len(dataset.index)):
        basket.append([str(dataset.values[i, j]) for j in range(0, 8)])

    # min_support = mininum frequency / total no. of transactions
    rules = apriori(transactions = basket, min_support = 0.05, min_confidence = 0.4, min_lift = 2, min_length = 2, max_length = 2)

    results = list(rules)

    # print(results)

    def inspect(results):
        lhs = [tuple(result[2][0][0])[0] for result in results]
        rhs = [tuple(result[2][0][1])[0] for result in results]
        supports = [result[1] for result in results]
        confidences = [result[2][0][2] for result in results]
        lifts = [result[2][0][3] for result in results]
        return list(zip(lhs, rhs, supports, confidences, lifts))

    resultsinDataFrame = pd.DataFrame(inspect(results),
                                      columns=['Left Hand Side', 'Right Hand Side', 'Support', 'Confidence', 'Lift'])

    # print unsorted rules
    # print(resultsinDataFrame)

    # print sorted rules according to confidence
    res = resultsinDataFrame.nlargest(n=15, columns='Confidence')
    # print(res)




    lis = []
    # str_item = 'Chicken Nuggets'
    res_left = res.loc[(res['Left Hand Side'] == str_item)]
    if res_left.empty:
        #     print("empty")
        res_right = res.loc[(res['Right Hand Side'] == str_item)]
        if res_right.empty:
            # print("empty")
            pass
        else:
            lis = res_right.iloc[:, 0]
    else:
        lis = res_left.iloc[:, 1]

    # recommend = "People who ordered " + str_item + " also ordered " + listToString(lis)

    return lis


# ghj = apriori_algorithm('Chicken Nuggets')
# print(ghj)
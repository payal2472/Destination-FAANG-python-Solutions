#121. Best Time to Buy and Sell Stock
#You are given an array prices where prices[i] is the price of a given stock on the ith day.
#You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.


def reverse_array_extra_array(arr):
    reversed_arr = arr[::-1]

    # Print reversed array
    print("Reversed Array:", end=" ")
    for i in reversed_arr:
        print(i, end=" ")

# Example usage:
original_arr = [1, 2, 3, 4, 5]
reverse_array_extra_array(original_arr)

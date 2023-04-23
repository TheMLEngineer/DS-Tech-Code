-- Define a function to calculate the sum of squares of even numbers
sum_of_squares_even :: [Int] -> Int
sum_of_squares_even xs = sum (map (^2) (filter even xs))

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print (sum_of_squares_even numbers) -- Output: 120

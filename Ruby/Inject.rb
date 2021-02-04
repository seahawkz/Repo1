fruits = ['apple', 'banana', 'pear']

size = fruits.inject(0) do |memo, fruit|
    memo + fruit.length
end
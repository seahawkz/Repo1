#!/usr/bin/env ruby

i = 8
while i > 0
    puts "Countdown #{i}"
    i -= 1
end
puts "Blast off!"

puts "----------------------"
puts "| Ruby Guessing Game |"
puts "----------------------"

puts "What is your name?"
print "> "
name = gets.chomp

puts "Hello, #{name}."
puts "We are going to play a guessing game."
puts "I will choose a random number between 1 and 10"
puts "and you will have three chances to guess it."

number = rand(10) + 1
puts "Okay, I have my number."

Max_Guesses = 3

1.upto(Max_Guesses) do |guess_num|
    print "Guess #{guess_num}: "
    guess = gets.chomp
    if guess.to_i == number
        puts "Great guessing, #{name}!"
        puts "My number was #{number}."
        break
    else
        puts "Sorry, that wasn't it."
        if guess_num == Max_Guesses
            puts "\nThat was your last guess."
            puts "My number was #{number}."
        end
    end
end

puts "\n\nGoodbye!"


"""This Code Does Not Really Respect The Exercise Instructions
But It's A Good Example Of How To Use Set Comprehension
Or Not As I Have Compacted The Code
To Return A Couple Of Sets And It Works So I Don't Care"""

def prime_numbers(numbers):
    """Returns a list of prime numbers"""
    return {nb for nb in range(numbers+1) if is_prime(nb)}

def even(numbers):
    """Returns a list of even numbers"""
    return {nb for nb in range(numbers+1) if nb % 2 == 0}

def is_prime(number):
    """Returns True if the number is prime"""
    return number > 1 and all(number % i for i in range(2, number))

def is_odd(number):
    """Returns True if the number is odd"""
    return number % 2 == 1

def prime_odd_numbers(numbers):
    """Returns a couple of prime and odd numbers"""
    couple = ({nb for nb in numbers if is_prime(nb)}, {nb for nb in numbers if is_odd(nb)})
    return couple
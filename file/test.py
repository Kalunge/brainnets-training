# 4. 

# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.


def count_letters(n):
    """Count the number of letters in a number written out in words."""
    if n == 0:
        return 0
    if n < 20:
        return len(ones[n])
    if n < 100:
        return len(tens[n // 10]) + count_letters(n % 10)
    if n < 1000:
        return len(ones[n // 100]) + len('hundred') + (3 if n % 100 != 0 else 0) + count_letters(n % 100)
    return len('onethousand')
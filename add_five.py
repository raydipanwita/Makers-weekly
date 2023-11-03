def add_five(num):
    print(f"I have received {num}")
    num_after_adding = num + 5
    print(f"I have calculated {num} + 5 = {num_after_adding}")
    return num_after_adding

result = add_five(23)
result1 = add_five(result)
result2 = add_five(result1)
print(result)


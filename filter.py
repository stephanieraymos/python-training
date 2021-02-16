ages = [1, 25, 28, 15, 35]

def function(x):
    if x < 18:
        return False
    else:
        return True

adults = filter(function, ages)

for x in adults: 
    print(x)

# Results: 25 28 35
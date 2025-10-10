# if condition:
#     # code to execute if condition is true

age = 18

if age >= 18:
    print("You are an adult.")
elif age == 17:
    print("You are almost an adult.")
else:
    print("You are a minor.")

# nested if
if age >= 18:
    if age >= 21:
        print("You can drink alcohol in the US.")
    else:
        print("You are an adult but cannot drink alcohol in the US.")

# logical operators
if age >= 18 and age < 21:
    print("You are an adult but didn't graduate the university.")


if age < 18 or age == 18:
    print("You are a minor.")
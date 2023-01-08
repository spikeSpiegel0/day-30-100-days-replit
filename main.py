print("30 days down - What did you think?")
print()
for i in range(1, 31):
  q = input(f"""Day {i} : 
  """)
  print()
  response = f"You thought day {i: ^3} was"
  print(f"{response: ^30}")
  print(f"{q: ^30}")
  print()
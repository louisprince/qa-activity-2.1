def evaluate_temperature(temperature: int) -> str:
  if temperature > 30 < 40:
    return "It's hot"
  elif temperature > 10 < 30:
    return "It's nice out"
  elif temperature > -20 < 10:
    return "It's cold"
  else:
    raise Exception("It appears something strange is happening with the weather")

print(evaluate_temperature(35))  # Should print "It's hot"
print(evaluate_temperature(25))  # Should print "It's nice out"
print(evaluate_temperature(7))  # Should print "It's cold"
print(evaluate_temperature(-100))  # Should raise an exception
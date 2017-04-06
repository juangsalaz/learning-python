def secret_message(string):
  return "".join(c for c in string if c.isupper())

print(secret_message('hello world!'))

def format_address(address_string):
  # Declare variables
   house_number = ''
   street = ''
  # Separate the address string into parts
   string = address_string.split()
  # Traverse through the address parts
   house_number = string[0]
   street = (' '.join(string[1:]))
  
  # Return the formatted string  
   return "house number {} on street named {}".format(house_number, street)

print(format_address("123 Main Street"))
# Print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Print "house number 55 on street named North Center Drive"

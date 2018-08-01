### creating a rainbow table
- generate all 8-character, lowercase letter combinations from a-z with `itertools.product`
- iterate throught the generated characters, and make each combination to a single string keyword
- i'm using python 3, so i need to cast string keyword to bytestring first before hashing it to md5 hash object
- hash the keyword to md5 without salt
- encrypt the md5 hash object to hex with `hexdigest()`
- write out the hashes to file with its original keyword

### reversing hashes to original password
to reverse hashes to its original keyword, 
- we only need to search through our generated rainbow table, 
- and find if it matches the given hash.
- if it does, then the equivalent keyword of that hash on the rainbow table is the original password
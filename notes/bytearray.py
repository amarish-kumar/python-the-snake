Help on class bytearray in module __builtin__:

class bytearray(object)
 |  bytearray(iterable_of_ints) -> bytearray.
 |  bytearray(string, encoding[, errors]) -> bytearray.
 |  bytearray(bytes_or_bytearray) -> mutable copy of bytes_or_bytearray.
 |  bytearray(memory_view) -> bytearray.
 |  
 |  Construct a mutable bytearray object from:
 |    - an iterable yielding integers in range(256)
 |    - a text string encoded using the specified encoding
 |    - a bytes or a bytearray object
 |    - any object implementing the buffer API.
 |  
 |  bytearray(int) -> bytearray.
 |  
 |  Construct a zero-initialized bytearray of the given length.
 |  
 |  Methods defined here:
 |  
 |  __add__(...)
 |      x.__add__(y) <==> x+y
 |  
 |  __alloc__(...)
 |      B.__alloc__() -> int
 |      
 |      Returns the number of bytes actually allocated.
 |  
 |  __contains__(...)
 |      x.__contains__(y) <==> y in x
 |  
 |  __delitem__(...)
 |      x.__delitem__(y) <==> del x[y]
 |  
 |  __eq__(...)
 |      x.__eq__(y) <==> x==y
 |  
 |  __ge__(...)
 |      x.__ge__(y) <==> x>=y
 |  
 |  __getattribute__(...)
 |      x.__getattribute__('name') <==> x.name
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(...)
 |      x.__gt__(y) <==> x>y
 |  
 |  __iadd__(...)
 |      x.__iadd__(y) <==> x+=y
 |  
 |  __imul__(...)
 |      x.__imul__(y) <==> x*=y
 |  
 |  __init__(...)
 |      x.__init__(...) initializes x; see help(type(x)) for signature
 |  
 |  __iter__(...)
 |      x.__iter__() <==> iter(x)
 |  
 |  __le__(...)
 |      x.__le__(y) <==> x<=y
 |  
 |  __len__(...)
 |      x.__len__() <==> len(x)
 |  
 |  __lt__(...)
 |      x.__lt__(y) <==> x<y
 |  
 |  __mul__(...)
 |      x.__mul__(n) <==> x*n
 |  
 |  __ne__(...)
 |      x.__ne__(y) <==> x!=y
 |  
 |  __reduce__(...)
 |      Return state information for pickling.
 |  
 |  __repr__(...)
 |      x.__repr__() <==> repr(x)
 |  
 |  __rmul__(...)
 |      x.__rmul__(n) <==> n*x
 |  
 |  __setitem__(...)
 |      x.__setitem__(i, y) <==> x[i]=y
 |  
 |  __sizeof__(...)
 |      B.__sizeof__() -> int
 |       
 |      Returns the size of B in memory, in bytes
 |  
 |  __str__(...)
 |      x.__str__() <==> str(x)
 |  
 |  append(...)
 |      B.append(int) -> None
 |      
 |      Append a single item to the end of B.
 |  
 |  capitalize(...)
 |      B.capitalize() -> copy of B
 |      
 |      Return a copy of B with only its first character capitalized (ASCII)
 |      and the rest lower-cased.
 |  
 |  center(...)
 |      B.center(width[, fillchar]) -> copy of B
 |      
 |      Return B centered in a string of length width.  Padding is
 |      done using the specified fill character (default is a space).
 |  
 |  count(...)
 |      B.count(sub [,start [,end]]) -> int
 |      
 |      Return the number of non-overlapping occurrences of subsection sub in
 |      bytes B[start:end].  Optional arguments start and end are interpreted
 |      as in slice notation.
 |  
 |  decode(...)
 |      B.decode([encoding[, errors]]) -> unicode object.
 |      
 |      Decodes B using the codec registered for encoding. encoding defaults
 |      to the default encoding. errors may be given to set a different error
 |      handling scheme.  Default is 'strict' meaning that encoding errors raise
 |      a UnicodeDecodeError.  Other possible values are 'ignore' and 'replace'
 |      as well as any other name registered with codecs.register_error that is
 |      able to handle UnicodeDecodeErrors.
 |  
 |  endswith(...)
 |      B.endswith(suffix [,start [,end]]) -> bool
 |      
 |      Return True if B ends with the specified suffix, False otherwise.
 |      With optional start, test B beginning at that position.
 |      With optional end, stop comparing B at that position.
 |      suffix can also be a tuple of strings to try.
 |  
 |  expandtabs(...)
 |      B.expandtabs([tabsize]) -> copy of B
 |      
 |      Return a copy of B where all tab characters are expanded using spaces.
 |      If tabsize is not given, a tab size of 8 characters is assumed.
 |  
 |  extend(...)
 |      B.extend(iterable int) -> None
 |      
 |      Append all the elements from the iterator or sequence to the
 |      end of B.
 |  
 |  find(...)
 |      B.find(sub [,start [,end]]) -> int
 |      
 |      Return the lowest index in B where subsection sub is found,
 |      such that sub is contained within B[start,end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Return -1 on failure.
 |  
 |  fromhex(...)
 |      bytearray.fromhex(string) -> bytearray
 |      
 |      Create a bytearray object from a string of hexadecimal numbers.
 |      Spaces between two numbers are accepted.
 |      Example: bytearray.fromhex('B9 01EF') -> bytearray(b'\xb9\x01\xef').
 |  
 |  index(...)
 |      B.index(sub [,start [,end]]) -> int
 |      
 |      Like B.find() but raise ValueError when the subsection is not found.
 |  
 |  insert(...)
 |      B.insert(index, int) -> None
 |      
 |      Insert a single item into the bytearray before the given index.
 |  
 |  isalnum(...)
 |      B.isalnum() -> bool
 |      
 |      Return True if all characters in B are alphanumeric
 |      and there is at least one character in B, False otherwise.
 |  
 |  isalpha(...)
 |      B.isalpha() -> bool
 |      
 |      Return True if all characters in B are alphabetic
 |      and there is at least one character in B, False otherwise.
 |  
 |  isdigit(...)
 |      B.isdigit() -> bool
 |      
 |      Return True if all characters in B are digits
 |      and there is at least one character in B, False otherwise.
 |  
 |  islower(...)
 |      B.islower() -> bool
 |      
 |      Return True if all cased characters in B are lowercase and there is
 |      at least one cased character in B, False otherwise.
 |  
 |  isspace(...)
 |      B.isspace() -> bool
 |      
 |      Return True if all characters in B are whitespace
 |      and there is at least one character in B, False otherwise.
 |  
 |  istitle(...)
 |      B.istitle() -> bool
 |      
 |      Return True if B is a titlecased string and there is at least one
 |      character in B, i.e. uppercase characters may only follow uncased
 |      characters and lowercase characters only cased ones. Return False
 |      otherwise.
 |  
 |  isupper(...)
 |      B.isupper() -> bool
 |      
 |      Return True if all cased characters in B are uppercase and there is
 |      at least one cased character in B, False otherwise.
 |  
 |  join(...)
 |      B.join(iterable_of_bytes) -> bytes
 |      
 |      Concatenates any number of bytearray objects, with B in between each pair.
 |  
 |  ljust(...)
 |      B.ljust(width[, fillchar]) -> copy of B
 |      
 |      Return B left justified in a string of length width. Padding is
 |      done using the specified fill character (default is a space).
 |  
 |  lower(...)
 |      B.lower() -> copy of B
 |      
 |      Return a copy of B with all ASCII characters converted to lowercase.
 |  
 |  lstrip(...)
 |      B.lstrip([bytes]) -> bytearray
 |      
 |      Strip leading bytes contained in the argument.
 |      If the argument is omitted, strip leading ASCII whitespace.
 |  
 |  partition(...)
 |      B.partition(sep) -> (head, sep, tail)
 |      
 |      Searches for the separator sep in B, and returns the part before it,
 |      the separator itself, and the part after it.  If the separator is not
 |      found, returns B and two empty bytearray objects.
 |  
 |  pop(...)
 |      B.pop([index]) -> int
 |      
 |      Remove and return a single item from B. If no index
 |      argument is given, will pop the last value.
 |  
 |  remove(...)
 |      B.remove(int) -> None
 |      
 |      Remove the first occurrence of a value in B.
 |  
 |  replace(...)
 |      B.replace(old, new[, count]) -> bytes
 |      
 |      Return a copy of B with all occurrences of subsection
 |      old replaced by new.  If the optional argument count is
 |      given, only the first count occurrences are replaced.
 |  
 |  reverse(...)
 |      B.reverse() -> None
 |      
 |      Reverse the order of the values in B in place.
 |  
 |  rfind(...)
 |      B.rfind(sub [,start [,end]]) -> int
 |      
 |      Return the highest index in B where subsection sub is found,
 |      such that sub is contained within B[start,end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Return -1 on failure.
 |  
 |  rindex(...)
 |      B.rindex(sub [,start [,end]]) -> int
 |      
 |      Like B.rfind() but raise ValueError when the subsection is not found.
 |  
 |  rjust(...)
 |      B.rjust(width[, fillchar]) -> copy of B
 |      
 |      Return B right justified in a string of length width. Padding is
 |      done using the specified fill character (default is a space)
 |  
 |  rpartition(...)
 |      B.rpartition(sep) -> (head, sep, tail)
 |      
 |      Searches for the separator sep in B, starting at the end of B,
 |      and returns the part before it, the separator itself, and the
 |      part after it.  If the separator is not found, returns two empty
 |      bytearray objects and B.
 |  
 |  rsplit(...)
 |      B.rsplit(sep[, maxsplit]) -> list of bytearray
 |      
 |      Return a list of the sections in B, using sep as the delimiter,
 |      starting at the end of B and working to the front.
 |      If sep is not given, B is split on ASCII whitespace characters
 |      (space, tab, return, newline, formfeed, vertical tab).
 |      If maxsplit is given, at most maxsplit splits are done.
 |  
 |  rstrip(...)
 |      B.rstrip([bytes]) -> bytearray
 |      
 |      Strip trailing bytes contained in the argument.
 |      If the argument is omitted, strip trailing ASCII whitespace.
 |  
 |  split(...)
 |      B.split([sep[, maxsplit]]) -> list of bytearray
 |      
 |      Return a list of the sections in B, using sep as the delimiter.
 |      If sep is not given, B is split on ASCII whitespace characters
 |      (space, tab, return, newline, formfeed, vertical tab).
 |      If maxsplit is given, at most maxsplit splits are done.
 |  
 |  splitlines(...)
 |      B.splitlines(keepends=False) -> list of lines
 |      
 |      Return a list of the lines in B, breaking at line boundaries.
 |      Line breaks are not included in the resulting list unless keepends
 |      is given and true.
 |  
 |  startswith(...)
 |      B.startswith(prefix [,start [,end]]) -> bool
 |      
 |      Return True if B starts with the specified prefix, False otherwise.
 |      With optional start, test B beginning at that position.
 |      With optional end, stop comparing B at that position.
 |      prefix can also be a tuple of strings to try.
 |  
 |  strip(...)
 |      B.strip([bytes]) -> bytearray
 |      
 |      Strip leading and trailing bytes contained in the argument.
 |      If the argument is omitted, strip ASCII whitespace.
 |  
 |  swapcase(...)
 |      B.swapcase() -> copy of B
 |      
 |      Return a copy of B with uppercase ASCII characters converted
 |      to lowercase ASCII and vice versa.
 |  
 |  title(...)
 |      B.title() -> copy of B
 |      
 |      Return a titlecased version of B, i.e. ASCII words start with uppercase
 |      characters, all remaining cased characters have lowercase.
 |  
 |  translate(...)
 |      B.translate(table[, deletechars]) -> bytearray
 |      
 |      Return a copy of B, where all characters occurring in the
 |      optional argument deletechars are removed, and the remaining
 |      characters have been mapped through the given translation
 |      table, which must be a bytes object of length 256.
 |  
 |  upper(...)
 |      B.upper() -> copy of B
 |      
 |      Return a copy of B with all ASCII characters converted to uppercase.
 |  
 |  zfill(...)
 |      B.zfill(width) -> copy of B
 |      
 |      Pad a numeric string B with zeros on the left, to fill a field
 |      of the specified width.  B is never truncated.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __new__ = <built-in method __new__ of type object>
 |      T.__new__(S, ...) -> a new object with type S, a subtype of T


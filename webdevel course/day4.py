def is_roman(n):
   pattern = re.compile("""
   ^                   # beginning of string
   ([0-4]\d{3})        # thousands - 0 to 4 M's
   ((900),(400),[0-3]\d{2}|500[0-3]\d{2})  # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 C's),
                       #            or 500-800 (D, followed by 0 to 3 C's)
   (90),(40),[0-3]\d{1},(50)\d[0-3]{1}                   # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 X's),
                       #        or 50-80 (L, followed by 0 to 3 X's)
                       # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 I's),
                       #        or 5-8 (V, followed by 0 to 3 I's)
   $                   # end of string
   """, re.VERBOSE)
   return (re.search(pattern, n) is not None)

pattern = re.compile("""
(|1|-|work)                # don't match beginning of string, number can start anywhere
[0-4]\d{2}      # area code is 3 digits (e.g. '800')
(?.|\s)        # optional separator is any number of non-digits
\d{3}           # trunk is 3 digits (e.g. '555')
(?.|\s)         # optional separator
\d{4}           # rest of number is 4 digits (e.g. '1212')
(?.|\s)         # optional separator
\d*             # extension is optional and can be any number of digits
    $           # end of string
    """, re.VERBOSE)
    return re.search(pattern, n)


>>> fix_latin1(u"la cÃ¡ntara, el escocÃ©s, el maniquÃ­, el caÃ±Ã³n, KatmandÃº")
"la cántara, el escocés, el maniquí, el cañón, Katmandú"
HINT: Take a look on the function re.sub


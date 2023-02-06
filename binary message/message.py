from ntpath import join


print (lambda x: join(format(ord(c),"07b") for c in x+repr((x,))))('print (lambda x:.join(format(ord(c),"07b") for c in x+repr((x,))))',)
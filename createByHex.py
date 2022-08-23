#info -> https://www.utf8-chartable.de/unicode-utf8-table.pl?start=65024&utf8=string-literal
base = "efb88"

for i in range(16):
    h = str(base + str(hex(i).replace("0x","")))
    print(h,":",bytes.fromhex(h).decode('utf-8'))
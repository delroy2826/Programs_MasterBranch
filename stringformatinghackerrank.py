n = 17
a=len(bin(n)[2:])
for i in range(1,n+1):
    print("{}".format(i).rjust(a),oct(i)[2:].rjust(a),hex(i)[2:].capitalize().rjust(a),bin(i)[2:].rjust(a))
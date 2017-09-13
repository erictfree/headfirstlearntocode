eighties = ['', 'duran duran', 'B-52s', 'muse']
newwave = ['flock of seagulls', 'postal service']

remember = eighties[1]
print(eighties, remember)
eighties[1] = 'culture club'
print(eighties, remember)
band = newwave[0]
print(eighties, remember, band)
eighties[3] = band
print(eighties, remember, band)
eighties[0] = eighties[2]
print(eighties, remember, band)
eighties[2] = remember
print(eighties, remember, band)
print(eighties)
print(eighties)

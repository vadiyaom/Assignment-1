# Write a lambda function to convert a list of song titles from Spotify to all lowercase letters and use map() to apply it to ['Shape Of You', 'Blinding Lights', 'Levitating', 'Senorita'], printing the cleaned list.

l = ['Shape Of You', 'Blinding Lights', 'Levitating', 'Senorita']

l_1 = list(map(lambda x: x.lower(), l))
print(l_1)
import hashlib



class Gerar:

     def fatiar(self, *string):
         save = open("lista.txt", "wb")
         for ax in range(len(string)):
             p_a = string[ax]
             for a in range(len(p_a)):
                 if a % 2 != 0:
                     save.write(str(p_a[a].upper()).encode())
                 else:
                     save.write(str(p_a[a]).encode())
             for b in range(len(p_a)):
                 if b % 2 == 0:
                     save.write(str(p_a[b].upper()).encode())
                 else:
                     save.write(str(p_a[b]).encode())
             for p1 in range(len(p_a)):
                 xx = p_a[p1:len(p_a) + 1]
                 yy = p_a[0:p1].upper()
                 juntar = "{}{}".format(yy, xx)
                 save.write(str(juntar).encode())

             for p1 in range(len(p_a)):
                 xx_x = p_a[p1:len(p_a)+1].upper()
                 yy_y = p_a[0:p1].lower()
                 juntar_xy = "{}{}".format(yy_y, xx_x)
                 save.write(str(juntar_xy).encode())







if __name__ == '__main__':
    tupla = "test\n", "teste\n", "testes\n"

    Gerar().fatiar(*tuple(tupla))
    infeite = "String                      Hashs"
    print(infeite)
    for i in open('lista.txt'):
        sha = str(i.strip("\n"))
        coda = hashlib.sha224(sha.encode())
        comparar = coda.hexdigest()

        if comparar in comparar:

            print(sha, " = ", comparar)

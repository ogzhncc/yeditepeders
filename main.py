yas = int(input('Yaşınız: '))
note = int(input('Notunuz: '))

if yas < 20:
    print("Yaşınız işe alım için uygun değil.")
elif note < 50:
    print("Notunuz işe alım için uygun değil.")
else:
    print("İşe alım için uygun şartlara sahipsiniz.")
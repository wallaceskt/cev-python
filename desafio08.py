num = float(input("Número: "))

# km    | hm   | dam | m | dm | cm  | mm
# 000.1 | 00.1 | 0.1 | 1 | 10 | 100 | 1000

km = num * 0.001
hm = num * 0.01
dam = num * 0.1
dm = num * 10
cm = num * 100
mm = num * 1000

print("{} m convertido(s) em quilômetros(s) é {:.3f}.".format(num, km))
print("{} m convertido(s) em hecômetros(s) é {:.2f}.".format(num, hm))
print("{} m convertido(s) em decâmetros(s) é {:.1f}.".format(num, dam))
print("{} m convertido(s) em decímetro(s) é {:.0f}.".format(num, dm))
print("{} m convertido(s) em centímetro(s) é {:.0f}.".format(num, cm))
print("{} m convertido(s) em milímetro(s) é {:.0f}.".format(num, mm))
medida = float(input('Uma distância em metros: '))
km = medida / 1000
hm = medida / 100
dam = medida / 10
m = medida * 1
dm = medida * 10
cm = medida * 100
mm = medida * 1000

print('A media de {}m corresponde a {}km\n{}hm\n{}dam\n{}m\n{}dm\n{}cm\n{}mm'.format(m, km, hm, dam, m, dm, cm, mm))
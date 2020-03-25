from math import sqrt

X = [28, 34, 39, 41, 46, 49, 53, 58, 61]
Y = [40, 51, 52, 55, 53, 60, 65, 67, 78]

alfa = 0.05

# Tamanho da Amostra:
n = len(X)

# Somatórios que serão usados em todas as demais fórmulas:
somatorio_xi_yi = round(sum([xi * yi for xi, yi in zip(X, Y)]), 4)
somatorio_xi = round(sum(X), 4)
somatorio_yi = round(sum(Y), 4)
somatorio_quadrado_xi = round(sum([xi**2 for xi in X]), 4)
somatorio_quadrado_yi = round(sum([yi**2 for yi in Y]), 4)

# Médias:
media_x = round(somatorio_xi / n, 4)
media_y = round(somatorio_yi / n, 4)

print("Tamanho da Amostra: n =", n)
print("Σxi*yi =", somatorio_xi_yi) 
print("Σxi =", somatorio_xi) 
print("Σyi =", somatorio_yi) 
print("Σxi² =", somatorio_quadrado_xi) 
print("Σyi² =", somatorio_quadrado_yi) 
print("(Σxi)² =", somatorio_xi**2) 
print("(Σyi)² =", somatorio_yi**2) 

# Correlação Linear de Pearson:
r = round((n*somatorio_xi_yi - somatorio_xi*somatorio_yi) / (sqrt(n*somatorio_quadrado_xi - somatorio_xi**2) * sqrt(n*somatorio_quadrado_yi - somatorio_yi**2)), 4)
print("\nCorrelação Linear de Pearson: r =", r)

print("\nTESTE DE SIGNIFICÂNCIA PARA O COEFICIENTE DE CORRELAÇÂO DE PEARSON:")
tc = round(r * sqrt((n - 2) / (1 - r**2)), 4)
print("Estatística de Teste: tc =", tc)

print("\nREGRESSÃO LINEAR SIMPLES:")
Sxx = (n*somatorio_quadrado_xi - somatorio_xi**2)/n
Sxx = round(Sxx, 4)
Syy = (n*somatorio_quadrado_yi - somatorio_yi**2)/n
Syy = round(Syy, 4)
Sxy = (n*somatorio_xi_yi - somatorio_xi*somatorio_yi)/n
Sxy = round(Sxy, 4)
print("Sxx =", Sxx)
print("Syy =", Syy)
print("Sxy =", Sxy)

print("\nPârametros da Regresão:")
beta_1 = round(Sxy/Sxx, 4)
beta_0 = round((somatorio_yi - beta_1*somatorio_xi)/n, 4)
print("^β1 =", beta_1)
print("^β0 =", beta_0)

SQTotal = Syy
SQRes = round(SQTotal - beta_1*Sxy, 4)
SQReg = round(SQTotal - SQRes, 4)
QMRes = round(SQRes/(n-2), 4)
print("\nSoma dos Quadrados Total (Variabilidade Total): SQTotal =", SQTotal)
print("Soma de Quadrados dos Resíduos (Variabilidade Não Explicada): SQRes =", SQRes)
print("Soma de Quadrados da Regressão: SQReg =", SQReg)
print("Variância Residual Populacional (ou Quadrado Médio dos Resíduos): QMRes = σres² =", QMRes)

RQuadrado = round(SQReg/SQTotal, 4)
RQuadrado_ajustado = 1 - ((n-1)/(n-2))*(1-RQuadrado)
RQuadrado_ajustado = round(RQuadrado_ajustado, 4)
print("\nCoeficiente de Determinação:", RQuadrado)
print("Coeficiente de Determinação Ajustado:", RQuadrado_ajustado)

print("\nIntervalos de Confiança para os Coeficientes da Regressão:")
IC_beta_1_sqrt = round(sqrt(QMRes/Sxx), 4)
print(
    "IC(" + str(1-alfa) + ")(β1) =",
    "[",
    str(beta_1) + " - " + "t(" + str(n-2) + ";" + str(alfa/2) + ")*" + str(IC_beta_1_sqrt),
    ";",
    str(beta_1) + " + " + "t(" + str(n-2) + ";" + str(alfa/2) + ")*" + str(IC_beta_1_sqrt),
    "]"
)
IC_beta_0_sqrt = round(sqrt( QMRes * ( (1/n) + ( (media_x**2)/Sxx ))), 4)
print(
    "IC(" + str(1-alfa) + ")(β0) =",
    "[",
    str(beta_0) + " - " + "t(" + str(n-2) + ";" + str(alfa/2) + ")*" + str(IC_beta_0_sqrt),
    ";",
    str(beta_0) + " + " + "t(" + str(n-2) + ";" + str(alfa/2) + ")*" + str(IC_beta_0_sqrt),
    "]"
)

print("\nIntervalo de Confiança para a Resposta Média de um Modelo de Regressão Linear Simples:")
somatorio_quadrado_de_xi_menos_mediax = round(sum([(xi - media_x)**2 for xi in X]), 4)

for x0 in X:
    IC_Y_x0_sqrt = sqrt(QMRes * ((1/n) + (((x0-media_x)**2)/(somatorio_quadrado_de_xi_menos_mediax))))
    IC_Y_x0_sqrt = round(IC_Y_x0_sqrt, 4)
    print(
        "IC(" + str(1-alfa) + ")(Y|x0=" + str(x0) + ") =",
        "[",
        str(beta_0) + "+" + str(beta_1) + "*" + str(x0) + " - " + "t(" + str(n-2) + ";" + str(alfa/2) + ")*" + str(IC_Y_x0_sqrt),
        ";",
        str(beta_0) + "+" + str(beta_1) + "*" + str(x0) + " + " + "t(" + str(n-2) + ";" + str(alfa/2) + ")*" + str(IC_Y_x0_sqrt),
        "]"
    )
    print(
        "IC(" + str(1-alfa) + ")(Y|x0=" + str(x0) + ") =",
        "[",
        str(round(beta_0+beta_1*x0, 4)) + " - " + "t(" + str(n-2) + ";" + str(alfa/2) + ")*" + str(IC_Y_x0_sqrt),
        ";",
        str(round(beta_0+beta_1*x0, 4)) + " + " + "t(" + str(n-2) + ";" + str(alfa/2) + ")*" + str(IC_Y_x0_sqrt),
        "]\n"
    )

print("Teste de Significância para os Coeficientes da Regressão Linear Simples:")
tc = round(beta_1/(sqrt(QMRes/Sxx)), 4)
print("β1 - Estatística de Teste: tc =", tc)
tc = round(beta_0/(sqrt(QMRes*((1/n)+((media_x**2)/Sxx)))), 4)
print("β0 - Estatística de Teste: tc =", tc)

print("\nANÁLISE DE RESÍDUOS DA REGRESSÃO LINEAR SIMPLES:")
print("Gráfico dos 45°:")
for xi, yi in zip(X, Y):
    yi_estimado = round(beta_0 + beta_1*xi, 4)
    print("yi =", yi, ";", "yi estimado = ^yi =", yi_estimado)

print("\nGráfico Versus Fits:")
print("Coordenada X ; Coordenada Y")
for xi, yi in zip(X, Y):
    yi_estimado = round(beta_0 + beta_1*xi, 4)
    ei = round(yi - yi_estimado, 4)
    print("xi =", xi, "ou", "^yi =", yi_estimado, ";", "resíduo = ei =", ei)

print("\nQQ-Plot:")
print("1) Cálculo dos ei:")
eis = []
for xi, yi in zip(X, Y):
    yi_estimado = round(beta_0 + beta_1*xi, 4)
    ei = round(yi - yi_estimado, 4)
    eis.append(ei)
    print("resíduo = ei =", ei)

somatorio_ei_quadrado = round(sum([ei**2 for ei in eis]), 4)
Se = round(sqrt((somatorio_ei_quadrado)/(n-2)), 4)
print("\n2) Se")
print("Σei² =", somatorio_ei_quadrado)
print("Se =", Se)

print("\n3) Resíduos Padronizados:")
dis = []
for ei in eis:
    di = round(ei/Se, 4)
    dis.append(di)
    print("di =", di)

print("\n4) Ordenar os di:")
djs = dis
djs.sort()
for dj in djs:
    print("dj =", dj)

print("\n5) Obter os Qj:")
for j in range(len(djs)):
    print("Qj = Q" + str(j+1) + " =", round((j+1-0.5)/n, 4))

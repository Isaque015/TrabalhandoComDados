import xlsxwriter

arquivo = xlsxwriter.Workbook('dados.xlsx')
planilha = arquivo.add_worksheet('teste')


dic = {
    'nome':['isaque','gustavo','rafael'],
    'idade':['20','18','34'],
    'UF':['SP', 'PR', 'MS'],
    'email':['dsadsa', 'fdssfd', 'dsadsadsa'],
    'dsdsadsa':['dsadsadsa', 'ddsasadsa', 'ddsasadsadsa'],
    'salario':['1800.99', '2300.88', '5400.55']
}


linha = 1
coluna = 0
bold = arquivo.add_format({'bold': True})
money = arquivo.add_format({'num_format': '$###,######0'})


for c, item in enumerate(dic):
    
    planilha.write(linha, c+1, item, bold)

    for lin, i in enumerate(dic[item]):
        if str(item) == 'salario':
            planilha.write(lin+2, c+1, float(i), money)
        else:
            planilha.write(lin+2, c+1, i)
        
           

arquivo.close()


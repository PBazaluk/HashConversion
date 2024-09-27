import hashlib

frases = [
    {
        # Frase 1
        'myText' : 'A primeira das instituições criadas pelo Pe. Roberto Sabóia de Medeiros foi a antiga Escola Superior de Administração de Negócios de São Paulo - ESAN/SP.',
        'entradaSHA256': "d24de3ec3835115c576a55188a31761b73af93ed2c45a171c810bb66b24b08f9",
        'entradaMD5': "c850e1a34a6ed572e0758ccd9c615bda"
    },
    {
        # Frase 2
        'myText': 'A FEI é uma instituição vinculada estatutariamente à Companhia de Jesus',
        'entradaSHA256': "6979a3d7a19e5921ae00ca7db9b814e1b83831dcedfca33dbb72e761ca084337",
        'entradaMD5': "b710771da8d7521524f45233ea9dd9e1"
    },
    {
        # Frase 3
        'myText': 'Em 20 de janeiro de 1951 foi realizada a sessão solene da congregação para a Colação de Grau da primeira turma da Faculdade de Engenharia Industrial.',
        'entradaSHA256': "6c582a993ba3ea454f11221a374878e534cfe666060c87ba03127de07f1ca4e6",
        'entradaMD5': "55748c2cb669a9d9508677cb914cb025"
    },
    {
        # Frase 4
        'myText': 'A Capela Santo Inácio de Loyola foi construída no ano de 1978, em concreto aparente.',
        'entradaSHA256': "254e695d0f8835651bc231f9cf1b2a7a097b849648f05f79f1855a55f85b089e",
        'entradaMD5': "f4a8a299fd4da2a5d70b374be2e48147"
    },
    {
        # Frase 5
        'myText': 'Tendo como função principal a promoção do aprimoramento profissional no campo administrativo e tecnológico, o IECAT (Instituto de Especialização em Ciências Administrativas e Tecnológicas) foi criado em 1982',
        'entradaSHA256': "d2150d688c337fc57e235adafd57f86d7aba0b8682c249b1006ba592706f88a0",
        'entradaMD5': "1c4ecc238571333ae507f82ff6a5e9e4"
    },
    {
        # Frase 6
        'myText': 'Dentro de uma proposta de integração e de agregação de competências, visando a excelência de seus cursos, as instituições FEI, FCI e ESAN foram transformadas no Centro Universitário da FEI no ano de 2002.',
        'entradaSHA256': "faefb927a21dd282ee00effe42bc0688f649450677a61edce15863a15461b721",
        'entradaMD5': "98420532cbf1be32a98be579f592cd72"
    },
    {
        # Frase 7
        'myText': 'O Centro Universitário da FEI passou a fazer parte do seleto grupo que produz ciência no Brasil, quando a CAPES aprovou o primeiro curso de Mestrado em Engenharia Elétrica em 2005.',
        'entradaSHA256': "da9f214449005850f4fd552238658820434c15ca06389d018b1814bb376abaa6",
        'entradaMD5': "2e20bfbece6fdc62de4c4bb80a77ba1f"
    },
    {
        # Frase 8
        'myText': 'Em 2016 foi realizada a primeira edição do congresso de inovação - Megatendências 2050.',
        'entradaSHA256': "56f4ba0ea34d91fe386f09dc687f1c35c757009b0230a828fa43e48ac08f8d0c",
        'entradaMD5': "5cbf7c58bf9acd451c3bf1b48392a9e6"
    },
    {
        # Frase 9
        'myText': 'Em 2012 o Centro Universitário FEI celebrou 70 anos de história e de excelência na inovação e na formação de mais de 50 mil profissionais altamente qualificados para o setor empresarial, entre Administradores, Engenheiros e Cientistas da Computação.',
        'entradaSHA256': "2707325bd4929bbbadb422851a2248615bf7998bf3607b6ad934168be6a45859",
        'entradaMD5': "a0a80cbc42bcd7b4b6ab317d0d2efa33"
    },
    {
        # Frase 10
        'myText': 'Em 1999 iniciam-se as atividades da FCI (Faculdade de Informática), como o curso de Ciência da Computação.',
        'entradaSHA256': "b2ff0457c8c20ccd84e20cd72f06c08140b8ea472d6a6848a5c291319bf9e4a8",
        'entradaMD5': "0288b32001adf2f237ba8410f8415e50"
    }
]

index = 1
resultadofim = []
for item in frases:
    print("Frase "+str(index)+"----------------------------------------------------")
    myText = item['myText']
    entradaSHA256 = item['entradaSHA256']
    entradaMD5 = item['entradaMD5']
    SHA256 = hashlib.sha256(myText.encode('utf-8')).hexdigest()
    MD5 = hashlib.md5(myText.encode('utf-8')).hexdigest()

    res = ""
    resSHA256 = ""
    if SHA256 == entradaSHA256:
        resSHA256 = "SHA256 - Igual\t"
        print(resSHA256)
    else:
        resSHA256 = "SHA256 - Diferente"
        print(resSHA256)
        
    resMD5 = ""
    if MD5 == entradaMD5:
        resMD5 = "MD5 - Igual"
        print(resMD5)
    else:
        resMD5 = "MD5 - Diferente"
        print(resMD5)
    res = resSHA256 + "\t" + resMD5
    resultadofim.append(res)

    print("Conversão: ")
    print("\"" +myText + "\" - " + SHA256 + " - " + MD5)
    print("Entrada: ")
    print("\"" +myText + "\" - " + entradaSHA256 + " - " + entradaMD5)

    print("Diferenças SHA256:")
    cont = 0
    for i in SHA256:
        if i != entradaSHA256[cont]:
            print("Diferente: "+i+"\tPosição: "+str(cont))
        cont+=1
    print("Diferenças MD5:")
    cont = 0
    for i in MD5:
        if i != entradaMD5[cont]:
            print("Diferente: "+i+"\tPosição: "+str(cont))
        cont+=1
    index += 1
print()
print("-------------------------------------------------------------------------")
print()
print("Resumo da execução:")
c = 0
for i in resultadofim:
    c+=1
    print(f"Frase {c}: {i}")
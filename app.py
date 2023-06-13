#chatbot para empresa que realiza declaração do imposto de renda
def answer(resposta, nome):
    #respostas do menu de opções
    if resposta == '1':
        print(f'\n{nome}, Para declarar o imposto de renda, você deve acessar o programa disponibilizado pela Receita Federal, '
              f'\nchamado de "Programa Gerador da Declaração" (PGD IRPF). '
              f'\nÉ necessário preencher todas as informações solicitadas, '
              f'\ncomo rendimentos, despesas, bens e direitos, e seguir as '
              f'\norientações do programa.\n')
    elif resposta == '2':
        print(f'\n{nome}, O prazo para enviar a declaração do imposto de renda varia a cada ano, '
              f'\nmas geralmente é até o final do mês de abril. '
              f'\nRecomenda-se verificar o prazo atualizado no '
              f'\nsite da Receita Federal.\n')
    elif resposta == '3':
        print(f'\n{nome}, Alguns documentos comuns que você precisará ter em mãos são: '
              f'\ncomprovantes de rendimentos (contracheques, informes de '
              f'\nrendimentos de instituições financeiras, entre outros), '
              f'\nrecibos de despesas dedutíveis (saúde, educação, pensão '
              f'\nalimentícia, entre outros), informes de rendimentos financeiros, '
              f'\ncomprovantes de compra e venda de bens, entre outros.\n')
    elif resposta == '4':
        print(f'\n{nome}, O carnê-leão é uma forma de recolhimento mensal obrigatório '
              f'\ndo imposto de renda para pessoas físicas que recebem '
              f'\nrendimentos de fontes no exterior ou do Brasil quando '
              f'\nnão há vínculo empregatício. O valor do imposto é calculado '
              f'\ncom base nos rendimentos mensais e deve ser pago até o último '
              f'\ndia útil do mês seguinte ao recebimento. Esses rendimentos '
              f'\ndevem ser declarados na sua declaração anual do imposto de renda.\n')
    elif resposta == '5':
        print(f'\n{nome}, Na declaração simplificada, você pode optar '
              f'\npor descontar um valor fixo (atualmente '
              f'\ndeterminado pela Receita Federal) em '
              f'\nsubstituição às deduções detalhadas. Essa '
              f'\nopção é vantajosa quando o valor do desconto '
              f'\nsimplificado é maior do que o total das deduções '
              f'\npossíveis. Já na declaração completa, todas as '
              f'\ndeduções são detalhadas, permitindo um possível'
              f'\nmaior abatimento no cálculo do imposto devido. '
              f'\nA escolha entre as modalidades vai depender da '
              f'\nanálise do seu caso específico.\n')
    elif resposta == '6':
        print(f'\n{nome}, Algumas das deduções permitidas na declaração do imposto '
              f'\nde renda incluem despesas com saúde, educação, '
              f'\npensão alimentícia, previdência social e privada, '
              f'\ndoações a instituições beneficentes, entre outras. '
              f'\nÉ importante conferir a legislação atualizada para '
              f'\nverificar todas as deduções possíveis.\n')
    elif resposta == '7':
        print(f'\n{nome}, Mesmo que você não tenha tido rendimentos, existem situações '
              f'\nem que é necessário fazer a declaração, como possuir bens '
              f'\nacima do limite estabelecido, ser residente no Brasil e '
              f'\nreceber benefícios do exterior, ou ter realizado operações '
              f'\nna bolsa de valores, por exemplo. Consulte as regras da '
              f'\nReceita Federal para saber se está obrigado a declarar.\n')
    elif resposta == '8':
        print(f'\n{nome}, Caso você não envie a declaração dentro do prazo estabelecido, '
              f'\nestará sujeito ao pagamento de multa. O valor da multa '
              f'\npode variar de acordo com o tempo de atraso e o valor do '
              f'\nimposto devido.\n')
    elif resposta == '9':
        print(f'\n{nome}, Sim, é possível retificar a declaração do imposto de renda após o '
              f'\nenvio, caso você tenha identificado algum erro ou omissão de '
              f'\ninformações. Para isso, utilize o mesmo programa utilizado para '
              f'\na declaração original e faça as correções necessárias.\n')
    elif resposta == '0':
        print(f'\n{nome}, Gostaria de tirar mais dúvidas ou contatar nossos serviços?'
                f'\n Entre em contato pelo número xxxxx-xxxx'
                f'\n e faça seu imposto de renda com a gente!'
                f'\n Damos 5 anos de garantia no seu imposto\n')
    else:
        print('Digite apenas números de 0 à 9')
def menssage():
    #apresenta o chatbot
    print('Olá! Obrigado por entrar em contato conosco! '
          '\nSou um assistente virtual da empresa de Imposto '
          '\nde Renda e estou aqui para ajudar. ')
    nome = input('Para iniciar o atendimento digite seu nome: ')
    #menu de opções
    while True:
        resposta = input(f'__________________________________________________________________________________'
                     f'\nComo posso ser útil hoje? Qual sua dúvida? Digite o número correspondente.'
                     f'\n[1] Como faço para declarar meu imposto de renda? '
                     f'\n[2] Qual é o prazo para enviar a declaração? '
                     f'\n[3] Quais documentos são necessários para a declaração?'
                     f'\n[4] O que é carnê-leão e como devo declará-lo'
                     f'\n[5] Qual a diferença de declaração simplificada e completa?'
                     f'\n[6] Quais são as deduções permitidas na declaração?'
                     f'\n[7] Preciso declarar meu imposto mesmo não tendo rendimentos?'
                     f'\n[8] O que acontece se eu não enviar a declaração dentro do prazo?'
                     f'\n[9] Posso retificar minha declaração depois de envia-lá?'
                     f'\n[0] Não encontrei minha dúvida!'
                     f'\n__________________________________________________________________________________\n')
        processar_resposta(resposta, nome)

#mensagem entrar em looping, assim que o arquivo for executado a função
if __name__ == '__main__':
    menssage()

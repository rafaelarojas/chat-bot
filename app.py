import os

def processar_resposta(resposta, nome):
    if resposta == '1':
        print(f'{os.linesep}{nome}, Para declarar o imposto de renda, você deve acessar o programa disponibilizado pela Receita Federal, '
              f'{os.linesep}chamado de "Programa Gerador da Declaração" (PGD IRPF). '
              f'{os.linesep}É necessário preencher todas as informações solicitadas, '
              f'{os.linesep}como rendimentos, despesas, bens e direitos, e seguir as '
              f'{os.linesep}orientações do programa.{os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep}{nome}, O prazo para enviar a declaração do imposto de renda varia a cada ano, '
              f'{os.linesep}mas geralmente é até o final do mês de abril. '
              f'{os.linesep}Recomenda-se verificar o prazo atualizado no '
              f'{os.linesep}site da Receita Federal.{os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep}{nome}, Alguns documentos comuns que você precisará ter em mãos são: '
              f'{os.linesep}comprovantes de rendimentos (contracheques, informes de '
              f'{os.linesep}rendimentos de instituições financeiras, entre outros), '
              f'{os.linesep}recibos de despesas dedutíveis (saúde, educação, pensão '
              f'{os.linesep}alimentícia, entre outros), informes de rendimentos financeiros, '
              f'{os.linesep}comprovantes de compra e venda de bens, entre outros.{os.linesep}')
    elif resposta == '4':
        print(f'{os.linesep}{nome}, O carnê-leão é uma forma de recolhimento mensal obrigatório '
              f'{os.linesep}do imposto de renda para pessoas físicas que recebem '
              f'{os.linesep}rendimentos de fontes no exterior ou do Brasil quando '
              f'{os.linesep}não há vínculo empregatício. O valor do imposto é calculado '
              f'{os.linesep}com base nos rendimentos mensais e deve ser pago até o último '
              f'{os.linesep}dia útil do mês seguinte ao recebimento. Esses rendimentos '
              f'{os.linesep}devem ser declarados na sua declaração anual do imposto de renda.{os.linesep}')
    elif resposta == '5':
        print(f'{os.linesep}{nome}, Na declaração simplificada, você pode optar '
              f'{os.linesep}por descontar um valor fixo (atualmente '
              f'{os.linesep}determinado pela Receita Federal) em '
              f'{os.linesep}substituição às deduções detalhadas. Essa '
              f'{os.linesep}opção é vantajosa quando o valor do desconto '
              f'{os.linesep}simplificado é maior do que o total das deduções '
              f'{os.linesep}possíveis. Já na declaração completa, todas as '
              f'{os.linesep}deduções são detalhadas, permitindo um possível'
              f'{os.linesep}maior abatimento no cálculo do imposto devido. '
              f'{os.linesep}A escolha entre as modalidades vai depender da '
              f'{os.linesep}análise do seu caso específico.{os.linesep}')
    elif resposta == '6':
        print(f'{os.linesep}{nome}, Algumas das deduções permitidas na declaração do imposto '
              f'{os.linesep}de renda incluem despesas com saúde, educação, '
              f'{os.linesep}pensão alimentícia, previdência social e privada, '
              f'{os.linesep}doações a instituições beneficentes, entre outras. '
              f'{os.linesep}É importante conferir a legislação atualizada para '
              f'{os.linesep}verificar todas as deduções possíveis.{os.linesep}')
    elif resposta == '7':
        print(f'{os.linesep}{nome}, Mesmo que você não tenha tido rendimentos, existem situações '
              f'{os.linesep}em que é necessário fazer a declaração, como possuir bens '
              f'{os.linesep}acima do limite estabelecido, ser residente no Brasil e '
              f'{os.linesep}receber benefícios do exterior, ou ter realizado operações '
              f'{os.linesep}na bolsa de valores, por exemplo. Consulte as regras da '
              f'{os.linesep}Receita Federal para saber se está obrigado a declarar.{os.linesep}')
    elif resposta == '8':
        print(f'{os.linesep}{nome}, Caso você não envie a declaração dentro do prazo estabelecido, '
              f'{os.linesep}estará sujeito ao pagamento de multa. O valor da multa '
              f'{os.linesep}pode variar de acordo com o tempo de atraso e o valor do '
              f'{os.linesep}imposto devido.{os.linesep}')
    elif resposta == '9':
        print(f'{os.linesep}{nome}, Sim, é possível retificar a declaração do imposto de renda após o '
              f'{os.linesep}envio, caso você tenha identificado algum erro ou omissão de '
              f'{os.linesep}informações. Para isso, utilize o mesmo programa utilizado para '
              f'{os.linesep}a declaração original e faça as correções necessárias.{os.linesep}')
    elif resposta == '0':
        print(f'{os.linesep} {nome}, Gostaria de tirar mais dúvidas ou contatar nossos serviços?'
                f'{os.linesep} Entre em contato pelo número xxxxx-xxxx')
    else:
        print('Digite apenas números de 0 à 9')
def start():
    #apresenta o chatbot
    print('Olá! Obrigado por entrar em contato conosco! '
          '\nSou um assistente virtual da empresa de Imposto '
          '\nde Renda e estou aqui para ajudar. ')
    nome = input('Para iniciar o atendimento digite seu nome: ')
    #menu de opções
    while True:
        resposta = input(f'__________________________________________________________________________________'
                     f'{os.linesep}Como posso ser útil hoje? Qual sua dúvida? Digite o número correspondente.'
                     f'{os.linesep}[1] Como faço para declarar meu imposto de renda? '
                     f'{os.linesep}[2] Qual é o prazo para enviar a declaração? '
                     f'{os.linesep}[3] Quais documentos são necessários para a declaração?'
                     f'{os.linesep}[4] O que é carnê-leão e como devo declará-lo'
                     f'{os.linesep}[5] Qual a diferença de declaração simplificada e completa?'
                     f'{os.linesep}[6] Quais são as deduções permitidas na declaração?'
                     f'{os.linesep}[7] Preciso declarar meu imposto mesmo não tendo rendimentos?'
                     f'{os.linesep}[8] O que acontece se eu não enviar a declaração dentro do prazo?'
                     f'{os.linesep}[9] Posso retificar minha declaração depois de envia-lá?'
                     f'{os.linesep}[0] Não encontrei minha dúvida!'
                     f'{os.linesep}__________________________________________________________________________________{os.linesep}')
        processar_resposta(resposta, nome)


if __name__ == '__main__':
    start()

from tkinter import *
janela = Tk()
janela.title('Contingência Agamenom')
janela.geometry('800x600')
janela.config(bg = '#022a3b')

label_aviso = Label(janela, text='====== Acesso Restrito! ======\nNível de Segurança: Ômega.')
label_aviso.pack()

janela.mainloop()



while True:
    nickname = input('Nickname: ')
    password = input('Password: ')
    if nickname == 'Batman' and password == 'DC27-5-1939':
        txt = 'Habilitando um novo protocolo, título: Contingência Agamenom.'
        print(txt)
        print("""Para qualquer membro da Liga da Justiça que se torne um vilão,\nprecisamos de planos e lugares para lidar com cada um de nós,\ncaso nos tornemos uma ameaça.\nOs membros da Liga são meus parceiros, mas precisamos\nestar preparados para o pior, sempre.""")

        busca = input('Contingência Agamenom: Codinome - ').lower()
        if busca == 'último filho':
            print("""Se o Superman tornar-se uma ameaça ao planeta, os seguintes\nprotocolos precisarão ser seguidos para garantir nossa sobrevivência.\nA amostra da Kryptonita verde, no cofre 7-B, cedida pelo próprio\nSuperman, irá incapacitá-lo com uma leve exposição.\nCom uma exposição prolongada, há probabilidade de ser fatal.
            
        As porções da Kryptonita exposta à radiação criou uma variação,
        cujo a cor é vermelha. Os efeitos colaterais dessa nova Kryptonita
        são desconhecidos. Testes aprofundados são requeridos.""")

        if busca == 'areias vermelhas':
                print("""J'onn J'onzz, o Caçador de Marte, é o coração e alma da
            Liga da Justiça. Mas sua força e velocidade fazem dele um
            oponente formidável, caso um dia ele vire-se contra nós.
                
            Sua vulnerabilidade ao fogo seria difícil explorar em uma
            posição defensiva, as pesquisas sugerem que um nano-vírus
            com nagnésio faz sua pele entrar em combustão em contato
            com o ar, neutralizando-o como uma ameaça.
                
            Devo investigar mais profundamente.""")

        if busca == '2814':
            print("""O anel do Lanterna Verde é a arma mais poderosa no universo, e é limitado
        apenas pela imaginação do portador. O anel não pode ser separado do seu
        portador, exceto por sua eventual morte.
            
        As defesas naturais do objeto lhe previnem de um ataque direto.
        Mas para usar o anel, o portador precisa ver o que está fazendo.
        Um ataque nos olhos seria recomendado para as defesas do anel.
            
        Veja a tabela 38-B para uma lista completa de ataques e probabilidades
        de sucesso. Pesquisas indicam que um pensamento pode ser implantado
        na mente dos Lanternas Verdes, fazendo-os acreditar que estão cegos.
        O anel iria cegá-los em virtude do seu próprio poder da vontade.""")

        if busca == 'olimpo':
            print("""Diana é uma boa amiga, mas é só um motivo de como seria difícil
        encará-la em combate se ela se voltar contra a Liga.
            
        Não é algo que gostaria de presenciar, mas se tiver de ser feito,
        as seguintes estratégias podem ser úteis: se ela puder ser
        convencida de que está a lutar contra um clone, ela seria presa
        em um combate eterno com um oponente fantasma.
            
        Preciso investigar a viabilidade de tecnologia virtual e neural.""")

        if busca == 'polímero':
            print("""Homem-Borracha, um oponente único. Cada molécula de seu corpo
        está sob seu controle e ele pode se transformar no que imaginar.
        Temos sorte de tê-lo ao nosso lado.
            
        Ele é mais preocupado em estar sossegado que qualquer coisa,
        mas caso se volte contra nós, congelá-lo com nitrogênio líquido ou
        algum outro agente é a melhor maneira que fui capaz de identificar.
            
        Depois disso, é só uma questão de armazenamento.""")

            repetir = input('Deseja realizar uma nova busca? [s/n]: ' )
            if repetir.lower() == 's':
                break

        else:
            print("Contingência Agamenom: Sessão de Anotações")
            print("""Respostas básicas para outros membros requer pesquisas aprofundadas.
         Flash, paralisia.
        Arqueiro Verde, imobilizar um dos seus braços.
        Zatanna, trauma na traqueia. Uma bomba sincronizada faria o serviço.
        Tornado Vermelho, PEM.
        Nuclear, Zona Fantasma? A falta de material bruto poderia diminuir os seus poderes.
        Aquaman, hidrofobia. Investigar modificações na toxina do Espantalho.
        Canário Negro, gás lacrimejante. Se administrado rapidamente pode cortar sua
        habilidade de falar e gritar. Alternativamente, eu gravei o seu grito que, se reproduzido
        ao contrário e com a mesma intensidade, ele poderia anular as ondas de som.""")

            print("""Se este plano de contingência for descoberto e eu
        estiver incapacitado, por favor entenda: isso deve
        ser feito para cada um de nós, o que nos leva a...""")

            print('Enter: Detetive')

            dtv = input('Contingência Agamenom: Codinome - ').lower()
            if dtv == 'detetive':
                print("""Bom, Batman é um mestre da estratégia em combate, mas ele é apenas
            um humano. A melhor maneira de anular as suas habilidade é distraí-lo.
                
            Os seus pais são um excelente ponto cego, assim como
            sua infinita cruzada para proteger os inocentes.
                
            Fazer reféns é uma boa distração, especialmente
            se forém amigos ou família.
                
            Pense BEM antes de fazer isso.""")
            else:
                print('ERRO! Contingência não encontrada!')

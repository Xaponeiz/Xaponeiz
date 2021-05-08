from random import choice
from time import sleep
print('\033[35m-=-' * 20)
print('\033[36mOlá, eu irei sortear o tema e o subtema da sua redação (:')
print('\033[35m-=-' * 20)
sleep(1)
print('\033[32mSorteando tema...')
sleep(1)
print('\033[35m.')
sleep(1)
print('\033[35m.')
sleep(1)
print('\033[35m.')
sleep(1)
li = ['Cultura', 'Educação', 'Juventude', 'Meio Ambiente', 'Saúde', 'Sociedade', 'Tecnologia', 'Violência']
tema = choice(li)
print('\033[34mO tema escolhido foi: {}'.format(tema))
if tema == 'ultura':
    c1 = 'Apropriação cultural no Brasil.C'
    c2 = 'A cultura do assédio no Brasil.'
    c3 = 'Memória e preservação do patrimônio cultural.'
    c4 = 'A falta de acesso à cultura na sociedade brasileira.'
    c5 = 'Implicações da pirataria no contexto cultural contemporâneo.'
    c6 = 'Pichação, grafite e os limites da arte urbana.'
    c7 = 'Demarcação de terras e impactos na cultura indígena.'
    c8 = 'Efeitos da intolerância ao multiculturalismo brasileiro.'
    c9 = 'A democratização do acesso à cultura em questão no Brasil.'
    c10 = 'A cultura de paz em oposição a violência na escola.'
    ls = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]
    n = choice(ls)
elif tema == 'Educação':
    e1 = 'Os entraves da educação a distância durante a paralisação escolar.'
    e2 = 'O processo de prevenção e recuoeração das ações de bullying no contexto escolar brasileir.'
    e3 = 'A reforma do ensino médio brasileiro e o papel da educação na sociedade contemporânea.'
    e4 = 'Evasão escolar no Brasil.'
    e5 = 'Educação alimentar e seus desafios na sociedade brasileira.'
    e6 = 'Homofobia no contexto escolar brasileiro.'
    e7 = 'Desafios para a fromação educacional de surdos no Brasil.'
    e8 = 'Precariedade do sistema educacional brasileiro.'
    e9 = 'Educação sexual e infância.'
    e10 = 'Escola Sem Partido e seus efeitos na educação brasileira.'
    l2 = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10]
    n = choice(l2)
elif tema == 'Juventude':
    j1 = 'Caminhos para combater o abuso sexual de crianças e adolescentes.'
    j3 = 'Combate ao uso indiscriminado das tecnologias digitais de informação por crianças.'
    j5 = 'O aumento das ISTs entre jovens no Brasil.'
    j6 = 'As implicações sociais dos casos de gravidez na adolescência.'
    j7 = 'Maus hábitos e infarto nos jovens.'
    j8 = 'Desafios e perspectivas para a juventude do século XXI.'
    j9 = 'As dificuldades da inserção de jovens no mercado de trabalho.'
    j10 = 'Os desafios da sexualidade no adolescência.'
    l3 = [j1, j5, j6, j7, j8, j9, j10]
    n = choice(l3)
elif tema == 'Meio Ambiente':
    m1 = 'Meios para o controle do lixo gerado no Brasil.'
    m2 = 'A promoção de saúde por meio de saneamento básico.'
    m3 = 'As perspectivas ambientais e sociasi da catástrofe de Brumadinho.'
    m4 = 'O agronegócio como ameaça ao meio ambiente.'
    m5 = 'Obsolência programada: implcações ambientais e de comportamento.'
    m6 = 'Lixo eletrônico e  impactos socioambientais.'
    m7 = 'alternativa para a diminuição do desperdício de alimentos no Brasil.'
    m8 = 'O consumismo e seus impactos ambientais.'
    m9 = 'As queimadas e a preservação do meio-ambiente.'
    m10 = 'Tragédias causadas por chuvas e enchentes: catástrofes naturais ou irresponsabilidade humana?.'
    l4 = [m1, m2, m3, m4, m5, m6, m7, m8, m9, m10]
    n = choice(l4)
elif tema == 'Saúde':
    t2 = 'Saúde mental no século XXI.'
    t3 = 'Poluição do ar: problemática da saúde e do desenvolvimento sustentável.'
    t4 = 'Impactos do agronegócio na saúde.'
    t5 = 'A tendência solitária mundial: problema de saúde publica ou necessidade humana?.'
    t6 = 'Os desafios de saúde pública do Brasil.'
    t7 = 'Via de nascimento: escolh da gestante ou quetão de saúde pública.'
    t8 = 'O combate a pandemias no mundo globalizado.'
    l5 = [t2, t3, t4, t5, t6, t7, t8]
    n = choice(l5)
elif tema == 'Sociedade':
    s1 = 'Os desafios para manter um sistema de saúde público no Brasil.'
    s2 = 'Desafio para a inclusão das pessoas com deficiência na sociedade.'
    s3 = 'Imediatismo na sociedade moderna e a dificuldade de lidar com frustrações.'
    s4 = 'A submissão feminina da sociedade.'
    s5 = 'Os impactos sociais das festas populares no cotidiano brasileiro.'
    s6 = 'Consequências da nomofobia no contexto mundial contemporâneo.'
    s7 = 'Medidas para combater a prática de bullying e de ciberbullying na sociedade brasileira.'
    s9 = 'O problema do alcollismo na sociedade brasileira.'
    l6 = [s1, s2, s3, s4, s5, s6, s7, s9]
    n = choice(l6)
elif tema == 'Tecnologia':
    t1 = 'As implicações das redes sociais nas relações interpessoais do indivíduo contemporâneo.'
    t2 = 'O reflexo da tecnologia no mercado de trabalho e as novas profissões.'
    t3 = 'Discurso de ódio e anonimato nas redes sociais no Brasil.'
    t4 = 'Combate ao uso indiscriminado das tecnologias digitais de informação por crianças.'
    t5 = 'Charlatanismo nas redes sociais.'
    t6 = 'Tecnologia une ou separa as diferentes classes sociais?.'
    t7 = 'Redes Sociais e o novo conceito de felicidade.'
    t8 = 'Desafio da alfabetização tecnológica para os idosos.'
    l7 = [t1, t2, t3, t4, t5, t6, t7, t8]
    n = choice(l7)
else:
    v1 = 'Violência nos estádios.'
    v2 = 'A violência obstrética como reflexo da violência contra a mulher no Brasil.'
    v3 = 'Linchamento virtual: violência coletiva como forma de sanar a injustiça.'
    v4 = 'A perspectiva social da violência urbana no Brasil.'
    v5 = 'A persistência da violência contra a mulher na sociedade brasileira.'
    l8 = [v1, v2, v3, v4, v5]
    n = choice(l8)
sleep(1)
print('\033[35m.')
sleep(1)
print('\033[35m.')
sleep(1)
print('\033[35m.')
sleep(1)
print('\033[35mE o subtema escolhido foi: {}'.format(n))

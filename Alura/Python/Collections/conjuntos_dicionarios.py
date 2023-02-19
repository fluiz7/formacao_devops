from collections import defaultdict, Counter

curso_de_design = [4,61,31,15]
curso_de_planejamento = [31, 16, 8, 15]

assistiram = curso_de_design.copy()
assistiram.extend(curso_de_planejamento)
# print(assistiram)

# print(set(assistiram))

curso_de_design = {4,61,31,15}
curso_de_planejamento = {31, 16, 8, 15}

# print(curso_de_planejamento | curso_de_design)
# print(curso_de_planejamento & curso_de_design)
# print(curso_de_planejamento ^ curso_de_design)
# print(curso_de_planejamento - curso_de_design)
# print(curso_de_design - curso_de_planejamento)

assistiram = curso_de_design | curso_de_planejamento
assistiram.add(53)
# print(assistiram)
assistiram = frozenset(assistiram)

alunos = {"Micael": 18, "Luiz": 21, "Junior": 22, "Carlos": 30}

# for aluno, idade in alunos.items():
#     print(aluno, idade)

alunos["Cavalo"] = 500
# print(alunos)
del alunos["Cavalo"]
teste = dict(Aleatorio = 21, Random = 14, Outro = 80)
# print(teste)

texto = "toda vez que eu chego em casa a barata da vizinha ta na minha cama eu nem acredito que isso possa estar acontecendo"
dicio = Counter(texto.split())

texto1 = """
Com a pandemia do COVID-19 e a transformação digital, o trabalho remoto se expandiu de forma considerável.

Afinal, era a forma de muitas empresas continuarem com suas operações sem colocar em risco a saúde de pessoas colaboradoras.

Mas, dois anos depois, o formato que ganhou adeptos, sobretudo no mercado de tecnologia, também passou a ser questionado.

Foi então que começou a era do trabalho híbrido — uma tentativa de misturar os dois formatos de trabalho: remoto e presencial.

De acordo com o estudo do Great Place to Work, 64,7% das pessoas colaboradoras preferem o trabalho híbrido. Na pesquisa, apenas 16,4% das pessoas preferem o trabalho remoto e 11,3% optam pelo formato presencial.

Mas qual é o melhor formato de trabalho para os times de tecnologia? Será que o formato híbrido é realmente positivo?

Para responder essas questões, este artigo vai refletir sobre as características do trabalho híbrido (principalmente, a partir da diferença em relação ao trabalho remoto e presencial) e quais as vantagens e desvantagens de cada formato.
O que é o trabalho híbrido
De forma geral, o modelo de trabalho híbrido é a combinação do trabalho remoto com o trabalho presencial. Ou seja, há alternância entre os dias que as pessoas colaboradoras trabalham dentro e fora das dependências da empresa.

Para regulamentar esse formato de trabalho, em 25/03/2022, foi publicada a Medida Provisória 1.108.

De acordo com essa nova norma, a caracterização do trabalho híbrido não depende de uma indicação formal para divisão dos períodos dentro e fora do estabelecimento empresarial.

Isto é, basta que existam esses dois formatos de trabalho (presencial e remoto) e que as partes negociem a respeito.

Diferença entre trabalho híbrido e trabalho remoto
Sendo assim, a principal distinção entre o trabalho remoto e o trabalho híbrido é que o remoto envolve apenas a prestação de serviços fora das dependências da empresa.

Então, diferente do trabalho híbrido, o trabalho remoto não compreende a realização de atividades dentro da empresa.

É importante ter em mente que o trabalho remoto vai muito além do home office — que é quando as pessoas colaboradoras trabalham de suas próprias casas. Isso porque, nessa modalidade, as pessoas podem trabalhar de qualquer lugar (inclusive, mas não somente, de casa).

Nesse caso, as lideranças também costumam trabalhar de forma remota. Assim, para estabelecer as dinâmicas de trabalho e repassar orientações, usam tecnologias de informação e comunicação.

No trabalho híbrido, por outro lado, as lideranças e pessoas colaboradoras podem se reunir de forma presencial para alinhar questões importantes.

Diferença entre trabalho híbrido e trabalho presencial
O trabalho presencial, por sua vez, é o regime de trabalho tradicional, em que as pessoas colaboradoras precisam se deslocar até as dependências da empresa para exercer suas funções.

Nesse formato, é comum que as empresas façam registros sobre a jornada de trabalho e disponibilizem um posto de trabalho para execução de tarefas.

Sendo assim, a principal distinção em relação ao trabalho híbrido é que o formato exclusivamente presencial não compreende atividades realizadas fora das dependências da empresa (de coworkings, home offices ou cafés, por exemplo), sob orientações por meio de tecnologias.

Vantagens do trabalho remoto
As principais vantagens do trabalho remoto compreende o fato de as pessoas colaboradoras conseguirem trabalhar de suas próprias casas ou de qualquer lugar que quiserem.

Assim, podem exercer as suas atividades do conforto do lar, sem se preocupar com trânsito ou com dresscode de escritório.

Além do mais, isso possibilita que as pessoas viajem enquanto trabalham, não apenas nas férias. Ou que trabalhem em localidades diferentes da sede da empresa - o que abre oportunidades tanto para as pessoas, quanto para as organizações.

Ainda, é comum que as empresas que operam a partir de trabalho remoto tenham horários flexíveis de trabalho. Isso dá autonomia para que as pessoas criem suas próprias rotinas.

Desvantagens do trabalho remoto
Por outro lado, as principais desvantagens do trabalho remoto envolve a infraestrutura para trabalhar e a necessidade de maior alinhamento na comunicação.

Em primeiro lugar, é comum que as empresas invistam em um apoio financeiro para construir a estrutura de trabalho. Então, por exemplo, fornecem os equipamentos eletrônicos e auxílio para internet.

No entanto, na prática, a estrutura de trabalho depende das circunstâncias de cada pessoa colaboradora. É necessário ter um espaço apropriado e mobília confortável (mesa e cadeira ergonômicas) para construir o escritório dentro de casa.

Além disso, o trabalho remoto exige uma atenção maior em relação à comunicação interna. As lideranças precisam encontrar boas formas de comunicar todos os processos e de alinhar as dinâmicas de trabalho, sem causar excesso de reuniões.

Vantagens do trabalho híbrido
Dados da Great Place to Work demonstram que a adoção de trabalho híbrido é, antes de mais nada, uma forma de investir na retenção de talentos. Afinal de contas, é o formato mais valorizado pelas pessoas profissionais.

Ainda, diferente do trabalho exclusivamente remoto, o trabalho híbrido garante a convivência entre as pessoas da empresa. Além do próprio engajamento entre as pessoas colaboradoras, a convivência pode afetar na motivação do trabalho.

Como se não bastasse, o formato híbrido fornece a oportunidade de a empresa proporcionar um ambiente com a estrutura necessária para o trabalho.

Considerando que o número de pessoas colaboradoras que vão diariamente no escritório é menor, a empresa consegue fornecer estrutura necessária sem causar tantas despesas.

Assim, é possível diminuir, de forma considerável, os custos de energia, internet, água, vale-transporte e outros tipos de custos.

Desvantagens do trabalho híbrido
Na prática, além de mesclar os benefícios do trabalho presencial e do trabalho remoto, é inevitável que o trabalho híbrido não consiga afastar as desvantagens de cada um desses formatos.

Então, por exemplo, as empresas devem arcar tanto com custos com infraestrutura da empresa, quanto com os equipamentos para organizar os escritórios nas casas das pessoas colaboradoras.

Ainda, as pessoas colaboradoras continuam a enfrentar tempos de deslocamento e a falta de flexibilidade de morar em um estado diferente da sede da empresa — assim como acontece no trabalho presencial.

Liderança no trabalho remoto
Assim como no trabalho remoto, o trabalho híbrido também faz com que as lideranças atuem de forma online.

A adaptação da liderança no modelo presencial para o remoto e híbrido não é tão simples assim. A distância física exige das lideranças um novo posicionamento.

Nesse contexto, surgiu o conceito de e-leadership, como um modelo de liderança que se adapta ao formato online. O principal desafio da e-leadership é entender qual a função e as necessidades da liderança no cenário remoto.

Os principais cuidados que as lideranças devem ter em ambiente remoto são:

Implementar uma cultura organizacional de transformação digital;
Apostar em flexibilidade, confiança e autogerenciamento nas relações de trabalho;
Fomentar relações mais horizontais (menos hierarquia entre os cargos) e maior autonomia das pessoas colaboradoras para desenvolver suas funções;
Treinar todas as pessoas colaboradoras para que saibam lidar com inovações digitais e soluções tecnológicas em suas rotinas de trabalho;
Promover o trabalho colaborativo entre a equipe;
Desenvolver a cultura do aprendizado contínuo;
Focar no equilíbrio e aproximação saudável entre vida profissional e pessoal;
Investir em softwares, sistemas e treinamento de comunicação empresarial.
Por que investir numa cultura digital para diferentes modelos de trabalho
Independentemente do formato de trabalho das pessoas colaboradoras (se híbrido ou completamente remoto), as empresas precisam se adaptar às transformações digitais e implementar seus processos de forma online.

Afinal de contas, uma coisa é certa: não está nem perto da hora de a tecnologia recuar. Pelo contrário, a tecnologia vem com força em todas as áreas e impacta de forma significativa no mercado.

Por consequência, as soluções tecnológicas conduzem constantes transformações globais, o que exige das empresas e das áreas tech duas atenções principais: atualização constante e adaptabilidade.

No final das contas, os times de tecnologia precisam estar atentos aos movimentos do mercado para prever possibilidades, gerenciar riscos e entregar soluções mais inovadoras em seus mercados.

Comunicação: a chave para o trabalho híbrido e para o trabalho remoto
Dentre todos os cuidados que as lideranças devem ter, o ponto de maior sensibilidade no trabalho híbrido e remoto é a comunicação e a conexão com a equipe.

Não é exagerado definir que manter uma comunicação fluida entre todas as pessoas da equipe é ainda mais difícil do que no modelo presencial.

Portanto, no trabalho híbrido e remoto, é necessário adotar algumas práticas frequentes para manter a qualidade do fluxo de trabalho e das entregas.

Sem dúvidas, o alinhamento da dinâmica de trabalho, a promoção de uma cultura de feedback e delegação de tarefas deve ser a prioridade das lideranças.

Inclusive, assim como propõe Eva Rimbau, professora de Recursos Humanos e Organização da Universidade Aberta da Catalunha, na entrevista ao El País, existem indícios de prejuízos reais para pessoas que trabalham em modelos híbridos:

“Em empresas onde alguns trabalham à distância e outros não, os trabalhadores remotos receberam menos promoções, menos capacitação e menos feedback sobre seu desempenho por estarem um pouco fora de vista”.

Qual o melhor formato de trabalho para profissionais de TI
É aí então que pode surgir a seguinte dúvida: qual o melhor formato para seu time de tecnologia?

A verdade é que muitas pessoas profissionais de TI gostam da flexibilidade que o trabalho 100% remoto oferece. Segundo, pesquisa da Microsoft, 53% das pessoas tendem mais a priorizar a saúde e o bem-estar ao trabalho após a pandemia. E isso pode refletir no modelo de trabalho, também.

No entanto, tudo depende da cultura da empresa e das pessoas da equipe. Há pessoas que vão sentir mais falta da convivência do que outras, há pessoas que são mais produtivas trabalhando na sede da empresa do que outras.

É importante que, independentemente do formato, a empresa ofereça infraestrutura suficiente para sustentar o formato que definir e, principalmente, que permaneça disposta a ouvir a opinião das pessoas colaboradoras.

No entanto, não se deve perder de vista os riscos, os benefícios e os prejuízos que acompanham uma decisão importante como essa.

E na sua empresa? Qual o modelo de trabalho adotado?
"""

def analisa_frequencia(texto):
    aparicoes = Counter(texto.lower())
    total_valores = sum(aparicoes.values())

    proporcoes = [(letra, frequencia / total_valores) for letra, frequencia in aparicoes.items()]
    proporcoes = Counter(dict(proporcoes))
    mais_comum = proporcoes.most_common(10)

    for letra, porcentagem in mais_comum:
        print(f"{letra} => {porcentagem*100:.2f}%")

analisa_frequencia(texto1)
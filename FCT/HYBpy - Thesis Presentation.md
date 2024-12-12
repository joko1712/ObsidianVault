
# 1
Bom dia vou dar então inicio a apresentação da tese HYBpy: A Web-Based Platform for Hybrid Modeling of Bioprocesses.

# 2
Esta será a estrutura da apresentação de hoje: 
	1. Contextualizar e demonstrar o problema que a tool HYBpy vem a resolver
	2. Referir as tools que mais se asemilhao á HYBpy e o porque de mesmo com algumas delas ainda ser essencial a criação da tool HYBpy
	3. Depois explicar como é a tool funciona e quais os principais detalhes
	4. Analisar 2 estudos de caso em que a tool foi posta em diferentes condições para podermos avaliar a performance/resultados
	5. Demo da tool em si
	6. Concluimos com user inputs que já utilizaram a tool e o que pode ainda a ser melhorado

# 3
1. Explicar o que sao bioreactores
	1. Um **reator biológico** ou **biorreator** corresponde a um volume onde decorrem reações biológicas
2. explicar o que sao hybrid models / o que e hybrid modeling
	1. Hybrid models são a combinação dos modelos mecanisticos com os modelos de machine learning para modelar no nosso caso expecifico reactor biologicos
3. Objetivo que será ( dar a opção a pessoas com ou sem conhecimento de programação a opção de conseguirem treinar e analisar estes hybrid models)
		1
Mas porque é que esta tool é necessaria de certo já existe algo semelhante

# 4
Verdade, já existe mas as opções que temos de momento não são acessiveis tudos aka: commercial softwares.
HYBpy a HybridML mas infelizmente para utilizar esta tool os utilizadores têm de ter conhecimentos de programação pois tudo é feito em código. 
É aqui que estra HYBpy como soluçao de ambos problemas. 

## Como é que vou falar sobre o SBML2HYB?
## Maybe falar aqui o que é HMOD e SBML?

# 5
Para ser mais fácil a apresentação desta tool eu dividia em 2 partes. A 1º vamos falar apenas da implementação python da tool ou seja o processamento da informação e depois o treino e depois faleremos da interface e do site.
# 6
Começando entao pela implementação python primeiro os dados do utilizador sao processados, após esse processo os dados são enviados para o treino do modelo e quando o modelo der o resultado do treino passamos a criação dos plots e das métricas do modelo

# 7
O processamento dos dados é aplicado a 2 ficheiros estes ficheiros são o Hmod que possui a informção sobre o modelo mecanistico do bioreactor e pode ou não ter a informação sobre o modelo de machine learning ( se este não existir o utilizador ao inserir no website vai lhe ser pedido que preencha umas caixas de texto para que este componenete seja introduzido no hmod) e o ficheiro CSV que contem as medições temporais das especies, a seu Desvio padrão e outros elementos como por exemplo o volume, o feedrate e a concentração. Este ficheiro tem de ser analisado pela tool e organizado pelos diferentes batches e dependendo da seleção dos batches feita pelo utilizador aka quais serao os batches utilizados para treino e utilizados para testeO processamento do hmod foi feito para garantir uma compatibilidade entre o HYBpy e o SBML2HYB mesmo com a network treinada. Ambos os ficheiros podem ser criados de raiz os utilizadores para tal podem seguir os ficheiros disponiveis no website.

# 8
Depois de termos então os ficheiros com toda a informação necessária da-se inicio ao treino.
A configuração do modelo de machine learning está dentro do ficheiro hmod. As opções que temos são definir a estrutura da neural network o numero de layers e o numero de hidden nodes, que tipo de activation function tangente hiperbolica ou ReLU, depois temos a decisão entre os metodos de treino Trust Region Reflective(trf), trust-constr trust region contructive se o utilizador utilizar o calculo do jacobiano ou o metodo L-BFGS-B, Dual Annealing e o ADAM, de seguida o utilizador pode tambem definir o numero de integrações no caso do TRF este numero será o número máximo de avaliações da função, temos tambem o numero de re inicializações depois existem opções mais delicadas que é recomendado ao utlizador menos experiente não alterar estas são: se o jac é calculado pela nossa função de treino ou se é calculado pelo metodo, se existe calculo de hessiano, o tau (), o modo de treino se é direto, indireto ou semi direto () e por fim se existe bootstraping ou não.




# 9
Para deixar uma melhor explicação da criação da rede neuronal.

## FALAR DE COMO A REDE É FORMADA E DE COMO O WEIGHTS E BAISES SÃO GERADOS.


# 10
A tool já foi testada com diversos modelos diferentes mas estes são os mais relevantes para demonstrar a generalidade da tool começando com o Park and Ramirez que podemos ver a (Aludir para a imagem com o modelo de ODES). Este modelo foi treinado com uma network com 1 layer e 3 hidden nodes com a activation function Tangente hiperbolica o metodo ADAM e 4000 sendo o numero de intetrações. Estes foram os gráficos gerados pela tool á esquerda temos o gráfico com a previsão do modelo face a dados temporais de teste, a linha vermelha representa a previsão e os pontos a verde representão as medições e os seus Desvios padrões respetivos. No grafico da direita conseguimos ver as todas as medições temporais presentes no ficheiro csv onde o eixo do y representa o valor onbservado nas medicões e o eixo do x o valor previsto pela network, ou seja o quão mais perto da euação da reta y=x melhor é a previsão da network. Mais a cima temos as medições da média do erro ao quadrado (diferença entre os valores previstos e o valores observados) e tambem o coeficiente de determinação (expressa a quantidade da variância dos dados). 

Neste caso expecífico acontece algo que não é comum pois existe um basis nos dados. 


# 11
Este é o modelo Chassagnole que podemos ver a (rede metabolica). Este modelo foi treinado com uma network com 2 layer e 5 hidden nodes com a activation function Tangente hiperbolica o metodo TRF e 400 sendo o numero de intetrações volto a referir que neste caso este numero é o maximo de evaliações que são feitas ao modelo. Estes foram os gráficos gerados pela tool á esquerda temos o gráfico com a previsão do modelo face a dados temporais de teste, a linha vermelha representa a previsão e os pontos a verde representão as medições e os seus Desvios padrões respetivos. No grafico da direita conseguimos ver as todas as medições temporais presentes no ficheiro csv onde o eixo do y representa o valor onbservado nas medicões e o eixo do x o valor previsto pela network, ou seja o quão mais perto da euação da reta y=x melhor é a previsão da network. Mais a cima temos as medições da média do erro ao quadrado (diferença entre os valores previstos e o valores observados) e tambem o coeficiente de determinação (expressa a quantidade da variância dos dados). Neste caso os resultados obtidos foram os esperados.

# 12
DEMO!!!!

# 13
### Não sei bem como explicar que como a tool e suposto ser super user friendly dado a isto tem vindo a ser alterada para melhor fruto do utilizador estas changes vem em forma de sugestões da equipa do lab e também 

A tool foi utilizada em Outubro no workshop da ("ESACT") - European Society for Animal Cell Technology - em Espanha dado Dr. Rui Oliveira. 

A tool foi exposta em forma de poster também em Outubro na conferencia ESBES (European  Society of Biochemical Engineering Sciences) na Dinamarca

Estamos também a finalizar um paper que será submetido na revista cientifica ("Computers & Chemical Engineering").


# 14
Devo também mencionar que já ouve muito trabalho feito na tool mas que esta tem muito ainda para ser melhorada, uma das principais melhorias seria o tempo de execução estamos de momento a tratar deste problema metendo a aplicação em um cloud service. Para futuro umas das principais melhorias será diminuir o tamanho dos tensores utilizados para os calculos matriciais assim perdemos um pouco de precisao (não assim tanto para ser detetável) mas melhoramos bastante o tempo de execução. E outro melhoramento que pode ser feito é passar os calculos e toda a execução em vez de ser feita no CPU para o GPU.

# 15
Questoes? 

Se ouver tempo ver se existe o resultado do treino da DEMO



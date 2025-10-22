

# REVIEW CHECKS:
- [x] Alter new intro for:
      biochemical industry. I suggest discussing the impact of hybrid models and reporting examples from other application cases, such as pharmaceutical cases, environmental applications, and petrochemical cases.
- [x] Add step by step guide on 3.1
- [x] Batch data visualization panel
- [x] Table 2 nº of runs
- [x] change reviewer 1 question 5
- [x] Email notification
- [x] 2.2.1 - rewrite intro

# Professor Rui

**A - New Hybrid Model**
A.1) Corrigir "New Hybrid Model" para "New Hybrid Modelling Project"
A.2) Load CSV, o requisito de "sd" ter que ser lowercase não faz sentido. Poderia até assumir-se que as colunas do sd podem ter um nome qualquer...
A.3) Add ML block to Hmod:  Deve permitir incluir como input à rede "Time" e qualquer variável na lista de parâmetros do hmod. De outra forma, a aplicação prática é reduzida
A.4) Edit HMOD settings:é preciso avaliar porque é que o levenberg-marquardt não funciona; esse seria o método mais apropriado e inclusivé mais rápido para os modelos híbridos shallow
A.5) Manual hold-out cross validation: deve ser possivel não escolher nada para validação nem para teste se o utilizador assim o desejar. O utilizador pode querer avaliar se o  treino converge e é estável sem o early stopping da validação. Ou seja, basta escolher um batch de treino para se poder iniciar o treino. Eu queria fazer isto para o modelo CHO que era suposto mostra em Espanha  e que não consegui. O modelo nunca funcionou. Quando um modelo não funciona o primeiro teste a fazer é deixar treinar durante muito tempo com apenas 1 batch para ver se esse batch é perfeitamente descrito.

**B - Hybrid Model Details**
B.0) Deveria ser possivel escolher um qualquer projeto concluído do historical e navegar nos respetivos resultados. 
B.1) "Show paraty plots" está trocado com "Show error plots". "Show paraty plots" deve ser corrigido para "Show **parity** plots" e "Show error plots" deve ser corrigido para "Show time series plots".
B.2)  Nos parity plots, os pontos de treino e validação devem ser distinguidos; a diagonal não precisa de legenda e deve ser a cheio; incluir duas linhas tracejadas com +5% diagonal e -5% diagonal; no título, "Predicted vs Observed" é redundante. Melhor destacar o nome da espécie e dos títulos dos eixos. 
B.3)  Os parity plots deveriam ser com a espécie normalizada da mesma forma que se usou no treino
B.4) Seria bom incluir um parity plot adicional com todas as espécies juntas normalizadas
B.5) Nos time series plots, deve ser possivel selecionar um qualquer batch; trocar "Value" pelo nome da espécie e eliminar o título do plot; Na legenda eliminar "data" Show details of completed run
B.6) Falta o "Close"  button
B.7) Corrigir "r2_train" para R^2 train; incluir Q^2 valid; corrigir r2_test para Q^2 test  (no futuro, estas métricas poderiam ser avaliadas individualmente por espécie e ser incluídas no parity plot ou então fazer aqui uma tabela)
B.8) Corrigir "mse" para "WMSE" e incluir WMSE valid
B.9) Incluir uma linha com o número de parâmetros optimizados na rede
B.10) Incluir uma linha com o CPU (não sei se isto faz sentido com processos na cloud)
B.11) Adicionar espaços entre os nomes das variáveis de entrada e saída da rede

**C - Historical**
C.1) Incluir projetos iniciados mas ainda não concluídos; Adicionar "Completed: XX%" logo a seguir a "StartdAt:xxxx"; Subsituir "FinishedAt: xxx" por "Duration: XXXX"; no caso de o processo não está terminado, a duration é a prevista
C.2) Permitir o delete de projetos iniciados e ainda não terminados
C.3) Talvez limitar o número máximo de projetos e não deixar criar um projeto novo sem apagar um antigo sempre que o número máximo de projetos é atingido

**D - Simulation** 
D.0) "Simulation" deve ser a seguir a "Hybrid Model Details"
D.1)  Não pode ser um novo projeto no historical; a ideia é simular apenas um batch selecionado e mostrar logo os resultados na janela
D.2)  Corrigir "Select a Previous Run" para "Select project" 
D.3)  Load CSV deve ser opcional; se não fizer load CSV usa o CSV do projecto utilizado para o treino
D.4) Seleccionar um (e apenas um) qualquer batch do CSV
D.5) Mostrar os time series plots dos compartments, species nos compartments, kinetic rates, control inputs, parameters ( a ideia é poder navegar na simulação do batch em grande detalhe)

**E - Train (nova opção do menu bar que deve aparecer a seguir a "Hybrid model details")**
E.1) Permitir selecionar um qualquer historical project completed
E.2) Não permitir mudar o nome do projeto.
E.3) STEP 1. Permitir editar apenas a janela "Edit HMOD Settings" 
E.4) STEP 2. Permitir "Select data split"
E.5) STEP 3. "New random parameters" OR "Parameters from previous training"
E.6) Quando se clica no start training;  os resultados escrevem por cima dos resultados anteriores, ou seja, retreinar o projeto 10 implica apagar o projeto 10 anterior e mudar o historical para "Completed:0%"

**F - Optimisation (nova opção do menu bar que deve aparecer a seguir a "Simulation")**
Não é prioritário agora;



# New additions to train:

1. Manual ho CV
2. Automatic ho CV
3. k-fold CV
4. LOO CV

1 - User selects Manually the train, validation and test 
```py
User selects and app.py receives:
train_batches = [[1,2,3,4,5,6],[7,8,11,12,1,2],[1,3,5,7,9,11]]

test_batches = [13,14,15]

val_batches = [[7,8,9,10,11,12],[3,4,5,6,9,10],[2,4,6,8,10,12]]

mode = "1"
crossval = 1
esemble = doesn't matter?
```

2 - User selects Manually the test 
```py
User selects:
test_batches = [13,14,15]

app.py receives:
test_batches = [13,14,15]
bacthes = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

mode = "2"
crossval = 1
esemble = doesn't matter?
```

3 - User selects test, then selects k-fold and the % for train and batch
```py
User selects:
test_batches = [13,14,15]
k-fold = 3
%train = 50%
%test = 50%

app.py receives:
test_batches = [13,14,15]
bacthes = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

mode = "2"
crossval = 1
esemble = doesn't matter?
```

## Functional:
- [x] Add Template csv and .hmod to the button
- [x] Add link to SBML2HYB to Guide
- [x] Fix issue where batch mode on Historical
- [x] Add Topbar to the logjn and register 
- [x] Fix issue when using the examples to appear name of files instead of template(n) #
- [x] Put footer bot on: Results and Historical pages 
- [x] Add readme to ModelsandData
- [x] Alter plot from Species to specie
- [x] Remove Time Series Prediction from historical 
- [x] Alter Get CSV template
- [x] Add description to hybpy link google = *Add **_What is HYBpy?_**
- [x] Add EndedAt # MIGHT BE DONE
- [x] Update PrintScreen on HELP
- [x] Contact Us
- [x] Add print of hmod with explanation using arrows with button to download(mandatory)- NOT PRIORITY 
- [x] Add **_What is HYBpy?_**  _(a bold com letra um pouco maior)_ _HYBpy is designed to simplify the construction and analyses hybrid models of [bioprocesses](__[https://www.sciencedirect.com/science/article/pii/S0098135422002897?via%3Dihub#abs0001](https://www.sciencedirect.com/science/article/pii/S0098135422002897?via%3Dihub#abs0001)__) and [biological systems](__[https://www.mdpi.com/2673-2688/4/1/14#B25-ai-04-00014](https://www.mdpi.com/2673-2688/4/1/14#B25-ai-04-00014)__)._ You can also install HYBpy on Windows to run locally. Please visit the [GitHub respository](__[https://github.com/joko1712/HYBpy](https://github.com/joko1712/HYBpy)__) page.
- [x] Tendo em conta que no documento da tese o link para o HYBpy está errado ([www.hybpy.org](http://www.hybpy.org)) inclua no link [https://github.com/joko1712/HYBpy_ModelsandData](https://github.com/joko1712/HYBpy_ModelsandData) que tb aparece na tese um readme com informações sobre o que está contido nas pastas, um titulo e ainda o link correto para a plataforma [www.hybpy.org](http://www.hybpy.org).
- [x] Add table for historical
- [x] Trained Hmod
- [x] In “Help” add in “**Step 3: Upload your data file.**” -> “The data file must be filled out using the template file structure”.
- [x] Make text smaller md/xs 
- [x] Reduce number of  decimal numbers
- [x] Make Start Training smaller
- [x] In Simulation only test batch or only initial line of batch and control variables over time
- [x] Change website description -- Don't know why is this not done
- [x] Add cloud functions for trainning
- [x] Review Trained Hmod creation
- [x] Add Csv download to guide
- [x] Add Hmod print to guide
- [x] Make login and sign up text and input smaller
- [x] if Last colum is number of batches remove from batch representation
- [x] When user gives 1 batch use it for "train in the simulation". when the user gives a multitude of batches use 1 for "train" and the others for test. 
	- [x] Test if user gives 1 line of a batch it works

## Aesthetics:
- [x] Show where you are on burger menu # Should be done
- [x] Make Nova .png smaller
- [x] Remove empty columns on csv examples
- [x] Alter Home: "please feel free to contact us contact us at:" to "please feel free to contact us (email do Jose ou o meu)"  Add both to (contact us)
- [x] On guide alter Step 6: "Verify and Modify Mlm Settings" to "Verify and Modify ML Settings" and "After adding the ML component" 
- [x] On the Help make the images from SBML2HYB smaller # DONE?
- [x] Help alter the download SBML2HYB to: SBML2HYB tool](windows) or  (macOS) # DONE?
- [x] Change hmod to HMOD # DONE?
- [x] Add line on each title#
- [x] If batch_number is last column cut it
## Writting:
- [ ] Write Article
- [x] Add Comparison and Analysis
- [x] Sec. 3 terá que ser reescrita. Veja por favor o estilo de escrita deste tipo de secções em artigos do mesmo tipo.
	- [x] https://pmc.ncbi.nlm.nih.gov/articles/PMC6108935/#S3 
		    [[Tellurium.pdf]]
	- [x] https://bmcsystbiol.biomedcentral.com/articles/10.1186/s12918-018-0607-5#Sec14  
			[[Escher_FBA.pdf]]
	- [x] https://bmcsystbiol.biomedcentral.com/articles/10.1186/1752-0509-7-74#Sec2 
			[[Cobrapy.pdf]]
	- [x] https://bmcsystbiol.biomedcentral.com/articles/10.1186/1752-0509-6-8#Sec4
			[[FAME.pdf]]
## Extra:
- [x] Add cycle graph to Historical
- [x] Duration
- [x] Add files to run local
- [x] Fix issue when showing graphs if only 1 graph don't show cycle 
- [ ] Add Tab to Results
	- [ ] https://mui.com/material-ui/react-tabs/
- [ ] Add stopper to training
- [ ] Limit 2 trains per user


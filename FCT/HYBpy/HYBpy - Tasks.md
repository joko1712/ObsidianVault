# TASKS:

## Review Modifications:
  
Reviewer 1: In this paper, the authors present a web-based tool integrating an interface to generate and train a hybrid model. The work is relevant and the subject is worth investigating, as the community needs such a tool. However, I suggest some modifications to improve the quality of the manuscript and give the reader a better context on the capabilities of the tool.  
  
1. In the introduction, the authors report examples from the biochemical industry. I suggest discussing the impact of hybrid models and reporting examples from other application cases, such as pharmaceutical cases, environmental applications, and petrochemical cases.  
2. For the case studies, I suggest reporting the employed model along with a screenshot or a small description on how to add them in the software.  
3. I suggest the authors highlight if there is a training management interface, such as running the test set creation and/or setting model training hyperparameters (e.g., learning rate and training epochs). Moreover, I suggest reporting the available benchmark metrics in the software.  
4. I suggest the authors report more insights about the techniques available in the software to visualise data and results.  
5. In Table 1, what is the median training time? How many training sessions did the authors run? How did they select the one to report in the paper? On which machine is the training run?  
6. In Table 1, the median training time is quite high. Is there a detached mode software run where the user can run the training and close the web interface while the backend runs the training? If so, is there a notification mode when the training is done?  
7. How does the software approach the numerical integration of differential equations?  
8. Is the software suitable only for dynamic systems, or does it also handle steady-state?  
9. Can the authors highlight whether they are open to contributions to the software, and under what license it was released?  
  
  
Reviewer 2: This manuscript presents an open-source web-based tools for developing hybrid models for biological systems. The authors outline the implementation of the framework, the web portal structure and as part of results navigate through the web-based tool through two simple examples. Although there is no research novelty, in terms of algorithmic development or use-cases demonstrated, this work can be viewed original in a sense in terms of streamlining the workflow for non-expert users. This is somewhat in line with the author's positioning of the work aiming at the development of a user-friendly, open-access hybrid modeling pipeline.  
General comments:  
1.       The description of the workflow is not very clear, lacking a smooth flow of information through the framework making it hard for the readers to follow the manuscript.  
2.      The authors claim that it is intended for use by non-experts, but it looks like a lot of choices lie with the user. For instance, defining the architecture, integrator, optimizer, parameters for integration, parameters for optimization etc. It is ironically that the user is a non-expert but is expected to have a lot of understanding about ML and numerical methods concepts. In which case it is highly likely that the user is already familiar with a programming language given coding is an integral part of both ML and numerical methods.  
3.      It is unclear how the hyperparameter optimization is performed or even if it is performed. Similarly, how the confidence intervals are obtained. All looping into a lack of coherence of presentation of the content.  
4.      The quality of figures is poor as nothing is clearly readable.  
On that note, following are the detailed comments to the different sections:  
Introduction  
1.      Title and Introduction mismatch - The title suggests that the framework is for biological systems. However, in the introduction (Pg 2, Line 50 - 57) where the authors summarize the typical hybrid modeling pipeline, they refer to bioreactor model. This and other in-consistencies of the similar sort should be addressed to ensure that the work is suitably positioned.  
2.      Pg 2 Line 15 - Missing reference corresponding to the statement "… hybrid modeling methods with several applications". References to literature covering different applications should be added.  
3.      Pg 2 Line 49 to 59 - Where the authors describe the current pipeline for building the hybrid model pipeline, it is hard to differentiate between steps iii, iv, v in the current phrasing. Please rephrase for clarity and a schematic in the main manuscript or supplementary information would aid in the understanding.  
Architecture Overview  
The architecture overview is currently very chaotic and hard to follow. There is abrupt back and forth.  
1.      I would suggest moving from left to right in Figure 1 and walking through element by element as they appear.  
2.      The section could start with: "The structure of HYBpy is designed to guide the user through the workflow from data upload towards model-derived insight."   
3.      Then describe the HMOD component (essentially the first paragraph in this section in the current manuscript). Then discuss about the csv file. Here, an example of how these two files look and what type of information they should contain must be described. A schematic/screenshot in the main manuscript or the supplementary information of both these file types will be helpful. I acknowledge that the file type reference to previous literatures have been provided, however constant switching between references and current manuscript makes it super hard to follow and breaks the flow.  
4.      Unwind the pipeline moving left to right describing sequentially what each function does as they appear in the framework. Similarly, add a visual clue as to how the data format changes after being processed through hybdata and csv2json. Without that is hard to understand statements like  
"It transforms the static data contained within HMOD files into a dynamic and structured format stored in a dictionary" : - Static how? Dynamic? Which structured format?  
"The function orchestrates the optimization process, configuring parameters and settings based on the user input (taken from the HMOD file)." - Since the reader doesn't know how such an HMOD file looks, what information it represents etc, it is hard to follow this.  
5.      Provide a table with all the function. What is the input, output and functionality of this function to provide a summary of the key components of the framework.  
6.      The description about the hybodesolver and odesfun is entirely missing from the manuscript. The role of the Interface and Server icons should be defined. And the pipeline should finally end with insights which is missing.  
7.      What are the hyperparameter optimization capabilities (if any)? Where is it implemented in the workflow? How is this specified in the HMOD file? From the description on Pg 5 Line 24-32, it seems like each HMOD file contains a model configuration, so one set of hyperparameters. How does it work then for hyperparameter optimization?  
8.      Pg 4 Line 32-38, Referring to paragraph "Additionally, the hybtrain.py ………., model compilation."  The description of the optimizer options is extremely confusing and needs to be rephrased for clarity.  
9.      No discussions about convergence determination criteria are mentioned. How is it handled. Is the best checkpoint model, based on an internal validation used? Or just run until some max iteration? Please clarify in the description of the relevant function (guess would be hybtrain.py in this case)  
Software Structure  
1.      "New Project" - What are the user specific decisions to be made and how do these functionalities appear on the interface and other files (e.g., HMOD).   
Case Study 1  
1.      From the description it looks like a lot of choices are to be made/defined by the user? If so, how is it accessible for non-experts? If it is intended for use by non-experts, a more Auto-ML'ish approach with built in hyper optimization would be expected for non-experts.  
2.      As per the description, all hyperparameters seems to be fixed a-priori (activation function, No. of layers, No. of nodes etc). What is the cross validation used for?  
3.      Plots in Figure 4 show confidence intervals. How are these obtained. No where in the architecture description it is mentioned what the source of confidence intervals are.  
4.      It would be nice to remind the readers how to navigate to these plots. For instance, saying by moving to the "Results" tab, the user can observe plot in Figure 3 and 4 or something along the similar lines.  
Results (General)  
1.      Is there a training/validation plot over iteration for the users to monitor the progress? If yes, discuss. If not, why so, discuss.  
2.      Are the results in Table 1, in terms of the metric available on the portal? If so, where and how? If not, why not?  
3.      It almost seems like, instead of the homepage screenshot, screenshot of the results tab might be more useful.  
4.      With regards to the bullet points, specifically "Ease of Use" and "Customization". The authors emphasize enough number of times that this pipeline is for non-experts with no programming knowledge. However, with the number of choices the user has to make from the optimizer type to NN type, architecture and parameters, it feels like the user has to know concepts of ML and numerical methods to a great degree.  In which case it is highly likely that the user is already familiar with a programming language given coding is an integral part of both ML and numerical methods. With an intent of use for non-expert, lower modularity in terms of model definition would be expected.  
Hybrid Model Simulations  
1.      Authors indicate early-on in the manuscript that the "simulations" tab can be used for future validations. It would be good to discuss and present the functionalities for such a validation. What quantitative metrics are available? Can you provide additional test data and compare different models? What does the workflow look like.  
Conclusions and Future Directions  
1.      Major comment here is in line with pt 4 in Results (General) section above. Re-iterating, with the number of choices the user has to make from the optimizer type to NN type, architecture and parameters, it feels like the user has to know concepts of ML and numerical methods to a great degree.  In which case it is highly likely that the user is already familiar with a programming language given coding is an integral part of both ML and numerical methods.  
2.      The authors briefly touch upon computational time. However, more discussions of possible directions to improve the training efficiency should be discussed. 4hs for a simple case study seems too much. Moving to GPUs may not be able to solve the entire issues. Changes to the training procedure itself might be required and some avenues in this area should be discussed.


# REVIEW CHECKS:
- [ ] 1.1 - 
- [ ] 1.2 - 
- [ ] 1.3 - 
- [ ] 1.4 - 
- [ ] 1.5 - 
- [ ] 1.6 - 
- [ ] 1.7 - 
- [ ] 1.8 -
- [ ] 1.9 -

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


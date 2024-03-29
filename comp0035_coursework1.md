# Coursework 1

## Technical information
### Repository URL

[Repository](https://github.com/ucl-comp0035/coursework-1-Yaseen048.git)

### Set-up instructions

Assume that requirements will be installed from requirements.txt.

If you have used any libraries that require set-up beyond `pip install ...` then use this section to explain any set-up
instructions to be followed to run your coursework.

If the marker cannot execute your coursework they can't grade it!

I installed the xlrd module to allow python to read data from Excel files. I also installed matplotlib to make graph plot.

## Selection of project methodology
### Methodology (or combination) selected
The methodology used for this project will be crisp-DM
### Selection criteria and justification of selection
The selection criteria includes:
    The size of the project team.
    What experience the team has in different methodologies?
    Is there an understanding of the business?
    Volatiltiy of requirements, so are the requirements fixed or do they change throughout the project?

Based on the selection critieria it was found that the crisp-DM methodology was the best suited for this project. Firstly, this project is a small one so a only small team is required. Crisp-DM is very adoptable and easy to learn. This suits this project as it means that everyone in the project should be able to implement this method, regardless of thier experience in other methodologies.

Crisp-DM also starts off its process with business understanding which matches the selection critieria[1]. In this project, the requirements are well defined and is very unlikely to change throughout the project. A disadvantage of crisp-DM is that it can be seen as rigid depending on how you implement crisp-DM, unlike scrum which is agile and allows for changes through inspection after each sprint[2]. However since the requirements are unlikely to change, the rigidness of crisp-DM won't affect the project too much. 
 
Scrum was another method that was considered for its agileness and allowing for constant improvements and changes but only  works if everyone in the team has experience with it[2]. As a result crisp-DM was chosen over scrum due to being easy to implement with a team that may not have experience in the same methodologies as each other whilst crisp-DM also providing more understanding of the business needs as the begining of the project cycle.


## Definition of the business need

### Problem definition
Due to covid-19 cinemas were temporarily shut down as everyone went into lockdown, the first of which started in March 2020[3]. This led to a loss in revenue for cinemas and film production companies as customers were not able to go to the cinemas which is their main source of income. Despite lockdown ending and cinemas being reopened, there are currently only a limited number of screenings. As a result, by analysing this dataset, this can useful to those who want to create a business plan just incase another scenario such as covid-19 occurs or it can  provide intel on how to increase sales or reduce costs by selecting certain types movies depending on they did during the pandemic.

### Target audience
The target audience are cinema CEOs

![Alex_Hover_persona](https://github.com/ucl-comp0035/coursework-1-Yaseen048/blob/master/Pictures/Alex_Hover_persona.png)

### Questions to be answered using the dataset
How has covid-19 affected the sales of movies in cinema after the pandemic and the re-opening of cinemas?
How has covid-19 affected the release of new movies?
Who are the movie distributors of movies that have the highest sales?
What countries make the most successful movies?

## Data preparation and exploration
### Data preparation

[Data Preparation](data_preparation.py)

### Prepared data set
The original dataset is made up of 3 files to represent how cinema was affected by Covid-19. The 3 files show cinema income before the first lockdown (March 2020), between the first and second lockdown when restrictions temporarily eased up (August 2020) and finally after the last lockdown (July 2021)[3]

[Original data set](data)
[Prepared data set](Prepared_dataset.csv)

### Data exploration

[Data Exploration](data_exploration.py)

Weekend Gross boxplot:

![Weekend Gross boxplot](https://github.com/ucl-comp0035/coursework-1-Yaseen048/blob/master/Pictures/Weekend_gross_boxplot.png)

Weeks on release of films boxplot:

![Weeks on release](https://github.com/ucl-comp0035/coursework-1-Yaseen048/blob/master/Pictures/Weeks_on_release_boxplot.png)


These plots show that despite the mean weekend gross being similar it was mainly due to an outlier that August 2020 made most of its sales. It also shows the number of new movies shown in August was low compared to March 2020 and July 2021 so cinemas had to show older movies to try increase their sales. March 2020 and July 2021 are very similar when shown on the boxplots meaning that cinemas were able to recover to some extent from the pandemic.

## Weekly progress reports

### Report 1

What I did in the last week:
This week I researched and decided what methodology i should use for the coursework project. This was crisp-DM.

What I plan to do in the next week:
Define business problem or problems  and how i could address them and who might be the target audience.

Issues blocking my progress (state ‘None’ if there are no issues):
None

### Report 2

What I did in the last week:
made problem statement(cinemas lost revenue due to covid and the data can be used to analyse how movies sales were affected and how to increase revenue) and found target audience - cinema owners/CEO

What I plan to do in the next week:
learn about data ethics and how to prepare data using pandas

Issues blocking my progress (state ‘None’ if there are no issues):
None

### Report 3

What I did in the last week:
learn about data ethics and how to prepare data using panda

What I plan to do in the next week:
learn and try to explore the data

Issues blocking my progress (state ‘None’ if there are no issues):
None

### Report 4

What I did in the last week:
learnt a bit of how to explore data using pandas

What I plan to do in the next week:
finish exploring data and finish off or improve on any other sections of coursework.

Issues blocking my progress (state ‘None’ if there are no issues):
Became very ill and was not able to come to university for the week. being ill and tired made it hard to focus and study

## References
Use any [referencing style](https://library-guides.ucl.ac.uk/referencing-plagiarism/referencing-styles) that you are
used to using in your course.

[1]Wijaya, C., 2021. CRISP-DM Methodology For Your First Data Science Project. [online] Medium. Available at: <https://towardsdatascience.com/crisp-dm-methodology-for-your-first-data-science-project-769f35e0346c> [Accessed 18 November 2021].

[2]Abdollazadeh, A., 2021. CRISP-DM and Agile-Scrum methodology for Data Science Project Delivery. [online] Linkedin.com. Available at: <https://www.linkedin.com/pulse/crisp-dm-agile-scrum-methodology-data-science-project-abdollazadeh> [Accessed 18 November 2021].

[3]Instituteforgovernment.org.uk. 2021. [online] Available at: <https://www.instituteforgovernment.org.uk/sites/default/files/timeline-lockdown-web.pdf> [Accessed 18 November 2021].

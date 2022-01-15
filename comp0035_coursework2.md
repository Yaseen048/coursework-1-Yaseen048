# Coursework 2

Most students will use the same repository for coursework 2. You may use this file to present the results of that
coursework if you wish. Alternatively you can use video or audio to provide the explanations instead of writing them.

## Requirements definition and analysis
The term 'requirements' is used in the broader sense, user stories and/or use cases may be used.
### Requirements identification methods
The two main methods I will use to identify requirements are an interview and brainstorming. The reason for using an interview is beacuse of the methodology used, which is crisp-DM. Crisp-DM starts with having a business understanding. An interview with the target audience (in this case, a cinema CEO) is a very good way to understand how the business works and will give us a good starting point in creating requirements that would be useful to the target audience. Also because cinema CEOs pretty much have the same target and goals, this means that a few interviews can be generalised for the all CEOs and this would be beneficial as it would save time and money. 

Brainstorming is the other method used to identify requirements. Brainstorming helps us to find additional requirements by coming up with similar ideas that we found from the responses of the interviews.
### Requirement specification method

### Prioritisation method
The method i have chosen to priortise my requirements is the MoSCoW technique. This is a relavtively simple method to help priortise the requirements by using four categories: Must have, should have, could have and won't have for now. Because of this it helps give you an idea of how long the project will take to complete as well as assisting you in your time management of which parts of the project will take longer to make or build

### Documented and prioritised requirements
Link to the full list of documented and prioritised requirements.

I documented the requirements through natural language. This is becaue it helps to identify which requirements are functional and non-functional.

![documented and prioritised requirements](https://github.com/ucl-comp0035/coursework-1-Yaseen048/blob/master/Pictures/Requirements_table.png)


## Design
### Structure and flow of the interface
The wireframes below provides a visual of the user inteface of the web app and dashboard.

The four wireframes represent the login/sign up page, the dashboard, a news page and finally a suggestion and improvement page.

This is designed for desktop use as it would be easier for the target audince to view the different graphs and statistics at the same time which will help them when looking to compare or find insight without having to scroll up or down.

![sign in/up](https://github.com/ucl-comp0035/coursework-1-Yaseen048/blob/master/Pictures/wireframe1.png)

![dashboard](https://github.com/ucl-comp0035/coursework-1-Yaseen048/blob/master/Pictures/wireframe2.png)

![news](https://github.com/ucl-comp0035/coursework-1-Yaseen048/blob/master/Pictures/wireframe3.png)

![improvemenst/suggestions](https://github.com/ucl-comp0035/coursework-1-Yaseen048/blob/master/Pictures/wireframe4.png)

### Relational database design

### Application structure
I decided to use a data- driven approach to intially identify the entities in the system. Using my requirements table, i identified the nouns as users, dashboard, news and improvements which are the classes. I then repeated the method to identfy methods by highligting verbs within the requirements. Although I used the DDD approach, I found it slightly harder to identfy adejctives to represent the attributes of each class. However knowing the methods of the class made it possible to find the attributes.

The design pattern I considered was the MVC. I identfied four models: Login, Dashboard, news and improvements. The views are represented by the four wireframes above. The main method of the conrtoller was to update the views (for example changing from the dashbaord page to the news page).

UML class diagram:

Please note that I accidently forgot to add a upvote() method to the improvement class.

![UML class diagram](https://github.com/ucl-comp0035/coursework-1-Yaseen048/blob/master/Pictures/UML_class_diagram.png)

## Testing
### Choice of unit testing library

### Tests
The tests should be in a separate and appropriately named file/directory.

### Test results
Provide evidence that the tests have been run and the results of the tests (e.g. screenshot).

### Continuous integration (optional)
Consider using GitHub Actions (or other) to establish a continuous integration pipeline. If you do so then please provide a link to the .yml and a screenshot of the results of a workflow run.

## Weekly progress reports

Copy and paste from Moodle or use the following structure. Delete this instruction text.

What I did in the last week:

- item
- item

What I plan to do in the next week:

- item
- item

Issues blocking my progress (state ‘None’ if there are no issues):

- item
- item

### Report 1

### Report 2

### Report 3

### Report 4

## References

Delete this instruction text before submitting:

- Include references to any templates you have used.
- If you justify any of your choices with references then remember to also include these.
- Use any [referencing style](https://library-guides.ucl.ac.uk/referencing-plagiarism/referencing-styles) that you are
  used to using in your course.

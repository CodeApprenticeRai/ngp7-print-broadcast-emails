"# ngp7-print-broadcast-emails"

## Instructions to Run
1. Create auth.json file and enter api key. Example:
```{"apiKey": "4EBE5864-F8F4-433C-8706-5651BB88BA33"}```
2. Run ```python take_home_problem.py```

## Follow Up Questions
1. __How long, roughly, did you spend working on this project? This won’t affect your evaluation; it helps us norm our problems to our expected time to complete them.__  
I spent about an hour or two working on the project. 

2. __Give the steps needed to deploy and run your code, written so that someone else can follow and execute them.__  
See above __Instructions to Run__ section. 

3. __What could you do to improve your code for this project if you had more time? Could you make it more efficient, easier to read, more maintainable? If it were your job to run this report monthly using your code, could it be made easier or more flexible? Give specifics where possible.__  
I could tie the apiKey generation process into the code to make ait fully automated.  
I could write a front-end for the project or write integrations so that it run well with other code. 

4. __Outline a testing plan for this report, imagining that you are handing it off to someone else to test. What did you do to test this as you developed it?__  
Request made from the program should return ```<200> Status Code``` responses. I would test the pagination, that is, in the cases there are more than 25 requests, pagination would be required in the program, and I would test that it return the correct number of emails (total emails available) at the end. 

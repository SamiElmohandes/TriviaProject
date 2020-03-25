# Full Stack API Final Project

## Full Stack Trivia

Udacity is invested in creating bonding experiences for its employees and students. A bunch of team members got the idea to hold trivia on a regular basis and created a  webpage to manage the trivia app and play the game, but their API experience is limited and still needs to be built out. 

That's where you come in! Help them finish the trivia app so they can start holding trivia and seeing who's the most knowledgeable of the bunch. The application must:

1) Display questions - both all questions and by category. Questions should show the question, category and difficulty rating by default and can show/hide the answer. 
2) Delete questions.
3) Add questions and require that they include question and answer text.
4) Search for questions based on a text query string.
5) Play the quiz game, randomizing either all questions or within a specific category. 

Completing this trivia app will give you the ability to structure plan, implement, and test an API - skills essential for enabling your future applications to communicate with others. 

## Tasks

There are `TODO` comments throughout project. Start by reading the READMEs in:

1. [`./frontend/`](./frontend/README.md)
2. [`./backend/`](./backend/README.md)

We recommend following the instructions in those files in order. This order will look familiar from our prior work in the course.

## Starting and Submitting the Project

[Fork](https://help.github.com/en/articles/fork-a-repo) the [project repository]() and [Clone](https://help.github.com/en/articles/cloning-a-repository) your forked repository to your machine. Work on the project locally and make sure to push all your changes to the remote repository before submitting the link to your repository in the Classroom. 

## About the Stack

We started the full stack application for you. It is desiged with some key functional areas:

### Backend

The `./backend` directory contains a partially completed Flask and SQLAlchemy server. You will work primarily in app.py to define your endpoints and can reference models.py for DB and SQLAlchemy setup. 

### Frontend

The `./frontend` directory contains a complete React frontend to consume the data from the Flask server. You will need to update the endpoints after you define them in the backend. Those areas are marked with TODO and can be searched for expediency. 

Pay special attention to what data the frontend is expecting from each API response to help guide how you format your API. 

[View the README.md within ./frontend for more details.](./frontend/README.md)

## API Documentation

### Introduction

* Base URL:  This application's backend is hosted at http://127.0.0.1:5000/
* Authentication: This API does not require authentication.

### Error Handling
Errors are returned in JSON format as following:

 
    {
      "success": False,
      
      "error": 404,
      
      "message": "not found"
    }
    
    {
      "success": False,
      "error": 422,
      "message": "unprocessable "
    }
    
    {
      "success": False,
      "error": 400,
      "message": "bad request"
    }
    
    {
      "success": False,
      "error": 500,
      "message": "Internal Server Error"
    }
    


The API will return the following error types:

* 400: bad request
* 404: resource not found
* 422: unable to process request
* 500: internal server error

### Endpoints
#### GET /categories
* Fetches a dictionary of all available categories
* Request arguments: None
* Curl Sample: curl http://127.0.0.1:5000/categories
* Sample Response   
   
           {
            "categories": {
               "id": 1,
      "type": "Science"
    
      "id": 2,
      "type": "Art"
    
      "id": 3,
      "type": "Geography"
    
      "id": 4,
      "type": "History"
     
      "id": 5,
      "type": "Entertainment"
   
      "id": 6,
      "type": "Sports"
            }, 
           "no_of_categories": 6,
           "success ": true 
        }

#### GET /questions
* Fetches a dictionary of all questions from all categories
* Request arguments: None
* Curl Sample: curl http://127.0.0.1:5000/questions OR http://127.0.0.1:5000/questions?page=[number]
* Sample Response   
   
           {
          "answer": "Agra",
          "category": 3,
          "difficulty": 2,
          "id": 15,
          "question": "The Taj Mahal is located in which Indian city?"

            }, 
             "Total_no_of_questions": 1,
             "current_category": null,
             "no_of_questions": 1,
             "success ": true
             }
             
             
             
#### DELETE /questions/<question_id>
* Deletes the question with the specified ID
* Request arguments: question_id
* Curl Sample: curl -X "DELETE" http://localhost:5000/questions/<question_id>
* Sample Response

         {
           "deleted": 2,
           "success": true

             }
             
             
#### POST /questions
* Adds a new question 
* Request arguments: question_question , question_answer , question_difficulty , question_category
* Curl Sample: curl -X POST -H "Content-Type: application/json" -d '{"question":"value1","answer":"value2","difficulty":"2","category":"3"}' http://localhost:5000/questions

* Sample Response

         {
           "success": true
            
            }
             
#### SEARCH /questions    
* Searches for a question with the keyword provided 
* Request arguments: SearchTerm
* Curl Sample: curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{"searchTerm": "beetle"}'
* Sample Response

         {
           "questions": [
         {
      "answer": "Scarab",
      "category": 4,
      "difficulty": 4,
      "id": 23,
      "question": "Which dung beetle was worshipped by the ancient Egyptians?"
       }
       ],
       "success": true,
       "total_questions": 1
       }
   
   
#### GET QUESTIONS BY CATEGORY /categories/<int:id>/questions
* Searches for questions within the specified category. 
* Request arguments: Category ID
* Curl Sample: curl http://127.0.0.1:5000/categories/(category_id)/questions
* Sample Response

      {
      "questions": [
        {
      "answer": "The Liver",
      "category": 1,
      "difficulty": 4,
      "id": 20,
      "question": "What is the heaviest organ in the human body?"
       },
      {
      "answer": "Alexander Fleming",
      "category": 1,
      "difficulty": 3,
      "id": 21,
      "question": "Who discovered penicillin?"
       },
       {
      "answer": "Blood",
      "category": 1,
      "difficulty": 4,
      "id": 22,
      "question": "Hematology is a branch of medicine involving the study of what?"
      }
      ],
      "success": true,
      "total_questions": 3
        }
        
        
#### POST QUIZ /quizzes
* Play the quiz . 
* Request arguments: previous_questions , quiz_category
* Curl Sample Example: curl curl -X POST http://localhost:5000/quizzes -d'{"previous_questions": [5,9], "quiz_category": {"id": 4, "type":   "History"}}' -H "Content-Type: application/json"


* Sample Response

      {
      "question": {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
       },
      "success": true
        }
        
        
        

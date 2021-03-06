# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

## Tasks

One note before you delve into your tasks: for each endpoint you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior. 

1. Use Flask-CORS to enable cross-domain requests and set response headers. 
2. Create an endpoint to handle GET requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories. 
3. Create an endpoint to handle GET requests for all available categories. 
4. Create an endpoint to DELETE question using a question ID. 
5. Create an endpoint to POST a new question, which will require the question and answer text, category, and difficulty score. 
6. Create a POST endpoint to get questions based on category. 
7. Create a POST endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question. 
8. Create a POST endpoint to get questions to play the quiz. This endpoint should take category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions. 
9. Create error handlers for all expected errors including 400, 404, 422 and 500. 

## API Reference
### Error Handling
Errors are returned as json objects in the following format
```
{
        "success": False, 
        "error": 404,
        "message": "Not found"
}
{
        "success": False, 
        "error": 422,
        "message": "unprocessable"
}
{
        "success": False, 
        "error": 500,
        "message": "internal server error"
}
{
        "success": False, 
        "error": 400,
        "message": "bad request"
}
```
### Endpoints

#### GET '/categories'
- Return all categories in object with key and value 
- Sample : curl -X GET http://127.0.0.1:5000/categories
or
- curl http://127.0.0.1:5000/categories
```
{
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports"
  }, 
  "success": true
}
```
#### GET '/questions'
- Return all questions objects, total questions, categories, current_category
- For each page only 10 questions via request argument to select page number start from one, by default set page one 
- Sample : curl -X GET http://127.0.0.1:5000/questions
or
- curl http://127.0.0.1:5000/questions
```
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "current_category": [
    2,
    3,
    4
  ],
  "questions": [
    {
      "answer": "George Washington Carver",
      "category": 2,
      "difficulty": 4,
      "id": 2,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": 2,
      "difficulty": 3,
      "id": 3,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 4,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    },
    {
      "answer": "Agra",
      "category": 2,
      "difficulty": 3,
      "id": 5,
      "question": "The Taj Mahal is located in which Indian city?"
    },
    {
      "answer": "Mona Lisa",
      "category": 3,
      "difficulty": 2,
      "id": 6,
      "question": "La Giaconda is better known as what?"
    },
    {
      "answer": "one",
      "category": 4,
      "difficulty": 2,
      "id": 7,
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    },
    {
      "answer": "The Liver",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What is the heaviest organ in the human body?"
    },
    {
      "answer": "Alexander Fleming",
      "category": 3,
      "difficulty": 1,
      "id": 10,
      "question": "Who discovered penicillin?"
    },
    {
      "answer": "Blood",
      "category": 4,
      "difficulty": 1,
      "id": 11,
      "question": "Hematology is a branch of medicine involving the study of what?"
    },
    {
      "answer": "Scarab",
      "category": 4,
      "difficulty": 4,
      "id": 12,
      "question": "Which dung beetle was worshipped by the ancient Egyptians?"
    }
  ],
  "success": true,
  "total_questions": 13
}
```
#### DELETE '/questions/<int:question_id>'
- delete the question of given id if exist
-return id and success
- Sample : curl http://127.0.0.1:5000/questions/12 -X DELETE
```
{
  "id": 12,
  "success": true
}
```
#### POST '/questions'
- add new question, answer for question, category and difficulty
- return the id of question with total question after added
- Sample : curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{"question": "what is srs in software engineering?", "answer": "software requirements specification", "category": 1,"difficulty": 1}'
```
{
  "question_id_created": 16,
  "total_question":13
  "success": true
}
```
#### POST '/categories/<int:category_id>/questions'
- return all questions based on category and success value
- Sample : curl http://127.0.0.1:5000/categories/1/questions OR
- curl -x GET http://127.0.0.1:5000/categories/1/questions
```
{
  "questions": [
    {
      "answer": "xsdsd",
      "category": 1,
      "difficulty": 5,
      "id": 13,
      "question": "what is xdd?"
    },
    {
      "answer": "Software requirements specification",
      "category": 1,
      "difficulty": 1,
      "id": 14,
      "question": "what is srs"
    },
    {
      "answer": "Software requirements specification",
      "category": 1,
      "difficulty": 4,
      "id": 15,
      "question": "what is srs"
    }
  ],
  "success": true
}
```
#### POST '/questions'
- Search for question(s) use searchTerm
- return question(s) have relevant with searchTerm and sccuess value
- Sample: curl -X POST http://127.0.0.1:5000/questions -H 'content-type: application/json' -d '{"searchTerm": "srs"}'
```
{
    "questions":[ 
        {
      "answer": "Software requirements specification",
      "category": 1,
      "difficulty": 1,
      "id": 14,
      "question": "what is srs"
    },
    {
      "answer": "Software requirements specification",
      "category": 1,
      "difficulty": 4,
      "id": 15,
      "question": "what is srs"
    }],
    "count": 2,
    "success":true
}

```
#### POST '/quizzes'
- get random question for specific category OR all categories 
- return random question and success value
- Sample: curl -X POST http://127.0.0.1:5000/quizzes -H 'content-type: application/json' -d '{"previous_questions": [],"quiz_category": { "id": 1", type": "Science"}}'
```
{
    "question": {
      "answer": "Software requirements specification",
      "category": 1,
      "difficulty": 1,
      "id": 14,
      "question": "what is srs"
    },
    "success":true
}

```
## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```
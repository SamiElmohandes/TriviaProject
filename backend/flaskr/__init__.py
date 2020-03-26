import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def paginatee(request, selection):
        page = request.args.get('page', 1, type=int)
        start = (page - 1) * QUESTIONS_PER_PAGE
        end = start + QUESTIONS_PER_PAGE

        items = [item.format() for item in selection]
        current_items = items[start:end]

        return current_items



def create_app(test_config=None):
  # create and configure the app
  #app = Flask(__name__)
 app = Flask(__name__)

 setup_db(app)
 cors = CORS(app, resources={r"/api/*": {"origins": "*"}}) 







 @app.after_request
 def after_request(response):
     response.headers.add('Access-Contro-Allow-Headers','Content-Type ,Authorization')
     response.headers.add('Access-Contro-Allow-Methods','GET, POST ,PATCH , DELETE ,OPTIONS')
     #response.headers.add('Access-Control-Allow-Origin' ,  'http://localhost:3000')
     return response 


 @app.route('/')
 def index():
    return jsonify({'message' : 'Hello'})



 @app.route('/categories', methods=['GET'])
 def get_categories():
   selection = Category.query.all()
   #categories = [category.format() for category in selection]

   return jsonify({
    'success': True ,
    'categories': [category.type for category in selection]
    #'no_of_categories' : len(categories)
        })

  
 @app.route('/questions', methods=['GET'])
 def get_questions():
  selection = Question.query.all()
  questions = paginatee(request, selection)
  categories = Category.query.all()
  #categories = all_categories().get_json()["categories"]
  return jsonify({
    'success': True ,
    'questions': questions,
    #'no_of_questions' : len(questions),
    'totalQuestions' : len(selection),
    'categories': [category.type for category in categories],
    'currentCategory': None,
    #'categories': categories
        })

  '''
  @TODO: 
  Create an endpoint to DELETE question using a question ID. 

  TEST: When you click the trash icon next to a question, the question will be removed.
  This removal will persist in the database and when you refresh the page. 
  '''
 @app.route('/questions/<int:question_id>', methods=['DELETE'])
 def delete_question(question_id):
    question = Question.query.filter(Question.id == question_id).one_or_none()
    if question is None:
        abort(404)
    
    question.delete()

    return jsonify({
                'success': True,
                'deleted': question_id,
            })
    



 @app.route('/questions', methods=['POST'])
 def create_question():
  try:
    body = request.get_json()
    new_question = body.get('question', None)
    new_answer = body.get('answer', None)
    new_category = body.get('category', None)
    new_difficulty = body.get('difficulty', None)
    search=body.get('searchTerm')
    if search:
     questions = Question.query.filter(Question.question.ilike(f'%{search}%')).all()
     if questions:
      current_questions = paginatee(request, questions)
      return jsonify({
          'success': True,
          'questions': current_questions,
          'totalQuestions': len(questions),
          'currentCategory': None
        })
     else:
          abort(404)
    else:
     question = Question(question=new_question, answer=new_answer, category=new_category, difficulty=new_difficulty)
     question.insert()
     return jsonify({
                'success': True
            })

  except:
    abort(422)



 @app.route('/categories/<int:id>/questions', methods=['GET'])
 def get_questions_by_category(id):
  selection = Question.query.filter(Question.category==str(id)).all()
  questions = paginatee(request, selection)
  category= Category.query.filter(Category.id == id).one_or_none()

  if len(questions) == 0:
   abort(404)

  else:
   return jsonify({
      'success': True,
      'questions': questions,
      'totalQuestions': len(selection),
      'currentCategory': category.type
        })



 @app.route('/quizzes', methods=['POST'])
 def post_quiz():
    try:
      body = request.get_json()
      previous_questions = body.get('previous_questions', None)
      quizCategory = body.get('quiz_category')
      if quizCategory["id"] :
        selection = Question.query.filter(~Question.id.in_(previous_questions), Question.category == quizCategory["id"]).all()
      else:
        selection = Question.query.filter(~Question.id.in_(previous_questions)).all()

      if selection:
        question = random.choice(selection).format()
      else:
        question= None 
      
      return jsonify({
        'success' : True,
        'question' : question
      })
    except:
      abort(422)









 @app.errorhandler(404)
 def not_found(error):
    return jsonify({
      "success": False,
      "error": 404,
      "message": "not found"
    }), 404

 @app.errorhandler(422)
 def unprocessable_entity(error):
    return jsonify({
      "success": False,
      "error": 422,
      "message": "unprocessable "
    }), 422

 @app.errorhandler(400)
 def bad_request(error):
    return jsonify({
      "success": False,
      "error": 400,
      "message": "bad request"
    }), 400
  
 @app.errorhandler(500)
 def not_allowed(error):
    return jsonify({
      "success": False,
      "error": 500,
      "message": "Internal Server Error"
    }), 500
  
 
 
 
 return app

    

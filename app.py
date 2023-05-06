from flask import Flask, request
from services.task.create import create_sum_two_numbers, create_hello_world, create_query_chat_gpt
from models.db.DB import DB
from services.task.retreive import retrieve


app = Flask(__name__)
localDB = DB()


@app.route('/sum_two_numbers', methods=['POST'])
def sum_two_numbers():
    first_num = request.json["firstNum"]
    second_num = request.json["secondNum"]
    return {'res': create_sum_two_numbers(first_num, second_num)}


@app.route('/query_chat_gpt', methods=['POST'])
def query_chat_gpt():
    prompt = request.json["prompt"]
    return {'res': create_query_chat_gpt(prompt)}


@app.route('/hello_world', methods=['POST'])
def hello_world():
    return {'res': create_hello_world()}


@app.route('/tasks/<task_id>', methods=['GET'])
def get_task_result(task_id):
    return {'res': retrieve(task_id)}


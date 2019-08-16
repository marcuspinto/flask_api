# encoding: utf-8
from flask import Flask, request, current_app, jsonify, render_template
import json

application = Flask(__name__)

@application.route("/")
def hello_world():
    return "Hello World! <strong>I am learning Flask</strong>", 200

@application.route("/<name>")
def index(name):
    if name.lower() == "marcus":
        return "Olá {}".format(name), 200
    else:
        return "Not Found", 404

@application.route("/test/")
@application.route("/test/<name>")
def test(name=None):
    if name:
        return "Olá, %s!" % name
    else:
        return "Olá, usuário!"


@application.route("/html/<nome>")
def html_page(nome):
    return render_template("template.html", nome=nome)

@application.route("/get/", methods=['GET'])
def get_api():
    pessoas = [
            {"nome": "Method: GET"},
            {"nome": "Bruno Rocha"},
            {"nome": "Arjen Lucassen"},
            {"nome": "Anneke van Giersbergen"},
            {"nome": "Steven Wilson"}]
    return json.dumps(pessoas), 200, {"Content-Type": "application/json"}

@application.route("/get/", methods=['POST'])
def get_post_api():
    pessoas = [
            {"nome": "Method: POST GET"},
            {"nome": "Bruno Rocha"},
            {"nome": "Arjen Lucassen"},
            {"nome": "Anneke van Giersbergen"},
            {"nome": "Steven Wilson"}]
    return json.dumps(pessoas), 200, {"Content-Type": "application/json"}

@application.route("/post/", methods=['POST'])
def post_api():
    pessoas = [
            {"nome": "Method: POST"},
            {"nome": "Bruno Rocha"},
            {"nome": "Arjen Lucassen"},
            {"nome": "Anneke van Giersbergen"},
            {"nome": "Steven Wilson"}]
    return json.dumps(pessoas), 200, {"Content-Type": "application/json"}

@application.route("/pessoas/", methods=['GET', 'POST'])
def json_api():
    if request.method == 'POST':
        pessoas = [
               {"nome": "Method: POST"},
               {"nome": "Bruno Rocha"},
               {"nome": "Arjen Lucassen"},
               {"nome": "Anneke van Giersbergen"},
               {"nome": "Steven Wilson"}]
    else:
        pessoas = [
               {"nome": "Method: GET"},
               {"nome": "Bruno Rocha"},
               {"nome": "Arjen Lucassen"},
               {"nome": "Anneke van Giersbergen"},
               {"nome": "Steven Wilson"}]
    return json.dumps(pessoas), 200, {"Content-Type": "application/json"}
    #from flask import jsonify
    #return jsonify(pessoas=pessoas, total=len(pessoas))
    
@application.route("/show_config")
def show_config():
    querystring_args = request.args.to_dict()
    post_args = request.form.to_dict()
    return jsonify(
        debug=current_app.config.get('DEBUG'),
        args=querystring_args,
        vars=post_args,
        method=request.method
    )
    
application.run()

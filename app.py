 
from bll.Authentication_BLL import *
from enu.Access import *
from flask import Flask, request, jsonify

app = Flask(__name__)
    
@app.route("/door/<rf_id>", methods=["GET"])
def open_door(rf_id):
    
    print("teste")
    pass
    '''
    uthentication_bll  = Authentication_BLL()
    
    access = authentication_bll.authenticate_person(rf_id)
    
    if  access == Access.AUTHORIZED:
        return jsonify([{f'access : {Access.AUTHORIZED}'}]),200
    if access == Access.SUSPENDED:
        return jsonify([{f'access : {Access.SUSPENDED}'}]),401
    return jsonify([{f'access : {Access.BLOQUED}'}]),401
    '''

if __name__ == '__main__':
    app.run(debug=True)
#!flask/bin/python
from flask import Flask, jsonify
from flask import request
from flask import abort
from flask import make_response
from datetime import datetime

import loadData

#http://127.0.0.1:5000/tasks?gymId=0&people_count=true&date=2017/SEP/05


app = Flask(__name__)
@app.route('/tasks', methods=['GET'])
def get_tasks():
    gymId = request.args.get('gymId')
    date = request.args.get('date')
    time = request.args.get('time')
    people_count = request.args.get('people_count')
    equipment_stats = request.args.get('equipment_stats')
    record = loadData.dataExtraction(loadData.PATH)
    today = datetime(2017,9,05,19,15,00)
    #return jsonify(record[today].serialize(0))


    if gymId!='0':
        abort(404)
    if people_count=='true' and equipment_stats==None and time==None and date!=None:
        date = datetime.strptime(date, '%Y/%b/%d')
        completeTime = date.replace(hour=12,minute=15,second=0)
        jsonResult = record[completeTime].serialize(0)
        jsonResult['people_visited']=500
        return jsonify(jsonResult)
    elif equipment_stats:
        pass
    else:
        abort(400)
    a = loadData.dataExtraction(loadData.PATH)[0]
    return jsonify(loadData.dataExtraction(loadData.PATH)[0].serialize())

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'parameter not supported'}), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run()
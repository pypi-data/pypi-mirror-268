import os
import sys
from flask import Flask, request, jsonify
from .config_drumpler import ConfigDrumpler
import json
from flask_sqlalchemy import SQLAlchemy
from .sql_base import Base
from .sql_request import SqlRequest
from .sql_job import SqlJob
from .sql_event import SqlEvent

app = Flask(__name__)
db = SQLAlchemy()
Base.metadata.bind = db.engine

class Drumpler:
    def __init__(self):
        self.__init_env()
        self.app = Flask(__name__)
        self.AUTHORIZATION_KEY = ConfigDrumpler.AUTHORIZATION_KEY

        # Fetching environment variables or using defaults
        self.host = os.environ.get("DRUMPLER_HOST", ConfigDrumpler.DRUMPLER_HOST)
        self.port = os.environ.get("DRUMPLER_PORT", ConfigDrumpler.DRUMPLER_PORT)
        self.debug = os.environ.get("DRUMPLER_DEBUG", ConfigDrumpler.DRUMPLER_DEBUG)
        
        self.app.config['SQLALCHEMY_DATABASE_URI'] = ConfigDrumpler.DATABASE_URI
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        # Initialize SQLAlchemy with the Flask app here instead of global scope
        db.init_app(self.app)

        with self.app.app_context():
            Base.metadata.create_all(db.engine)  # Ensure this is Base.metadata.create_all
            
        self.__setup_routes()

    def __setup_routes(self):
        self.app.add_url_rule('/', view_func=self.hello_world, methods=['GET'])
        self.app.add_url_rule('/request', view_func=self.__process_request, methods=['POST'])
        self.app.add_url_rule('/request/<int:request_id>', view_func=self.__get_request, methods=['GET'])
        self.app.add_url_rule('/request/next-unhandled', view_func=self.__get_next_unhandled_request, methods=['GET'])
        self.app.add_url_rule('/request/<int:request_id>', view_func=self.__update_request, methods=['PUT'])
        self.app.add_url_rule('/request/<int:request_id>', view_func=self.__delete_request, methods=['DELETE'])
        self.app.add_url_rule('/jobs', view_func=self.__create_job, methods=['POST'])
        self.app.add_url_rule('/jobs/<int:job_id>', view_func=self.__update_job, methods=['PUT'])
        self.app.add_url_rule('/events', view_func=self.__create_event, methods=['POST'])

    def __init_env(self):
        if not os.path.exists(".env"):
            sys.exit("ERROR! You must create a .env file that contains a single line 'AUTHORIZATION_KEY=YourAuthorizationKeyHere'")

    def __authorize_request(self):
        authorization = request.headers.get('Authorization')
        return authorization and authorization == f"Bearer {self.AUTHORIZATION_KEY}"
    
    def hello_world(self):
        return "Hello World"

    def __process_request(self):
        if not self.__authorize_request():
            return jsonify({"message": "Invalid or missing authorization"}), 401

        data = request.get_json() or {}  # Fallback to an empty dict if no JSON is provided
        custom_value = request.args.get('custom_value', None)

        new_request = SqlRequest(
            source_ip=request.remote_addr,
            user_agent=request.user_agent.string,
            method=request.method,
            request_url=request.url,
            request_raw=json.dumps(data),
            custom_value=custom_value
        )
        db.session.add(new_request)
        db.session.commit()
        return jsonify({"message": "Request processed successfully", "id": new_request.id}), 200
    
    def __get_next_unhandled_request(self):
        with db.session.begin():
            query = db.session.query(SqlRequest)\
                .filter(SqlRequest.is_handled == 0, 
                        SqlRequest.is_being_processed == False)
            custom_value = request.args.get('custom_value', None)
            if custom_value is not None:
                query = query.filter(SqlRequest.custom_value == custom_value)
            unhandled_request = query.order_by(SqlRequest.id)\
                .with_for_update(skip_locked=True).first()
            if unhandled_request:
                unhandled_request.is_being_processed = True
                request_data = {
                    "id": unhandled_request.id,
                    "timestamp": unhandled_request.timestamp.isoformat(),
                    "source_ip": unhandled_request.source_ip,
                    "user_agent": unhandled_request.user_agent,
                    "method": unhandled_request.method,
                    "request_url": unhandled_request.request_url,
                    "request_raw": unhandled_request.request_raw,
                    "custom_value": unhandled_request.custom_value,
                    "is_handled": unhandled_request.is_handled
                }
        if unhandled_request:
            return jsonify(request_data), 200
        else:
            return jsonify({"message": "No unhandled requests found."}), 404

    def __get_request(self, request_id):
        if not self.__authorize_request():
            return jsonify({"message": "Invalid or missing authorization"}), 401
        request_entry = SqlRequest.query.get(request_id)
        if request_entry:
            return jsonify({
                "id": request_entry.id,
                "timestamp": request_entry.timestamp.isoformat(),
                "source_ip": request_entry.source_ip,
                "user_agent": request_entry.user_agent,
                "method": request_entry.method,
                "request_url": request_entry.request_url,
                "request_raw": json.loads(request_entry.request_raw),
                "custom_value": request_entry.custom_value,
                "is_handled": request_entry.is_handled
            }), 200
        else:
            return jsonify({"message": "Request not found"}), 404

    def __update_request(self, request_id):
        if not self.__authorize_request():
            return jsonify({"message": "Invalid or missing authorization"}), 401
        request_entry = SqlRequest.query.get(request_id)
        if request_entry:
            data = request.get_json()
            request_entry.is_handled = data.get('is_handled', request_entry.is_handled)
            db.session.commit()
            return jsonify({"message": "Request updated successfully"}), 200
        else:
            return jsonify({"message": "Request not found"}), 404

    def __delete_request(self, request_id):
        if not self.__authorize_request():
            return jsonify({"message": "Invalid or missing authorization"}), 401
        request_entry = SqlRequest.query.get(request_id)
        if request_entry:
            db.session.delete(request_entry)
            db.session.commit()
            return jsonify({"message": "Request deleted successfully"}), 200
        else:
            return jsonify({"message": "Request not found"}), 404

    def __create_job(self):
        if not self.__authorize_request():
            return jsonify({"message": "Unauthorized access"}), 401
        data = request.get_json()
        new_job = SqlJob(request_id=data['request_id'], status='Pending')
        db.session.add(new_job)
        db.session.commit()
        return jsonify({'job_id': new_job.id}), 201

    def __update_job(self, job_id):
        if not self.__authorize_request():
            return jsonify({"message": "Unauthorized access"}), 401
        data = request.get_json()
        job = SqlJob.query.get(job_id)
        if job:
            job.status = data.get('status', job.status)
            job.finished_date = data.get('finished_date', job.finished_date)
            db.session.commit()
            return jsonify({"message": "Job updated successfully"}), 200
        else:
            return jsonify({"message": "Job not found"}), 404

    def __create_event(self):
        if not self.__authorize_request():
            return jsonify({"message": "Unauthorized access"}), 401
        data = request.get_json()
        new_event = SqlEvent(job_id=data['job_id'], message=data['message'])
        db.session.add(new_event)
        db.session.commit()
        return jsonify({'event_id': new_event.id}), 201

    def run(self):
        app.run(host=self.host, port=self.port, debug=self.debug)

if __name__ == '__main__':
    drumpler = Drumpler()
    drumpler.run()

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4
import os
import datetime
import hashlib
import base64
import logging
logger = logging.getLogger()

# Initialize Flask app
app = Flask(__name__)
# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///agents.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Agent model
class Agent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    api_key = db.Column(db.String(128), unique=True, nullable=False)
    uuid = db.Column(db.String(36), unique=True, nullable=True)
    last_ping = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f'<Agent {self.uuid}>'

class Pipeline(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(36), db.ForeignKey('agent.uuid'), nullable=False)
    name = db.Column(db.String(128), nullable=False)
    namespace = db.Column(db.String(128), nullable=False)
    yaml_content = db.Column(db.Text, nullable=False)  # Storing YAML content as text
    yaml_hash = db.Column(db.String(64), nullable=False)  # Storing the SHA-256 hash of the YAML content

    def __repr__(self):
        return f'<Pipeline {self.name} in {self.namespace}>'

# Initialize database within application context
with app.app_context():
    db.create_all()

def generate_api_key():
    """ Generate a unique API key using random bytes, converted to hexadecimal """
    return os.urandom(24).hex()

@app.route('/agent', methods=['POST'])
def create_agent():
    """ Endpoint to create a new agent with a unique API key """
    api_key = generate_api_key()
    new_agent = Agent(api_key=api_key)
    db.session.add(new_agent)
    db.session.commit()
    return jsonify({"api_key": api_key}), 201

@app.route('/agent', methods=['DELETE'])
def delete_agent():
    """ Endpoint to delete an agent from the database using an API key """
    api_key = request.headers.get('X-API-Key')
    if not api_key:
        return jsonify({"error": "API key is required"}), 400
    agent = Agent.query.filter_by(api_key=api_key).first()
    if agent:
        db.session.delete(agent)
        db.session.commit()
        return jsonify({"message": "Agent deleted"}), 200
    return jsonify({"error": "Invalid API key"}), 404

@app.route('/registration', methods=['POST'])
def register():
    """ Endpoint to register an agent using an API key; sets a UUID for the agent.
        Ensures that one API key can only be associated with one UUID. """
    api_key = request.headers.get('X-API-Key')
    if not api_key:
        return jsonify({"error": "API key is required"}), 400

    agent = Agent.query.filter_by(api_key=api_key).first()

    # Check if the API key is already associated with a UUID
    if agent is None:
        return jsonify({"error": "Invalid API key"}), 400
    elif agent.uuid:
        return jsonify({"error": "This API key is already registered with a UUID"}), 409

    # If the API key is valid and not yet registered, assign a new UUID
    agent.uuid = str(uuid4())
    db.session.commit()
    return jsonify({"uuid": agent.uuid}), 200


@app.route('/registration', methods=['DELETE'])
def deregister():
    """ Endpoint to deregister an agent by removing its UUID """
    api_key = request.headers.get('X-API-Key')
    uuid = request.headers.get('X-UUID')
    if not uuid:
        return jsonify({"error": "UUID is required"}), 400
    agent = Agent.query.filter_by(uuid=uuid, api_key=api_key).first()
    if agent:
        agent.uuid = None
        db.session.commit()
        return jsonify({"message": "Agent deregistered"}), 200
    return jsonify({"error": "Invalid UUID"}), 404


@app.route('/ping', methods=['POST'])
def ping():
    """ Endpoint to receive a ping from a registered agent; updates the last ping timestamp """
    api_key = request.headers.get('X-API-Key')
    uuid = request.headers.get('X-UUID')
    if not uuid:
        return jsonify({"error": "UUID is required"}), 400
    agent = Agent.query.filter_by(uuid=uuid, api_key=api_key).first()
    if agent:
        agent.last_ping = datetime.datetime.now()
        db.session.commit()
        return jsonify({"message": "Ping received"}), 200
    return jsonify({"error": "Invalid UUID"}), 404


@app.route('/pipeline', methods=['POST'])
def create_pipeline():
    api_key = request.headers.get('X-API-Key')
    uuid = request.headers.get('X-UUID')
    name = request.form['name']
    namespace = request.form['namespace']
    yaml_file = request.files.get('yaml_file')

    if not all([uuid, name, namespace, yaml_file]):
        return jsonify({"error": "All fields are required: uuid, name, namespace, and yaml_file"}), 400

    # Ensure the file is a YAML file
    if not yaml_file.filename.endswith('.yaml'):
        return jsonify({"error": "File must be a YAML file"}), 400

    # Read and encode the content of the YAML file
    yaml_content = base64.b64encode(yaml_file.read())

    agent = Agent.query.filter_by(uuid=uuid).first()
    if not agent:
        return jsonify({"error": "No agent found with the provided UUID"}), 404

    # Calculate the SHA-256 hash of the YAML content
    hash_object = hashlib.sha256()
    hash_object.update(yaml_content)
    yaml_hash = hash_object.hexdigest()

    new_pipeline = Pipeline(uuid=uuid, name=name, namespace=namespace, yaml_content=yaml_content, yaml_hash=yaml_hash)
    db.session.add(new_pipeline)
    db.session.commit()

    return jsonify({"message": f"Pipeline '{name}' created successfully"}), 201

@app.route('/pipeline', methods=['GET'])
def fetch_pipelines():
    api_key = request.headers.get('X-API-Key')
    uuid = request.headers.get('X-UUID')

    if not api_key or not uuid:
        return jsonify({"error": "Both API_KEY and UUID headers are required"}), 400

    agent = Agent.query.filter_by(api_key=api_key, uuid=uuid).first()
    if not agent:
        return jsonify({"error": "No agent found with the provided API_KEY and UUID"}), 404

    pipelines = Pipeline.query.filter_by(uuid=uuid).all()
    pipelines_data = [{
        "name": pipeline.name,
        "namespace": pipeline.namespace,
        "hash": pipeline.yaml_hash
    } for pipeline in pipelines]

    return jsonify(pipelines_data), 200

@app.route('/pipeline/<namespace>/<name>', methods=['GET'])
def get_pipeline_yaml(namespace, name):
    api_key = request.headers.get('X-API-Key')
    uuid = request.headers.get('X-UUID')
    if not all([api_key, uuid, namespace, name]):
        return jsonify({"error": "API_KEY, UUID, namespace, and name are required"}), 400

    agent = Agent.query.filter_by(api_key=api_key, uuid=uuid).first()
    if not agent:
        return jsonify({"error": "No agent found with the provided API_KEY and UUID"}), 404

    pipeline = Pipeline.query.filter_by(uuid=uuid, name=name, namespace=namespace).first()
    if not pipeline:
        return jsonify({"error": "No pipeline found matching the criteria"}), 404

    return jsonify({"yaml_content": pipeline.yaml_content.decode('utf-8')}), 200

def start_app():
    # Run the Flask app with debugging turned off in production
    app.run(host="0.0.0.0", port=8080, debug=True)

import flask from Flask, render_template
import os
from flask_cors import CORS

app = Flask( __name__, templates_folder='templates')
CORS(app)

@app.route('/')
def index():
	return 'Hello World!'

if __name__ == '__main__' :
	app.run( debug=True, host='0.0.0.0', port=int( os.getenv( 'VCAP_APP_PORT', '8000' )))


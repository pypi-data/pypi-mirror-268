
'''
	python3 /apoplast/venues/stages/apoplast/_interfaces/sanic/__init__.py
	
	sanic /apoplast/venues/stages/apoplast/_interfaces/sanic
'''

'''
	itinerary:
		[ ] pass the current python path to this procedure
'''



'''
	https://sanic.dev/en/guide/running/manager.html#dynamic-applications
'''

'''
	worker manager:
		https://sanic.dev/en/guide/running/manager.html
'''

'''
	Asynchronous Server Gateway Interface, ASGI:
		https://sanic.dev/en/guide/running/running.html#asgi
		
		uvicorn harbor:create
'''

'''
	--factory
'''

import json
import os
import traceback

USDA_food_ellipse = os.environ.get ('USDA_food')
NIH_supp_ellipse = os.environ.get ('NIH_supp')

import apoplast.clouds.food_USDA.deliveries.one as retrieve_1_food
import apoplast.clouds.food_USDA.nature_v2 as food_USDA_nature_v2

from sanic import Sanic
import sanic.response as sanic_response
#from sanic_swagger import swagger_blueprint

'''
	https://sanic.dev/en/guide/running/running.html#using-a-factory
'''
def create ():
	
	'''
		#
		#	https://sanic.dev/en/guide/running/configuration.html#inspector
		#
		INSPECTOR_PORT
	'''
	app = Sanic (__name__)
	app.config.INSPECTOR = True
	app.config.INSPECTOR_HOST = "0.0.0.0"
	app.config.INSPECTOR_PORT = "6457"
	
	
	#app.blueprint(swagger_blueprint)

	@app.route ("/")
	async def home (request):
		return sanic_response.text ("home")
	
	
	@app.route ("/off")
	async def off (request):
		return sanic_response.text ("not possible")
		
	
	@app.route ("/PID")
	async def PID (request):
		return sanic_response.text ("not possible")
	
	@app.websocket('/ws')
	async def ws_handler(request, ws):
		while True:
			data = await ws.recv ()  # Receive data from the client
			await ws.send(f"Echo: {data}")  # Send the received data back to the client
	
	#
	#	#@app.route ("/USDA/food")
	#
	'''
		
	'''
	@app.patch('/USDA/food_v2')
	async def USDA_food (request, name):
		data = request.json
	
		return json.dumps (data, indent = 4)
		
	
	
	'''
		 2369390
	'''
	@app.route ('/USDA/food_v2/FDC_ID/<id>')
	async def USDA_food_FDC_ID (request, id):
		FDC_ID = id
	
		try:
			print ('food_USDA parse?')
		
			food_USDA = retrieve_1_food.presently (
				FDC_ID = FDC_ID,
				API_ellipse = USDA_food_ellipse
			)
		except Exception as E:
			traceback_str = traceback.format_exc()
			print (traceback_str)
			return sanic_response.text ("USDA food API call exception:" + str (E))
			
		try:
			print ('food_USDA')
			
			nature = food_USDA_nature_v2.create (food_USDA ["data"])
			
			return sanic_response.json (nature)
			
		except Exception as E:
			traceback_str = traceback.format_exc()
			print (traceback_str)
			
			return sanic_response.text ("exception:" + str (E))
		
		return sanic_response.text (str (id))
		
	@app.patch ("/NIH/supp")
	async def NIH_supp (request):
		data = request.json
	
		return sanic_response.json (json.dumps (data, indent = 4))
		
	return app


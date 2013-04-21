import web
render = web.template.render('templates/')

#urls = (
#		'/', 'index'
#		)

urls = (
		'/(.*)', 'index'
		)

class index:
	def GET(self, name):
		return render.index(name)
		#3.i = web.input(name=None)
		#3.return render.index(i.name)


		#2.name = 'Bob'
		#2.return render.index(name)
		
		#1.return "Hello, world! \nThis is xsy257@murphy!"

if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()

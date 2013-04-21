import web
import os

urls = (
		'/', 'index',
		)

class index:
	def GET(self):
		return "\nHello, world! \nThis is xsy257@murphy!\n\n"

	def POST(self):
		post_data = web.input()
		vertexName = post_data.vertex_name

		idFile = os.popen("curl \"http://localhost:8182/graphs/graph/tp/gremlin?script=g.V('name','" + vertexName + "').id()\"")
		idContent = idFile.read(16)
		id = filter(str.isdigit, idContent)

		neighborFile = os.popen("curl \"http://localhost:8182/graphs/graph/vertices/" + id + "/both\"")
		neighborContent = neighborFile.readlines()

		result = vertexName + '\'s neighbor(s):\n'

		for eachline in neighborContent:
			strlist = eachline.split('}')
			for value in strlist:
				value = value[value.find('\"name\"'):]
				value = value[:value.find(',')]
				flag = result.find(value)
				if flag == -1:
					result = result + value + '\n'

		return '\n' + result + '\n' 

if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()

try:


    import pdb
    pdb.set_trace()#import os
#os.system("pip install sanic")
    from sanic import Sanic
    from sanic.response import json

except ModuleNotFoundError:
    import os
    import pdb
    pdb.set_trace()
    os.system("pip install -r requirements.txt")
from sanic import Sanic
from sanic.response import json

app = Sanic("MyHelloworldapp")

@app.route('/')
async def test(request):
    return json({'hello': 'world'})

if __name__ == '__main__':
    app.run()

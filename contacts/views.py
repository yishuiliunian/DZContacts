from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from contacts.models import DZContact
from contacts.serializers import DZContactSerializer
import pdb
class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders it's content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)
        pass
pass
@csrf_exempt
def contact_list(request):
    if request.method == 'GET':
        contacts = DZContact.objects.all()
        serializer = DZContactSerializer(contacts)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DZContactSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status = 201)
        else:
            return JSONResponse(serializer.data, status = 400)

def user_avater(request):
    image_data = open('/Users/dzpqzb/Downloads/avater.jpeg', 'rb').read()
    return HttpResponse(image_data, mimetype = "image/jpeg")

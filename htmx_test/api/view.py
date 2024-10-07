from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import OperaSerializer

from ..forms import OperaForm
from ..models import Opera


@api_view(['GET'])
def api_opera_list(request):
    operas = Opera.objects.all()
    serializer = OperaSerializer(operas, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def api_opera_add(request):
    serializer = OperaSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def api_opera_update(request, pk):
    opera = Opera.objects.get(id=pk)
    serializer = OperaSerializer(instance=opera, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def api_opera_delete(request, pk):
    opera = Opera.objects.get(id=pk)
    opera.delete()

    return Response(f'Opera {opera.title} was successfully deleted!')
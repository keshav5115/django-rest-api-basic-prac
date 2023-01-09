from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from restapp.api.serilizers import movieserial
from restapp.models import Movie
@api_view(['GET','POST'])
def movielist(request):
    movie=Movie.objects.all()
    serilizer=movieserial(movie,many=True)
    if request.method =='POST':
        serilizer=movieserial(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data)
        else:
            return Response(serilizer.errors)
    return Response(serilizer.data)


@api_view(['GET','PUT','DELETE'])
def movieone(request,pk):
    if request.method =='GET':
        try:
            movie=Movie.objects.get(id=pk)
        except Movie.DoesNotExist :
            content='page not existed'
            return Response(content,status.HTTP_404_NOT_FOUND)
        serilizer=movieserial(movie)
        return Response(serilizer.data)
    if request.method == 'PUT':
        movie=Movie.objects.get(id=pk)
        serilizer=movieserial(instance=movie,data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data)
        else:
            return Response(serilizer.errors,status.HTTP_400_BAD_REQUEST)

    if request.method =='DELETE':
        movie=Movie.objects.get(id=pk).delete()
        content='movie was not there'
        return Response(content,status.HTTP_204_NO_CONTENT)



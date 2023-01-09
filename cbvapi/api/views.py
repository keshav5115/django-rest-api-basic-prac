from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import APIView
from cbvapi.api.serilizers import MovieSerial
from cbvapi.models import Movie

class MovieListAV(APIView):

    def get(self,request):
        movie=Movie.objects.all()
        serilizer=MovieSerial(movie,many=True)
        return Response(serilizer.data)

    def post(self,request):
        serilizer=MovieSerial(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data)
        else:
            return Response(serilizer.errors)
    

class MovieDetailAV(APIView):

    def get(self,request,pk):
        try:
            movie=Movie.objects.get(id=pk)
        except Movie.DoesNotExist :
            content='page not existed'
            return Response(content,status.HTTP_404_NOT_FOUND)
        serilizer=MovieSerial(movie)
        return Response(serilizer.data)

    def put(self,request,pk):
        movie=Movie.objects.get(id=pk)
        serilizer=MovieSerial(instance=movie,data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data)
        else:
            return Response(serilizer.errors,status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        movie=Movie.objects.get(id=pk).delete()
        content='movie was not there'
        return Response(content,status.HTTP_204_NO_CONTENT)
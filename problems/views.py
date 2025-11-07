from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Problem
from problems.serializer import ProblemSerializer

class ProblemListCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    # GET all problems
    def get(self, request):
        problems = Problem.objects.all().order_by('-created_at')
        serializer = ProblemSerializer(problems, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # POST create new problem
    def post(self, request):
        serializer = ProblemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProblemDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    # Helper method to get object
    def get_object(self, pk):
        try:
            return Problem.objects.get(pk=pk)
        except Problem.DoesNotExist:
            return None

    # GET single problem by id
    def get(self, request, pk):
        problem = self.get_object(pk)
        if not problem:
            return Response({'error': 'Problem not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProblemSerializer(problem)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # PUT update problem
    def put(self, request, pk):
        problem = self.get_object(pk)
        if not problem:
            return Response({'error': 'Problem not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProblemSerializer(problem, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE problem
    def delete(self, request, pk):
        problem = self.get_object(pk)
        if not problem:
            return Response({'error': 'Problem not found'}, status=status.HTTP_404_NOT_FOUND)
        problem.delete()
        return Response({'message': 'Problem deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

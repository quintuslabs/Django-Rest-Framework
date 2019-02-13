from rest_framework import generics, status
from rest_framework.response import Response

from article.models import Employee
from article.reatapi.serializers.article import EmployeeSerializer


class EmployeeCreateAPIView(generics.CreateAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        return Employee.objects.all()

    def post(self, request, *args, **kwargs):
        employee = Employee()
        employee.name = request.data.get('name')
        employee.phone = request.data.get('phone')
        employee.gender = request.data.get('gender')
        employee.image = request.data.get('image')
        employee.height = request.data.get('height')
        employee.weight = request.data.get('weight')
        employee.save()
        return Response(EmployeeSerializer(employee).data)


class EmployeeListAPIView(generics.ListAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        return Employee.objects.all()


class EmployeeDetailAPIView(generics.RetrieveAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        return Employee.objects.filter(id=self.kwargs['pk'])


class EmployeeUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

    def patch(self, request, *args, **kwargs):
        employee_id = self.kwargs['pk']
        employee = Employee.objects.get(id=employee_id)

        if employee:
            if request.data.get('name') is not None:
                employee.name = request.data.get('name')
            if request.data.get('phone') is not None:
                employee.phone = request.data.get('phone')
            if request.data.get('gender') is not None:
                employee.gender = request.data.get('gender')
            if request.data.get('image') is not None:
                employee.image = request.data.get('image')
            if request.data.get('height') is not None:
                employee.height = request.data.get('height')
            if request.data.get('weight') is not None:
                employee.gender = request.data.get('weight')
                employee.save()
            return Response(EmployeeSerializer(employee).data)
        else:
            return Response({"message": "User Not found"})


class EmployeeDeleteAPIView(generics.RetrieveDestroyAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

    def destroy(self, request, *args, **kwargs):
        employee_id = self.kwargs['pk']
        employee = Employee.objects.get(id=employee_id)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, reverse, get_object_or_404
from django.views.generic import CreateView, TemplateView, DeleteView, UpdateView, DetailView

from crud_with_cbv.forms import StudentForm
from crud_with_cbv.models import StudentModel
from django.contrib import messages


# Create your views here.


class IndexView(TemplateView):
    template_name = 'crud_with_cbv/home.html'


class CreateStudentView(SuccessMessageMixin, CreateView):
    model = StudentModel
    form_class = StudentForm
    template_name = "crud_with_cbv/index.html"
    success_url = '/'
    success_message = "Student Created successfully"

    def get_context_data(self, **kwargs):
        context = super(CreateStudentView, self).get_context_data(**kwargs)
        context['student_list'] = StudentModel.objects.all()
        return context


class StudentEdit(SuccessMessageMixin, UpdateView):
    model = StudentModel
    form_class = StudentForm
    template_name = "crud_with_cbv/edit.html"
    success_message = "Student Updated successfully"

    def get_success_url(self, **kwargs):
        return self.object.get_absolute_url()


class StudentStatus(SuccessMessageMixin, DetailView):
    pass


class StudentDelete(DeleteView):
    model = StudentModel
    success_url = '/'
    success_message = "Student Deleted Successfully"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)

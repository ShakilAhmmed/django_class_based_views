from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse, get_object_or_404
from django.views import View
from django.views.generic import CreateView, TemplateView, DeleteView, UpdateView, DetailView

from crud_with_cbv.forms import StudentForm
from crud_with_cbv.models import StudentModel
from django.contrib import messages


# Create your views here.


class IndexView(TemplateView):
    template_name = 'crud_with_cbv/home.html'
    
#Handle Mutiple Form
# class CreateStudentView(View):
# form = StudentForm
# address_form = StudentAddressForm
# template_name = 'crud_with_cbv/index.html'

# def get(self, request):
#     form = self.form(None)
#     address_form = self.address_form(None)

#     context = {
#         'form': form,
#         'address_form': address_form,
#         'student_list': StudentModel.objects.all()
#     }
#     return render(request, self.template_name, context)

# def post(self, request):
#     form = self.form(request.POST)
#     address_form = self.address_form(request.POST)

#     if form.is_valid():
#         form_save = form.save()
#         form_address_save = address_form.save(commit=False)
#         form_address_save.student = form_save
#         if address_form.is_valid():
#             form_address_save.save()
#         messages.success(request, 'Student Added Successfully')
#         return HttpResponseRedirect(reverse('home-view'))
#     context = {
#         'form': form,
#         'address_form': address_form,
#         'student_list': StudentModel.objects.all()
#     }
#     return render(request, self.template_name, context)

#Handle Single Form
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


class StudentStatus(View):
    def get(self, request, pk):
        student_data = get_object_or_404(StudentModel, pk=pk)
        if student_data.status == 'Active':
            student_data.status = 'Inactive'
            messages.success(request, 'Student Status Changed Into Inactive')
        else:
            student_data.status = 'Active'
            messages.success(request, 'Student Status Changed Into Active')
        student_data.save()
        return HttpResponseRedirect(reverse('home-view'))


class StudentDelete(DeleteView):
    model = StudentModel
    success_url = '/'
    success_message = "Student Deleted Successfully"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *

class UserListView(ListView):
    model = User
    template_name = 'user_list.html'
    context_object_name = 'users'

class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'
    context_object_name = 'user'

class UserCreateView(CreateView):
    model = User
    template_name = 'user_form.html'
    fields = ['first_name', 'last_name', 'email', 'avatar', 'date_of_birth']

class UserUpdateView(UpdateView):
    model = User
    template_name = 'user_form.html'
    fields = ['first_name', 'last_name', 'email', 'avatar', 'date_of_birth']

class UserDeleteView(DeleteView):
    model = User
    template_name = 'user_confirm_delete.html'
    success_url = reverse_lazy('user_list')

# class MessageListView(ListView):
#     model = Message
#     template_name = 'message_list.html'
#     context_object_name = 'messages'
#
# class MessageDetailView(DetailView):
#     model = Message
#     template_name = 'message_detail.html'
#     context_object_name = 'message'
#
# class MessageCreateView(CreateView):
#     model = Message
#     template_name = 'message_form.html'
#     fields = ['text_message', 'sender', 'receiver']
#
# class MessageUpdateView(UpdateView):
#     model = Message
#     template_name = 'message_form.html'
#     fields = ['text_message', 'sender', 'receiver']
#
# class MessageDeleteView(DeleteView):
#     model = Message
#     template_name = 'message_confirm_delete.html'
#     success_url = reverse_lazy('message_list')

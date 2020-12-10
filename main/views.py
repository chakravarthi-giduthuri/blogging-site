from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.http import HttpResponse
from .models import Post
from django.db.models import Q


# Create your views here.
def home(request):
	context={
	   'posts':Post.objects.all()
	}
	return render(request,'main/home.html',context)

class PostListView(ListView):
	model = Post
	template_name='main/home.html'
	context_object_name ='posts'
	ordering =['-date_posted']

class PostDetailView(DetailView):
	model = Post


class PostCreateView(LoginRequiredMixin,CreateView):
	model = Post
	fields =['title','content']

	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
	model = Post
	fields =['title','content']

	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
	model = Post
	success_url='/'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

def about(request):
	return HttpResponse('<h1>about</h1>')


def search(request):
	query = request.GET.get('q','')
	if query:
		queryset=(Q(title__icontains=query))
		results=Post.objects.filter(queryset).distinct()
	else:
	  results=[]
	return render(request,'main/search.html',{'results':results, 'query':query})
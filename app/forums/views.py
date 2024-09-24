from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, PostCategory
from .forms import PostForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from forums.sexual_checker import check_message
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponseRedirect

class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'forums/post_list.html'
    login_url = '/login/'

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'forums/post_detail.html'
    login_url = '/login/'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'forums/post_form.html'
    login_url = '/login/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        self.object = form.save()
        category = check_message(self.object.content)
        print(category)
        PostCategory.objects.create(post=self.object, category=category)
        print(category)
        if category == 'predator':

            mail_content = f"""A post with sexual content has been detected. Please review the post and take necessary actions. 
Username: {self.object.author.username}, 
Post: {self.object.title}, 
Post URL:  http://localhost:8000{self.object.get_absolute_url()},
Email: {self.object.author.email}
Content: {self.object.content}, 
            """

            status = send_mail(
                "Warning! Sexual content detected!",
                mail_content,
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER],
                fail_silently=False,
            )

        return HttpResponseRedirect(self.get_success_url())

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'forums/post_form.html'
    login_url = '/login/'

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'forums/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')
    login_url = '/login/'
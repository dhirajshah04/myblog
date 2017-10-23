from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm
from .forms import ContactForm
from django.core.mail import  EmailMessage
from django.template import Context
from django.template.loader import  get_template
from django.contrib.auth.decorators import login_required
from myblog import helpers

def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/index.html', {'posts':posts})


def about(request):
    return render(request, 'blog/about.html', {})

def contact(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            Name = request.POST.get('Name', '')

            Email = request.POST.get('Email', '')

            Message = request.POST.get('Message', '')

            template = get_template('blog/contact_template')
            Context = {
                'Name': Name,
                'Email': Email,
                'Message': Message,
            }

            content = template.render(Context)

            Email = EmailMessage(
                "New Contact Form Submission",
                content,
                "Your Website" +'',
                ['youremail@gmail.com'],
                headers = {'Reply-To': Email}
            )

            Email.send()
            return render(request, 'blog/contact.html', {'form':form_class})



    return render(request, 'blog/contact.html', {'form': form_class})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    post = helpers.pg_records(request, posts, 5)
    return render(request, 'blog/post_list.html', {'posts': post})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


@login_required
def	post_new(request):
    if	request.method	==	"POST":
        form = PostForm(request.POST, request.FILES)
        if	form.is_valid():
            post = form.save(commit=False)
            post.author	= request.user
            #post.published_date = timezone.now()
            #post.status = 'published'
            post.save()
            return redirect('post_detail',	pk=post.pk)
    else:
        form = PostForm()
    return	render(request,	'blog/post_edit.html',	{'form': form})

@login_required()
def	post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            #post.status = 'published'
            post.save()
            return	redirect('post_detail',	pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required()
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('-created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

@login_required()
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

@login_required()
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')
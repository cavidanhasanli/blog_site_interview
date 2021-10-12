from django.shortcuts import render, redirect
from base_app.models import *
from base_app.forms import PostContactForm, PostCreateForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import auth
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

User = get_user_model()


@login_required(login_url='login_page')
def home_view(request):
    context = {}
    posts_queryset = PostModel.objects.filter(user_id=request.user, is_activate=True)
    context['posts_queryset'] = posts_queryset
    return render(request, 'index.html', context)

@login_required(login_url='login_page')
def post_detail_view(request, post_id):
    context = {}
    post_detail_queryset = PostModel.objects.filter(id=post_id).first()
    post_detail_images = PostImageModel.objects.filter(post_id=post_id)
    context['post_detail_queryset'] = post_detail_queryset
    context['post_detail_images'] = post_detail_images
    return render(request, 'post_detail.html', context)


def post_contact_view(request):
    context = {}
    form = PostContactForm()

    if request.method == 'POST':
        form = PostContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_page')
        else:
            context['form'] = form
            return render(request, 'contact.html', context)

    context['form'] = form
    return render(request, 'contact.html', context)


@login_required(login_url='login_page')
def post_create_view(request):
    context = {}
    form = PostCreateForm()
    if request.method == 'POST':
        images = request.FILES.getlist("images_all")
        tags = request.POST.getlist('tags[]')
        form_new = PostCreateForm(request.POST, request.FILES)
        if form_new.is_valid():
            forms = form_new.save(commit=False)
            forms.user_id = request.user
            forms.save()

            for i in images:
                PostImageModel.objects.create(
                    post_id_id=forms.id,
                    images=i
                )

            for i in tags:
                PostTags.objects.create(
                    post_id_id=forms.id,
                    tag_name=i
                )

            return redirect('home_page')
        else:

            context['form'] = form_new
            messages.error(request, form_new.errors)
            return render(request, 'post_create.html', context)

    context['form'] = form
    return render(request, 'post_create.html', context)


def register_view(request):
    context = {}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_page')
        else:
            context['form'] = form
            messages.error(request, form.errors)
            return render(request, 'register.html', context)

    else:
        form = UserCreationForm()
        context['form'] = form
    return render(request, 'register.html', context)


def login_view(request):
    context = {}
    username = request.POST.get('username')
    raw_password = request.POST.get('password')
    user = authenticate(username=username, password=raw_password)
    if user:
        login(request, user)
        return redirect('home_page')
    else:
        context['error_message'] = "ERROR"
        return render(request, 'login.html', context)


def logout_view(request):
    auth.logout(request)
    return redirect('login_page')

@login_required(login_url='login_page')
def post_update_view(request, post_id):
    context = {}
    update_data = PostModel.objects.filter(id=post_id).first()
    form = PostCreateForm(instance=update_data)

    if request.method == 'POST':
        images = request.FILES.getlist("images_all")
        form_new = PostCreateForm(request.POST, instance=update_data)
        if form_new.is_valid():
            form_new.save()
            for i in images:
                PostImageModel.objects.update(
                    post_id_id=form_new.id,
                    images=i
                )

            return redirect('home_page')
        else:

            context['form'] = form_new
            messages.error(request, form_new.errors)
            return render(request, 'post_create.html', context)

    context['form'] = form
    context['post_id'] = update_data
    return render(request, 'post_update.html', context)

@login_required(login_url='login_page')
def post_delete_view(request, post_id):
    post_delete = PostModel.objects.filter(id=post_id).first()
    post_delete.delete()
    return redirect('home_page')

@login_required(login_url='login_page')
def search_result_view(request):
    context = {}
    if request.method == 'POST':
        searched = request.POST.get('searched', False)
        posts_queryset = PostModel.objects.filter(Q(postmodel__tag_name=searched) | Q(post_title=searched) | Q(post_text=searched),
                                                  user_id=request.user,
                                                  is_activate=True)
        print(posts_queryset)
        context['posts_queryset'] = posts_queryset
        context['error_text'] = 'NETICE TAPILMADI'
        return render(request, 'search_result.html', context)

    context['error_text'] = 'NETICE TAPILMADI'
    return render(request, 'search_result.html', context)
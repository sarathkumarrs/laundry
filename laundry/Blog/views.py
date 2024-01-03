from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib import messages
from main.forms import *
from .models import *
from django.shortcuts import render, get_object_or_404
from .models import Comment
from .forms import CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def post_comment(request, pk):
    if request.method == 'POST':
        blog = get_object_or_404(Blog, pk=pk)
        form2 = CommentForm(request.POST)

        if form2.is_valid():
            comment = form2.save(commit=False)
            comment.blog = blog
            comment.save()
            return redirect('Blog:blog_details', pk=pk)
    else:
        form = CommentForm()

    return render(request, 'blog/blog_details.html', {'form2': form2})

def blog(request):
    blogs = Blog.objects.all()
    categories=Category.objects.all()
    booking = Booking.objects.all()
    services = LaundryService.objects.all()
    form = BookingForm()
    recent_blogs = Blog.objects.order_by('-date')[:4]

    # Number of blogs to display per page
    blogs_per_page =4
    paginator = Paginator(blogs, blogs_per_page)

    page = request.GET.get('page')
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        # If the page parameter is not an integer, show the first page
        blogs = paginator.page(1)
    except EmptyPage:
        # If the page is out of range, deliver the last page of results
        blogs = paginator.page(paginator.num_pages)

    context = {
        'form': form,
        'services': services,
        'booking': booking,
        'blogs': blogs,
        'categories':categories,
        'recent_blogs':recent_blogs,
    }

    return render(request, 'blog/blog.html', context)

def blog_details(request,pk):
    categories=Category.objects.all()
    recent_blogs = Blog.objects.order_by('-date')[:4]
    blog=get_object_or_404(Blog, pk=pk)
    booking =Booking.objects.all()
    services = LaundryService.objects.all()
    form = BookingForm()
    form2 = CommentForm()
    next_post = Blog.objects.filter(date__gt=blog.date).order_by('date').first()
    prev_post = Blog.objects.filter(date__lt=blog.date).order_by('-date').first()
    return render(request,'blog/blog_details.html', {'form': form,
                                                     'form2':form2,
                                                     'services':services,
                                                     'booking':booking,
                                                     'blog': blog,
                                                     'prev_post': prev_post,
                                                     'next_post': next_post,
                                                     'categories':categories,
                                                     'recent_blogs':recent_blogs,})    


def search_view(request):
    booking =Booking.objects.all()
    services = LaundryService.objects.all()
    form = BookingForm()
    query = request.GET.get('q', '')
    print(f"Search Query: {query}")
    results = Blog.objects.filter(title__icontains=query)
    print(f"Search Results: {results}")
    return render(request, 'blog/search_results.html', {'query': query, 'results': results,'form': form,'services':services,'booking':booking})                                                      

def blogs_by_category(request, category_id):
    # Get the category or return a 404 response if it doesn't exist
    category = get_object_or_404(Category, id=category_id)
    categories=Category.objects.all()
    # Get blogs associated with the selected category
    blogs = Blog.objects.filter(categories=category)
    booking = Booking.objects.all()
    services = LaundryService.objects.all()
    form = BookingForm()
    recent_blogs = Blog.objects.order_by('-date')[:4]

    # Number of blogs to display per page
    blogs_per_page =4
    paginator = Paginator(blogs, blogs_per_page)

    page = request.GET.get('page')
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        # If the page parameter is not an integer, show the first page
        blogs = paginator.page(1)
    except EmptyPage:
        # If the page is out of range, deliver the last page of results
        blogs = paginator.page(paginator.num_pages)

    context = {
        'form': form,
        'services': services,
        'booking': booking,
        'recent_blogs':recent_blogs,
        'category': category,
        'blogs': blogs,
        'categories':categories,
    }

    return render(request, 'Blog/blog_by_category.html', context)
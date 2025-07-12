# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import BlogPostForm
from .models import BlogImage, BlogPost
from django.http import JsonResponse

def create_and_list_blog_posts(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        files = request.FILES.getlist('images')

        if form.is_valid():
            if len(files) > 2:
                posts = BlogPost.objects.all().order_by('-created_at')
                return render(request, 'blog/create_post.html', {
                    'form': form,
                    'posts': posts,
                    'error': 'You can upload a maximum of 2 images.'
                })

            post = form.save()

            for image in files:
                BlogImage.objects.create(blog=post, image=image)

            return redirect('create_post')  # Redirect to self to avoid resubmission

    else:
        form = BlogPostForm()

    posts = BlogPost.objects.all().order_by('-created_at')

    return render(request, 'blog/create.html', {'form': form, 'posts': posts})


def edit_blog_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)

    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        files = request.FILES.getlist('images')

        if form.is_valid():
            if len(files) > 2:
                return render(request, 'blog/edit.html', {
                    'form': form,
                    'post': post,
                    'error': 'You can upload a maximum of 2 images.',
                    'images': post.images.all()
                })

            form.save()

            if files:
                post.images.all().delete()
                for image in files:
                    BlogImage.objects.create(blog=post, image=image)

            return redirect('create_post')
    else:
        form = BlogPostForm(instance=post)

    return render(request, 'blog/edit.html', {
        'form': form,
        'post': post,
        'images': post.images.all()
    })

def delete_blog_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)

    if request.method == 'POST':
        post.delete()  # This will also delete images if `on_delete=models.CASCADE` is used
        return redirect('create_post')

    return render(request, 'blog/delete.html', {'post': post})



    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        query = request.GET.get('term', '')
        posts = BlogPost.objects.filter(title__icontains=query)[:10]
        results = [post.title for post in posts]
        return JsonResponse(results, safe=False)
    
    # Always return a fallback response if not AJAX
    return JsonResponse({'error': 'Invalid request'}, status=400)
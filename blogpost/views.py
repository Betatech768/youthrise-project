# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import BlogPostForm
from .models import BlogImage, BlogPost
from django.http import JsonResponse


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
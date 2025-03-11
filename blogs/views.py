from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import View

from blogs.models import Blog, BlogComment


class BlogListView(View):

    def get(self, request):
        blogs = Blog.objects.all()

        

        context = {
            'blogs': blogs
        }
        return render(request, 'blogs/blogs.html', context)


class BlogDetailView(View):

    def get(self, request, slug):
        blog = get_object_or_404(Blog, slug=slug)

        context = {
            'blog': blog
        }
        return render(request, 'blogs/blog_detail.html', context)

    def post(self, request, slug):
        if not request.user.is_authenticated:
            return redirect(reverse_lazy('accounts:login'))  # Login sahifasiga yo‘naltirish

        blog = get_object_or_404(Blog, slug=slug)
        comment_text = request.POST.get('comment', '').strip()

        if comment_text:  # Bo‘sh bo‘lmagan kommentlarni saqlaymiz
            BlogComment.objects.create(
                blog=blog,
                user=request.user,
                text=comment_text
            )

        return redirect(reverse('blogs:blog-detail', kwargs={'slug': blog.slug}))

from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest,HttpResponse
from django.views.generic import ListView, DetailView
from .models import Post

class PostListView(ListView):
    model = Post

PostLIstView = PostListView.as_view()

from django.shortcuts import render
from .models import Post
def post_list(request):
    qs = Post.object.all()
    q = request.Get.get('q', '')
    if q:
        qs = qs.filter(name__icontains=q)
    return render(request, 'instagram/post_list.html', {
        'item_list' : qs,
        'q': q,
    })

"""def post_detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    """"""
    try:
        post = Post.object.get(pk =pk)
    :except Post.DoseNotExist:
        raise Http404
        
    """ """
    return render(request, 'instagram/post_detail.html', {
        'post': post,
    })


"""
post_detail = DetailView.as_view(model=Post)
"""

def archives_year(request,year):
    return HttpResponse(f"{year}년 archives")




"""



# @login_requried
# def post_new(request):
#   if request.method == 'POST':
#       form = PostForm(request.POST, request.FILES)
#       if form.is_valid():
#       post = form.save(commit = False)
#       post.author = request.user
#       post.save()
#       return redirect(post)
#    else:
#       form = PostForm()
#
#      return render(request, ;instagram/post_form.html'


#
#
#

"""

실무에서는 안쓰일 코드

def generate_view_fn(model):
    def view_fn(request, id):
    instance = get_object_or_404(model, id=id)
    instance_name = model._meta.model_name
    template_name = '{}/{}_detail'.html.format(model._meta.app_label, instance_name)
    return render(request, template_name, {
        instance_name: instance,
        })
    return view_fn
    
post_detail = generate_view_fn(post)

article_detail = generate_view_fn(Article)



"""
""""""
"""
class view:
    def __init__(self):
        # ...

    @classonlvmethod
    def as_view(cls, **innit):
        def view(request, *args, **kwargs)
            return self.dispatch(request, *args, **kwargs)
    return view

    def dispatch(self, request, *args , **kwargs):
        handler = getattr(self, request.mothod.lower(),
                          self,http_method_not_allowed)
"""



""" 
clss의 디테일뷰로  표현해보자 
class DetailView:
    def __init__ (self, model):
    self.model = model
    






    @classmethod
    def as_view(cls, model):
        def view(request, *args, **Kwargs):
            self = cls(model)
            return self.dispatch(request, *args, **kwargs)
            retrun view
"""

post_archive = ArchieveIndexView.as_view(model=Post, date_field='created_date')




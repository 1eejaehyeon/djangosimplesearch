from django.contrib.auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def protected_view1(request):
    return render(request, 'myapp/secret.html')



def protected_view2(request):
    return render(request, 'myapp/secret.html')


protected_view2 = login_required(protected_view2)

# 장고에서 클래스로 장식자함수를 쓸라면:

post_list = login_required(LIstView.as_view(model=Post, paginate_by=10))

@methode_decorator(login_required, name='dispatch')
class PostListView(ListView):
    model = Post
    paginate_by = 10

class SecretView(TemplateView):
    template_name = 'myapp/secret.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


    @login_required
    def g함수:
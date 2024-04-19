from django.shortcuts import render
from _data import zenblogds
from django_utilsds import utils
from hitcount.views import HitCountDetailView
from django.views import generic
from .forms import SearchForm
from .models import Post, CATEGORY

num_pagination = 7


def make_page_bundle(page_range, n=5):
    # 전체 페이지를 n 개수의 묶음으로 만든다.
    # pagination에 사용
    l = [i for i in page_range]
    return [l[i:i + n] for i in range(0, len(l), n)]


def robots(request):
    from django.shortcuts import HttpResponse
    file_content = utils.make_robots()
    return HttpResponse(file_content, content_type="text/plain")


def home(request):
    c = zenblogds.context
    c.update({
        'category': CATEGORY,
    })
    return render(request, 'zenblogds/index.html', c)


def about(request):
    c = zenblogds.context
    return render(request, 'zenblogds/about.html', c)


def contact(request):
    c = zenblogds.context
    return render(request, 'zenblogds/contact.html', c)


class PostDetailView(HitCountDetailView):
    model = Post
    template_name = 'zenblogds/single-post.html'
    context_object_name = 'object'
    slug_field = 'slug'
    count_hit = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update(zenblogds.context)
        return context


class SearchResult(generic.ListView):
    template_name = 'zenblogds/search-result.html'
    paginate_by = num_pagination

    def get_queryset(self):
        form = SearchForm(self.request.GET)
        if form.is_valid():
            q = form.cleaned_data['q']
        else:
            q = ''
        return Post.objects.filter(content__contains='' if q is None else q).filter(status=1).order_by('-updated_on')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        pages_devided = make_page_bundle(context['paginator'].page_range)

        # 현재 페이지에 해당하는 묶음을 page_bundle로 전달한다.
        for page_bundle in pages_devided:
            if context['page_obj'].number in page_bundle:
                context['page_bundle'] = page_bundle

        context.update(zenblogds.context)
        return context


class SearchTag(SearchResult):
    def get_queryset(self):
        # https://stackoverflow.com/questions/56067365/how-to-filter-posts-by-tags-using-django-taggit-in-django
        return Post.objects.filter(tags__name__in=[self.kwargs['tag']]).filter(status=1).order_by('-updated_on')


class Category(generic.ListView):
    template_name = 'zenblogds/category.html'
    paginate_by = num_pagination

    def get_queryset(self):
        return Post.objects.filter(status=1).filter(category=self.kwargs['category_int']).order_by('-updated_on')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        pages_devided = make_page_bundle(context['paginator'].page_range)

        # 현재 페이지에 해당하는 묶음을 page_bundle로 전달한다.
        for page_bundle in pages_devided:
            if context['page_obj'].number in page_bundle:
                context['page_bundle'] = page_bundle

        context.update({
            'selected_category': CATEGORY[self.kwargs['category_int']][1],
        })

        context.update(zenblogds.context)
        return context
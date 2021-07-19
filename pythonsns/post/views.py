from django.shortcuts import render

# テンプレートを返す
def post_list(request):
    context = {}
    return render(request, 'post/post_list.html', context)

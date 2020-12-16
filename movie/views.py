from django.shortcuts import render
from .models import Movies
import math
def pageq(num,size=30):
    #接收当前页码数
    num=int(num)
    #总记录
    tot = Movies.objects.count()
    #总页数
    tota = int(math.ceil(tot*1.0/size))
    #判断是否越界
    if num<1:
        num = 1

    if num>tota:
        num = tota
    #计算每页显示的数量
    move = Movies.objects.all()[((num-1)*size):(num*size)]
    return move,num
#原生分页
def index(request):

    num = request.GET.get('num',1)
    move,n = pageq(num)
    context = {
        'movies':move,
        'shangye': n-1,#下页
        'xiaye' :n+1 #上页
    }
    return render(request,'index01.html',context=context)

#django分页
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
def index2(request):
    #获取当前页码数
    num = request.GET.get('num',1)
    n = int(num)

    #查询所有
    movies = Movies.objects.all()

    #创建分页器
    pager = Paginator(movies,30)

    #获取当前页数据
    try:
        p = pager.page(n)
    except PageNotAnInteger:#输入的值不是整数
        p = pager.page(1) #默认走第一页
    except EmptyPage: #不存在的页码
        p = pager.page(pager.num_pages) #走最后一页

    return render(request,'index01.html',{'pager':pager,'p':p})


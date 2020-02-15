import hashlib
import random
import string

from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
import json

from ddapp.captcha.image import ImageCaptcha
from ddapp.models import TCategory, TBook, TUser, TShoppingCart, TAddr, TOrder, TOrderDetail


# 主页面
def index(request):
    dele=request.GET.get('dele')
    if dele:
        if request.session.get('username'):
            del request.session['username']
        if request.session.get('login'):
            del request.session['login']
    name=request.session.get('username')
    category1=TCategory.objects.filter(parent_id__isnull=True)
    category2 = TCategory.objects.filter(parent_id__isnull=False)
    new_book=TBook.objects.all().order_by('-publication_time')[0:8]
    zhubian=TBook.objects.all().order_by('price')[0:10]
    new_hot=TBook.objects.all().order_by('-publication_time','-column_28')[0:5]
    new_hot2 = TBook.objects.all().order_by('-publication_time', '-column_28')[0:10]
    return render(request,'index.html',
                  {
                      'category1':category1,
                      'category2': category2,
                      'new_book':new_book,
                      'zhubian':zhubian,
                      'new_hot':new_hot,
                      'new_hot2':new_hot2,
                      'name':name
                  })

# booklist页面
def booklist(request):
    dele = request.GET.get('dele')
    if dele:
        if request.session.get('username'):
            del request.session['username']
        if request.session.get('login'):
            del request.session['login']
    book_category=[]
    name=request.session.get('username')
    category1 = TCategory.objects.filter(parent_id__isnull=True)
    category2 = TCategory.objects.filter(parent_id__isnull=False)
    id=request.GET.get('id')
    id1=request.GET.get('id1')
    num=request.GET.get('num')
    if id:
        p_book = TCategory.objects.get(id=id)
        book_category.append(p_book)
        new_id=id
    else:
        s_book=TCategory.objects.get(id=id1)
        p_book=TCategory.objects.get(id=s_book.parent_id)
        book_category.append(p_book)
        book_category.append(s_book)
        new_id=id1
    if not num:
        num=1
    category_book=TCategory.objects.filter(parent_id=id).values('id')
    a=[]
    xiaolei=TBook.objects.filter(second_category=id1)
    for k in xiaolei:
        a.append(k)
    for i in category_book:
        category_book2=TBook.objects.filter(second_category=i['id'])
        for j in category_book2:
            a.append(j)
    page = Paginator(a, per_page=6).page(num)
    return render(request,'booklist.html',{
        'category1': category1,
        'category2': category2,
        'page':page,
        'new_id':new_id,
        'book_category':book_category,
        'num':num,
        'name':name
    })

# 验证码
def getcaptcha(request):
    image=ImageCaptcha()   #创建验证码图片对象
    code_list=random.sample(string.ascii_letters+string.digits,4)
    random_str=''.join(code_list)
    request.session['code']=random_str
    #生成验证码图片
    data=image.generate(random_str)
    return HttpResponse(data,'image/png')

# 注册页面
def regist(request):
    return render(request,'register.html')

# 注册判断账号是否存在
def regist_logic(request):
    name=request.POST.get('name')
    regist_user=TUser.objects.filter(username=name)
    if regist_user:
        return HttpResponse('该账号已存在')
    else:
        return HttpResponse('可使用')

# 验证码判断
def yzm_logic(request):
    code=request.session.get('code')
    yzm=request.POST.get('yzm')
    if code.lower() == yzm.lower():
        return HttpResponse(1)
    else:
        return  HttpResponse(0)

#   注册添加到数据库
def regist_l(request):
    tiao=request.session.get('tiao')
    name=request.POST.get('name')
    pwd=request.POST.get('pwd')
    id=TUser.objects.last().id
    idd=int(id)+1
    s='15648451654@#$%^$%afjoiGIUYIH'
    y=random.sample(s,5)
    y=''.join(y)    #盐
    pwd1=pwd+y
    h=hashlib.sha256()
    h.update(pwd1.encode())
    pwd_jm=h.hexdigest()
    TUser.objects.create(username=name,userpwd=pwd_jm,id=idd,column_4=y)
    request.session['username']=name
    if tiao:
        request.session['login']=login
        return HttpResponse('tiao')
    return HttpResponse('1')

# 注册ok页面
def register_ok(request):
    usernmae=request.session.get('username')
    request.session['login']='ok'
    return render(request, 'register ok.html',{'usernmae':usernmae})

# 登录页面
def login(request):
    tiao=request.GET.get('tiao')
    request.session['tiao']=tiao
    return render(request,'login.html',{'tiao':tiao})

# 登录判断
def login_logic(request):
    tiao_ok=request.session.get('tiao')
    print(tiao_ok)
    name=request.POST.get('name')
    pwd=request.POST.get('pwd')
    user=TUser.objects.filter(username=name)
    password=user.values('userpwd')[0]['userpwd']
    print(password)
    salt=user.values('column_4')[0]['column_4']
    if user:
        pwd1=pwd+salt
        h1=hashlib.sha256()
        h1.update(pwd1.encode())
        pwd2=h1.hexdigest()
        if pwd2==password:
            if tiao_ok:
                request.session['username'] = name
                request.session['login'] = 'ok'
                return HttpResponse('跳')
            else:
                request.session['username']=name
                request.session['login']='ok'
                return HttpResponse('登录成功')

        else:
            return HttpResponse('账号或密码错误，请重新登录')
    else:
        return  HttpResponse('账号或密码错误，请重新登录')

#书籍详情页
def bookde(request):
    dele = request.GET.get('dele')
    name = request.session.get('username')
    if dele:
        if request.session.get('username'):
            del request.session['username']
        if request.session.get('login'):
            del request.session['login']
    id=request.GET.get('id')
    book=TBook.objects.filter(id=id)
    for i in book:
        pass
    return render(request,'Book details.html',{'book':i,'id':id,'name':name})


from ddapp.car import Cart,Cart_items
# 购物车页面
def car(request):
    dele = request.GET.get('dele')
    if dele:
        if request.session.get('username'):
            del request.session['username']
        if request.session.get('login'):
            del request.session['login']
    na=request.session.get('username')
    s_cart=request.session.get('cart')
    login=request.session.get('login')
    if login:
        cart=Cart()
        user=TUser.objects.get(username=na)
        shopcar=TShoppingCart.objects.filter(user_id=user.id)
        print(shopcar)
        for i in shopcar:
            print(i.count)
            print(i.book_id)
            cart.cart_items.append(Cart_items(TBook.objects.filter(id=i.book_id)[0],i.count))
            print(i.count,i.book.discount)
            cart.total_price+=int(i.count)*int(i.book.discount)
            cart.save_price+=int(i.book.price-i.book.discount)*int(i.count)
        request.session['cart']=cart
        s_cart=cart
        print(s_cart)
        if  s_cart:
            len_car=len(s_cart.cart_items)
            print('存session')
            request.session['len']=len_car
            return render(request,'car.html',{'na':na,'cart':s_cart,'len_car':len_car})
        len_car = len(s_cart.cart_items)
        request.session['len'] = len_car
    return render(request,'car.html',{'cart':s_cart})



# 增加商品
def add_car(request):
    name=request.GET.get('name')   #获取书籍id
    login=request.session.get('login')
    if login:
        number=request.GET.get('number')
        username=request.session.get('username')
        user=TUser.objects.get(username=username)
        userid=TUser.objects.get(username=username).id
        print(userid,'******************************')

        s_car=TShoppingCart.objects.filter(book_id=name,user_id=userid)
        if s_car:
            s_car=s_car[0]
            print(s_car.count)
            s_car.count=int(s_car.count)+int(number)
            s_car.save()
        else:
            if  TShoppingCart.objects.last() is None:
                idd=1
            else:
                id = TShoppingCart.objects.last().id
                idd = int(id) + 1
            TShoppingCart.objects.create(book_id=name,user_id=user.id,count=number,id=idd)
    cart=request.session.get('cart')
    if not cart:
        cart=Cart()
        cart.add_car(name)
        request.session['cart'] = cart
    else:
        cart.add_car(name)
        request.session['cart']=cart
    sum_price = cart.total_price
    save_price = cart.save_price
    return HttpResponse(str(sum_price) + '-' + str(save_price))  # 拼接成字符串传给前端
# 删除商品
def del_car(request):
    id=request.GET.get('id')

    login=request.session.get('login')
    if login:
        username = request.session.get('username')
        print(username)
        userid = TUser.objects.get(username=username).id
        TShoppingCart.objects.filter(book_id=id,user_id=userid).delete()
    cart = request.session.get('cart')
    cart.del_car(id)
    request.session['cart']=cart
    sum_price = cart.total_price
    save_price = cart.save_price
    return HttpResponse(str(sum_price) + '-' + str(save_price))  # 拼接成字符串传给前端

# 修改商品
def change_car(request):
    id=request.GET.get('id')
    number=request.GET.get('number')
    login=request.session.get('login')
    if login:
        username = request.session.get('username')
        userid = TUser.objects.get(username=username).id
        shopcar=TShoppingCart.objects.filter(book_id=id,user_id=userid)
        shopcar=shopcar[0]
        shopcar.count=number
        shopcar.save()
    cart=request.session.get('cart')
    cart.change_nums(id,number)
    sum_price=cart.total_price
    save_price=cart.save_price
    request.session['cart']=cart
    return HttpResponse(str(sum_price)+'-'+str(save_price))  #拼接成字符串传给前端

# 结算
def closing(request):
    login = request.session.get('login')
    cart=request.session.get('cart')
    if login:
        if cart.cart_items ==[]:
            return HttpResponse('ojbk')
        # get_car = request.session.get('car')
        return HttpResponse('ok')   # ok 直接跳转到订单页面
    return HttpResponse('bad')  # bad 强制登录，跳转登录页面


def indent(request):
    login=request.session.get('login')
    if login:
        username=request.session.get('username')
        un = TUser.objects.get(username=username).id
        cart=request.session.get('cart')
        len_cart=len(cart.cart_items)
        request.session['len']=len_cart
        addr=TAddr.objects.filter(user_id=un)
        addr_list=[]
        for i in addr:
            addr_list.append(i.addr)
        return render(request,'indent.html',{'username':username,'cart':cart,'addr_list':addr_list})
    else:
        return redirect('ddapp:login')

def indent_add(request):
    username=request.session.get('username')
    un=TUser.objects.get(username=username).id
    name=request.POST.get('name1')
    addr=request.POST.get('addr')
    yb=request.POST.get('yb')
    tp=request.POST.get('tp')
    card=request.POST.get('card')
    count=request.POST.get('count')
    request.session['count']=count
    if TAddr.objects.last() is None:
        idd = 1
    else:
        id = TAddr.objects.last().id
        idd = int(id) + 1

    addr_add=TAddr.objects.filter(name=name,addr=addr,zip_code=yb,telephone=tp,phone=card,user_id=un)
    if not addr_add:
        TAddr.objects.create(id=idd,name=name,addr=addr,zip_code=yb,telephone=tp,phone=card,user_id=un)

    str = ""
    for i in range(6):
        ch = chr(random.randrange(ord('0'), ord('9') + 1))
        str += ch
    TOrder.objects.create(id=str,amount_price=count,user_id=un)
    request.session['ddh']=str

    shopcar = TShoppingCart.objects.filter(user_id=un)
    for i in shopcar:
        str1 = ""
        for j in range(6):
            ch = chr(random.randrange(ord('0'), ord('9') + 1))
            str1 += ch
        TOrderDetail.objects.create(id=str1,order_id=str,book_id=i.book_id,count=int(i.count))
    shopcar.delete()
    if request.session.get('cart'):
        del request.session['cart']
    return HttpResponse('1')


def indent_ok(request):
    login=request.session.get('login')
    len=request.session.get('len')
    ddh=request.session.get('ddh')
    count=request.session.get('count')
    if not login:
        return redirect('ddapp:login')
    name=request.session.get('username')

    return render(request,'indent ok.html',{'name':name,'ddh':ddh,'len':len,'count':count})

def mydefault(a):
    if isinstance(a,TAddr):
        return {'uname':a.name,'addr':a.addr,'zip_code':a.zip_code,'telephone':a.telephone,'phone':a.phone}
def change(request):
    chan=request.GET.get('chan')

    ad=TAddr.objects.filter(addr=chan)
    json_addr=json.dumps(list(ad),default=mydefault)
    return HttpResponse(json_addr)

def book_de2(request):
    num=request.GET.get('num')
    id=request.GET.get('id')
    login=request.session.get('login')
    if login:
        username = request.session.get('username')
        user = TUser.objects.get(username=username)
        userid=user.id

        s_car = TShoppingCart.objects.filter(book_id=id,user_id=userid)
        if s_car:
            s_car = s_car[0]
            s_car.count = int(s_car.count) + int(num)
            s_car.save()
        else:
            if TShoppingCart.objects.last() is None:
                idd = 1
            else:
                iddd = TShoppingCart.objects.last().id
                idd = int(iddd) + 1
            TShoppingCart.objects.create(book_id=id, user_id=userid, count=num, id=idd)
    cart = request.session.get('cart')
    if not cart:
        cart=Cart()
    for k in cart.cart_items:
        print(k.book.id,'asdadadadsaddd')
        print(id)
        if id == k.book.id:
            k.count=int(k.count)+int(num)
            num=int(k.count)

    else:
        cart.change_nums(id, num)
        request.session['cart'] = cart

    # if not cart:
    #     cart = Cart()
    #     cart.change_nums(id,num)
    #     request.session['cart'] = cart


    return HttpResponse('1')
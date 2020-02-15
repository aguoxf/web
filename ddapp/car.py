from ddapp.models import TBook


class Cart_items():
    def __init__(self,book,count):
        self.book=book
        self.count=count
    def xiaoji(self):
        print(self.book.discount,'******',self.count)
        self.xj=int(self.book.discount)*int(self.count)
        print(self.xj)
        return self.xj

class Cart():
    def __init__(self):
        self.total_price=0
        self.save_price=0
        self.cart_items=[]
        # self.del_items=[]

    # 计算总价
    def sums(self):
        self.total_price=0
        self.save_price=0
        for i in self.cart_items:
            self.total_price+=int(i.book.discount)*int(i.count)
            self.save_price+=(int(i.book.price)-int(i.book.discount))*int(i.count)

    # 增加商品
    def add_car(self,bookid):
        for i in self.cart_items:
            if int(i.book.id)==int(bookid):
                print('*************************')
                i.count=int(i.count)+1
                print(i.count)
                self.sums()
                return
        else:
            self.cart_items.append(Cart_items(TBook.objects.filter(id=bookid)[0], 1))  # 若没有，向Car_items中添加一个Car_items对象
            self.sums()

    # 删除商品
    def del_car(self,bookid):
        for i in self.cart_items:
            if int(i.book.id)==int(bookid):
                self.cart_items.remove(i)
                # self.del_items.append(TBook.objects.filter(id=bookid),i.count)
                self.sums()

    # 修改商品
    def change_nums(self,bookid,nums):
        for i in self.cart_items:
            print('+++++++++++')
            if i.book.id==bookid:
                i.count=nums
                self.sums()
                return
        else:
            print('------------------------')
            self.cart_items.append(Cart_items(TBook.objects.filter(id=bookid)[0], int(nums)))  # 若没有，向Car_items中添加一个Car_items对象
            print(self.cart_items.count)
            self.sums()
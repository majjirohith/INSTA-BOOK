from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from django.contrib import messages
from . models import user_posts


## extensions are from line 327

def comments(comment_str):
    lst = []
    str0 = ""
    for i in comment_str[3:]:
        if i == "$":
            lst.append(str0)
            str0 = "@"
            continue
        str0 = str0 + i
    lst.reverse()
    lst.append(str0)
    return lst, "NUMBER OF COMMENTS: " + str(len(lst)-1)

def multi_upload(name, lst):
    ans =[]
    b = len(name)
    for i in lst:
        if i.u_name[3:] == name:
            if i.u_name[:2] == '0U':
                continue
            ans.append(int(i.u_name[:2]))
    if not ans:
        return '00' + ':' + name
    c=str(max(ans)+1)
    if len(c) == 1:
        c = '0' + c
    return c + ':' + name

# Create your views here.
def fun_for_all(username):
    lst0 = user_posts.objects.all()
    lst1 = User.objects.all()
    dests, count = [], -1
    user_details0, user_details1 = 0, 0
    user_prf_pic ,official= [],["SAC'22","CLUB ORG","Sport Council","FEST ORG"]
    for i in lst0:
        if i.u_name[3:] in official:
            continue
        if i.u_name == '0U' + ':' + username:
            user_details0 = i
        if i.u_name[:2] == '0U':
            i.u_name = i.u_name[3:]
            user_prf_pic.append(i)
            continue
        count = 0
        for j in i.comments:
            if j == '$':
                count+=1
        i.comments = i.comments[:3] + str(count)
        i.id = i.u_name[3:]
        dests.append(i)
    for i in lst1:
        if i.username == username:
            user_details1 = i


#    profile, un_profile = filter_users(lst0, lst1)
    dests.reverse()
    dict ={'dests': dests, 'user_details0': user_details0, 'user_details1': user_details1,
                   'user_prf_pic':user_prf_pic,}
    return dict

def my_profile(username):
    lst = user_posts.objects.all()
    lst1 = User.objects.all()
    dests = []
    user_details0,user_details1=0,0
    for i in lst:
        if i.u_name[3:] == username:
            if i.u_name == '0U' + ':' + username:
                user_details0 = i
                continue
            count = 0
            for j in i.comments:
                if j == '$':
                    count+=1
            i.comments = i.comments[:3] + str(count)
            dests.append(i)
    for i in lst1:
        if i.username == username:
            user_details1 = i
    dests.reverse()
    return {'dests':dests,'username':username,'user_details0':user_details0,
            'user_details1':user_details1}

def comments_for_all(username,username_m):
    lst0 = user_posts.objects.all()
    lst1 = User.objects.all()
    user_details0, user_details1, user_details2, a, b = 0, 0, 0, 0, 0
    for i in lst0:
        if i.u_name == username:
            a, b = i.u_name, i.caption
            comment, no_of_comms = comments(i.comments)
            comment.insert(0, no_of_comms)
        if i.u_name == '0U' + ':' + username_m:
            user_details0 = i
        if i.u_name == '0U' + ':' + username[3:]:
            user_details2 = i
    count = 0
    for i in lst1:
        if i.username == username_m:
            user_details1 = i
        count += 1

    dict = {'a': a, 'b': b, 'user_details0': user_details0, 'user_details2': user_details2,
                   'user_details1': user_details1, 'comment': comment}
    return dict

# Create your views here.
def reg_log(request):
    return render(request, 'login,register.html')
def register(request):
    return render(request, 'register.html')

def comment(request):
    return render(request, 'comments.html')
def main_page(request):
    if request.method == 'POST':
        username = request.POST["input1"]
        return render(request, 'mobile_login_page.html', fun_for_all(username))
    else:
        return render(request, 'login,register.html')
def main_page_L(request):

    if request.method == 'POST':
        username = request.POST["input1"]
        password = request.POST["input2"]
        user = auth.authenticate(username = username, password = password)
        if user:
# using fun_for_all
#            if username == 'Vidya Sagar':
            return render(request, 'mobile_login_page.html',fun_for_all(username))
#            else:
#                messages.info(request, 'this site was buyed by other clients, ask the owener of this site to login')
#                return render(request, 'login,register.html')
        else:
            messages.info(request, 'invalid credentials, if u dont have an account goto create an account HOWLE:')
            return render(request, 'login,register.html')
    else:
        return render(request, 'login,register.html')

def official_page(request):
    if request.method == 'POST':
        username = request.POST["input1"]
        user_details0, user_details1 = 0, 0
        lst0 = user_posts.objects.all()
        lst1 = User.objects.all()
        official = ["SAC'22","CLUB ORG","Sport Council","FEST ORG"]
        dests = []
        user_prf_pic = []
        for i in lst0:
            if i.u_name == '0U' + ':' + username:
                user_details0 = i
            if i.u_name[:2] == '0U' and i.u_name[3:] in official:
                i.u_name = i.u_name[3:]
                user_prf_pic.append(i)
                continue
            if i.u_name[3:] in official:
                count = 0
                for j in i.comments:
                    if j == '$':
                        count += 1
                i.comments = i.comments[:3] + str(count)
                i.id = i.u_name[3:]
                dests.append(i)
        for i in lst1:
            if i.username == username:
                user_details1 = i

        dict = {'dests': dests, 'user_details0': user_details0, 'user_details1': user_details1,
                   'user_prf_pic':user_prf_pic,}
        return render(request, 'OFFICIAL PAGE.html', dict)



def main_page_R(request):

    if request.method == 'POST':
        username = request.POST["input0"]
        first_name = request.POST["input1"]
        last_name = request.POST["input2"]
        password1 = request.POST["input3"]
        password2 = request.POST["input4"]
        email = request.POST["input5"]

        if username and first_name and last_name and password1 and password2 and email:
            if password1 != password2:
                messages.info(request, "When will u grown up!!, password1 and password2 aren't matching")
                return render(request, 'register.html')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "UserName was already taken, please register with another user name")
                return render(request, 'register.html')
            elif password1 == password2:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name,last_name=last_name)
                user.save()

# using fun_for_all
                return render(request, 'mobile_login_page.html', fun_for_all(username))
#                messages.info(request, 'this site was buyed by other clients, ask the owener of this site to login')
#                return render(request, 'register.html')
            else:
                return render(request, 'register.html')
        else:
            messages.info(request, "Fill All The Details While Registering")
            return render(request, 'register.html')
    else:
        return render(request, 'register.html')

def main_page_U(request):
    if request.method == "POST":
        table = user_posts()
        username = request.POST["input1"]
        table.u_name = multi_upload(username, user_posts.objects.all())
        try:
            table.U_main_pic = request.FILES["input3"]
            table.caption = request.POST["input4"]
            table.comments = '000' + '@'
        except:
            messages.info(request, 'fill all the details')
            return render(request, 'home.html', my_profile(username))
        if len(table.caption) == 0:
            messages.info(request, 'enter the caption')
            return render(request, 'home.html', my_profile(username))
        table.save()

# using fun_for_all
        return render(request, 'home.html', my_profile(username))
    else:
        return render(request, 'login,register.html')

def del_my_details(request):
    if request.method == "POST":
        username = request.POST["input1"]
        username_m = request.POST["input2"]
        del_my_details = user_posts.objects.get(u_name = username)
        del_my_details.delete()
# using fun_for_all
        return render(request, 'mobile_login_page.html', my_profile(username_m))
    else:
        return render(request, 'login,register.html')

def your_profile(request):
    if request.method == "POST":
        username = request.POST['input1']
# my_profile
        return render(request, 'home.html', my_profile(username))
    else:
        return render(request, 'login,register.html')

def profile_pic(request):
    if request.method == "POST":
        username = request.POST['input1']
        try:
            profile_pic = request.FILES['input3']
        except:
            return render(request, 'home.html', my_profile(username))
        user = user_posts.objects.all()

        for i in user:
            if i.u_name == '0U' + ':' + username:
                user = user_posts.objects.get(u_name = '0U' + ':' + username)
                user.U_main_pic = profile_pic
                user.save()
                break
        else:
            table = user_posts()
            table.u_name = '0U' + ':' + username
            table.caption = 'df'
            table.U_main_pic = profile_pic
            table.save()
# using my_profile
        return render(request, 'home.html', my_profile(username))

def user_name_user_details(request):
    if request.method == "POST":
        username = request.POST['input0']
        username_m = request.POST['input1']
        lst0 = user_posts.objects.all()
        lst1 = User.objects.all()

        user_details0,user_details1,user_details2 = 0,0,0
        dests = []
        for i in lst0:
            if i.u_name[3:] == username_m and i.u_name[1] == 'U':
                user_details0 = i
            if i.u_name == '0U' + ':' + username[3:]:
                i.u_name = i.u_name[3:]
                user_details2 = i
                continue
            if i.u_name[3:] == username[3:]:
                count = 0
                for j in i.comments:
                    if j == '$':
                        count += 1
                i.comments = i.comments[:3] + str(count)
                dests.append(i)
        for i in lst1:
            if i.username == username_m:
                user_details1 = i
                break
        return render(request, 'user_name_user_details.html', {'dests':dests,'user_details1':user_details1,
                            'user_details2':user_details2,'username':username_m,'user_details0':user_details0})

def post_comments(request):
    if request.method == "POST":
        #username1 = user
        #username2 = user_uploads
        username_m = request.POST["advance2"]
        username = request.POST["advance1"]
        comment = request.POST["advance0"]

        if not comment:
            return render(request,'comments.html',comments_for_all(username, username_m))

        user = user_posts.objects.get(u_name = username)
        p=username_m.upper()
        user.comments = user.comments + p + " : " + comment + "$"
        user.save()
# using fun_for_all
        return render(request,'comments.html',comments_for_all(username, username_m))
    else:
        return render(request, 'login,register.html')


def view_comments(request):
    if request.method == 'POST':
        username = request.POST['advance1']
        username_m = request.POST['advance0']
        return render(request,'comments.html',comments_for_all(username, username_m))
    else:
        return render(request, 'login,register.html')

def post_likes(request):
    if request.method == 'POST':
        username = request.POST['advance1']
        username_m = request.POST['advance2']
        user = user_posts.objects.get(u_name=username)
        a = str(int(user.comments[:3])+1)
        if len(a) == 1:
            a = '00' + a
        elif len(a) == 2:
            a = '0' + a
        user.comments =  a + user.comments[3:]
        user.save()

        return render(request, 'mobile_login_page.html', fun_for_all(username_m))















## extensions of the appp
def acedemic_fun(username):
    lst0 = user_posts.objects.all()
    lst1 = User.objects.all()
    user_details0, user_details1 = 0, 0
    for i in lst0:
        if i.u_name == '0U' + ':' + username:
            user_details0 = i
            break
    for i in lst1:
        if i.username == username:
            user_details1 = i
            break
    dict = {'user_details0': user_details0, 'user_details1': user_details1 }
    return dict

def fests(request):
    if request.method == 'POST':
        username = request.POST['input1']
        return render(request, 'FESTS.html', acedemic_fun(username))
def clubs(request):
    if request.method == 'POST':
        username = request.POST['input1']
        return render(request, 'CLUBS.html', acedemic_fun(username))
def sports(request):
    if request.method == 'POST':
        username = request.POST['input1']
        return render(request, 'SPORTS.html', acedemic_fun(username))
def odyssey(request):
    if request.method == 'POST':
        username = request.POST['input1']
        return render(request, 'odyssey.html', acedemic_fun(username))
def foot_ball(request):
    if request.method == 'POST':
        username = request.POST['input1']
        return render(request, 'foot_ball.html', acedemic_fun(username))
def acedemic(request):
    if request.method == 'POST':
        username = request.POST['input1']
        return render(request, 'ACEDEMIC.html', acedemic_fun(username))





def chatting_for_all(username):
    user = user_posts.objects.get(u_name='0U' + ':' + 'Vidya Sagar')
    str0 = "@"
    dests = []
    for i in user.comments[1:]:
        if i == '@':
            dests.append(str0)
            str0 = '@'
            continue
        str0 += i
        if str0 == "@" + username:
            str0 = ':'
    if str0 != '@':
        dests.append(str0)
    lst1 = User.objects.all()
    user_details1 = 0
    for i in lst1:
        if i.username == username:
            user_details1 = i
            break
    user_details0 = 0
    lst0 = user_posts.objects.all()
    for i in lst0:
        if i.u_name == '0U' + ':' + username:
            user_details0 = i
            break
    dests.reverse()
    length = len(username) + 1
    return {'dests': dests, 'user_details1': user_details1,'user_details0': user_details0, 'length':length }

def all_chatting(request):
    if request.method == 'POST':
        username = request.POST['input1']
        return render(request, 'all_group_message.html', chatting_for_all(username))
def chatting(request):
    if request.method == 'POST':
        username = request.POST['input1']
        return render(request, 'chatting.html', chatting_for_all(username))

def post_message(request):
    if request.method == 'POST':
        username = request.POST['input1']
        message = request.POST['message']
        user = user_posts.objects.get(u_name='0U' + ':' + 'Vidya Sagar')
        user.comments = user.comments + '@' + username + ':' + message
        user.save()
        return render(request, 'chatting.html', chatting_for_all(username))
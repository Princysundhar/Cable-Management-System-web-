import random

import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect

# Create your views here.
from App.models import *
from invoice import generate_invoice_pdf




def loginn(request):
    return render(request,"login_index.html")

def login_post(request):
    username=request.POST['textfield']
    password=request.POST['textfield2']
    data = login.objects.filter(username=username, password=password)
    if data.exists():
        request.session['lid']=data[0].id
        request.session['lg']="lin"
        if data[0].usertype == 'admin':
            return redirect('/admin_home')
        if data[0].usertype == 'staff':
            return redirect('/staff_home')
        else:
            return HttpResponse("<script>alert('Invalid Authentication!.. Try Again');window.location='/'</script>")
    else:
        return HttpResponse("<script>alert('404 Error!!');window.location='/'</script>")

def logout(request):
    request.session['lg'] =""
    return HttpResponse("<script>alert('Logout Successfully');window.location='/'</script>")

def forgot_password(request):
    return render(request,"forgot_password.html")

def forgot_password_post(request):
    email = request.POST['textfield']
    res = login.objects.filter(username=email)
    if res.exists():
        pwd = res[0].password
        import smtplib

        s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        s.starttls()
        s.login("hanimamanoj3@gmail.com", "ldfg unko cbal goyb")
        msg = MIMEMultipart()  # create a message.........."
        msg['From'] = "hanimamanoj3@gmail.com"
        msg['To'] = email
        msg['Subject'] = "Your Password for Cable Managament System Website"
        body = "Your Password is:- - " + str(pwd)
        msg.attach(MIMEText(body, 'plain'))
        s.send_message(msg)
        return HttpResponse("<script>alert('password sended');window.location='/'</script>")
    return HttpResponse("mail incorrect")

def and_customer_forgot_password(request):
    email = request.POST['email']
    res = login.objects.filter(username=email)
    if res.exists():
        pwd = res[0].password
        import smtplib

        s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        s.starttls()
        s.login("hanimamanoj3@gmail.com", "ggcf hklw pngz wvsh")
        msg = MIMEMultipart()  # create a message.........."
        msg['From'] = "hanimamanoj3@gmail.com"
        msg['To'] = email
        msg['Subject'] = "Your Password for Cable Managament System Website"
        body = "Your Password is:- - " + str(pwd)
        msg.attach(MIMEText(body, 'plain'))
        s.send_message(msg)
        return JsonResponse({"status": "ok"})
    else:
        return JsonResponse({"status":"no"})


# .............................................. ADMIN ............................................................................

def admin_home(request):
    request.session['ok'] = "Admin"

    return render(request,"admin/admin_index.html")

def area_add(request):
    request.session['name'] = "AREA MANAGEMENT"
    return render(request,"admin/area.html")

def area_add_post(request):
    area_name = request.POST['textfield']
    data = area.objects.filter(area_name=area_name)
    if data.exists():
        return HttpResponse("<script>alert('Area already Exists!!');window.location='/area_add'</script>")
    else:
        obj = area()
        obj.area_name = area_name
        obj.save()
        return HttpResponse("<script>alert('Area Added');window.location='/area_add'</script>")

def view_area(request):
    request.session['name'] = "AREA MANAGEMENT"
    data=area.objects.all()
    return render(request,"admin/view_area.html",{'data':data})

def area_update(request,id):
    request.session['name'] = "AREA MANAGEMENT"
    res=area.objects.get(id=id)
    return render(request, "admin/update_area.html",{'data':res})

def area_update_post(request,id):
    area_name=request.POST['textfield']
    area.objects.filter(id=id).update(area_name=area_name)
    return HttpResponse("<script>alert('area updated');window.location='/view_area'</script>")

def area_delete(request,id):
    area.objects.filter(id=id).delete()
    return HttpResponse("<script>alert('deleted successfully');window.location='/view_area'</script>")


def staff_add(request):
    request.session['name'] = "STAFF MANAGEMENT"
    return render(request, "admin/staff.html")

def staff_add_post(request):
    Name = request.POST['textfield']
    Place=request.POST['textfield2']
    Post = request.POST['textfield3']
    Pin = request.POST['textfield4']
    Email = request.POST['textfield5']
    Contact = request.POST['textfield6']
    Qualification = request.POST['textfield8']
    Experience = request.POST['textfield9']
    Category=request.POST['category']
    Photo = request.FILES['fileField']
    d = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    FS = FileSystemStorage()
    FS.save(r"C:\Users\rithi\OneDrive\Desktop\New folder (3)\COM_SYSTEM\COM_SYSTEM\App\static\image\\" + d + '.jpg', Photo)
    path = "/static/image/" + d + '.jpg'
    p = random.randint(0000,9999)
    data = login.objects.filter(username=Email)
    if data.exists():
        return HttpResponse("<script>alert('Already Exists');window.location='/staff_add'</script>")
    else:
        log = login()
        log.username = Email
        log.usertype = 'staff'
        log.password=p
        log.save()
        obj=staff()
        obj.s_name=Name
        obj.s_place=Place
        obj.s_post=Post
        obj.s_pin=Pin
        obj.s_email=Email
        obj.s_contact=Contact
        obj.s_photo = path
        obj.s_qualification=Qualification
        obj.s_experience=Experience
        obj.s_category=Category
        obj.LOGIN = log
        obj.save()

        import smtplib

        s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        s.starttls()
        s.login("hanimamanoj3@gmail.com", "bldw wfiy gfge cxqe")
        msg = MIMEMultipart()  # create a message.........."
        msg['From'] = "hanimamanoj3@gmail.com"
        msg['To'] = Email
        msg['Subject'] = "Your Password for Cable Managament System Website"
        body = "Your Password is:- - " + str(p)
        msg.attach(MIMEText(body, 'plain'))
        s.send_message(msg)
        # return HttpResponse("<script>alert('password sended');window.location='/'</script>")

        return HttpResponse("<script>alert('staff addeded successfully,Password Sended');window.location='/staff_add'</script>")


def view_staff(request):
    request.session['name'] = "STAFF MANAGEMENT"
    data=staff.objects.all()
    return render(request, "admin/view_staff.html", {'data': data})


def staff_update(request,id):
    request.session['name'] = "STAFF MANAGEMENT"
    res=staff.objects.get(id=id)
    return render(request, "admin/update_staff.html",{'data':res})

def staff_update_post(request,id):
    try:

        Name = request.POST['textfield']
        Place = request.POST['textfield2']
        Post = request.POST['textfield3']
        Pin = request.POST['textfield4']
        Email = request.POST['textfield5']
        Contact = request.POST['textfield6']
        Qualification = request.POST['textfield8']
        Experience = request.POST['textfield9']
        Category = request.POST['category']
        Photo = request.FILES['fileField']
        d = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        FS = FileSystemStorage()
        FS.save(r"C:\Users\rithi\OneDrive\Desktop\New folder (3)\COM_SYSTEM\COM_SYSTEM\App\static\image\\" + d + '.jpg', Photo)
        path = "/static/image/" + d + '.jpg'
        staff.objects.filter(id=id).update(s_name=Name, s_place=Place, s_post=Post, s_pin=Pin, s_email=Email,s_contact=Contact, s_qualification=Qualification, s_experience=Experience,s_category=Category,s_photo=path)
        return HttpResponse("<script>alert('staff updated');window.location='/view_staff'</script>")
    except Exception as e:
        Name = request.POST['textfield']
        Place = request.POST['textfield2']
        Post = request.POST['textfield3']
        Pin = request.POST['textfield4']
        Email = request.POST['textfield5']
        Contact = request.POST['textfield6']
        Qualification = request.POST['textfield8']
        Experience = request.POST['textfield9']
        Category = request.POST['category']
        staff.objects.filter(id=id).update(s_name=Name,s_place=Place, s_post=Post, s_pin=Pin, s_email=Email,s_contact=Contact, s_qualification=Qualification,s_experience=Experience, s_category=Category)
        return HttpResponse("<script>alert('staff updated');window.location='/view_staff'</script>")

def staff_delete(request,id):
    staff.objects.filter(id=id).delete()
    return HttpResponse("<script>alert('deleted successfully');window.location='/view_staff'</script>")

def area_allocations(request,id):
    request.session['name'] = "AREA ALLOCATION"
    data = area.objects.all()
    return render(request, "admin/area_allocation.html",{'id':id,'data': data})

def area_allocation_post(request,id):
    area_name = request.POST['select']
    data = area_allocation.objects.filter(AREA=area_name)
    if data.exists():
        return HttpResponse("<script>alert('Area Already Allocated');window.location='/view_staff'</script>")
    else:
        obj = area_allocation()
        obj.AREA_id = area_name
        obj.STAFF_id = id
        obj.save()
        return HttpResponse("<script>alert('area allocated');window.location='/view_staff'</script>")

def view_allocations(request,id):
    request.session['name'] = "AREA ALLOCATION"
    data=area_allocation.objects.filter(STAFF_id=id)
    return render(request, "admin/view_area_allocation.html", {'data': data})


def package_add(request):
    request.session['name'] = "PACKAGE MANAGEMENT"
    return render(request, "admin/add package.html")

def package_add_post(request):
    Type = request.POST['textfield']
    Name = request.POST['textfield2']
    Amount = request.POST['textfield3']
    data = package.objects.filter(pa_name = Name)
    if data.exists():
        return HttpResponse("<script>alert('Package Already Exists!');window.location='/package_add'</script>")
    else:
        obj = package()
        obj.pa_type=Type
        obj.pa_name = Name
        obj.pa_amount=Amount
        obj.save()
        return HttpResponse("<script>alert('Package Added');window.location='/package_add'</script>")

def view_package(request):
    request.session['name'] = "PACKAGE MANAGEMENT"
    data=package.objects.all()
    return render(request,"admin/view_package.html",{'data':data})

def package_update(request,id):
    request.session['name'] = "PACKAGE MANAGEMENT"
    res=package.objects.get(id=id)
    return render(request, "admin/update_package.html",{'data':res})

def package_update_post(request,id):
    Type = request.POST['textfield']
    Name = request.POST['textfield2']
    Amount = request.POST['textfield3']
    package.objects.filter(id=id).update(pa_type=Type,pa_name=Name,pa_amount=Amount)
    return HttpResponse("<script>alert('package updated');window.location='/view_package'</script>")

def package_delete(request,id):
    package.objects.filter(id=id).delete()
    return HttpResponse("<script>alert('deleted successfully');window.location='/view_package'</script>")

def view_customer(request):
    request.session['name'] = "VIEW CUSTOMER"
    data=customer.objects.all()
    return render(request, "admin/view_customer.html", {'data': data})

def view_subscription_list(request):
    request.session['name'] = "VIEW SUBCRIPTION LIST"
    data = subscription_list.objects.filter(status='active')
    return render(request, "admin/view_subscription_list.html", {'data': data})

def salary_add(request,id):
    request.session['name'] = "ADD SALARY"
    return render(request,"admin/salary.html",{'id':id})

def salary_add_post(request,id):
    Amount=request.POST['textfield']
    data = salary.objects.filter(STAFF=id)
    if data.exists():
        return HttpResponse("<script>alert('Salary Already Credited');window.location='/view_staff'</script>")
    else:
        obj = salary()
        obj.s_amount=Amount
        obj.STAFF_id = id
        obj.date = datetime.datetime.now().strftime("%Y-%m-%d")
        obj.s_credited = 'not credited'
        obj.save()
        return HttpResponse("<script>alert('salary added');window.location='/view_staff'</script>")


def view_salary(request,id):
    request.session['name'] = "VIEW SALARY"
    data=salary.objects.filter(STAFF_id=id)
    return render(request, "admin/view_salary.html", {'data': data})

# ........... SALARY  .....................

def payment_mode(request,id):
    qry=staff.objects.all()
    return render(request,"admin/payment_mode.html",{"data":qry,"id":id})

def payment_mode_post(request,id):
    mode = request.POST['mode']
    st = request.POST['s']
    # sid = request.session['sidd']

    # print("sssssss",st)
    if mode == 'Offline':
        ob = payment()
        ob.date = datetime.datetime.today()
        ob.STAFF_id = st
        ob.amount = request.session['pay_amount']
        ob.date = datetime.datetime.now().strftime("%Y-%m-%d")
        ob.year = datetime.datetime.now().strftime("%Y")
        ob.payment_status = "offline"
        ob.month = datetime.datetime.now().strftime("%m")
        ob.save()
        return HttpResponse('''<script>alert("salary is offline");window.location="/view_staff"</script>''')

    else:
        return redirect('/user_pay_proceed')



def user_pay_proceed(request):

    # amt=request.POST['textfield9']
    data = salary.objects.all()
    for i in data:
        amt = i.s_amount
        sid = i.STAFF.id

    request.session['pay_amount'] = amt
    request.session['sidd'] = sid

    import razorpay

    razorpay_api_key = "rzp_test_MJOAVy77oMVaYv"
    razorpay_secret_key = "MvUZ03MPzLq3lkvMneYECQsk"

    razorpay_client = razorpay.Client(auth=(razorpay_api_key, razorpay_secret_key))

    amount = int(amt)*100
    # amount = float(amount)

    # Create a Razorpay order (you need to implement this based on your logic)
    order_data = {
        'amount': amount,
        'currency': 'INR',
        'receipt': 'order_rcptid_11',
        'payment_capture': '1',  # Auto-capture payment
    }

    # Create an order
    order = razorpay_client.order.create(data=order_data)

    context = {
        'razorpay_api_key': razorpay_api_key,
        'amount': order_data['amount'],
        'currency': order_data['currency'],
        'order_id': order['id'],
    }

    return render(request, 'admin/UserPayProceed.html', {'razorpay_api_key': razorpay_api_key,
                                            'amount': order_data['amount'],
                                            'currency': order_data['currency'],
                                            'order_id': order['id']})


def on_payment_success(request):
    sid= request.session['sidd']
    print("ssss",sid)
    qry=payment.objects.filter(STAFF_id=sid,month=datetime.datetime.now().strftime('%m'))
    if qry.exists():
        return HttpResponse('''<script>alert("Already Paid");window.location="/view_staff"</script>''')

    ob=payment()
    ob.date=datetime.datetime.today()
    ob.STAFF_id= sid
    ob.amount=  request.session['pay_amount']
    ob.date=datetime.datetime.now().strftime("%Y-%m-%d")
    ob.year=datetime.datetime.now().strftime("%Y")
    ob.payment_status="online"
    ob.month=datetime.datetime.now().strftime("%m")
    ob.save()
    salary.objects.filter(STAFF=sid).update(s_credited='salary credited')
    return HttpResponse('''<script>alert("Success!");window.location="/view_staff"</script>''')


def view_customer_status(request,id):
    request.session['name'] = "VIEW CUSTOMER STATUS"
    # data=subscription_list.objects.filter(Q(status='active') | Q(status='inactive'))
    data=subscription_list.objects.filter(CUSTOMER=id)
    return render(request, "admin/view_customer_status.html", {'data': data})

def view_attendance(request,id):
    request.session['name'] = "VIEW ATTENDANCE"
    data=attendance.objects.filter(STAFF=id)
    return render(request, "admin/view_attendance.html", {'data': data})

def view_collection_payment(request):
    request.session['name'] = "VIEW COLLECTION PAYMENT"
    data = collection_payment.objects.all()
    return render(request, "admin/view_collection_payment.html", {'data': data})

def report_generation(request):

    request.session['name'] = "REPORT GENERATION"

    return render(request,"admin/report_generation.html")


def report_generation_post(request):
    try:
        current_month = datetime.datetime.now().month
        option = request.POST['select']
        print("option",option)
        # print(option,"okkkkkkkkk")
        month = request.POST['select2']
        # print("dataaaaaaa",month)
        if option == 'salary':
            data = payment.objects.filter(date__month=current_month)
            return render(request, "admin/report_generation.html", {"data": data})
        else:
            data1 = subscription_list.objects.filter(date__month = month)
            total = 0
            for i in data1:
                total = total + int(i.amount)
            return render(request,"admin/report_generation.html",{"data1":data1,"total":total})
    except:
        return redirect("/")


# ............................................ STAFF .......................................................................

def staff_home(request):
    name = staff.objects.get(LOGIN=request.session['lid']).s_name
    img = staff.objects.get(LOGIN=request.session['lid']).s_photo
    # print("nnnnnnnn",name)
    return render(request,"staff/staff_index.html",{"name":name,"img":img})

def manage_staff_profile(request):
    request.session['head'] = "My Profile"
    name = staff.objects.get(LOGIN=request.session['lid']).s_name
    img = staff.objects.get(LOGIN=request.session['lid']).s_photo
    data = staff.objects.get(LOGIN=request.session['lid'])
    return render(request,"staff/Manage_staff.html",{"data":data,"name":name,"img":img})

def manage_staff_profile_post(request):
    Name = request.POST['textfield']
    Place = request.POST['textfield2']
    Post = request.POST['textfield3']
    Pin = request.POST['textfield4']
    Email = request.POST['textfield5']
    Contact = request.POST['textfield6']
    Qualification = request.POST['textfield8']
    Experience = request.POST['textfield9']
    Category = request.POST['category']
    Photo = request.FILES['fileField']
    d = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    FS = FileSystemStorage()
    FS.save(r"C:\Users\rithi\OneDrive\Desktop\New folder (3)\COM_SYSTEM\COM_SYSTEM\App\static\image\\" + d + '.jpg', Photo)
    path = "/static/image/" + d + '.jpg'
    staff.objects.filter(LOGIN=request.session['lid']).update(s_name=Name,s_place=Place,s_post=Post,
                                                              s_pin=Pin,s_email=Email,s_contact=Contact,s_photo=path,
                                                              s_qualification=Qualification,s_experience=Experience,s_category=Category)
    return HttpResponse("<script>alert('Profile Updated');window.location='/staff_home'</script>")


def view_allocated_area(request):
    name = staff.objects.get(LOGIN=request.session['lid']).s_name
    img = staff.objects.get(LOGIN=request.session['lid']).s_photo
    request.session['head'] = "ALLOCATED AREA"
    data = area_allocation.objects.filter(STAFF__LOGIN=request.session['lid'])
    return render(request,"staff/view_allocated_area.html",{"data":data,"name":name,"img":img})

def staff_add_customer(request,id):
    name = staff.objects.get(LOGIN=request.session['lid']).s_name
    img = staff.objects.get(LOGIN=request.session['lid']).s_photo
    request.session['head'] = "CUSTOMER MANAGEMENT"
    return render(request,"staff/add_customer.html",{"id":id,"name":name,"img":img})

def staff_add_customer_post(request,id):
    name = request.POST['textfield']
    place = request.POST['textfield2']
    post = request.POST['textfield3']
    pin = request.POST['textfield4']
    email = request.POST['textfield5']
    contact = request.POST['textfield6']
    number = request.POST['textfield7']
    image = request.FILES['fileField']
    d = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    FS = FileSystemStorage()
    FS.save(r"C:\Users\rithi\OneDrive\Desktop\New folder (3)\COM_SYSTEM\COM_SYSTEM\App\static\image\\" + d + '.jpg', image)
    path = "/static/image/" + d + '.jpg'
    data = login.objects.filter(username=email)
    if data.exists():
        return HttpResponse("<script>alert('Customer is already Exists!!');window.location='/staff_home'</script>")
    else:
        obj = login()
        obj.username = email
        obj.password = random.randint(0000,9999)
        obj.usertype = 'customer'
        obj.save()

        obj1 = customer()
        obj1.c_name = name
        obj1.c_place = place
        obj1.c_post = post
        obj1.c_pin = pin
        obj1.c_email = email
        obj1.c_contact = contact
        obj1.c_number = number
        obj1.c_photo = path
        obj1.AREA_id = id
        obj1.LOGIN = obj
        obj1.save()
        return HttpResponse("<script>alert('customer Added');window.location='/staff_home'</script>")

def staff_view_customer(request,id):
    name = staff.objects.get(LOGIN=request.session['lid']).s_name
    img = staff.objects.get(LOGIN=request.session['lid']).s_photo
    request.session['head'] = "CUSTOMER MANAGEMENT"
    data = customer.objects.filter(AREA = id)
    return render(request,"staff/view_customer.html",{"data":data,"name":name,"img":img})

def staff_edit_customer(request,id):
    name = staff.objects.get(LOGIN=request.session['lid']).s_name
    img = staff.objects.get(LOGIN=request.session['lid']).s_photo
    data = customer.objects.get(id=id)
    return render(request,"staff/edit_customer.html",{"data":data,"id":id,"name":name,"img":img})

def staff_edit_customer_post(request,id):
    try:
        name = request.POST['textfield']
        place = request.POST['textfield2']
        post = request.POST['textfield3']
        pin = request.POST['textfield4']
        email = request.POST['textfield5']
        contact = request.POST['textfield6']
        image = request.FILES['fileField']
        d = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        FS = FileSystemStorage()
        FS.save(r"C:\Users\rithi\OneDrive\Desktop\New folder (3)\COM_SYSTEM\COM_SYSTEM\App\static\image\\" + d + '.jpg', image)
        path = "/static/image/" + d + '.jpg'
        customer.objects.filter(id=id).update(c_name = name,c_place = place,c_post = post,c_pin = pin,c_email = email,c_contact = contact,c_photo = path)
        return HttpResponse("<script>alert('customer Updated');window.location='/staff_home'</script>")
    except Exception as e:
        name = request.POST['textfield']
        place = request.POST['textfield2']
        post = request.POST['textfield3']
        pin = request.POST['textfield4']
        email = request.POST['textfield5']
        contact = request.POST['textfield6']
        customer.objects.filter(id=id).update(c_name=name, c_place=place, c_post=post, c_pin=pin, c_email=email,c_contact=contact)
        return HttpResponse("<script>alert('customer Updated');window.location='/staff_home'</script>")


def staff_delete_customer(request,id):
    customer.objects.get(id=id).delete()
    return HttpResponse("<script>alert('customer Deleted');window.location='/staff_home'</script>")



# ....... MANAGE OFFER ...........

def staff_add_offer(request):
    name = staff.objects.get(LOGIN=request.session['lid']).s_name
    img = staff.objects.get(LOGIN=request.session['lid']).s_photo
    request.session['head'] = "OFFER MANAGEMENT"
    return render(request,"staff/add_offer.html",{"name":name,"img":img})

def staff_add_offer_post(request):
    offer_type = request.POST['textfield']
    title = request.POST['textfield2']
    offers = request.POST['textfield3']
    data = offer.objects.filter(o_type=offer_type)
    if data.exists():
        return HttpResponse("<script>alert('Offer already Exists!!');window.location='/staff_add_offer'</script>")
    else:
        obj = offer()
        obj.o_type = offer_type
        obj.o_title = title
        obj.o_offers = offers
        obj.STAFF = staff.objects.get(LOGIN=request.session['lid'])
        obj.save()
        return HttpResponse("<script>alert('Offer added');window.location='/staff_home'</script>")

def staff_view_offer(request):
    name = staff.objects.get(LOGIN=request.session['lid']).s_name
    img = staff.objects.get(LOGIN=request.session['lid']).s_photo
    request.session['head'] = "OFFER MANAGEMENT"
    data = offer.objects.filter(STAFF__LOGIN=request.session['lid'])
    return render(request,"staff/view_offer.html",{"data":data,"name":name,"img":img})

def staff_edit_offer(request,id):
    name = staff.objects.get(LOGIN=request.session['lid']).s_name
    img = staff.objects.get(LOGIN=request.session['lid']).s_photo
    request.session['head'] = "OFFER MANAGEMENT"
    data =offer.objects.get(id=id)
    return render(request,"staff/update_offer.html",{"data":data,"id":id,"name":name,"img":img})

def staff_edit_offer_post(request,id):
    offer_type = request.POST['textfield']
    title = request.POST['textfield2']
    offers = request.POST['textfield3']
    offer.objects.filter(id=id).update(o_type = offer_type,o_title = title,o_offers = offers)
    return HttpResponse("<script>alert('Offer Edited');window.location='/staff_view_offer'</script>")

def staff_delete_offer(request,id):
    offer.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Offer Removed');window.location='/staff_view_offer'</script>")


def staff_view_salary(request):
    name = staff.objects.get(LOGIN=request.session['lid']).s_name
    img = staff.objects.get(LOGIN=request.session['lid']).s_photo
    request.session['head'] = "MY SALARY"
    data = payment.objects.filter(STAFF__LOGIN=request.session['lid'])
    return render(request,"staff/view_salary.html",{"data":data,"name":name,"img":img})


def staff_view_customer_request(request):
    name = staff.objects.get(LOGIN=request.session['lid']).s_name
    img = staff.objects.get(LOGIN=request.session['lid']).s_photo
    request.session['head'] = "CUSTOMER REQUEST"
    data = subscription_list.objects.filter(status='pending')
    return render(request,"staff/view_customer_request.html",{"data":data,"name":name,"img":img})

def staff_approve_customer_request(request,id):
    subscription_list.objects.filter(id=id).update(status='active')
    return HttpResponse("<script>alert('Approved');window.location='/staff_view_customer_request'</script>")

def staff_reject_customer_request(request,id):
    subscription_list.objects.filter(id=id).update(status='inactive')
    return HttpResponse("<script>alert('Rejected');window.location='/staff_view_customer_request'</script>")


def staff_view_complaints(request):
    name = staff.objects.get(LOGIN=request.session['lid']).s_name
    img = staff.objects.get(LOGIN=request.session['lid']).s_photo
    request.session['head'] = "COMPLAINTS"
    data = complaint.objects.all()
    return render(request,"staff/view_complaint.html",{"data":data,"name":name,"img":img})

def staff_send_reply(request,id):
    name = staff.objects.get(LOGIN=request.session['lid']).s_name
    img = staff.objects.get(LOGIN=request.session['lid']).s_photo
    return render(request,"staff/send_reply.html",{"id":id,"name":name,"img":img})

def staff_send_reply_post(request,id):
    reply = request.POST['textarea']
    complaint.objects.filter(id=id).update(reply=reply,r_date=datetime.datetime.now().strftime("%Y-%m-%d"))
    return HttpResponse("<script>alert('Reply Sended');window.location='/staff_view_complaints'</script>")

def staff_view_collection_details(request):
    name = staff.objects.get(LOGIN=request.session['lid']).s_name
    img = staff.objects.get(LOGIN=request.session['lid']).s_photo
    request.session['head'] = "COLLECTION DETAILS"
    data = collection_payment.objects.all()
    return render(request,"staff/view_collection_details.html",{"data":data,"name":name,"img":img})

def staff_view_previous_service(request):
    name = staff.objects.get(LOGIN=request.session['lid']).s_name
    img = staff.objects.get(LOGIN=request.session['lid']).s_photo
    dt = datetime.datetime.now().strftime("%Y-%m-%d")
    data = subscription_list.objects.filter(date__lt=dt)
    return render(request,"staff/view_previous_service.html",{"data":data,"name":name,"img":img})

def staff_view_customer_status(request):
    name = staff.objects.get(LOGIN=request.session['lid']).s_name
    img = staff.objects.get(LOGIN=request.session['lid']).s_photo
    request.session['head'] = "CUSTOMER STATUS"
    data = subscription_list.objects.filter(Q(status='active')| Q(status='inactive'))
    return render(request,"staff/view_customer_status.html",{"data":data,"name":name,"img":img})


def staff_view_subcribed_package(request):
    name = staff.objects.get(LOGIN=request.session['lid']).s_name
    img = staff.objects.get(LOGIN=request.session['lid']).s_photo
    request.session['head'] = "VIEW SUBCRIBED PACKAGE"
    data = area_allocation.objects.filter(STAFF__LOGIN=request.session['lid'])
    ar = []
    for i in data:
        res = customer.objects.filter(AREA=i.AREA)
        for k in res:
            data1 = subscription_list.objects.filter(CUSTOMER=k).order_by('-id')
            # print(data1,"data1111111111111")
            # exp_date = data1[0].expiry_date
            status = data1[0].status
            # dt = datetime.datetime.now().strftime("%Y-%m-%d")
            import datetime
            exp_date = datetime.datetime.strptime(data1[0].expiry_date, "%Y-%m-%d")



            dt_str = datetime.datetime.now().strftime("%Y-%m-%d")
            dt = datetime.datetime.strptime(dt_str, "%Y-%m-%d")

            # dt = datetime.datetime.now().strptime(datetime.datetime.now().strftime("%Y-%m-%d"))


            if exp_date > dt:
                ar.append(
                    data1[0]
                )




        print("dataaaa",ar)
    return render(request,"staff/view_subcribed_packages.html",{"data":ar,"name":name,"img":img})

def choose_valid_date(request,id):
    return render(request,"staff/choose_valid_date.html",{"id":id})

def choose_valid_date_post(request,id):
    date = request.POST['textfield']
    obj = collection_payment()
    obj.date = date
    obj.p_date = 'pending'
    obj.p_status = 'pending'
    obj.SUBSCRIPTION_LIST_id = id
    obj.save()
    return HttpResponse("Added")




def send_remainder(request,email):
    # try:
    #     gmail = smtplib.SMTP('smtp.gmail.com', 587)
    #     gmail.ehlo()
    #     gmail.starttls()
    #     gmail.login('riss.princytv@gmail.com', 'vile vivc hvnh xdgs')
    # except Exception as e:
    #     print("Couldn't setup email!!" + str(e))
    # msg = MIMEText("Cable Service!!!!")
    # msg['Subject'] = 'Cable Information'
    # msg['To'] = email
    # msg['From'] = 'riss.princytv@gmail.com'
    # try:
    #     gmail.send_message(msg)
    # except Exception as e:
    #     print("COULDN'T SEND EMAIL", str(e))

    import smtplib

    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login("hanimamanoj3@gmail.com", "bldw wfiy gfge cxqe")
    msg = MIMEMultipart()  # create a message.........."
    msg['From'] = "hanimamanoj3@gmail.com"
    msg['To'] = email
    msg['Subject'] = "Your Password for Cable Managament System Website"
    body = "Your Password is:- - " + str(email)
    msg.attach(MIMEText(body, 'plain'))
    s.send_message(msg)
    return HttpResponse("<script>alert('Remainder sended,Check it !');window.location='/staff_view_subcribed_package'</script>")



# ............ ATTENDANCE MANAGEMENT .....................

def manage_attendance(request):
    obj = attendance.objects.filter(STAFF__LOGIN=request.session['lid'], a_date=datetime.datetime.now().strftime("%Y-%m-%d"))
    if obj.exists():
        if obj[0].a_checkout == "pending":
            obj.update(a_checkout=datetime.datetime.now().strftime("%H:%M"))
            return HttpResponse("<script>alert('Checkout added'); window.location='/staff_view_attendance'</script>")
        else:
            return HttpResponse("<script>alert('Already added'); window.location='/staff_view_attendance'</script>")


    else:
        obj = attendance()
        obj.a_checkin = datetime.datetime.now().strftime("%H:%M")
        obj.a_checkout = "pending"
        obj.a_date = datetime.datetime.now().strftime("%Y-%m-%d")
        obj.STAFF = staff.objects.get(LOGIN=request.session['lid'])
        obj.save()
        return HttpResponse("<script>alert('Checkin Added'); window.location='/staff_view_attendance'</script>")

def staff_view_attendance(request):
    name = staff.objects.get(LOGIN=request.session['lid']).s_name
    img = staff.objects.get(LOGIN=request.session['lid']).s_photo
    request.session['head'] = "VIEW ATTENDANCE"
    data = attendance.objects.filter(STAFF__LOGIN=request.session['lid'])
    return render(request,"staff/staff_view_attendance.html",{"data":data,"name":name,"img":img})

#............................ CUSTOMER (ANDROID ) ....................................



def and_customer_login(request):
    username = request.POST['username']
    password = request.POST['password']
    data = login.objects.filter(username=username,password=password)
    if data.exists():
        lid = data[0].id
        type = data[0].usertype
        res = customer.objects.get(LOGIN=lid)
        name = res.c_name
        email = res.c_email
        photo = res.c_photo
        return JsonResponse({"status":"ok","lid":lid,"type":type,"name":name,"email":email,"photo":photo})
    else:
        return JsonResponse({"status":None})


def and_customer_register(request):
    name = request.POST['name']
    place = request.POST['place']
    post = request.POST['post']
    pin = request.POST['pin']
    email = request.POST['email']
    contact = request.POST['contact']
    password = request.POST['password']
    number = request.POST['number']
    image = request.FILES['pic']
    fs = FileSystemStorage()
    d = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    fs.save(r"C:\Users\rithi\OneDrive\Desktop\New folder (3)\COM_SYSTEM\COM_SYSTEM\App\static\customers\\" + d + '.jpg', image)
    path = "/static/customers/" + d + '.jpg'

    obj1 = login()
    obj1.username = email
    obj1.password = password
    obj1.usertype = 'customer'
    obj1.save()

    obj = customer()
    obj.c_name = name
    obj.c_place = place
    obj.c_post = post
    obj.c_pin = pin
    obj.c_email = email
    obj.c_contact = contact
    obj.c_photo = path
    obj.c_number = number
    obj.LOGIN = obj1
    obj.save()
    return JsonResponse({"status":"ok"})


def and_view_area(request):
    res = area.objects.all()
    ar = []
    for i in res:
        ar.append(
            {
                "area_id":i.id,
                "area_name":i.area_name
            }
        )
    return JsonResponse({"status":"ok","data":ar})


def and_customer_view_profile(request):
    lid = request.POST['lid']
    res = customer.objects.get(LOGIN=lid)
    return JsonResponse({"status":"ok","name":res.c_name,"place":res.c_place,"post":res.c_post,"pin":res.c_pin,
                         "email":res.c_email,"contact":res.c_contact,"area":res.AREA.area_name,"photo":res.c_photo,"number":res.c_number})

def and_customer_change_password(request):
    lid = request.POST['lid']
    cur_password = request.POST['cur_password']
    new_password = request.POST['new_password']
    confirm_password = request.POST['confirm_password']
    data = login.objects.filter(password=cur_password, id=lid)
    if data.exists():
        if new_password == confirm_password:
                login.objects.filter(id=lid).update(password=confirm_password)
                return JsonResponse({"status": "ok"})
        else:
            return JsonResponse({"status": "mismatch"})
    else:
        return JsonResponse({"status": "error"})


def and_view_offer(request):
    res = offer.objects.all()
    ar = []
    for i in res:
        ar.append(
            {
                "offer_id":i.id,
                "type":i.o_type,
                "title":i.o_title,
                "offer":i.o_offers
            }
        )
    return JsonResponse({"status":"ok","data":ar})


def and_customer_view_reply(request):
    lid = request.POST['lid']
    res = complaint.objects.filter(CUSTOMER__LOGIN=lid)
    ar = []
    for i in res:
        ar.append(
            {
                "cid":i.id,
                "complaint":i.complaint,
                "date":i.date,
                "reply":i.reply,
                "reply_date":i.r_date
            }
        )
    return JsonResponse({"status":"ok","data":ar})

def and_customer_send_complaint(request):
    complaints = request.POST['complaint']
    lid = request.POST['lid']
    obj = complaint()
    obj.complaint = complaints
    obj.date = datetime.datetime.now().date()
    obj.reply = 'pending'
    obj.r_date = 'pending'
    obj.CUSTOMER = customer.objects.get(LOGIN=lid)
    obj.save()
    return JsonResponse({"status":"ok"})


# ........... SUBCRIPTION MANAGEEMENT ............................

def and_customer_view_package(request):
    res = package.objects.all()
    ar = []
    for i in res:
        ar.append(
            {
                "package_id":i.id,
                "type":i.pa_type,
                "name":i.pa_name,
                "amount":i.pa_amount
            }
        )
    return JsonResponse({"status":"ok","data":ar})

def and_customer_view_subscription_list(request):
    package_id = request.POST['package_id']
    lid = request.POST['lid']
    res = subscription_list.objects.filter(PACKAGE=package_id,CUSTOMER__LOGIN=lid)
    ar = []
    for i in res:
        ar.append(
            {
                "subcription_id":i.id,
                "type":i.type,
                "amount":i.amount,
                "status":i.status,
                "date":i.date,
                "expiry_date":i.expiry_date,
                "name":i.CUSTOMER.c_name,
                "contact":i.CUSTOMER.c_contact
            }
        )

    return JsonResponse({"status":"ok","data":ar})

def and_customer_add_subscription_list(request):
    type = request.POST['type']
    amount = request.POST['amount']
    lid = request.POST['lid']
    package_id = request.POST['package_id']
    current_date = datetime.datetime.now().date()
    obj = subscription_list()
    obj.status = 'pending'
    obj.CUSTOMER = customer.objects.get(LOGIN=lid)
    obj.type = type
    obj.amount = amount
    obj.date = current_date
    obj.expiry_date = current_date + datetime.timedelta(days=3*31)
    obj.PACKAGE_id = package_id
    obj.valid_upto = 'pending'
    obj.save()
    return JsonResponse({"status":"ok"})


# def and_customer_update_subscription_list(request):
#     type = request.POST['type']
#     amount = request.POST['amount']
#     lid = request.POST['lid']
#     package_id = request.POST['package_id']
#     subcription_id = request.POST['subcription_id']
#     current_date = datetime.datetime.now().date()
#     subscription_list.objects.filter(id=subcription_id).update(CUSTOMER = customer.objects.get(LOGIN=lid),
#                                                                type=type,amount = amount,date = datetime.datetime.now().date(),
#                                                                expiry_date=current_date + datetime.timedelta(days=3 * 31),PACKAGE_id = package_id)
#     return JsonResponse({"status":"ok"})
#
# def and_customer_delete_subscription_list(request):
#     subcription_id = request.POST['subcription_id']
#     print(subcription_id)
#     subscription_list.objects.get(id=subcription_id).delete()
#     return JsonResponse({"status":"ok"})


def and_offline_payment(request):
    amount = request.POST['amount']
    lid = request.POST['lid']
    subcription_id = request.POST['subcription_id']
    mode = request.POST['mode']
    p_date = datetime.datetime.now().date()
    # data = collection_payment.objects.filter(p_date=p_date)
    # if data.exists():
    #     return HttpResponse("already exists")
    # else:
    collection_payment.objects.filter(SUBSCRIPTION_LIST=subcription_id).update(p_date=datetime.datetime.now().date(),p_status = 'offline')
    # obj1 = collection_payment()
    # obj1.p_date=datetime.datetime.now().date()
    # obj1.p_status = 'offline'
    # obj1.date = p_date
    # obj1.SUBSCRIPTION_LIST_id = subcription_id
    # obj1.save()


    return JsonResponse({"status":"ok"})
    # else:
    #     return JsonResponse({"status":None})

def android_online_payment(request):
    amount = request.POST['amount']
    lid = request.POST['lid']
    mode = request.POST['mode']
    subcription_id = request.POST['subcription_id']
    collection_payment.objects.filter(SUBSCRIPTION_LIST=subcription_id).update(p_date=datetime.datetime.now().date(),
                                                                               p_status='online')
    # if mode == 'pending':
    # obj = payment()
    # obj.payment_status = 'online'
    # obj.date = datetime.datetime.now().date()
    # obj.month = datetime.datetime.now().month
    # obj.year = datetime.datetime.now().year
    # obj.CUSTOMER = customer.objects.get(LOGIN=lid)
    # obj.amount = amount
    # obj.save()
    # collection_payment.objects.filter(id=id).update()
    return JsonResponse({"status": "ok"})
    # else:
    #     return JsonResponse({"status":None})

def and_view_previous_history(request):
    lid = request.POST['lid']
    res = collection_payment.objects.filter(Q(p_status='online') | Q(p_status='offline'))
    ar = []
    for i in res:
        ar.append(
            {
                "hid":i.id,
                "date":i.date,
                "payment_date": i.p_date,
                "payment_status":i.p_status,
                "subcription_details":i.SUBSCRIPTION_LIST.status,
                "amount": i.SUBSCRIPTION_LIST.amount,
            }
        )
    return JsonResponse({"status":"ok","data":ar})



# ............................ INVOICE GENERATING ...................................

def generate_invoice(request):
    current_date = datetime.datetime.now().date()
    expiry_date = current_date + datetime.timedelta(days=3 * 31)
    sub_id = request.POST['subcription_id']
    invoice_number = "INVOICE"
    cust_obj = customer.objects.get(subscription_list = sub_id)
    obj = package.objects.get(subscription_list=sub_id)

    p_amount = obj.pa_amount
    p_name = obj.pa_name

    p_date = expiry_date - current_date
    items = [
        {"name": p_name, "amount": p_amount, "Duration": p_date}]

    generate_invoice_pdf(invoice_number,cust_obj.c_name,items,sub_id + ".pdf")
    path="/static/pdf/" +sub_id + ".pdf"

    return JsonResponse({"status":"ok", "path":path})

# # Example data
# invoice_number = "INVOICE"
# customer_name = "John Doe"
# items = [
#     {"name": "Product A", "quantity": 2, "price": 10},
#     {"name": "Product B", "quantity": 1, "price": 20},
#     {"name": "Product C", "quantity": 3, "price": 15}
# ]
#
# # Generate the invoice PDF
# generate_invoice_pdf(invoice_number, customer_name, items, "invoice.pdf")


def and_send_request(request):
    package_id = request.POST['package_id']
    amount = request.POST['amount']
    lid = request.POST['lid']
    current_date = datetime.datetime.now().date()
    obj = subscription_list()
    obj.amount = amount
    obj.date = current_date
    obj.expiry_date = current_date + datetime.timedelta(days=3*31)
    # obj.
    return JsonResponse({"status","ok"})


def and_customer_report(request):
    lid = request.POST['lid']
    res  = subscription_list.objects.filter(CUSTOMER__LOGIN=lid)
    ar = []
    for i in res:
        ar.append(
            {
                "subcription_id":i.id,
                "type":i.type,
                "amount":i.amount,
                "status":i.status,
                "date":i.date,
                "expiry_date":i.expiry_date,
                "name":i.CUSTOMER.c_name,
                "contact":i.CUSTOMER.c_contact
            }
        )

    print(ar)

    return JsonResponse({"status":"ok","data":ar})

def generate_report(request):
    current_date = datetime.datetime.now().date()
    expiry_date = current_date + datetime.timedelta(days=3 * 31)
    sub_id = request.POST['subcription_id']
    # print("dataaaaaaa",sub_id)
    invoice_number = "INVOICE"
    cust_obj = subscription_list.objects.all()
    # cust_obj = customer.objects.get(subscription_list=sub_id)
    obj = package.objects.get(subscription_list=sub_id)

    p_amount = obj.pa_amount
    p_name = obj.pa_name

    p_date = expiry_date - current_date
    items = [
        {"name": p_name, "amount": p_amount, "Duration": p_date}]

    generate_invoice_pdff(invoice_number, cust_obj.c_name, items, sub_id + ".pdf")
    path = "/static/pdf/" + sub_id + ".pdf"
    return JsonResponse({"status":"ok"})
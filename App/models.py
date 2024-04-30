from django.db import models

# Create your models here.
class login(models.Model):
    username=models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    usertype = models.CharField(max_length=100)

class area(models.Model):
    area_name=models.CharField(max_length=100)

class staff(models.Model):
    s_name = models.CharField(max_length=100)
    s_place = models.CharField(max_length=100)
    s_post = models.CharField(max_length=100)
    s_pin = models.CharField(max_length=100)
    s_email = models.CharField(max_length=100)
    s_contact = models.CharField(max_length=100)
    s_photo = models.CharField(max_length=100)
    s_qualification=models.CharField(max_length=100)
    s_experience = models.CharField(max_length=100)
    s_category=models.CharField(max_length=100)
    LOGIN = models.ForeignKey(login, on_delete=models.CASCADE, default=1)

class area_allocation(models.Model):
    STAFF = models.ForeignKey(staff, on_delete=models.CASCADE, default=1)
    AREA = models.ForeignKey(area, on_delete=models.CASCADE, default=1)

class salary(models.Model):
    s_amount = models.CharField(max_length=100)
    s_credited = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    STAFF = models.ForeignKey(staff, on_delete=models.CASCADE, default=1)


class customer(models.Model):
    c_name = models.CharField(max_length=100)
    c_place = models.CharField(max_length=100)
    c_post = models.CharField(max_length=100)
    c_pin = models.CharField(max_length=100)
    c_email = models.CharField(max_length=100)
    c_contact = models.CharField(max_length=100)
    c_photo = models.CharField(max_length=100)
    c_number = models.CharField(max_length=100)
    AREA = models.ForeignKey(area, on_delete=models.CASCADE, default=1)
    LOGIN = models.ForeignKey(login, on_delete=models.CASCADE, default=1)

class package(models.Model):
    pa_type = models.CharField(max_length=100)
    pa_name = models.CharField(max_length=100)
    pa_amount = models.CharField(max_length=100)


class subscription_list(models.Model):
    type = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    date = models.DateField()
    expiry_date = models.CharField(max_length=100)
    valid_upto = models.CharField(max_length=100)
    CUSTOMER = models.ForeignKey(customer, on_delete=models.CASCADE, default=1)
    PACKAGE = models.ForeignKey(package, on_delete=models.CASCADE, default=1)


class payment(models.Model):
    amount=models.CharField(max_length=1000)
    payment_status=models.CharField(max_length=1000)
    date=models.DateField()
    month = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    STAFF = models.ForeignKey(staff, on_delete=models.CASCADE, default=1)

class collection_payment(models.Model):
    date = models.CharField(max_length=100)
    p_date = models.CharField(max_length=100)
    p_status = models.CharField(max_length=100)
    SUBSCRIPTION_LIST = models.ForeignKey(subscription_list, on_delete=models.CASCADE, default=1)

class complaint(models.Model):
    complaint = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    reply = models.CharField(max_length=100)
    r_date = models.CharField(max_length=100)
    CUSTOMER = models.ForeignKey(customer, on_delete=models.CASCADE, default=1)

class offer(models.Model):
    o_type = models.CharField(max_length=100)
    o_title = models.CharField(max_length=100)
    o_offers = models.CharField(max_length=100)
    STAFF = models.ForeignKey(staff, on_delete=models.CASCADE, default=1)

class attendance(models.Model):
    a_date = models.CharField(max_length=100)
    # a_time = models.CharField(max_length=20)
    a_checkin = models.CharField(max_length=100)
    a_checkout = models.CharField(max_length=100)
    STAFF = models.ForeignKey(staff, on_delete=models.CASCADE, default=1)




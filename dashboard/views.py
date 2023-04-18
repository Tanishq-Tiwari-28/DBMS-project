import json
from django.http import JsonResponse
from django.db import connection
from urllib.parse import urlencode
# import mysql.connector
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Customer, Driver
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.hashers import make_password, BCryptSHA256PasswordHasher, check_password
# from django.contrib.auth.decorators import login_required
# from django.urls import reverse
# from django.contrib.auth import logout
# from .forms import SignupForm
from .models import request_made
user_data = None


def set_user_data(data):
    global user_data
    if not data:
        user_data = None
    else:
        user_data = data


def get_user_data():
    return user_data


def home(request):
    output = get_user_data()
    type = request.GET.get('user_type')
    print(output)
    if(output):
        return render(request, 'home.html', {'output': output})
    return render(request, 'home.html')


def usertype(request):
    return render(request, 'usertype.html')


def signup_view(request):
    if request.method == 'POST':
        role = request.POST.get('ride-type')
        email = request.POST.get('email')
        password = request.POST.get('password')
        hashed_password = make_password(password)
        firstname = request.POST.get('firstname')
        middlename = request.POST.get('middlename')
        lastname = request.POST.get('lastname')
        contact = request.POST.get('contact')
        dob = request.POST.get('DOB')
        license = request.POST.get('license')
        # import ipdb
        # ipdb.set_trace()

        # with connection.cursor() as cursor:
        #     cursor.execute("SELECT * FROM Customer WHERE email=%s", [email])
        #     cursor.execute("SELECT * FROM driver WHERE email=%s", [email])
        #     customer = cursor.fetchone()
        #     driver = cursor.fetchone()
        # if ((customer is None) and (driver is not None)):
        #     print(customer)  # customer does not exists but driver exists
        #     if(role == "Customer"):
        #         print("Email already exists in Customer table, cannot create driver")
        #         return redirect("http://127.0.0.1:8000/signup")
        #     else:
        #         with connection.cursor() as cursor:
        #             cursor.execute("INSERT INTO Customer (email, pass_word, firstname, middlename, lastname, contact, DOB) VALUES (%s, %s,%s, %s, %s, %s, %s)", [
        #                 email, hashed_password, firstname, middlename, lastname, contact, dob])
        #             print("account created")
        #             return redirect("http://127.0.0.1:8000/login")

        # elif (customer is not None and driver is None):
        #     if(role == "Customer"):
        #         output_driver = {}
        #         with connection.cursor() as cursor:
        #             cursor.execute("INSERT INTO driver (email,pass_word, firstname, middlename, lastname, contact, DOB) VALUES (%s,%s, %s, %s, %s, %s, %s)", [
        #                 email, hashed_password, firstname, middlename, lastname, contact, dob])
        #             driver_id = cursor.lastrowid
        #             output_driver = {'driver_id': driver_id, 'firstname': firstname,
        #                              'middlename': middlename, 'lastname': lastname}
        #             print(output_driver)
        #             return redirect("http://127.0.0.1:8000/signup/vehicle", output_driver)
        #     else:

        #         print("Email already exists in driver table, cannot create Customer")
        #         return redirect("http://127.0.0.1:8000/signup")
        # else:
        if(role == "Customer"):
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO Customer (email, pass_word, firstname, middlename, lastname, contact, DOB) VALUES (%s, %s,%s, %s, %s, %s, %s)", [
                    email, hashed_password, firstname, middlename, lastname, contact, dob])
                customer_id = cursor.lastrowid
                print("account created")
                cursor.execute(
                    "insert into customer_details(customer_id , contact) values(%s , %s)", [customer_id, contact])
                return redirect("http://127.0.0.1:8000/login")
        output_driver = {}
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT admin_id FROM Admins ORDER BY admin_id DESC LIMIT 1")
            row = cursor.fetchone()
            admin_id = row[0]
        with connection.cursor() as cursor:
            print(admin_id)
            cursor.execute("INSERT INTO driver (email,pass_word, firstname, middlename, lastname, contact, DOB , license_no , verified , verified_by) VALUES (%s,%s, %s, %s, %s, %s, %s , %s , %s ,%s)", [
                email, hashed_password, firstname, middlename, lastname, contact, dob, license, 1, admin_id])
            driver_id = cursor.lastrowid
            cursor.execute(
                "UPDATE Admins SET verified_Driver = verified_Driver + 1 WHERE admin_id = %s;", [admin_id])
            cursor.execute("INSERT INTO verifies(driver_id, Admin_id) VALUES(%s, %s)", [
                           driver_id, admin_id])
            cursor.execute(
                "insert into driver_details(driver_id , contact) values(%s , %s)", [driver_id, contact])
            output_driver = {'driver_id': driver_id, 'firstname': firstname,
                             'middlename': middlename, 'lastname': lastname}
            print(output_driver)
            return redirect("http://127.0.0.1:8000/signup/vehicle?driver_id={}&firstname={}&middlename={}&lastname={}".format(driver_id, firstname, middlename, lastname))

    return render(request, 'signup.html')


def reg_vehicle(request):
    driver_id = request.GET.get('driver_id')
    firstname = request.GET.get('firstname')
    middlename = request.GET.get('middlename')
    lastname = request.GET.get('lastname')
    print("dodhgild", driver_id)
    if request.method == 'POST':
        type = request.POST.get('car_type')
        engine_no = request.POST.get('engine_no')
        manufacturing_date = request.POST.get('manufacturing_date')
        valid_till = request.POST.get('valid_till')
        car_model = request.POST.get('car_model')
        car_make = request.POST.get('car_make')
        if(type == "SEDAN"):
            comfort = request.POST.get('comfort_level')
        elif(type == "SUV"):
            road = request.POST.get('roadtype')
        elif(type == "HATCHBACK"):
            passengers = request.POST.get('tot_passengers')

        with connection.cursor() as cursor:
            cursor.execute(
                "insert into Vehicle (owner_firstname, owner_middlename, owner_lastname, engine_no, date_of_manufacture, validity, car_model, car_make, car_type ,driver_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s ) ",
                [firstname, middlename, lastname, engine_no, manufacturing_date, valid_till, car_model, car_make, type, driver_id])
            print("Vehicle registered")
            vehicle_id = cursor.lastrowid
            if(type == "SEDAN"):
                cursor.execute(
                    "insert into sedan(vehicle_id , comfort_level) values(%s,%s)", [vehicle_id, comfort])
            elif(type == "SUV"):
                cursor.execute("insert into SUV(vehicle_id , roadtype) values(%s,%s)", [
                               vehicle_id, road])
            elif(type == "HATCHBACK"):
                cursor.execute("insert into Hatchback(vehicle_id , tot_passengers) values(%s,%s)", [
                               vehicle_id, passengers])
            print(vehicle_id)
            return redirect("http://127.0.0.1:8000/login")

    return render(request, 'regvehicle.html')


def Login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        cursor = connection.cursor()
        print(email)
        print(password)
        string = f'''SELECT r.email,
                        COALESCE(c.firstname ,d.firstname) AS owner_firstname,
                        COALESCE(c.middlename ,d.middlename) AS owner_middlename,
                        COALESCE(c.lastname ,d.lastname) AS owner_lastname,
                        COALESCE(c.dob ,d.dob) AS owner_dob,
                        COALESCE(c.contact ,d.contact) AS owner_contact,
                        COALESCE(c.customer_id ,d.driver_id) AS owner_id,
                        CASE
                            WHEN c.email IS NOT NULL THEN 'Customer'
                            WHEN d.email IS NOT NULL THEN 'Driver'
                            ELSE 'Unknown'
                        END AS owner_type,
                        CASE
                            WHEN c.email IS NOT NULL THEN c.pass_word
                            WHEN d.email IS NOT NULL THEN d.pass_word
                            ELSE NULL
                        END AS owner_password
                        FROM (
                        SELECT email FROM Customer
                        UNION
                        SELECT email FROM driver
                        ) AS r
                        LEFT JOIN Customer c ON r.email = c.email
                        LEFT JOIN driver d ON r.email = d.email
                        WHERE r.email='{email}';
                        '''
        cursor.execute(string)
        user = cursor.fetchone()
        print(user)
        if user is not None:
            output = {'id': user[6], 'email': user[0], 'firstname': user[1], 'middlename': user[2],
                      'lastname': user[3],  'phone': user[5], 'type': user[7]}
            password_match = check_password(password, user[8])
            print(user[1])
            if password_match:
                print("matched")
                # setting logged in USER to global variable
                set_user_data(output)
                return redirect("http://127.0.0.1:8000")
            else:
                print("not matched")
                messages.error(request, 'Invalid login credentials')
        else:
            messages.error(request, 'User not found')

    return render(request, 'loginpage.html')


def booking(request):
    output = get_user_data()
    print('dsdgs')
    print(output)
    accept_decline = {}
    if request.method == 'POST':
        from_ = request.POST['location_from']
        to_ = request.POST['location_to']
        print(from_)
        print(to_)
        accept_decline = {'f': from_, 't': to_}
        print(accept_decline)
        return redirect("request/?from={}&to={}".format(from_, to_))
    return render(request, 'booking.html', {'output': output})


def Request(request):
    print('in request')
    from_ = request.GET.get('from')
    to_ = request.GET.get('to')
    output = get_user_data()
    print(output)
    # data = json.loads(request.body)
    # distance = data.get('distance')
    # new_locationlat = data.get('new_locationlat')
    # current_locationlat = data.get('current_locationlat')
    # new_locationlong = data.get('new_locationlong')
    # current_locationlong = data.get('current_locationlong')
    # trip_data = {"d": distance, 'nlat': new_locationlat, 'nlong': new_locationlong,
    #              'clat': current_locationlat, 'clong': current_locationlong}
    # print(trip_data)
    output2 = {'from': from_, 'to': to_, 'output': output}
    if(output):
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO trip(pickup_location , drop_location , ride_status) Values(%s , %s ,%s)", [from_, to_, "PENDING"])
            trip_id = cursor.lastrowid
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO requests(customer_id , trip_id) VALUES(%s , %s)", [output['id'], trip_id])
    if(request.method == "POST"):
        if 'cancel_request' in request.POST:
            cancel_request = request.POST['cancel_request']
            print(cancel_request)
            with connection.cursor() as cursor:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "DELETE FROM requests WHERE trip_id = %s ", [trip_id])
                with connection.cursor() as cursor:
                    cursor.execute(
                        "UPDATE trip SET ride_status = 'Cancelled' WHERE trip_id=%s", [trip_id])
            return redirect("http://127.0.0.1:8000/booking")

    # Emit custom signal
    # request_made.send(sender=request.user, request=request)
    return render(request, 'request.html',  {'output': output2})


def driver_requests(request):
    print('in driver requests')
    output = get_user_data()
    if(output):
        print(output)
        with connection.cursor() as cursor2:
            print("INquery")
            cursor2.execute(
                "SELECT * FROM requests r JOIN trip t ON r.trip_id=t.trip_id;")
            print("outquery")
            data = cursor2.fetchall()
        output2 = {'output': output, 'data': data}
        print(output2)
        if(request.method == "POST"):
            if 'accept' in request.POST:
                accept = request.POST['accept']
                print(accept)
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO accept_or_decline VALUES(%s, %s);", [output['id'], data[0][0]])
                return redirect("http://127.0.0.1:8000/request/dtracking")

            if 'decline' in request.POST:
                decline = request.POST['decline']
                print(decline)
                with connection.cursor() as cursor:
                    cursor.execute(
                        "DELETE FROM requests WHERE trip_id = %s ", [data[0][0]])
                with connection.cursor() as cursor:
                    cursor.execute(
                        "UPDATE trip SET ride_status = 'Cancelled' WHERE trip_id=%s", [data[0][0]])
                    return redirect("http://127.0.0.1:8000/drequests/")
        return render(request, 'drequest.html', {'output2': output2})


def driver_tracking(request):
    return render(request, 'dtracking.html')


def tracking(request):
    output = get_user_data()
    print('in tracking')
    data = request.GET.get('data')
    print(data)
    return render(request, 'tracking.html')


def payment(request):
    output = get_user_data()
    return render(request, 'payment.html')


def profile(request):
    output = get_user_data()
    print(output)
    if(request.method == "POST"):
        if 'update_user' in request.POST:
            return redirect("http://127.0.0.1:8000/updateprofile")
        elif('add_phone' in request.POST):
            return redirect("http://127.0.0.1:8000/addphone")
        else:
            if(output['type'] == 'Customer'):
                with connection.cursor() as cursor:
                    cursor.execute(
                        "delete from Customer where customer_id = %s ", [output['id']])
                return redirect("http://127.0.0.1:8000/goodbye")
            if(output['type'] == 'Driver'):
                with connection.cursor() as cursor:
                    cursor.execute(
                        "delete from driver where driver_id = %s ", [output['id']])
                return redirect("http://127.0.0.1:8000/goodbye")
    return render(request, 'profile.html', {'output': output})


def account_delete(request):
    set_user_data(None)
    return render(request, 'goodbye.html')


def updateprofile(request):
    output = get_user_data()
    if(request.method == "POST"):
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        phone = request.POST['phone']

        if 'update_profile' in request.POST:
            if(output['type'] == 'Customer'):
                with connection.cursor() as cursor:
                    cursor.execute(
                        '''
                        UPDATE Customer SET firstname=%s, lastname=%s, contact=%s WHERE customer_id=%s;
                        ''', [firstname, lastname, phone, output['id']]
                    )

                    cursor.execute(
                        "update customer_details set contact=%s where customer_id=%s;", [phone, output['id']])
                    output['firstname'] = firstname
                    output['lastname'] = lastname
                    output['phone'] = phone
                return redirect("http://127.0.0.1:8000/profile", {})
            elif(output['type'] == 'driver'):
                with connection.cursor() as cursor:
                    cursor.execute(
                        '''
                        UPDATE driver SET firstname='%s', lastname='%s', contact='%s' WHERE idriver_d=%s;

                        ''', [firstname, lastname, phone, output['id']]
                    )
                    cursor.execute(
                        "update driver_details set contact=%s where driver_id=%s;", [phone, output['id']])
                    output['firstname'] = firstname
                    output['lastname'] = lastname
                    output['phone'] = phone
                return redirect("http://127.0.0.1:8000/profile")
    return render(request, 'updateprofile.html')


def addphone(request):
    output = get_user_data()
    if(request.method == "POST"):
        phone = request.POST.get('add_phone')
        if(output['type'] == 'Customer'):
            print(output['id'])
            print(phone)
            with connection.cursor() as cursor:
                cursor.execute("insert into customer_details(customer_id , contact) values(%s , %s)", [
                               output['id'], phone])
                output['phone'] = phone
            return redirect("http://127.0.0.1:8000/profile")
        elif(output['type'] == 'driver'):
            with connection.cursor() as cursor:
                cursor.execute(
                    '''
                        INSERT INTO driver_details(contact , driver_id) VALUES(%s , %s);
                    ''', [phone, output['id']]
                )
                output['phone'] = phone
            return redirect("http://127.0.0.1:8000/profile")

    return render(request, 'addphone.html')


def passwordchange(request):
    if(request.method == "POST"):
        newpass = request.POST["password"]
        confirmpass = request.POST["cpassword"]
        email = request.POST["email"]
        print(email)
        print(newpass)
        print(confirmpass)
        with connection.cursor() as cursor:
            cursor.execute(
                '''
                SELECT 'driver' as user_type, pass_word FROM driver WHERE email = %s 
                UNION ALL 
                SELECT 'customer' as user_type, pass_word FROM customer WHERE email = %s;
                ''', [email, email]
            )
            data = cursor.fetchone()
        print(data)
        if(newpass != confirmpass):
            messages.error(request, 'Password Does not match..Try again')
        else:
            if(data[0] == 'customer'):
                newpass = make_password(confirmpass)
                with connection.cursor() as cursor:
                    cursor.execute(
                        "update Customer set pass_word = %s", [newpass])
                return redirect("http://127.0.0.1:8000/login")
            elif(data[0] == 'driver'):
                with connection.cursor() as cursor:
                    cursor.execute(
                        "update driver set pass_word = %s", [newpass])
                return render("http://127.0.0.1:8000/login")
    return render(request, 'passwordchange.html')


def Logout_view(request):
    set_user_data(None)  # clear user data
    print(user_data)
    return render(request, 'thankyou.html')


def aboutus(request):
    output = get_user_data()
    return render(request, 'about-us.html')


def contactus(request):
    output = get_user_data()
    return render(request, 'contact-us.html')


# def table(request):
#     with connection.cursor() as cursor:
#         try:

#             # First embedded query
#             cursor.execute("""
#                 SELECT r.email, COALESCE(a.firstname, c.firstname, d.firstname) AS owner_name,
#                 CASE
#                     WHEN a.email IS NOT NULL THEN 'Admin'
#                     WHEN c.email IS NOT NULL THEN 'Customer'
#                     WHEN d.email IS NOT NULL THEN 'Driver'
#                     ELSE 'Unknown'
#                 END AS owner_type,
#                 CASE
#                     WHEN c.email IS NOT NULL THEN c.customer_id
#                     WHEN d.email IS NOT NULL THEN d.driver_id
#                     WHEN a.email IS NOT NULL THEN a.admin_id
#                     ELSE NULL
#                 END AS owner_id
#                 FROM (
#                 SELECT email FROM Admins
#                 UNION
#                 SELECT email FROM Customer
#                 UNION
#                 SELECT email FROM driver
#                 ) AS r
#                 LEFT JOIN Admins a ON r.email = a.email
#                 LEFT JOIN Customer c ON r.email = c.email
#                 LEFT JOIN driver d ON r.email = d.email
#                 WHERE r.email = 'rbuse2r@privacy.gov.au';
#                 """)
#             result1 = cursor.fetchall()

#             # Second embedded query
#             cursor.execute("""
#                 SELECT d.firstname , r.stars
#                 FROM Driver d
#                 JOIN accept_or_decline t ON d.driver_id = t.driver_id
#                 JOIN rating r ON t.trip_id = r.trip_id
#                 WHERE r.stars > 3;
#                 """)
#             result2 = cursor.fetchall()
#             table = {'result1': result1, 'result2': result2}

#         except Exception as e:
#             print(e)

#     return render(request, 'tables.html', table)

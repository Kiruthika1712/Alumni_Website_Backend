from django.shortcuts import render
from django.utils import timezone
from rest_framework.decorators import api_view
from .serializers import mailverSerializer
from .models import mailVerification 
from rest_framework.response import Response
from django.core.mail import send_mail
from rest_framework import status
# Create your views here.

@api_view(['POST'])
def email_verification(request):
    # cget email from user and send otp
    mail = request.data.get('email')
    serializer = mailverSerializer(data= request.data)
    try:
        if serializer.is_valid():
            mailVerification.objects.create(email=mail,otp_expires_at=timezone.now()+timezone.timedelta(minutes=5))
            
            user =  mailVerification.objects.filter(email=mail).last()
            

            subject ="Email verification"
            message = f"""
                            Hi, here is your OTP is {user.otp}. It expires in 5 minutes.
                            Use the link below to redirect to the website
                            http://127.0.0.1:8000/verify-email/{user.email}
                    """
            sender= "aanishaalmaaz03@gmail.com"
            receiver = [user.email,]


            send_mail(
                    subject,
                    message,
                    sender,
                    receiver,
                    fail_silently=False
            )

            return Response({"message":"mail sent"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message":"not valid"},serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        mailVerification.objects.filter(email=mail).delete()
        print("--------------errorrr",e)
        return Response({"message":"server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

# verifying the otp 
@api_view(['POST'])
def verify_otp(request,email):  
    
    try:
        user_check = mailVerification.objects.filter(email=email).exists()
        if user_check:
            user = mailVerification.objects.filter(email=email).last()
            

            # if otp is true
            if user.otp == request.data.get('otp'):

                # check for otp expiration
                if user.otp_expires_at > timezone.now():
                    user.is_verified= True
                    user.save() #use this to update an existing instance
                    return Response({"message":"Email verification successfull"}, 
                                    status=status.HTTP_200_OK)

                else:
                    return Response({"message":"OTP expired"},
                                    status=status.HTTP_205_RESET_CONTENT)
                    # though the otp is valid it expired hence reset the content and provide a resend otp link
            else:
                return Response({"message":"Incorrect otp"},
                                status=status.HTTP_403_FORBIDDEN)
                # 403 is used to indicate that the user should not be allowed to proceed further
            
        else:
            return Response({"message":"Email not in DB"}, 
                            status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['POST'])
def resend_otp(request):
    try:
        user_mail= request.data.get('email')
        
        if mailVerification.objects.filter(email=user_mail).exists():
            mailVerification.objects.filter(email=user_mail).delete()
            mailVerification.objects.create(email=user_mail,otp_expires_at=timezone.now()+timezone.timedelta(minutes=5))
            
            user =  mailVerification.objects.filter(email=user_mail).last()
                

            subject ="Email verification"
            message = f"""
                            Hi, here is your OTP is {user.otp}. It expires in 5 minutes.
                            Use the link below to redirect to the website
                            http://127.0.0.1:8000/otpv/{user.email}
                    """
            sender= "aanishaalmaaz03@gmail.com"
            receiver = [user.email,]


            send_mail(
                    subject,
                    message,
                    sender,
                    receiver,
                    fail_silently=False
            )

        else:
            return Response({"message":"Incorrect email"},status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
from django.shortcuts import render
def division(request):
    division = ["Dhaka","Rajshahi","Barisal","Khulna"]
    return render(request,"division.html",{"division_list":division})
def Dhaka(request):
    Dhaka = ['Gazipur','Manikganj','Mymensingh']
    return render(request,"Dhaka.html",{"Dhaka_list":Dhaka})
def Rajshahi(request):
    Rajshahi = ['Bogra','Pabna','Joypurhat']
    return render(request,"Rajshahi.html",{"Rajshahi_list":Rajshahi})
def Khulna(request):
    Khulna = ['Magura','Jessore','Bagerhat']
    return render(request,"Khulna.html",{"Khulna_list":Khulna})
def Barisal(request):
    Barisal = ['Bhola','Jhalakati','Ptuakhali']
    return render(request,"Barisal.html",{"Barisal_list":Barisal})

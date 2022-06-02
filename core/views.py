from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request,nome,idade):
    return HttpResponse('<h1>Hello {} de {} anos</h1>'.format(nome, idade))
def soma(request,num1,num2):
    soma=num1+num2
    return HttpResponse('A soma do número {} com o número {} é {}:'.format(num1,num2,soma))
def multiplicacao(request,num1,num2):
    multiplicacao=num1*num2
    return HttpResponse('A multiplicacao do numero {} com o numero {} é {}'.format(num1,num2,multiplicacao))
def div(request,num1,num2):
    div=num1/num2
    return HttpResponse('A divisao do numero {} com o numero {} é: {}'.format(num1,num2,div))
def sub(request,num1,num2):
    sub=num1-num2
    return  HttpResponse('A subtração do numero {} com o numero {} é: {}'.format(num1,num2,sub))
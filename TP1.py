import turtle
import random

turtle.speed(10)

#blue = (0, 129, 200)
#black = (0, 0, 0)
#red = (238, 51, 78)
#yellow = (252, 177, 49)
#green = (0, 166, 81)

#Arah kursor
#Biar gampang mau belok ke mana
#Positif x = 0
#Positif y = 270
direction = 0
#Jari jari lingkaran
radius = 50

#Definisikan warna
#Data warna di line 4--8 dibagi dengan rgb max(255)
#Dikonversi karena python range-nya cuma dari 0 sampai 1 inklusif
blue = 0, 129/255, 200/255
black = 0,0,0
red = 238/255, 51/255, 78/255
yellow = 252/255, 177/255, 49/255
green = 0, 166/255, 81/255

#Biar simetris
#-120 random, tetapi harus negatif agar simetris
#150 juga random, tetapi agak tinggi agar board di akhir tetap terlihat di layar

turtle.penup()
turtle.goto(-120, 150)
turtle.pendown()

#lingkaran pertama, paling kiri
turtle.pencolor(random.random(), random.random(), random.random())
turtle.pensize(5)
turtle.circle(50)

#Pindah ke lingkaran tengah
turtle.penup()
turtle.goto(0, 150)
turtle.pendown()

#Menggambar lingkaran tengah
turtle.color(random.random(), random.random(), random.random())
turtle.circle(radius)

#Pindah ke lingkaran ketiga
turtle.penup()
turtle.goto(120, 150)
turtle.pendown()

#Menggambar lingkaran kanan
turtle.color(random.random(), random.random(), random.random())
turtle.circle(radius)

#Pindah ke lingkaran keempat
#-60 dan 110 adalah kordinat random tetapi harus sesuai(y lebih kecil daripada y lingkaran sebelumnya)

turtle.penup()
turtle.goto(-60, 110)
turtle.pendown()

#Menggambar lingkaran keempat
turtle.color(random.random(), random.random(), random.random())
turtle.circle(radius)

#Pindah ke lingkaran kelima
turtle.penup()
turtle.goto(60, 110)
turtle.pendown()

#Menggambar lingkaran kelima
turtle.color(random.random(), random.random(), random.random())
turtle.circle(radius)

#Melakukan overlap

#Dimulai dari cincin pertama
turtle.penup()

#Pada awalnya, turtle mengarah ke sumbu positif x (0, sesuai perjanjian awal di line 13)
#Dalam membuat lingkaran, turtle bergerak ke arah kiri
#turtle harus menghadap sumbu y positif agar sesuai dengan lingkaran
#turtle.speed(5)
turtle.left(90)
#-70 didapat dari kordinat titik paling bawah lingkaran 1 (-120) ditambah(+) radius lingkaran [-120+50 = -70]
#200 didapat dari titik paling bawah lingkaran (150) ditambah radius [150+50 = 200]
turtle.goto(-70,200)
turtle.pendown()
turtle.color(blue)
#Menggambar lingkaran cukup hingga 90 derajat
turtle.circle(radius, 90)

#Arah akhir turtle
direction = 180

#Menggunakan prinsip seperti sebelumnya
#melakukan overlap di kiri bawah lingkaran kedua
turtle.penup()
#-50 didapat dari kordinat titik paling bawah lingkaran 2 (0) dikurang radius
#200 didapat dari kordinat titik paling bawah lingkaran 2 (150) ditambah radius
turtle.goto(-50,200)
turtle.pendown()
turtle.color(black)
#Agar sesuai dengan lingkaran
turtle.left(90)
#Cukup digambar hingga 90 derajat
turtle.circle(radius,90)
direction = 0


#Melakukan overlap di kanan atas lingkaran kedua

turtle.penup()

#50 didapat dari kordinat titik paling bawah lingkaran 2 (0) ditambah radius
#200 didapat dari kordinat titik paling bawah lingkaran 2 (150) ditambah radius
turtle.goto(50, 200)
turtle.pendown()
#Agar sesuai dengan lingkaran
turtle.left(90)
turtle.color(black)
turtle.circle(radius, 90)
direction = 180

turtle.penup()

#Melakukan overlap di lingkaran ketiga

#120 didapat dari kordinat titik paling bawah lingkaran 3
#250 didapat dari kordinat titik paling bawah lingkaran 3 (200) ditambah radius
turtle.goto(120, 250)
turtle.pendown()

#Arah sudah sesuai
turtle.color(red)
#Turtle bergerak mundur, ditandai dengan simbol (-)
turtle.circle(radius, -225)
#arah akhir turtle
direction = 135

turtle.penup()

#Agar simetris
#jarak antar dua titik pusat = 2r-x; x = panjang antar jari jari yang overlap
#4(2r-x) = 240; 240 diambil dari jarak antarkordinat x lingkaran paling kiri dan lingkaran paling kanan
#x = 40
#2r-x = 2(50) - 40 = 60; <-- Jarak sumbu-x antar dua titik pusat lingkaran 
turtle.left(45)
direction = 0

#Menggambar rangkaian lingkaran kedua
turtle.goto(-120, -50)
turtle.pendown()
turtle.color(blue)
turtle.circle(radius)
turtle.penup()

turtle.goto(-120+60, -50)
turtle.pendown()
turtle.color(yellow)
turtle.circle(radius)
turtle.penup()

turtle.goto(-120+60*2, -50)
turtle.pendown()
turtle.color(black)
turtle.circle(radius)
turtle.penup()

turtle.goto(-120+60*3, -50)
turtle.pendown()
turtle.color(green)
turtle.circle(radius)
turtle.penup()

turtle.goto(-120+60*4, -50)
turtle.pendown()
turtle.color(red)
turtle.circle(radius)
turtle.penup()

turtle.speed(5)

#Melakukan overlap
#Kordinat titik bawah lingkaran paling kiri = (-120, -50)
#Kordinat titik paling kanan di lingkaran paling kiri (-120 + r, -50 + r)
#Kordinat titik paling kanan di lingkaran paling kiri (-70, 0)

turtle.left(90)
direction = 270

turtle.color(blue)
turtle.goto(-70, 0)
turtle.pendown()
turtle.circle(radius, 90)
turtle.penup()

turtle.color(yellow)
turtle.goto(-70+60-radius, 0+radius)
turtle.pendown()
turtle.circle(radius, -90)
turtle.penup()

turtle.color(black)
turtle.goto(-70+60*2, 0)
turtle.pendown()
turtle.circle(radius, 90)
turtle.penup()

turtle.color(green)
turtle.goto(-70+60*3-radius, 0+radius)
turtle.pendown()
turtle.circle(radius, -90)
turtle.penup()

direction = 270

turtle.right(90)

#--------------------------
#Checkboard

#Minval dan maxval diatur sesuai ketentuan pada soal
rows = int(turtle.numinput("","Enter the Number of Rows: ", minval=2, maxval=25))
size = turtle.numinput("", "Enter the Size of A Square: ", minval = 5, maxval = 50)
lebar = int(turtle.numinput("", "Masukkan lebarnya: "))

#Agar simetris
#-80 kordinat random
turtle.goto(-(size*rows)/2, -80)

turtle.pendown()


#shapesize mengali besar square daripada besar square semula
for i in range (rows):
    for j in range (rows):
        turtle.color(random.random(), random.random(), random.random())
        turtle.shape("square")
        turtle.shapesize(size / 20, lebar / 20)#20 adalah size default square
        turtle.stamp()
        turtle.penup()
        turtle.forward(lebar)
        turtle.pendown()
    turtle.penup()
    turtle.goto(-(size*rows)/2, -(size+i*size)-80)
    turtle.pendown()
    
turtle.hideturtle()



turtle.exitonclick()




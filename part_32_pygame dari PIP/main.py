import pygame


# 1.init , untuk menjalankan game enginenya
pygame.init()
isRun = True # DUMMY VARIABLE

# membuat display surface object (gui), harus menggunakan sintaks pygame.display.update() agar asset" terdisplay, jika tidak akan hanya muncul kotak gui hitam kosong 
window_lebar = 500
window_panjang = 500
window = pygame.display.set_mode((window_lebar,window_panjang))

# membuat object game
x = 250 # letak objek relatif dengan pixel di window
y = 250 # letak objek relatif dengan pixel di window

# ukuran
panjang = 20
lebar = 20

# kecepatan gerak
speed = 0.1

while isRun:
    # pygame.time.delay(10)

    # USER INPUT, DATABASE INPUT (input berupa pencetan dari keyboard,stick,mouse dll)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False

    # mengambil semua keyboard action/pencetan
    keys = pygame.key.get_pressed()

    # press left
    if keys[pygame.K_LEFT] and x > 0:
        x -= speed # bacanya, syarat untuk bisa kekiri adalah jika x > 0, jika x kurang dari 0 maka akan false (stop gerak)

    # press right
    if keys[pygame.K_RIGHT] and x < window_lebar-lebar:
        x += speed # bacanya, syarat untuk bisa ke kanan adalah jika x kurang dari 480, jika x lebih dari 480 makan akan false (stop gerak)

    # press up
    if keys[pygame.K_UP] and y > 0:
        y -= speed # bacanya, syarat untuk bisa ke atas adalah jika y > 0 , jika y kurang dari 0 makan akan false (stop gerak)

    # press down
    if keys[pygame.K_DOWN] and y < window_panjang-panjang:
        y += speed # bacanya, syarat untuk bisa ke bawah adalah jika y < 480 , jika y lebih dari 480 makan akan false (stop gerak)
    


    # update asset
    window.fill((255,255,255)) # background windownya akan berwarna putih
    pygame.draw.rect(window,(200,240,35),(x,y,lebar,panjang))
    # render ke display, jika tidak begini maka akan hanya muncul kotak gui hitam kosong 
    pygame.display.update()

pygame.quit() # quit pygame







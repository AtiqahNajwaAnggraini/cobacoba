jawab="ya"
while(jawab=="ya"):
      print()
      print("""Silahkan pilih item yang akan dihitung ?
      1. Konversi Kurs Dolar ke Rupiah
      2. Volume Balok
      3. Volume Prisma""")
      pilih=input("Silahkan masukkan item yang akan dihitung (1-3) : ")
      if(pilih=="1"):
            print()
            print("Pilihan anda Konversi Kurs Dolar ke Rupiah")
            print()
            print("Menghitung Konversi Kurs Dolar ke Rupiah")
            print()
            d = input("Masukkan nilai panjang kurs Dollar =")
            j = input("Masukkan nilai jumlah dollar =")
            di=int(d)
            ji=int(j)
            Konversi = (di*ji)
            print()
            print("===========================================================================================================")
            print("Konversi dolar ke rupiah dengan nilai panjang kurs Dollar = " +d+ " dan nilai jumlah dollar = " +j+ " adalah sebesar "+str(Konversi)+".-")
            print("===========================================================================================================")
      elif(pilih=="2"):
            print()
            print("Pilihan anda Volume Balok")
            print()
            print("Menghitung Volume Balok")
            print("Silahkan Masukkan Ukuran Balok")
            print()
            p = input("Masukkan Panjang =")
            l = input("Masukkan Lebar =")
            t = input("Masukkan Tinggi =")
            pi=int(p)
            li=int(l)
            ti=int(t)
            Volume = (pi*li*ti)
            print()
            print("====================================================================================================")
            print("Perhitungan volume balok dengan panjang = "+p+" dan lebar balok = "+l+" serta tinggi balok = "+t+" adalah sebesar "+str(Volume)+" m3 ")
            print("====================================================================================================")
      elif(pilih=="3"):
            print()
            print("Pilihan anda Volume Prisma")
            print()
            print("Menghitung Volume Prisma")
            print("Silahkan Masukkan Ukuran Prisma")
            print()
            a = input("Masukkan alas segitiga =")
            t = input("Masukkan tinggi segitiga =")
            s = input("Masukkan tinggi prisma =")
            ai=int(a)
            ti=int(t)
            si=int(s)
            Volume = (1/2*ai*ti*si)
            print()
            print("===========================================================================================================")
            print("Perhitungan volume prisma segitiga dengan alas segitiga = "+a+" dan tinggi segitiga = "+t+" serta tinggi prisma = "+s+" adalah sebesar "+str(Volume)+" m3 ")
            print("===========================================================================================================")
      else:
            print("Pilihan anda salah")
      jawab=input("Apakah anda ingin mengulang dan menghitung item yang lain? [ya/tidak]")


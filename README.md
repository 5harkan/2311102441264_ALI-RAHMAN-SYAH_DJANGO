
# Personal Portfolio
<div align="center">
  <img height="150" src="https://media.giphy.com/media/M9gbBd9nbDrOTu1Mqx/giphy.gif"  />
</div>

[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff)](#)
[![Django](https://img.shields.io/badge/Django-%23092E20.svg?logo=django&logoColor=white)](#)

<h3 align="left">👩‍💻  About Me</h3>
<p align="left">I'm Ali Rahman Syah from Universitas Muhammadiyah Kalimantan Timur. This This git will continue to grow as the 4th semester lectures go on<br><br>
- 🔭 I am currently working on an advanced web programming course project<br>
- 📚 I'm currently learning to develop a website with Django Framework<br>

## Cara clone repo

1. Salin projek

```shell
git clone https://github.com/5harkan/2311102441264_ALI-RAHMAN-SYAH_DJANGO.git
```

2. Buat virtual environment

```shell
# Universal Python
python -m venv .venv
```

ada beberapa kasus commad tidak berfungsi, gunakan command dibawah

```shell
# Python 3 Specified
python3 -m venv .venv
```

3. Activate .venv

```shell
# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

4. Install dependency

```shell
pip install django
pip install mysqlclient
pip install pillow
```

## Update MariaDB pada XAMPP

Update mariadb XAMMP kalian ke versi terbaru, berikut cara update-nya:

1. Download MaridDB di https://mariadb.org/download/?t=mariadb&o=true&p=mariadb&r=11.7.2&os=windows&cpu=x86_64&pkg=zip&mirror=citrahost, pastikan file download berekstensi ```.zip```

2. Ekstrak file, kemudian masuk kedalam folder dan ubah nama folder didalamnya menjadi ```mysql```

3. Copy folder ```mysql``` ke dalam folder instalasi XAMMP, sebelum kalian copy ubah nama folder ```mysql``` bawaan menjadi ```mysql_old``` dan copy ```mysql``` yang baru kedalam path xammp

4. Copy file dibawah ini dari folder ```mysql_old``` ke ```mysql```
```commandline
mysql_uninstallservice
mysql_installservice
data
scripts
```
kemudian copy juga file ```my.ini``` yang terdapat pada folder ```"mysql_old\bin"``` ke dalam ```mysql\bin```

5. Setelah itu kita masuk ke ```mysql\data``` hapus semua file dan folder didalamnya, dan copy kembali 4 folder yang berada di ```mysql\backup``` kedalam ```mysql\data```. Berikut nama folder yang di copy:
```commandline
mysql
performance_schema
phpmyadmin
test
```
Setelah melakukan step by step diatas selanjutnya kita buka Xammp dan aktifkan Apache serta Mysql.
itu tadi cara update MariaDB.
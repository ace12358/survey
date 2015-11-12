#/usr/bin/sh

for i in 03 06 09 12 14
do
wget -O htmls/EACL20$i.html https://aclweb.org/anthology/E/E$i/
done

for i in 83 85 87 89 91 93 95 97 99
do
wget -O htmls/EACL19$i.html https://aclweb.org/anthology/E/E$i/
done


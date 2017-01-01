#bash!
while true; do
	clear
	echo
	echo "*** LINUX AX84 INSTALL ****"
	echo
	lsblk -l | grep -E "sd[a-z]+\s"
	echo
	echo "Selezionare un dispositivo hard disk, esempio : sda, sdb, etc ..."
	echo
	read -p "Digitare dispositivo hard disk ? " device
	echo
	lsblk -l /dev/${device}	
	if [ $? == 0 ]; then
		break
	else
		echo
	fi
done

echo
echo "Attenzione tutti i dati presenti nell'unita' [ $device ]"
read -p "verranno eliminati, procedere (si/no) ? " cdevice

if [ $cdevice == "si" ]; then

umount /dev/${device}1
dd if=/dev/zero of=/dev/${device} bs=4096 count=100000

fdisk /dev/${device} <<EOF
n
p
1


w
EOF

mkfs.ext4 /dev/${device}1
mount /dev/${device}1 /mnt

cat > /mnt/packages.sh <<AEOF
pacman -S xorg --noconfirm
pacman -S xfce4 --noconfirm
pacman -S xfce4-taskmanager --noconfirm
pacman -S firefox --noconfirm
pacman -S firefox-i18n-it --noconfirm
pacman -S flashplugin --noconfirm
pacman -S libreoffice --noconfirm
pacman -S libreoffice-fresh-it --noconfirm
pacman -S gimp --noconfirm
pacman -S geany --noconfirm
pacman -S gvfs --noconfirm
pacman -S wget --noconfirm
pacman -S linux-headers base-devel --noconfirm
pacman -S gnome-packagekit --noconfirm
pacman -S xarchiver --noconfirm
pacman -S zip --noconfirm
pacman -S unzip --noconfirm
pacman -S grub --noconfirm
grub-install /dev/${device} --force
grub-mkconfig /dev/${device} -o /boot/grub/grub.cfg
systemctl enable dhcpcd
wget www.massimo7000.altervista.org/setup.zip.tar
mv /setup.zip.tar /root/setup.zip.tar
cd /root
tar xvf setup.zip.tar
rm /root/setup.zip.tar
cd /
wget www.massimo7000.altervista.org/Awesome-Arch-Linux-Wallpaper.jpg
mv /Awesome-Arch-Linux-Wallpaper.jpg /usr/share/backgrounds/xfce/Awesome-Arch-Linux-Wallpaper.jpg
rm /Awesome-Arch-Linux-Wallpaper.jpg
cat > /etc/locale.conf <<CEOF
LANG="it_IT.UTF-8"
LC_COLLATE="C"
LC_TIME="it_IT.UTF-8"
CEOF
cat > /etc/locale.gen <<DEOF
it_IT.UTF-8 UTF-8
DEOF
locale-gen
cat > /root/.profile <<BEOF
loadkeys it
startxfce4
BEOF
AEOF

pacstrap /mnt
chmod 777 /mnt/packages.sh
arch-chroot /mnt ./packages.sh

echo
echo "Installazione terminata riavviare il computer e selezionare"
echo "nel bios l'hard disk come dispositivo di boot principale"
echo

exit

fi

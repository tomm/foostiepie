#!/usr/bin/env python
import time, random; D=64; _=[random.randint(0,1) for i in range(0,D*D)]
while time.sleep(0.2) or True:
    print chr(0xa).join(map(''.join, zip(*[iter([chr(32+3*j) for j in _])]*D)))
    p=lambda p:_[(p[0]%D)+D*(p[1]%D)];n=lambda x,y:reduce(lambda x,y:x+y,map(p,
    [(x+i%3-1,y+i/3-1)for i in range(0,9) if i!=4]));_=[int(((p((j%D,j/D))|n(j%
    D,j/D))==3)or(~p((j%D,j/D))and n(j%D,j/D)==3))for j in range(0,D*D)]

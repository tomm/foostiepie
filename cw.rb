D=32;d=(0...D*D);b=d.map{rand 2};p=->y,x{b[x%D+y%D*D]}
n=->y,x{[*0..3,*5..8].map{|i|p[y+i/3-1,x+i%3-1]}.reduce :+}
loop{sleep 1;puts"\033[2J";b.map{|c|(32+3*c).chr}.each_slice(D){|p|p p.join}
b=d.map{|j|m=j/D,j%D;p[*m]|n[*m]==3||~p[*m]&&n[*m]==3?1:0}}

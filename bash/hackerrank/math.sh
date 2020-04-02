# Given two integers, x and y, find their sum, difference, product, and quotient.
read X
read Y
s=`expr $X + $Y`
m=`expr $X - $Y`
mul=`expr $X \* $Y`
d=`expr $X / $Y`
echo $s
echo $m
echo $mul
echo $d
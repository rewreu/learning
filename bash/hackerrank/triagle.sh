read x
read y
read z

if [ $x -eq $y ] || [ $x -eq $z ] || [ $z -eq $y ]
then
    if [ $x -eq $y ] && [ $x -eq $z ]
    then
    echo "EQUILATERAL"
    else
    echo "ISOSCELES"
    fi
else
echo "SCALENE"
fi
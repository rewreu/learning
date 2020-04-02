read X
read Y
if [ $X -gt $Y ] 
then
echo "X is greater than Y"
else
    if [ $X -lt $Y ] 
    then
    echo "X is less than Y"
    else
        if [ $X -eq $Y ] 
        then
        echo "X is equal to Y"
        fi
    fi
fi
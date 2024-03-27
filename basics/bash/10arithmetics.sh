
echo 31+21	# not adding

n1=4
n2=20
echo $(( n1 + n2 ))
echo $(( n1 - n2 ))
echo $(( n1 * n2 ))
echo $(( n1 / n2 ))
echo $(( n1 % n2 ))
echo $( expr $n1 + $n2 )	# same as first




echo "Enter Hex number"
read Hex
echo -n "Decimal of $Hex is: "
echo "obase=10; ibase=16; $Hex" | bc

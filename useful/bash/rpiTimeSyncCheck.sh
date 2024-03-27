ue0="192.168.2.2"
ue1="192.168.2.6"
ue2="192.168.2.10"
ue3="192.168.2.14"
ue4="10.0.14.27"

echo "NO CORRECTION"


ue01_diff=$(echo $(ssh -l lad ${ue0} "( date +%s%3N )") "-" $(ssh -l lad ${ue1} "( date +%s%3N )") | bc)
ue10_diff=$(echo $(ssh -l lad ${ue1} "( date +%s%3N )") "-" $(ssh -l lad ${ue0} "( date +%s%3N )") | bc)
tot01=$(echo $ue01_diff "-" $ue10_diff | bc)
echo "ue0 -> ue1: " $ue01_diff
echo "ue1 -> ue0: " $ue10_diff
echo "difference: " $tot01
echo

#ue02_diff=$(echo $(ssh -l lad ${ue0} "( date +%s%3N )") "-" $(ssh -l lad ${ue2} "( date +%s%3N )") | bc)
#ue03_diff=$(echo $(ssh -l lad ${ue0} "( date +%s%3N )") "-" $(ssh -l lad ${ue3} "( date +%s%3N )") | bc)

#ue34_diff=$(echo $(ssh -l lad ${ue3} "( date +%s%3N )") "-" $(ssh -l root ${ue4} "( date +%s%3N )") | bc)
#ue43_diff=$(echo $(ssh -l root ${ue4} "( date +%s%3N )") "-" $(ssh -l lad ${ue3} "( date +%s%3N )") | bc)
#tot34=$(echo $ue34_diff "-" $ue43_diff | bc)

#echo $ue01_diff
#echo $ue02_diff
#echo $ue03_diff

echo "\nWITH CORRECTION"
ue00_diff=$(echo $(ssh -l lad ${ue0} "( date +%s%3N )") "-" $(ssh -l lad ${ue0} "( date +%s%3N )") | bc)
echo "ssh delay: " $ue00_diff

ue00_diff=$(echo $(ssh -l lad ${ue0} "( date +%s%3N )") "-" $(ssh -l lad ${ue0} "( date +%s%3N )") | bc)
ue10_diff=$(echo $(ssh -l lad ${ue1} "( date +%s%3N )") "-" $(ssh -l lad ${ue0} "( date +%s%3N )") | bc)
tot10correct=$(echo $ue10_diff "-" $ue00_diff | bc)
echo "ue1 -> ue0 " $tot10correct

#echo $ue34_diff
#echo $ue43_diff
#echo $tot34


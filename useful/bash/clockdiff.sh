ue0=192.168.2.2
ue1=192.168.2.6
ue2=192.168.2.10
ue3=192.168.2.14
ue4=10.0.14.27

ue01_diff=$(echo $(ssh -l lad ${ue0} "(sudo clockdiff -o $ue1)" ))
echo $ue01_diff




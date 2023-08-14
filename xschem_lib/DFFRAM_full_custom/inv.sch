v {xschem version=3.0.0 file_version=1.2 }
G {}
K {}
V {}
S {}
E {}
N 1040 -1600 1100 -1600 {
lab=X}
N 1100 -1650 1100 -1590 {
lab=X}
N 1100 -1590 1100 -1540 {
lab=X}
N 1140 -1620 1140 -1570 {
lab=Y}
N 1140 -1600 1220 -1600 {
lab=Y}
N 1140 -1720 1140 -1680 {
lab=VDD}
N 1140 -1510 1140 -1440 {
lab=VSS}
N 1140 -1650 1170 -1650 {
lab=VDD}
N 1170 -1700 1170 -1650 {
lab=VDD}
N 1140 -1700 1170 -1700 {
lab=VDD}
N 1140 -1540 1180 -1540 {
lab=VSS}
N 1180 -1540 1180 -1480 {
lab=VSS}
N 1140 -1480 1180 -1480 {
lab=VSS}
C {symbols/nfet_03v3.sym} 1120 -1540 0 0 {name=M1
L=0.28u
W=NF*0.85u
nf=NF
m=1
ad="'int((nf+1)/2) * W/nf * 0.18u'"
pd="'2*int((nf+1)/2) * (W/nf + 0.18u)'"
as="'int((nf+2)/2) * W/nf * 0.18u'"
ps="'2*int((nf+2)/2) * (W/nf + 0.18u)'"
nrd="'0.18u / W'" nrs="'0.18u / W'"
sa=0 sb=0 sd=0
model=nfet_03v3
spiceprefix=X
}
C {symbols/pfet_03v3.sym} 1120 -1650 0 0 {name=M2
L=0.28u
W=NF*1.7u
nf=NF
m=1
ad="'int((nf+1)/2) * W/nf * 0.18u'"
pd="'2*int((nf+1)/2) * (W/nf + 0.18u)'"
as="'int((nf+2)/2) * W/nf * 0.18u'"
ps="'2*int((nf+2)/2) * (W/nf + 0.18u)'"
nrd="'0.18u / W'" nrs="'0.18u / W'"
sa=0 sb=0 sd=0
model=pfet_03v3
spiceprefix=X
}
C {iopin.sym} 1140 -1450 1 0 {name=p2 lab=VSS}
C {ipin.sym} 1050 -1600 0 0 {name=p3 lab=X}
C {opin.sym} 1210 -1600 0 0 {name=p4 lab=Y}
C {iopin.sym} 1140 -1710 3 0 {name=p1 lab=VDD}

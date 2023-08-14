v {xschem version=3.0.0 file_version=1.2 }
G {}
K {}
V {}
S {}
E {}
N 1030 -1680 1030 -1500 {
lab=X}
N 1030 -1680 1130 -1680 {
lab=X}
N 1030 -1500 1030 -1330 {
lab=X}
N 1030 -1330 1130 -1330 {
lab=X}
N 1090 -1450 1130 -1450 {
lab=EN}
N 1090 -1570 1130 -1570 {
lab=ENB}
N 1170 -1540 1170 -1480 {
lab=Y}
N 1170 -1420 1170 -1360 {
lab=#net1}
N 1170 -1650 1170 -1600 {
lab=#net2}
N 1170 -1500 1210 -1500 {
lab=Y}
N 1170 -1760 1170 -1710 {
lab=VDD}
N 1170 -1680 1200 -1680 {
lab=VDD}
N 1200 -1730 1200 -1680 {
lab=VDD}
N 1170 -1730 1200 -1730 {
lab=VDD}
N 1170 -1570 1200 -1570 {
lab=VDD}
N 1200 -1680 1200 -1570 {
lab=VDD}
N 1170 -1300 1170 -1240 {
lab=VSS}
N 1170 -1330 1210 -1330 {
lab=VSS}
N 1210 -1330 1210 -1270 {
lab=VSS}
N 1170 -1270 1210 -1270 {
lab=VSS}
N 1170 -1450 1210 -1450 {
lab=VSS}
N 1210 -1450 1210 -1330 {
lab=VSS}
N 1020 -1500 1030 -1500 {
lab=X}
N 990 -1500 1020 -1500 {
lab=X}
C {ipin.sym} 1000 -1500 0 0 {name=p1 lab=X}
C {ipin.sym} 1100 -1570 0 0 {name=p2 lab=ENB}
C {ipin.sym} 1100 -1450 0 0 {name=p3 lab=EN}
C {opin.sym} 1200 -1500 0 0 {name=p4 lab=Y}
C {iopin.sym} 1170 -1750 3 0 {name=p5 lab=VDD}
C {iopin.sym} 1170 -1250 1 0 {name=p6 lab=VSS}
C {symbols/pfet_03v3.sym} 1150 -1680 0 0 {name=M1
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
C {symbols/pfet_03v3.sym} 1150 -1570 0 0 {name=M2
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
C {symbols/nfet_03v3.sym} 1150 -1450 0 0 {name=M3
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
C {symbols/nfet_03v3.sym} 1150 -1330 0 0 {name=M4
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

v {xschem version=3.0.0 file_version=1.2 }
G {}
K {}
V {}
S {}
E {}
N 130 -310 170 -310 {
lab=X}
N 170 -310 170 -250 {
lab=X}
N 130 -250 130 -190 {
lab=Y}
N 130 -190 170 -190 {
lab=Y}
N 70 -280 90 -280 {
lab=A_bar}
N 210 -220 230 -220 {
lab=A}
N 40 -220 170 -220 {
lab=VSS}
N 130 -280 240 -280 {
lab=VDD}
N 150 -320 150 -310 {
lab=X}
N 150 -190 150 -170 {
lab=Y}
C {symbols/nfet_03v3.sym} 190 -220 0 1 {name=M1
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
C {symbols/pfet_03v3.sym} 110 -280 0 0 {name=M2
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
C {iopin.sym} 40 -220 2 0 {name=p2 lab=VSS}
C {ipin.sym} 70 -280 0 0 {name=p3 lab=A_bar}
C {iopin.sym} 240 -280 0 0 {name=p1 lab=VDD}
C {ipin.sym} 230 -220 0 1 {name=p5 lab=A}
C {iopin.sym} 150 -320 3 0 {name=p4 lab=X}
C {iopin.sym} 150 -170 1 0 {name=p6 lab=Y}

v {xschem version=3.0.0 file_version=1.2 }
G {}
K {}
V {}
S {}
E {}
N 280 -420 280 -380 {
lab=VDD}
N 280 -320 280 -270 {
lab=#net1}
N 280 -210 280 -150 {
lab=Y}
N 120 -150 280 -150 {
lab=Y}
N 280 -90 280 -50 {
lab=VSS}
N 120 -90 280 -90 {
lab=VSS}
N 120 -120 170 -120 {
lab=VSS}
N 170 -120 170 -90 {
lab=VSS}
N 280 -120 330 -120 {
lab=VSS}
N 330 -120 330 -70 {
lab=VSS}
N 280 -70 330 -70 {
lab=VSS}
N 280 -180 350 -180 {
lab=Y}
N 240 -240 240 -120 {
lab=A}
N 80 -350 80 -120 {
lab=B}
N 80 -350 240 -350 {
lab=B}
N 0 -180 240 -180 {
lab=A}
N 0 -250 80 -250 {
lab=B}
N 280 -350 310 -350 {
lab=VDD}
N 310 -400 310 -350 {
lab=VDD}
N 280 -400 310 -400 {
lab=VDD}
N 280 -240 310 -240 {
lab=VDD}
N 310 -350 310 -240 {
lab=VDD}
C {iopin.sym} 280 -410 3 0 {name=p1 lab=VDD}
C {iopin.sym} 280 -60 1 0 {name=p2 lab=VSS}
C {opin.sym} 350 -180 0 0 {name=p3 lab=Y}
C {ipin.sym} 0 -180 0 0 {name=p4 lab=A}
C {ipin.sym} 0 -250 0 0 {name=p5 lab=B}
C {symbols/pfet_03v3.sym} 260 -350 0 0 {name=M3
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
C {symbols/pfet_03v3.sym} 260 -240 0 0 {name=M4
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
C {symbols/nfet_03v3.sym} 100 -120 0 0 {name=M1
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
C {symbols/nfet_03v3.sym} 260 -120 0 0 {name=M2
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

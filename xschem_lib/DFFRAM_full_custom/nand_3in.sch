v {xschem version=3.0.0 file_version=1.2 }
G {}
K {}
V {}
S {}
E {}
N 40 -170 40 -110 {
lab=VDD}
N -110 -140 -110 -110 {
lab=VDD}
N -110 -140 40 -140 {
lab=VDD}
N 190 -140 190 -110 {
lab=VDD}
N 40 -140 190 -140 {
lab=VDD}
N -110 -80 -70 -80 {
lab=VDD}
N -70 -140 -70 -80 {
lab=VDD}
N 40 -80 80 -80 {
lab=VDD}
N 80 -140 80 -80 {
lab=VDD}
N 190 -80 230 -80 {
lab=VDD}
N 230 -140 230 -80 {
lab=VDD}
N 190 -140 230 -140 {
lab=VDD}
N 40 -50 40 -0 {
lab=Y}
N -110 -50 -110 -30 {
lab=Y}
N -110 -30 40 -30 {
lab=Y}
N 190 -50 190 -30 {
lab=Y}
N 40 -30 190 -30 {
lab=Y}
N 40 60 40 100 {
lab=#net1}
N 40 160 40 200 {
lab=#net2}
N 190 -30 250 -30 {
lab=Y}
N 40 260 40 310 {
lab=VSS}
N 40 230 80 230 {
lab=VSS}
N 80 230 80 290 {
lab=VSS}
N 40 290 80 290 {
lab=VSS}
N 40 130 80 130 {
lab=VSS}
N 80 130 80 230 {
lab=VSS}
N 40 30 80 30 {
lab=VSS}
N 80 30 80 130 {
lab=VSS}
N -170 -80 -150 -80 {
lab=A}
N -20 -80 0 -80 {
lab=B}
N 130 -80 150 -80 {
lab=C}
N -20 30 0 30 {
lab=A}
N -20 130 0 130 {
lab=B}
N -20 230 0 230 {
lab=C}
C {iopin.sym} 40 -160 3 0 {name=p1 lab=VDD}
C {opin.sym} 250 -30 0 0 {name=p2 lab=Y}
C {iopin.sym} 40 300 1 0 {name=p3 lab=VSS}
C {lab_pin.sym} -170 -80 0 0 {name=l2 sig_type=std_logic lab=A}
C {lab_pin.sym} -20 -80 0 0 {name=l1 sig_type=std_logic lab=B}
C {lab_pin.sym} 130 -80 0 0 {name=l3 sig_type=std_logic lab=C
}
C {lab_pin.sym} -20 30 0 0 {name=l4 sig_type=std_logic lab=A}
C {lab_pin.sym} -20 130 0 0 {name=l5 sig_type=std_logic lab=B}
C {lab_pin.sym} -20 230 0 0 {name=l6 sig_type=std_logic lab=C}
C {ipin.sym} -180 30 0 0 {name=p4 lab=A}
C {ipin.sym} -180 70 0 0 {name=p5 lab=B}
C {ipin.sym} -180 110 0 0 {name=p6 lab=C}
C {symbols/pfet_03v3.sym} -130 -80 0 0 {name=M1
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
C {symbols/nfet_03v3.sym} 20 30 0 0 {name=M4
L=0.28u
W=NF*0.85u
nf=1
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
C {symbols/nfet_03v3.sym} 20 130 0 0 {name=M5
L=0.28u
W=NF*0.85u
nf=1
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
C {symbols/nfet_03v3.sym} 20 230 0 0 {name=M6
L=0.28u
W=NF*0.85u
nf=1
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
C {symbols/pfet_03v3.sym} 20 -80 0 0 {name=M2
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
C {symbols/pfet_03v3.sym} 170 -80 0 0 {name=M3
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

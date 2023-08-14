v {xschem version=3.0.0 file_version=1.2 }
G {}
K {}
V {}
S {}
E {}
N 130 0 150 0 {
lab=OUT}
N -60 -90 -60 -10 {
lab=#net1}
N -60 -10 10 -10 {
lab=#net1}
N -60 10 -60 90 {
lab=#net2}
N -60 10 10 10 {
lab=#net2}
N -150 140 -150 150 {
lab=VSS}
N -150 20 -150 40 {
lab=VDD}
N -150 -40 -150 -20 {
lab=VSS}
N -150 -150 -150 -140 {
lab=VDD}
N -230 -110 -200 -110 {
lab=A0}
N -230 -70 -200 -70 {
lab=A1}
N -230 70 -200 70 {
lab=A2}
N -230 110 -200 110 {
lab=A3}
N 60 -60 60 -50 {
lab=VDD}
N 60 50 60 60 {
lab=VSS}
C {xschem_lib/DFFRAM_full_custom/nand.sym} -180 -60 0 0 {name=X_nand1 NF=NF}
C {xschem_lib/DFFRAM_full_custom/nand.sym} -180 120 0 0 {name=X_nand2 NF=NF}
C {xschem_lib/DFFRAM_full_custom/nor.sym} 40 10 0 0 {name=X_nor1 NF=NF}
C {iopin.sym} 60 60 1 0 {name=p5 lab=VSS}
C {iopin.sym} 60 -60 3 0 {name=p6 lab=VDD}
C {ipin.sym} -230 -110 0 0 {name=p7 lab=A0}
C {ipin.sym} -230 -70 0 0 {name=p8 lab=A1}
C {ipin.sym} -230 70 0 0 {name=p9 lab=A2}
C {ipin.sym} -230 110 0 0 {name=p10 lab=A3}
C {opin.sym} 150 0 0 0 {name=p11 lab=OUT}
C {lab_pin.sym} -150 -150 0 0 {name=l1 sig_type=std_logic lab=VDD}
C {lab_pin.sym} -150 -20 0 0 {name=l2 sig_type=std_logic lab=VSS}
C {lab_pin.sym} -150 20 0 0 {name=l3 sig_type=std_logic lab=VDD}
C {lab_pin.sym} -150 150 0 0 {name=l4 sig_type=std_logic lab=VSS}

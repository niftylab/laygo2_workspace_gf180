v {xschem version=3.0.0 file_version=1.2 }
G {}
K {}
V {}
S {}
E {}
N 60 -250 60 -170 {
lab=C0}
N 60 10 60 90 {
lab=C0_bar}
N 60 270 60 350 {
lab=C0}
N 140 180 200 180 {
lab=#net1}
N 200 180 200 440 {
lab=#net1}
N 140 440 200 440 {
lab=#net1}
N 140 180 200 180 {
lab=#net1}
N 200 180 200 440 {
lab=#net1}
N 140 440 200 440 {
lab=#net1}
N 140 -340 200 -340 {
lab=#net2}
N 200 -340 200 -80 {
lab=#net2}
N 140 -80 200 -80 {
lab=#net2}
N -120 -210 60 -210 {
lab=C0}
N -120 -210 -120 310 {
lab=C0}
N -120 310 60 310 {
lab=C0}
N 60 -520 60 -430 {
lab=C0_bar}
N 60 -520 250 -520 {
lab=C0_bar}
N 250 -520 250 570 {
lab=C0_bar}
N 60 570 250 570 {
lab=C0_bar}
N 60 530 60 570 {
lab=C0_bar}
N 60 50 250 50 {
lab=C0_bar}
N 200 310 340 310 {
lab=#net1}
N 200 -210 340 -210 {
lab=#net2}
N -60 -340 -20 -340 {
lab=X0}
N -60 -80 -20 -80 {
lab=X1}
N -60 180 -20 180 {
lab=X2}
N -60 440 -20 440 {
lab=X3}
N 140 -410 160 -410 {
lab=VSS}
N 140 -280 160 -280 {
lab=VDD}
N 140 -150 160 -150 {
lab=VSS}
N 140 -20 160 -20 {
lab=VDD}
N 140 110 160 110 {
lab=VSS}
N 140 240 160 240 {
lab=VDD}
N 140 370 160 370 {
lab=VSS}
N 140 500 160 500 {
lab=VDD}
N 420 -120 420 220 {
lab=C1}
N 420 400 420 430 {
lab=C1_bar}
N 320 430 420 430 {
lab=C1_bar}
N 320 -320 320 430 {
lab=C1_bar}
N 320 -320 420 -320 {
lab=C1_bar}
N 420 -320 420 -300 {
lab=C1_bar}
N -180 -340 -60 -340 {
lab=X0}
N -180 -80 -60 -80 {
lab=X1}
N -180 180 -60 180 {
lab=X2}
N -180 440 -60 440 {
lab=X3}
N 500 -280 530 -280 {
lab=VSS}
N 500 -150 530 -150 {
lab=VDD}
N 500 240 540 240 {
lab=VSS}
N 500 370 540 370 {
lab=VDD}
N 500 -210 560 -210 {
lab=OUT}
N 560 -210 600 -210 {
lab=OUT}
N 600 -210 600 310 {
lab=OUT}
N 500 310 600 310 {
lab=OUT}
N 600 60 650 60 {
lab=OUT}
N -120 -510 -120 -210 {
lab=C0}
N 280 50 420 50 {
lab=C1}
N 280 -410 280 50 {
lab=C1}
N -120 -510 -90 -510 {
lab=C0}
N 420 -410 420 -320 {
lab=C1_bar}
N 420 -410 440 -410 {
lab=C1_bar}
N 280 -410 310 -410 {
lab=C1}
C {xschem_lib/DFFRAM_full_custom/tr_gate.sym} 60 -80 2 1 {name=xTr1 NF=2}
C {xschem_lib/DFFRAM_full_custom/tr_gate.sym} 60 -340 2 1 {name=xTr2 NF=2}
C {xschem_lib/DFFRAM_full_custom/tr_gate.sym} 60 440 2 1 {name=xTr3 NF=2}
C {xschem_lib/DFFRAM_full_custom/tr_gate.sym} 60 180 2 1 {name=xTr4 NF=2}
C {xschem_lib/DFFRAM_full_custom/tr_gate.sym} 420 310 2 1 {name=xTr5 NF=2}
C {xschem_lib/DFFRAM_full_custom/tr_gate.sym} 420 -210 2 1 {name=xTr7 NF=2}
C {lab_pin.sym} 160 -280 2 0 {name=l1 sig_type=std_logic lab=VDD}
C {lab_pin.sym} 160 -410 2 0 {name=l2 sig_type=std_logic lab=VSS}
C {ipin.sym} -90 -510 2 0 {name=p1 lab=C0}
C {ipin.sym} 250 -520 2 0 {name=p2 lab=C0_bar}
C {ipin.sym} 440 -410 2 0 {name=p3 lab=C1_bar}
C {ipin.sym} 310 -410 2 0 {name=p4 lab=C1}
C {ipin.sym} -180 -340 0 0 {name=p5 lab=X0}
C {ipin.sym} -180 -80 0 0 {name=p6 lab=X1}
C {ipin.sym} -180 180 0 0 {name=p7 lab=X2}
C {ipin.sym} -180 440 0 0 {name=p8 lab=X3}
C {opin.sym} 650 60 0 0 {name=p9 lab=OUT}
C {iopin.sym} 0 -660 0 0 {name=p10 lab=VDD}
C {iopin.sym} 0 -620 0 0 {name=p11 lab=VSS}
C {lab_pin.sym} 160 -20 2 0 {name=l3 sig_type=std_logic lab=VDD}
C {lab_pin.sym} 160 -150 2 0 {name=l4 sig_type=std_logic lab=VSS}
C {lab_pin.sym} 160 240 2 0 {name=l5 sig_type=std_logic lab=VDD}
C {lab_pin.sym} 160 110 2 0 {name=l6 sig_type=std_logic lab=VSS}
C {lab_pin.sym} 160 500 2 0 {name=l7 sig_type=std_logic lab=VDD}
C {lab_pin.sym} 160 370 2 0 {name=l8 sig_type=std_logic lab=VSS}
C {lab_pin.sym} 540 370 2 0 {name=l9 sig_type=std_logic lab=VDD}
C {lab_pin.sym} 540 240 2 0 {name=l10 sig_type=std_logic lab=VSS}
C {lab_pin.sym} 530 -150 2 0 {name=l11 sig_type=std_logic lab=VDD}
C {lab_pin.sym} 530 -280 2 0 {name=l12 sig_type=std_logic lab=VSS}

v {xschem version=3.0.0 file_version=1.2 }
G {}
K {}
V {}
S {}
E {}
N 80 -170 80 -160 {
lab=VDD}
N 80 -40 80 -30 {
lab=VSS}
N 80 -30 80 -20 {
lab=VSS}
N -20 -130 -0 -130 {
lab=X0}
N -20 -110 -0 -110 {
lab=X1}
N -20 -90 0 -90 {
lab=X2}
N -20 -70 0 -70 {
lab=X3}
N 110 -100 140 -100 {
lab=OUT}
N 140 -100 200 -100 {
lab=OUT}
C {xschem_lib/DFFRAM_full_custom/mux4to1.sym} 50 -100 0 0 {name=xMux1 NF=2}
C {lab_pin.sym} 80 -170 2 0 {name=l1 sig_type=std_logic lab=VDD}
C {lab_pin.sym} 80 -20 2 0 {name=l2 sig_type=std_logic lab=VSS}
C {vsource.sym} -410 -30 0 0 {name=V1 value=3.3}
C {lab_pin.sym} -410 -60 1 0 {name=l3 sig_type=std_logic lab=VDD}
C {lab_pin.sym} -470 -60 1 0 {name=l4 sig_type=std_logic lab=VSS}
C {vsource.sym} -470 -30 0 0 {name=V2 value=0}
C {gnd.sym} -470 0 0 0 {name=l5 lab=GND}
C {gnd.sym} -410 0 0 0 {name=l6 lab=GND}
C {gnd.sym} -470 -170 0 0 {name=l2649 lab=GND}
C {lab_pin.sym} -330 -60 1 0 {name=l2650 sig_type=std_logic lab=C0}
C {vsource.sym} -470 -200 0 0 {name=V18 value="PULSE(0V 3.3 2n 50p 50p 2n 4n)"}
C {lab_pin.sym} 30 -190 1 0 {name=l7 sig_type=std_logic lab=C0}
C {gnd.sym} -470 -300 0 0 {name=l8 lab=GND}
C {lab_pin.sym} -270 -60 1 0 {name=l9 sig_type=std_logic lab=C0_bar}
C {vsource.sym} -470 -330 0 0 {name=V3 value="PULSE(0V 3.3 0 50p 50p 2n 4n)"}
C {lab_pin.sym} 30 -10 3 0 {name=l10 sig_type=std_logic lab=C0_bar}
C {gnd.sym} -250 -170 0 0 {name=l11 lab=GND}
C {lab_pin.sym} -200 -60 1 0 {name=l12 sig_type=std_logic lab=C1}
C {vsource.sym} -250 -200 0 0 {name=V4 value="PULSE(0V 3.3 4n 50p 50p 4n 8n)"}
C {gnd.sym} -250 -300 0 0 {name=l13 lab=GND}
C {lab_pin.sym} -140 -60 1 0 {name=l14 sig_type=std_logic lab=C1_bar}
C {vsource.sym} -250 -330 0 0 {name=V5 value="PULSE(0V 3.3 0 50p 50p 4n 8n)"}
C {lab_pin.sym} 50 -190 1 0 {name=l15 sig_type=std_logic lab=C1}
C {lab_pin.sym} 50 -10 3 0 {name=l16 sig_type=std_logic lab=C1_bar}
C {vsource.sym} -270 -30 0 0 {name=V6 value=3.3}
C {lab_pin.sym} -470 -360 1 0 {name=l17 sig_type=std_logic lab=X1}
C {lab_pin.sym} -470 -230 1 0 {name=l18 sig_type=std_logic lab=X0}
C {vsource.sym} -330 -30 0 0 {name=V7 value=0}
C {gnd.sym} -330 0 0 0 {name=l19 lab=GND}
C {gnd.sym} -270 0 0 0 {name=l20 lab=GND}
C {vsource.sym} -140 -30 0 0 {name=V8 value=3.3}
C {lab_pin.sym} -250 -360 1 0 {name=l21 sig_type=std_logic lab=X3}
C {lab_pin.sym} -250 -230 1 0 {name=l22 sig_type=std_logic lab=X2}
C {vsource.sym} -200 -30 0 0 {name=V9 value=0}
C {gnd.sym} -200 0 0 0 {name=l23 lab=GND}
C {gnd.sym} -140 0 0 0 {name=l24 lab=GND}
C {lab_pin.sym} -20 -130 0 0 {name=l25 sig_type=std_logic lab=X0}
C {lab_pin.sym} -20 -110 0 0 {name=l26 sig_type=std_logic lab=X1}
C {lab_pin.sym} -20 -90 0 0 {name=l27 sig_type=std_logic lab=X2}
C {lab_pin.sym} -20 -70 0 0 {name=l28 sig_type=std_logic lab=X3}
C {code_shown.sym} -540 -530 0 0 {name=s1 only_toplevel=false value="
.control
save all
tran 25p 18n
write tb_mux_nf2_250M.raw
.endc
"}
C {devices/code_shown.sym} -240 -520 0 0 {name=MODELS only_toplevel=true
format="tcleval( @value )"
value="
.include $::180MCU_MODELS/design.ngspice
.lib $::180MCU_MODELS/sm141064.ngspice typical
"}
C {lab_pin.sym} 140 -100 1 0 {name=l29 sig_type=std_logic lab=OUT}
C {xschem_lib/DFFRAM_full_custom/inv.sym} 200 -60 0 0 {name=X_inv1 NF=2}
C {lab_pin.sym} 260 -140 2 0 {name=l30 sig_type=std_logic lab=VDD}
C {lab_pin.sym} 260 -60 3 0 {name=l31 sig_type=std_logic lab=VSS}

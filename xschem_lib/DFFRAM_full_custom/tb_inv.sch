v {xschem version=3.0.0 file_version=1.2 }
G {}
K {}
V {}
S {}
E {}
B 2 530 -160 1330 240 {flags=graph
y1=-2
y2=0
ypos1=0
ypos2=2
divy=5
subdivy=1
unity=1
x1=-2.00741e-06
x2=7.99264e-06
divx=5
subdivx=1
node=""
color=""
dataset=0
unitx=u
}
N 140 -40 200 -40 {
lab=Vout1}
N 140 120 200 120 {
lab=Vout2}
N 140 290 200 290 {
lab=Vout3}
N 60 330 60 340 {
lab=GND}
N 260 330 260 340 {
lab=GND}
N 60 160 60 170 {
lab=GND}
N 260 160 260 170 {
lab=GND}
N 60 0 60 10 {
lab=GND}
N 260 -0 260 10 {
lab=GND}
N 60 -90 60 -80 {
lab=VDD}
N 260 -90 260 -80 {
lab=VDD}
N 60 70 60 80 {
lab=VDD}
N 260 70 260 80 {
lab=VDD}
N 60 240 60 250 {
lab=VDD}
N 260 240 260 250 {
lab=VDD}
N -180 -60 -180 -40 {
lab=VDD}
N -180 20 -180 40 {
lab=GND}
N -160 120 -160 140 {
lab=Vin}
N -160 200 -160 220 {
lab=GND}
N -160 120 -0 120 {
lab=Vin}
N -40 -40 0 -40 {
lab=Vin}
N -40 -40 -40 120 {
lab=Vin}
N -40 290 -0 290 {
lab=Vin}
N -40 120 -40 290 {
lab=Vin}
N 340 -40 360 -40 {
lab=#net1}
N 340 120 360 120 {
lab=#net2}
N 340 290 360 290 {
lab=#net3}
C {xschem_lib/DFFRAM_full_custom/inv.sym} 0 0 0 0 {name=X_inv1 NF=2}
C {xschem_lib/DFFRAM_full_custom/inv.sym} 200 0 0 0 {name=X_inv2 NF=2}
C {xschem_lib/DFFRAM_full_custom/inv.sym} 0 160 0 0 {name=X_inv3 NF=2}
C {xschem_lib/DFFRAM_full_custom/inv.sym} 200 160 0 0 {name=X_inv4 NF=6}
C {xschem_lib/DFFRAM_full_custom/inv.sym} 0 330 0 0 {name=X_inv5 NF=2}
C {xschem_lib/DFFRAM_full_custom/inv.sym} 200 330 0 0 {name=X_inv6 NF=20}
C {devices/gnd.sym} 60 10 0 0 {name=l1 lab=GND}
C {devices/gnd.sym} 260 10 0 0 {name=l2 lab=GND}
C {devices/gnd.sym} 60 170 0 0 {name=l3 lab=GND}
C {devices/gnd.sym} 260 170 0 0 {name=l4 lab=GND}
C {devices/gnd.sym} 60 340 0 0 {name=l5 lab=GND}
C {devices/gnd.sym} 260 340 0 0 {name=l6 lab=GND}
C {devices/vdd.sym} 60 -90 0 0 {name=l7 lab=VDD}
C {devices/vdd.sym} 260 -90 0 0 {name=l8 lab=VDD}
C {devices/vdd.sym} 60 70 0 0 {name=l9 lab=VDD}
C {devices/vdd.sym} 260 70 0 0 {name=l10 lab=VDD}
C {devices/vdd.sym} 60 240 0 0 {name=l11 lab=VDD}
C {devices/vdd.sym} 260 240 0 0 {name=l12 lab=VDD}
C {devices/vdd.sym} -180 -60 0 0 {name=l13 lab=VDD}
C {devices/vsource.sym} -180 -10 0 0 {name=V1 value=1.8}
C {devices/gnd.sym} -180 40 0 0 {name=l14 lab=GND}
C {devices/vsource.sym} -160 170 0 0 {name=V2 value="PULSE(0V 1.8 100p 50p 50p 100p 500p)"}
C {devices/gnd.sym} -160 220 0 0 {name=l15 lab=GND}
C {devices/lab_pin.sym} -80 120 1 0 {name=l16 sig_type=std_logic lab=Vin}
C {devices/lab_pin.sym} 180 -40 1 0 {name=l17 sig_type=std_logic lab=Vout1}
C {devices/lab_pin.sym} 180 120 1 0 {name=l18 sig_type=std_logic lab=Vout2}
C {devices/lab_pin.sym} 180 290 1 0 {name=l19 sig_type=std_logic lab=Vout3}
C {devices/code_shown.sym} -280 -210 0 0 {name=control only_toplevel=false value="
.control
save all
tran 3p 600p
plot Vin Vout1 Vout2 Vout3
.endc
"}
C {devices/code_shown.sym} 0 -260 0 0 {name=MODELS only_toplevel=true
format="tcleval( @value )"
value="
.lib /usr/local/share/pdk/sky130A/libs.tech/ngspice/sky130.lib.spice tt
"
}

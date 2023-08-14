###########################################
#                                         #
#       32bit WORD Layout Generator       #
#        Created by HyungJoo Park         #   
#                                         #
###########################################


import numpy as np
import pprint
import laygo2
import laygo2.interface
import laygo2_tech as tech
# Parameter definitions #############
# Variables
cell_type = 'word_v2'
nf = 1
nf_inv = 2
# Templates
tpmos_name = 'pmos'
tnmos_name = 'nmos'
# Grids
pg_name = 'placement_basic'
r12_name = 'routing_12_cmos'
r23_basic_name = 'routing_23_basic'
r23_cmos_name = 'routing_23_cmos'
r34_name = 'routing_34_basic'
# Design hierarchy
libname = 'logic_advanced'
ref_dir_template = './laygo2_example/' #export this layout's information into the yaml in this dir 
ref_dir_export = './laygo2_example/logic_advance/'
ref_dir_MAG_exported = './laygo2_example/logic_advance/TCL/'
ref_dir_layout = './magic_layout'
# End of parameter definitions ######

# Generation start ##################
# 1. Load templates and grids.
print("Load templates")
templates = tech.load_templates()
tpmos, tnmos = templates[tpmos_name], templates[tnmos_name]
tlogic_prim = laygo2.interface.yaml.import_template(filename=ref_dir_template+'logic/logic_generated_templates.yaml')
tlogic_adv = laygo2.interface.yaml.import_template(filename=ref_dir_template+'logic_advance/logic_advanced_templates.yaml')

print("Load grids")
grids = tech.load_grids(templates=templates)
pg, r12, r23, r34 = grids[pg_name], grids[r12_name], grids[r23_cmos_name], grids[r34_name]

cellname = cell_type+'_'+str(nf)+'x'
print('--------------------')
print('Now Creating '+cellname)

# 2. Create a design hierarchy
lib = laygo2.object.database.Library(name=libname)
dsn = laygo2.object.database.Design(name=cellname, libname=libname)
lib.append(dsn)

# 3. Create istances.
print("Create instances")
cells=list()
cells.append(tlogic_adv['byte_dff_left_'+str(nf)+'x'].generate(name='byte4'))
cells.append(tlogic_adv['byte_dff_left_'+str(nf)+'x'].generate(name='byte3'))
cells.append(tlogic_adv['byte_dff_right_'+str(nf)+'x'].generate(name='byte2'))  
cells.append(tlogic_adv['byte_dff_right_'+str(nf)+'x'].generate(name='byte1'))  

buf_sel = list()
buf_sel.append(tlogic_prim['inv_1x'].generate(name='buf_sel0'))
buf_sel.append(tlogic_prim['inv_4x'].generate(name='buf_sel1'))
buf_ck = list()
buf_ck.append(tlogic_prim['inv_'+str(nf_inv)+'x'].generate(name='buf_ck0'))
buf_ck.append(tlogic_prim['inv_'+str(nf_inv*4)+'x'].generate(name='buf_ck1'))
gate_RE = list()
gate_RE.append(tlogic_prim['nand_1x'].generate(name='gt_re0'))
gate_RE.append(tlogic_prim['inv_'+str(nf_inv)+'x'].generate(name='gt_re1'))
gate_RE.append(tlogic_prim['inv_'+str(nf_inv*3)+'x'].generate(name='gt_re2'))
gate_RE.append(tlogic_prim['inv_'+str(nf_inv*9)+'x'].generate(name='gt_re3'))

# NTAP0 = templates[tntap_name].generate(name='MNT0', params={'nf':2, 'tie':'TAP0'})
# PTAP0 = templates[tptap_name].generate(name='MPT0', transform='MX',params={'nf':2, 'tie':'TAP0'})
# NTAP1 = templates[tntap_name].generate(name='MNT1', params={'nf':2, 'tie':'TAP0'})
# PTAP1 = templates[tptap_name].generate(name='MPT1', transform='MX',params={'nf':2, 'tie':'TAP0'})

# 4. Place instances.
pg_list = [cells[0], cells[1], cells[2], cells[3]]
cursor = 2
for cell in buf_ck:
    pg_list.insert(cursor,cell)
    cursor += 1
for cell in gate_RE:
    pg_list.insert(cursor,cell)
    cursor += 1
for cell in buf_sel:
    pg_list.insert(cursor,cell)
    cursor += 1
dsn.place(grid=pg, inst=pg_list, mn=[0,0])
# 5. Create and place wires.
print("Create wires")
track_selbuf = [None, r34.mn(buf_sel[1].pins['O'])[1,1]+1]
track_clkbuf = [None, r34.mn(buf_sel[1].pins['O'])[1,1]]
track_rebuf = [None, r34.mn(buf_sel[1].pins['O'])[1,1]-1]
# sel_buf
mn_selbuf = [r34.mn(buf_sel[1].pins['O'])[0]]
for i in range(4):
    mn_selbuf.append(r34.mn(cells[i].pins['SEL'])[0])
dsn.route_via_track(grid=r34, mn=mn_selbuf, track=track_selbuf)
# clk_buf
mn_clkbuf = [r34.mn(buf_ck[1].pins['O'])[0]]
for i in range(4):
    mn_clkbuf.append(r34.mn(cells[i].pins['CLK'])[0])
dsn.route_via_track(grid=r34, mn=mn_clkbuf, track=track_clkbuf)
# RE_buf
mn_rebuf = [r34.mn(gate_RE[-1].pins['O'])[0]]
for i in range(4):
    mn_rebuf.append(r34.mn(cells[i].pins['RE'])[0])
dsn.route_via_track(grid=r34, mn=mn_rebuf, track=track_rebuf)

# sel
track_sel = [None, r34.mn(buf_sel[1].pins['O'])[0,1]-2]
mn_sel = [r34.mn(gate_RE[0].pins['A'])[1],r34.mn(buf_sel[0].pins['I'])[1]]
rsel = dsn.route_via_track(grid=r34, mn=mn_sel, track=track_sel)

# internal
_track = [None, (r23.mn(buf_sel[1].pins['O'])[0,1] + r23.mn(buf_sel[1].pins['O'])[1,1])/2]
mn_int = [r23.mn(buf_sel[0].pins['O'])[0], r23.mn(buf_sel[1].pins['I'])[0]]
dsn.route_via_track(grid=r23, mn=mn_int, track=_track)

mn_int = [r23.mn(buf_ck[0].pins['O'])[0], r23.mn(buf_ck[1].pins['I'])[0]]
dsn.route_via_track(grid=r23, mn=mn_int, track=_track)

mn_int = [r23.mn(gate_RE[0].pins['OUT'])[0], r23.mn(gate_RE[1].pins['I'])[0]]
dsn.route_via_track(grid=r23, mn=mn_int, track=_track)
mn_int = [r23.mn(gate_RE[1].pins['O'])[0], r23.mn(gate_RE[2].pins['I'])[0]]
dsn.route_via_track(grid=r23, mn=mn_int, track=_track)
mn_int = [r23.mn(gate_RE[2].pins['O'])[0], r23.mn(gate_RE[3].pins['I'])[0]]
dsn.route_via_track(grid=r23, mn=mn_int, track=_track)

# VSS
rvss0 = dsn.route(grid=r12, mn=[r12.mn.bottom_left(cells[0]), r12.mn.bottom_right(cells[3])])
# VDD
rvdd0 = dsn.route(grid=r12, mn=[r12.mn.top_left(cells[0]), r12.mn.top_right(cells[3])])

# 6. Create pins.
psel = dsn.pin(name='SEL', grid=r34, mn=r34.mn.bbox(rsel[-1]))
pwe = list()
for i in range(4):
    pwe.append(dsn.pin(name='WE'+str(3-i), grid=r34, mn=r34.mn.bbox(cells[i].pins['WE'])))
pclk = dsn.pin(name='CLK', grid=r34, mn=r34.mn.bbox(buf_ck[0].pins['I']))
pre = dsn.pin(name='RE', grid=r34, mn=r34.mn.bbox(gate_RE[0].pins['B']))
pDo = list()
pDi = list()
for i in range(4):
    for j in range(8):
        pDo.append(dsn.pin(name='Do'+str(8*(3-i)+j), grid=r34, mn=r34.mn.bbox(cells[i].pins['Do'+str(j)])))
        pDi.append(dsn.pin(name='Di'+str(8*(3-i)+j), grid=r34, mn=r34.mn.bbox(cells[i].pins['Di'+str(j)])))
pvss0 = dsn.pin(name='VSS', grid=r12, mn=r12.mn.bbox(rvss0))
pvdd0 = dsn.pin(name='VDD', grid=r12, mn=r12.mn.bbox(rvdd0))

# Uncomment for BAG export
laygo2.interface.magic.export(lib, filename=ref_dir_MAG_exported +libname+'_'+cellname+'.tcl', cellname=None, libpath=ref_dir_layout, scale=tech.name, reset_library=False, tech_library=tech.name)

# 8. Export to a template database file.
nat_temp = dsn.export_to_template()
laygo2.interface.yaml.export_template(nat_temp, filename=ref_dir_export+libname+'_templates.yaml', mode='append')
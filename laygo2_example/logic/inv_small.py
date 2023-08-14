######################################
#                                    #
#   3 input NAND Layout Gernerator   #
#      Created by Hyungjoo Park      #
#                                    #
######################################

import numpy as np
import pprint
import laygo2
import laygo2.interface
import laygo2_tech as tech
# Parameter definitions #############
# Variables
cell_type = 'inv'
# Templates
tpmos_name = 'pmos'
tnmos_name = 'nmos'
# Grids
pg_name = 'placement_basic'
r12_name = 'routing_12_cmos'
r23_name = 'routing_23_cmos'
# Design hierarchy
libname = 'logic_generated'
ref_dir_template = './laygo2_example/logic/' #export this layout's information into the yaml in this dir 
ref_dir_MAG_exported = './laygo2_example/logic/TCL/'
ref_dir_layout = './magic_layout'
# End of parameter definitions ######

# Generation start ##################
# 1. Load templates and grids.
print("Load templates")
templates = tech.load_templates()
tpmos, tnmos = templates[tpmos_name], templates[tnmos_name]

print("Load grids")
grids = tech.load_grids(templates=templates)
pg, r12, r23 = grids[pg_name], grids[r12_name], grids[r23_name]

cellname = cell_type+'_1x'
print('--------------------')
print('Now Creating '+cellname)

# 2. Create a design hierarchy
lib = laygo2.object.database.Library(name=libname)
dsn = laygo2.object.database.Design(name=cellname, libname=libname)
lib.append(dsn)

# 3. Create istances.
print("Create instances")
in0 = templates['nmos180_fast_center_nf1_left'].generate(name='nm0')
nbndl = templates['nmos180_fast_boundary'].generate(name='nbndl')
nbndr = templates['nmos180_fast_boundary'].generate(name='nbndr')
ip0 = templates['pmos180_fast_center_nf1_left'].generate(name='pm0', transform='MX')
pbndl = templates['pmos180_fast_boundary'].generate(name='pbndl', transform='MX')
pbndr = templates['pmos180_fast_boundary'].generate(name='pbndr', transform='MX')
# 4. Place instances.
dsn.place(grid=pg, inst=nbndl, mn=[0,0])
dsn.place(grid=pg, inst=pbndl, mn=pg.mn.top_left(nbndl)+pg.mn.height_vec(pbndl))
dsn.place(grid=pg, inst=in0, mn=pg.mn.bottom_right(nbndl))
dsn.place(grid=pg, inst=ip0, mn=pg.mn.top_left(in0) + pg.mn.height_vec(ip0))
dsn.place(grid=pg, inst=nbndr, mn=pg.mn.bottom_right(in0))
dsn.place(grid=pg, inst=pbndr, mn=pg.mn.top_left(nbndr)+pg.mn.height_vec(pbndr))
# # 5. Create and place wires.
# print("Create wires")
# IN
_mn = [r12.mn(in0.pins['G0'])[0], r12.mn(ip0.pins['G0'])[0]]
dsn.route(grid=r12, mn=_mn, via_tag=[False, True])

_mn = [r23.mn(in0.pins['G0'])[0], r23.mn(ip0.pins['G0'])[0]]
dsn.route(grid=r23, mn=[_mn[1],_mn[1]+[1,0]],via_tag=[True,False])
rI0 = dsn.route(grid=r23, mn=_mn, via_tag=[False, False])

# OUT
_mn = [r12.mn(ip0.pins['S0'])[0], r12.mn(ip0.pins['D0'])[0]]
dsn.route(grid=r12, mn=_mn, via_tag=[False,False])

_mn = [r12.mn(in0.pins['G0'])[0], r12.mn(ip0.pins['G0'])[0]]
dsn.route(grid=r12, mn=_mn, via_tag=[False, True])
_mn = [r12.mn(in0.pins['D0'])[1], r12.mn(ip0.pins['D0'])[0]]
dsn.route(grid=r12, mn=_mn, via_tag=[False,True])
_mn = [r23.mn(in0.pins['D0'])[1], r23.mn(ip0.pins['D0'])[0]]
rout0,vout1 = dsn.route(grid=r23, mn=_mn, via_tag=[False,True])

# VSS  
# M2 Rect
_mn = [r12.mn.bottom_left(nbndl), r12.mn.bottom_right(nbndr)]
rvss0 = dsn.route(grid=r12, mn=_mn)

# tie
_mn = [r12.mn(in0.pins['S0'])[1], r12.mn(in0.pins['S0'])[1]+[0,-2]]
rvss1, _ = dsn.route(grid=r12, mn=_mn, via_tag=[False, True])

# VDD
# M2 Rect
_mn = [r12.mn.top_left(pbndl), r12.mn.top_right(pbndr)]
rvdd0 = dsn.route(grid=r12, mn=_mn)

_mn =[r12.mn(ip0.pins['S0'])[0],[r12.mn(ip0.pins['S0'])[0,0], r12.mn.top_left(pbndl)[1]]]
dsn.route(grid=r12, mn=_mn, via_tag=[False,True])

# # 6. Create pins.

pinA = dsn.pin(name='I', grid=r12, mn=r23.mn.bbox(rI0))
pout0 = dsn.pin(name='O', grid=r23, mn=r23.mn.bbox(rout0))
pvss0 = dsn.pin(name='VSS', grid=r12, mn=r12.mn.bbox(rvss0))
pvdd0 = dsn.pin(name='VDD', grid=r12, mn=r12.mn.bbox(rvdd0))

# 7. Export to physical database.
print("Export design")
print("")

# Uncomment for BAG export
laygo2.interface.magic.export(lib, filename=ref_dir_MAG_exported +libname+'_'+cellname+'.tcl', cellname=None, libpath=ref_dir_layout, scale=tech.scale, reset_library=False, tech_library=tech.name)

# 8. Export to a template database file.
nat_temp = dsn.export_to_template()
laygo2.interface.yaml.export_template(nat_temp, filename=ref_dir_template+libname+'_templates.yaml', mode='append')
# nMap.netMap.lvs_check(lib['nand_4x'], r23_basic, {"via_M2_M3_0":('M2','M3')})
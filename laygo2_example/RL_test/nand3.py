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
import laygo2_example.RL_test.myTemplate as myTemplate
# Parameter definitions #############
# Variables
cell_type = 'nand3'
nf_list = [2,4]
# Templates
tpmos_name = 'pmos'
tnmos_name = 'nmos'
# Grids
pg_name = 'placement_basic'
r12_name = 'routing_12_cmos'
r23_name = 'routing_23_cmos'
# Design hierarchy
libname = 'RL_test'
ref_dir_template = './laygo2_example/RL_test/' #export this layout's information into the yaml in this dir 
ref_dir_MAG_exported = './laygo2_example/RL_test/TCL/'
ref_dir_layout = './magic_layout'
# End of parameter definitions ######

# Generation start ##################
# 1. Load templates and grids.
print("Load templates")
templates = tech.load_templates()
tpmos, tnmos = templates[tpmos_name], templates[tnmos_name]
#tlib = laygo2.interface.yaml.import_template(filename=ref_dir_template+'logic_generated_templates.yaml')
print(templates[tpmos_name], templates[tnmos_name], sep="\n")

print("Load grids")
grids = tech.load_grids(templates=templates)
pg, r12, r23 = grids[pg_name], grids[r12_name], grids[r23_name]
print(grids[pg_name], grids[r12_name], grids[r23_name], sep="\n")

abut = [2,0]
for nf in nf_list:
   cellname = cell_type+'_'+str(nf)+'x'
   print('--------------------')
   print('Now Creating '+cellname)

# 2. Create a design hierarchy
   lib = laygo2.object.database.Library(name=libname)
   dsn = laygo2.object.database.Design(name=cellname, libname=libname)
   lib.append(dsn)

# 3. Create istances.
   print("Create instances")
   in0 = tnmos.generate(name='MN0', params={'nf': nf, 'tie': 'S'})
   ip0 = tpmos.generate(name='MP0', transform='MX', params={'nf': nf, 'tie': 'S'})
   in1 = tnmos.generate(name='MN1', params={'nf': nf, 'trackswap': True})
   ip1 = tpmos.generate(name='MP1', transform='MX', params={'nf': nf, 'tie': 'S'})
   in2 = tnmos.generate(name='MN2', params={'nf': nf})
   ip2 = tpmos.generate(name='MP2', transform='MX', params={'nf': nf, 'tie': 'S'})
# 4. Place instances.
   dsn.place(grid=pg, inst=in0, mn=[0,0])
   dsn.place(grid=pg, inst=ip0, mn=pg.mn.top_left(in0) + pg.mn.height_vec(ip0))
   dsn.place(grid=pg, inst=in1, mn=pg.mn.bottom_right(in0)-abut)
   dsn.place(grid=pg, inst=ip1, mn=pg.mn.top_right(ip0)-abut)
   dsn.place(grid=pg, inst=in2, mn=pg.mn.bottom_right(in1)-abut)
   dsn.place(grid=pg, inst=ip2, mn=pg.mn.top_right(ip1)-abut)

# 5. Create and place wires.
   print("Create wires")
   # A
   if nf == 2:
      _mn = [r23.mn(in2.pins['G'])[0], r23.mn(ip2.pins['G'])[0]]
      _track = [r23.mn(in2.pins['G'])[0,0]-1, None]
      rA_t0 = dsn.route_via_track(grid=r23, mn=_mn, track=_track)
   else:
      _mn = [r23.mn(in2.pins['G'])[0], r23.mn(ip2.pins['G'])[0]]
      vA0, rA0, vA1 = dsn.route(grid=r23, mn=_mn, via_tag=[True, True])

   # B
   _mn = [r23.mn(in1.pins['G'])[0], r23.mn(ip1.pins['G'])[0]]
   vB0, rB0, vB1 = dsn.route(grid=r23, mn=_mn, via_tag=[True, True])

   # C
   _mn = [r23.mn(in0.pins['G'])[0], r23.mn(ip0.pins['G'])[0]]
   vC0, rC0, vC1 = dsn.route(grid=r23, mn=_mn, via_tag=[True, True])
   # Internal
   # _mn = [r12.mn(ip0.pins['D'])[1], r12.mn(ip1.pins['D'])[0]]
   # dsn.route(grid=r12, mn=_mn, netname='Internal')
   _mn = [r12.mn(in0.pins['D'])[1], r12.mn(in1.pins['S'])[0]]
   dsn.route(grid=r12, mn=_mn)
   _mn = [r12.mn(in1.pins['D'])[1], r12.mn(in2.pins['S'])[0]]
   dsn.route(grid=r12, mn=_mn)

   # OUT
   _mn = [r12.mn(ip0.pins['D'])[1], r12.mn(ip2.pins['D'])[0]]
   dsn.route(grid=r12, mn=_mn)
   _mn = [r23.mn(in2.pins['D'])[1], r23.mn(ip2.pins['D'])[1]]
   vout0, rout0, vout1 = dsn.route(grid=r23, mn=_mn, via_tag=[True, True])

   # VSS
   rvss0 = dsn.route(grid=r12, mn=[r12.mn(in0.pins['RAIL'])[0], r12.mn(in2.pins['RAIL'])[1]])

   # VDD
   rvdd0 = dsn.route(grid=r12, mn=[r12.mn(ip0.pins['RAIL'])[0], r12.mn(ip2.pins['RAIL'])[1]])

# 6. Create pins.
   if nf==2:
      pinA = dsn.pin(name='A', grid=r23, mn=r23.mn.bbox(rA_t0[2]))
   else:
      pinA = dsn.pin(name='A', grid=r23, mn=r23.mn.bbox(rA0))
   pinB = dsn.pin(name='B', grid=r23, mn=r23.mn.bbox(rB0))
   pinC = dsn.pin(name='C', grid=r23, mn=r23.mn.bbox(rC0))
   pout0 = dsn.pin(name='Y', grid=r23, mn=r23.mn.bbox(rout0))
   pvss0 = dsn.pin(name='VSS', grid=r12, mn=r12.mn.bbox(rvss0))
   pvdd0 = dsn.pin(name='VDD', grid=r12, mn=r12.mn.bbox(rvdd0))

def import_templates(): # dsn_name:str):
   _template = myTemplate.export_templates(lib, celltype=cell_type)
   return _template

if __name__=='__main__':
# 7. Export to physical database.
   print("Export design")
   print("")
   
# Uncomment for BAG export
   laygo2.interface.magic.export(lib, filename=ref_dir_MAG_exported +libname+'_'+cellname+'.tcl', cellname=None, libpath=ref_dir_layout, scale=0.1, reset_library=False, tech_library=tech.name)

# 8. Export to a template database file.
   nat_temp = dsn.export_to_template()
   laygo2.interface.yaml.export_template(nat_temp, filename=ref_dir_template+libname+'_templates.yaml', mode='append')
# nMap.netMap.lvs_check(lib['nand_4x'], r23_basic, {"via_M2_M3_0":('M2','M3')})
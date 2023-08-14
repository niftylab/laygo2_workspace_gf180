###########################################
#                                         #
#      D-Flip Flop Layout Generator       #
#  Created by Taeho Shin & HyungJoo Park  #   
#                                         #
###########################################


import numpy as np
import pprint
import laygo2
import laygo2.interface
import laygo2_tech as tech
import laygo2_example.RL_test.myTemplate as myTemplate
import laygo2_example.RL_test.inv as inv
import laygo2_example.RL_test.tinv as tinv
import laygo2_example.RL_test.tinv_small_1x as tinv_small
# Parameter definitions #############
# Variables
cell_type = 'dff'
nf_list = [2,4]
# Templates
tpmos_name = 'pmos'
tnmos_name = 'nmos'
# Grids
pg_name = 'placement_basic'
r12_name = 'routing_12_cmos'
r23_name = 'routing_23_cmos'
r34_name = 'routing_34_basic'
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
tlib = laygo2.interface.yaml.import_template(filename=ref_dir_template+libname+'_templates.yaml')

# load templates as Virtual instances
# TODO 이렇게 nf별로 따로 template를 불러와야 하는 것이 매우 아쉬움. 하지만 일단 기존의 만든 legacy laygo2코드를 재사용하기 위해 nf별로 template을 구별함
#      궁극적으로는 inv.py에 있는 dsn 생성 코드를 import_templates의 generator 코드가 필요할 때 마다 nf를 바꿔서 call해오는 방식으로 바꿔야 함
t_inv = inv.import_templates()
t_tinv = tinv.import_templates()
t_tinv_small = tinv_small.import_templates()

print("Load grids")
grids = tech.load_grids(templates=templates)
pg, r12, r23, r34 = grids[pg_name], grids[r12_name], grids[r23_name], grids[r34_name]
#print(grids[pg_name], grids[r12_name], grids[r23_basic_name], grids[r34_name], sep="\n")

abut = [0,0]
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
   inv0 = t_inv.generate(name='inv0', params={'nf': nf})
   inv1 = t_inv.generate(name='inv1', params={'nf': nf})
   inv2 = t_inv.generate(name='inv2', params={'nf': nf})
   inv3 = t_inv.generate(name='inv3', params={'nf': nf}) 

   tinv0 = t_tinv.generate(name='tinv0', params={'nf': nf})
   tinv1 = t_tinv.generate(name='tinv1', params={'nf': nf})

   tinv_small0 = t_tinv_small.generate(name='tinv_small0')
   tinv_small1 = t_tinv_small.generate(name='tinv_small1')

# 4. Place instances.
   dsn.place(grid=pg, inst=inv0, mn=[0,0])
   dsn.place(grid=pg, inst=inv1, mn=pg.mn.bottom_right(inv0)-abut)
   dsn.place(grid=pg, inst=tinv0, mn=pg.mn.bottom_right(inv1)-abut)
   dsn.place(grid=pg, inst=tinv_small0, mn=pg.mn.bottom_right(tinv0)-abut)
   dsn.place(grid=pg, inst=inv2, mn=pg.mn.bottom_right(tinv_small0)-abut)
   dsn.place(grid=pg, inst=tinv1, mn=pg.mn.bottom_right(inv2)-abut)
   dsn.place(grid=pg, inst=tinv_small1, mn=pg.mn.bottom_right(tinv1)-abut)
   dsn.place(grid=pg, inst=inv3, mn=pg.mn.bottom_right(tinv_small1)-abut)
   
   # 5. Create and place wires.
   print("Create wires")
   
   # 1st M4
   _mn = [r34.mn(inv1.pins['O'])[0], r34.mn(tinv_small1.pins['ENB'])[0]]
   _track = [None, r34.mn(inv1.pins['O'])[0,1]-2]
   mn_list=[]
   mn_list.append(r34.mn(inv1.pins['O'])[0])
   mn_list.append(r34.mn(tinv0.pins['ENB'])[0])
   mn_list.append(r34.mn(tinv1.pins['EN'])[0])
   mn_list.append(r34.mn(tinv_small0.pins['EN'])[0])
   mn_list.append(r34.mn(tinv_small1.pins['ENB'])[0])
   dsn.route_via_track(grid=r34, mn=mn_list, track=_track)
   
   # 2nd M4
   _track[1] += 1
   mn_list=[]
   mn_list.append(r34.mn(inv0.pins['O'])[0])
   mn_list.append(r34.mn(inv1.pins['I'])[0])
   mn_list.append(r34.mn(tinv0.pins['EN'])[0])
   mn_list.append(r34.mn(tinv1.pins['ENB'])[0])
   mn_list.append(r34.mn(tinv_small0.pins['ENB'])[0])
   mn_list.append(r34.mn(tinv_small1.pins['EN'])[0])
   dsn.route_via_track(grid=r34, mn=mn_list, track=_track)
   
   # 1st M2
   mn_list=[]
   mn_list.append(r23.mn(inv2.pins['O'])[0])
   mn_list.append(r23.mn(tinv_small0.pins['I'])[0])
   mn_list.append(r23.mn(tinv1.pins['I'])[0])
   _track = [None, (r23.mn(tinv_small0.pins['I'])[0,1]+r23.mn(tinv_small0.pins['I'])[1,1])/2]
   dsn.route_via_track(grid=r23, mn=mn_list, track=_track)
   # 2nd M2
   mn_list=[]
   mn_list.append(r34.mn(inv2.pins['I'])[0])
   mn_list.append(r34.mn(tinv0.pins['O'])[0])
   mn_list.append(r34.mn(tinv_small0.pins['O'])[0])
   _track = [None, r23.mn(tinv0.pins['O'])[0,1]]
   dsn.route_via_track(grid=r23, mn=mn_list, track=_track)
   # 3rd M2
   mn_list=[]
   mn_list.append(r34.mn(inv3.pins['I'])[0])
   mn_list.append(r34.mn(tinv1.pins['O'])[0])
   mn_list.append(r34.mn(tinv_small1.pins['O'])[0])
   _track = [None, r23.mn(tinv1.pins['O'])[0,1]]
   dsn.route_via_track(grid=r23, mn=mn_list, track=_track)
   # 4th M2
   mn_list=[]
   mn_list.append(r34.mn(inv3.pins['O'])[0])
   mn_list.append(r34.mn(tinv_small1.pins['I'])[0]) 
   _track = [None, r23.mn(inv3.pins['O'])[0,1]]
   dsn.route_via_track(grid=r23, mn=mn_list, track=_track)
  
   # VSS
   rvss0 = dsn.route(grid=r12, mn=[r12.mn.bottom_left(inv0), r12.mn.bottom_right(inv3)])
   
   # VDD
   rvdd0 = dsn.route(grid=r12, mn=[r12.mn.top_left(inv0), r12.mn.top_right(inv3)])
   
   # 6. Create pins.
   pin0 = dsn.pin(name='I', grid=r23, mn=r23.mn.bbox(tinv0.pins['I']))
   pclk0 = dsn.pin(name='CLK', grid=r23, mn=r23.mn.bbox(inv0.pins['I']))
   pout0 = dsn.pin(name='O', grid=r23, mn=r23.mn.bbox(inv3.pins['O']))
   pvss0 = dsn.pin(name='VSS', grid=r12, mn=r12.mn.bbox(rvss0))
   pvdd0 = dsn.pin(name='VDD', grid=r12, mn=r12.mn.bbox(rvdd0))
   
   # 7. Export to physical database.
   print("Export design")
   
   # Uncomment for BAG export
   laygo2.interface.magic.export(lib, filename=ref_dir_MAG_exported +libname+'_'+cellname+'.tcl', cellname=None, libpath=ref_dir_layout, scale=0.1, reset_library=False, tech_library=tech.name)
   
   # 8. Export to a template database file.
   nat_temp = dsn.export_to_template()
   laygo2.interface.yaml.export_template(nat_temp, filename=ref_dir_template+libname+'_templates.yaml', mode='append')
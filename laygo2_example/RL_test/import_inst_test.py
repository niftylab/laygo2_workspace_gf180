##########################################
#                                        #
#       Inverter Layout Gernerator       #
#        Created by Hyungjoo Park        #
#                                        #
##########################################

import numpy as np
import pprint
import laygo2
import laygo2.interface
import laygo2_tech as tech
import laygo2_example.RL_test.inv as t_inv
from laygo2_example.RL_test.nodemap import node_map as nmap
import matplotlib.pyplot as plt
import matplotlib.patches as pth
# Parameter definitions #############
# Variables
# Templates
tpmos_name = 'pmos'
tnmos_name = 'nmos'
# Grids
pg_name = 'placement_basic'
r12_name = 'routing_12_cmos'
r23_name = 'routing_23_cmos'
# Design hierarchy
libname = 'RL_test'
# cellname in for loop
ref_dir_template = './laygo2_example/logic/' #export this layout's information into the yaml in this dir 
ref_dir_MAG_exported = './laygo2_example/RL_test/TCL/'
ref_dir_layout = './magic_layout'
# End of parameter definitions ######

# Generation start ##################
# 1. Load templates and grids.
print("Load templates")
templates = tech.load_templates()
# temp_inv = inv.import_templates('inv_2x')
# temp_inv_hs = inv.import_templates('inv_hs_2x')
temp_inv = t_inv.import_templates()
print("Load grids")
grids = tech.load_grids(templates=templates)
pg, r12, r23 = grids[pg_name], grids[r12_name], grids[r23_name]
lib = laygo2.object.database.Library(name=libname)
cellname = 'inv_flat'
print('--------------------')
print('Now Creating '+cellname)

# 2. Create a design hierarchy
dsn = laygo2.object.database.Design(name=cellname, libname=libname)
lib.append(dsn)

# 3. Create instances.
print("Create instances")
inv0 = temp_inv.generate(name='INV0', params={'nf': 4})
inv1 = temp_inv.generate(name='INV1', transform='MX', params={'nf': 2})
inv2 = temp_inv.generate(name='INV2', params={'nf': 2})
#inv_hs0 = temp_inv_hs.generate(name='INV_HS0')
# 4. Place instances.
dsn.place(grid=pg, inst=inv0, mn=[0,0])
dsn.place(grid=pg, inst=inv1, mn=pg.mn.bottom_right(inv0))
dsn.place(grid=pg, inst=inv2, mn=pg.mn.bottom_right(inv1))
# 5. Create and place wires.
print("Create wires")
_mn = [r23.mn(inv0.pins['O'])[0], r23.mn(inv1.pins['I'])[0]]
_track = [None, r23.mn(inv0.pins['O'])[0,1]+2]
rint0 = dsn.route_via_track(grid=r23, mn=_mn, track=_track)

_mn = [r23.mn(inv1.pins['O'])[0], r23.mn(inv2.pins['I'])[0]]
_track = [None, r23.mn(inv1.pins['O'])[0,1]]
rint1 = dsn.route_via_track(grid=r23, mn=_mn, track=_track)

# # Get all the metal wire informations (node & edge infos)
# route_table = {1:r12, 2:r23, 3:r23}
# route_map = nmap(route_table)
# #route_map = map_temp(route_table)
# for elem in dsn.elements.values():
#    if elem.__class__ == laygo2.object.physical.Rect or elem.name == None:
#       route_map.get_map(elem)
#       #get_map(self, obj, prefix='', offset_master=[0,0], transform_master=np.array([[1,0],[0,1]])):
#    #print(elem.name)
#    else:
#       route_map.get_map(elem, prefix=elem.name+'_')
# del route_map.pin.nets[0]
# del route_map.metal.nets[0]
# np.delete(route_map.metal.nodes, 0)
# np.delete(route_map.metal.edges, 0)

# fig = plt.figure()
# pypobjs = []
# ax = fig.add_subplot(111)
# colormap = {    
#    1: ["c", "c", 0.5],
#    2: ["y", "y", 0.5],
#    3: ["g", "g", 0.5],
#    4: ["m", "m", 0.5]
# }
# for rect in route_map.metal.nets:
#    xy1 = rect[0][0]
#    xy2 = rect[0][1]
#    _rect = pth.Rectangle(
#       xy1, xy2[0]-xy1[0], xy2[1]-xy1[1],
#       facecolor=colormap[rect[1]][1],
#       edgecolor=colormap[rect[1]][0],
#       alpha=colormap[rect[1]][2],
#       lw=6,
#    )
#    ax.add_patch(_rect)
# for pin in route_map.pin.nets:
#    xy1 = pin[0][0]
#    xy2 = pin[0][1]
#    _rect = pth.Rectangle(
#       xy1, xy2[0]-xy1[0], xy2[1]-xy1[1],
#       facecolor=colormap[pin[1]][1],
#       edgecolor=colormap[pin[1]][0],
#       alpha=colormap[pin[1]][2],
#       lw=4,
#    )
#    ax.add_patch(_rect)   
# plt.autoscale()
# plt.show()



if __name__ == "__main__":
# 7. Export to physical database.
   print("Export design")
   print("")
# 8. Export to a template database file.
   for dsn_name, dsn in lib.items():
      nat_temp = dsn.export_to_template()
      laygo2.interface.yaml.export_template(nat_temp, filename=ref_dir_template+libname+'_templates.yaml', mode='append')
# Uncomment for BAG export
   laygo2.interface.magic.export(lib, filename=ref_dir_MAG_exported +libname+'_'+cellname+'.tcl', cellname=None, libpath=ref_dir_layout, scale=0.1, reset_library=False, tech_library=tech.name)

import numpy as np
import pprint
import laygo2
import laygo2.interface
import laygo2_tech as tech

class node_map:
    table_transform = my_dict = {
        'R0': np.array([[1,0],[0,1]]),
        'MX': np.array([[1,0],[0,-1]]),
        'MY': np.array([[-1,0],[0,1]]),
        'R90': np.array([[-1,0],[0,-1]])
    }
    class _pin:
        def __init__(self) -> None:
            self.nets = [[[None, None],None,None]]
    class _metal:
        def __init__(self) -> None:
            self.nets = [[[None, None],None,None]]
            self.nodes = np.array([[None, None, None]])
            self.edges = np.array([[None, None, None]])

    def __init__(self, table_grid):
        self.table_grid = table_grid
        self.metal = node_map._metal()
        self.pin = node_map._pin()

# netmap 함수
    def get_map(self, obj, prefix='', offset_master=[0,0], transform_master=np.array([[1,0],[0,1]])):
        # case1: Virtual Instances
        if obj.__class__ == laygo2.object.physical.VirtualInstance:
            # 1. pins -> obj의 xy(offset)와 transform이 자체적으로 bbox에 반영됨
            # pin 정보는 metal과 분리해서 따로 pin 객체에 저장해둠
            for pin_name, pin in obj.pins.items():
                layer_num  = int(pin.layer[0][-1])
                print(prefix+pin_name)
                print("offset: ",self.table_grid[layer_num].phy2abs(offset_master))
                print("tr_master: ",[transform_master[0], transform_master[1]])
                print('pin origin: ',[ pin.bbox[0], pin.bbox[1] ])
                _netname   = prefix + pin.netname
                _trans     = transform_master # virtual instance's master -> grand_parent to pin
                pin_mn = self.table_grid[layer_num].mn(pin)
                offset_mn = self.table_grid[layer_num].mn(offset_master)
                _bbox      = offset_mn + pin_mn.dot(_trans)
                point_ll   = np.array([min(_bbox[0][0],_bbox[1][0]),min(_bbox[0][1],_bbox[1][1])])
                point_ur   = np.array([max(_bbox[0][0],_bbox[1][0]),max(_bbox[0][1],_bbox[1][1])])
                print('pin_trans: ', [point_ll,point_ur])
                print('')
                self.pin.nets.append([np.vstack((point_ll,point_ur)),layer_num,_netname])
            # 2. Native elements -> obj의 xy(offset)와 transform이 bbox에 반영되지 않음 -> 보정하여 자식 node에 넘김
            for elem_name, elem in obj.native_elements.items():
                # print(prefix+elem_name)
                # print("tr_master: ",[transform_master[0], transform_master[1]])
                if elem.__class__ == laygo2.object.physical.Rect:
                    _prefix = prefix
                else:
                    #_trans = node_map.table_transform[obj.transform] # ex) table_transform['MX'] == np.array[[1,0],[0,-1]]
                    _prefix = prefix + elem_name+'_'
                _trans = node_map.table_transform[obj.transform] # ex) table_transform['MX'] == np.array[[1,0],[0,-1]]
                # print('tran_vinst: ',[_trans[0],_trans[1]],obj.transform)
                # print("tr_tot: ",[_trans.dot(transform_master)[0],_trans.dot(transform_master)[1]])
                # print('')
                self.get_map(elem, prefix=_prefix, offset_master=offset_master + obj.xy.dot(transform_master), transform_master=_trans.dot(transform_master))
        # case2: Instances
        elif obj.__class__ == laygo2.object.physical.Instance:
            # Virtual Instance의 pin과 사실상 같음
            # pin 정보는 metal과 분리해서 따로 pin 객체에 저장해둠
            for pin_name, pin in obj.pins.items():
                layer_num  = int(pin.layer[0][-1])
                _netname   = prefix + pin.netname
                _trans     = transform_master
                pin_mn = self.table_grid[layer_num].mn(pin)
                offset_mn = self.table_grid[layer_num].mn(offset_master)
                _bbox      = offset_mn + pin_mn.dot(_trans)
                point_ll   = np.array([min(_bbox[0][0],_bbox[1][0]),min(_bbox[0][1],_bbox[1][1])])
                point_ur   = np.array([max(_bbox[0][0],_bbox[1][0]),max(_bbox[0][1],_bbox[1][1])])
                self.pin.nets.append([np.vstack((point_ll,point_ur)),layer_num,_netname])
        # case3: Rects -> obj 자체가 rect이기 때문에 transform과 offset이 offset_master, transform_master에 이미 반영되어 있음
        elif obj.__class__ == laygo2.object.physical.Rect:
            layer_num  = int(obj.layer[0][-1])
            if obj.netname == None:
                _netname = None
            else:
                _netname = prefix + obj.netname
            _trans     = transform_master
            _bbox      = self.table_grid[layer_num].phy2abs(offset_master + obj.bbox.dot(_trans))
            point_ll   = np.array([min(_bbox[0][0],_bbox[1][0]),min(_bbox[0][1],_bbox[1][1])])
            point_ur   = np.array([max(_bbox[0][0],_bbox[1][0]),max(_bbox[0][1],_bbox[1][1])])
            # print('rect_origin: ', [self.table_grid[layer_num].phy2abs(obj.bbox)[0],
            #                         self.table_grid[layer_num].phy2abs(obj.bbox)[1]])
            # print('rect_trans: ', [point_ll,point_ur])
            # print('')
            self.metal.nets.append([np.vstack((point_ll,point_ur)),layer_num,_netname]) # 후에 사용할 수 있을 것 같아 구현해둠. 당장은 없어도 됨
            for i in range(point_ll[0], point_ur[0]+1):
                for j in range(point_ll[1], point_ur[1]+1):
                    self.metal.nodes = np.append(self.metal.nodes, np.array([[i,j,layer_num]]),axis=0)
                    if j != point_ur[1]:
                        self.metal.edges = np.append(self.metal.edges, np.array([[i,j+0.5,layer_num]]),axis=0)
                if i != point_ur[0]: 
                    self.metal.edges = np.append(self.metal.edges, np.array([[i+0.5,j,layer_num]]),axis=0)
        # error case
        else:
            print("error object type ",str(obj.__class__)," doesn't implemented") 
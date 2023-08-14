import numpy as np
import pprint
import laygo2
import laygo2.interface
import laygo2_tech as tech
# Parameter definitions #############

def export_templates(lib, celltype):

    def _update_params(params:dict):
        if params == None:
            params = {'nf': 1}
        elif 'nf' not in params:
            params['nf'] = 1
        return params
    
    def _generate(name=None, shape=None, pitch=np.array([0, 0]),
    transform="R0", params:dict=None, netname:dict=None):
        params = _update_params(params)
        _cellname = celltype + '_'+str(params['nf'])+'x'
        dsn = lib[_cellname]
        inst_pins:dict = dsn.pins
        inst_native_elements = dict()
        for elname, element in dsn.elements.items():
            if not element.__class__ == laygo2.object.Pin:
                inst_native_elements[elname] = element
        # inst_native_elements:dict = dsn.elements
        # for pin in dsn.pins.keys():
        #     inst_native_elements.pop(pin,None)
        inst = laygo2.object.physical.VirtualInstance(
            name=name,
            libname=dsn.libname,
            cellname=dsn.cellname,
            xy=np.array([0, 0]),
            native_elements=inst_native_elements,
            shape=shape,
            pitch=pitch,
            unit_size= _bbox(params)[1],
            pins=inst_pins,
            transform=transform,
        )
        return inst
    
    def _bbox(params):
        params = _update_params(params)
        _cellname = celltype + '_'+str(params['nf'])+'x'
        dsn = lib[_cellname]
        params = _update_params(params)

        return dsn.bbox
    def _pins(params) -> dict:
        params = _update_params(params)
        _cellname = celltype + '_'+str(params['nf'])+'x'
        dsn = lib[_cellname]
        return dsn.pins
    """
    export a pre-designed template as an Userdefined template
    for more sophisticated reusing
    """

    mytemp = laygo2.object.UserDefinedTemplate(
        name = celltype,
        bbox_func = _bbox,
        pins_func = _pins,
        generate_func = _generate,
    )
    return mytemp
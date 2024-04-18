# -*- coding: utf-8 -*-
"""

"""
import h5py
from numpy import array, dtype
from pyfem.assembly.Assembly import Assembly


def write_hdf5(hdf5_data, assembly: Assembly) -> None:
    """
        将计算结果过写入hdf5文件。
        """
    props = assembly.props
    timer = assembly.timer
    dimension = props.mesh_data.dimension

    hdf5_data['node_coords'] = props.mesh_data.nodes
    hdf5_data['elements_connectivity'] = props.mesh_data.elements
    hdf5_data['node_sets'] = props.mesh_data.node_sets
    hdf5_data['elements_sets'] = props.mesh_data.element_sets

    # hdf5_data['time'].append(timer.time0)
    # hdf5_data['increment'].append(timer.increment)
    hdf5_data['time'] = timer.time0
    hdf5_data['increment'] = timer.increment

    # 判断自由度属于什么（props.dof.name->assembly.dof_solution),问题：dof_solution是一维list，以节点的自由度值依次排下去，所以下面这段代码有问题。
    # print(assembly.dof_solution)
    # print(len(props.mesh_data.nodes))
    # print(len(props.dof.names))
    Displacement = []
    for node_number in range(len(props.mesh_data.nodes)):
        for dof_number in range(len(props.dof.names)):
            if int(dof_number) <= dimension:
                Displacement.append(assembly.dof_solution[node_number * len(props.dof.names) + dof_number])
            else:
                hdf5_data[props.dof.names[int(dof_number)]].append(assembly.dof_solution[node_number * len(props.dof.names) + dof_number])
    hdf5_data['FeildOutputs']['Displacement'].append(Displacement)

    # for dof_name in props.dof.names:
    #     if dof_name in ['u1','u2','u3']:
    #         dof_solution = []
    #         dof_solution.append(assembly.dof_solution)
    #         hdf5_data['Displacement'].append(dof_solution)
    #     else:
    #         dof_solution = []
    #         dof_solution.append(assembly.dof_solution)
    #         hdf5_data[dof_name].append(dof_solution)

    for field_name, field_values in assembly.field_variables.items():
        field = []
        field.append(assembly.field_variables[field_name])
        hdf5_data['FeildOutputs'][field_name].append(field)


def initiation(hdf5_data, assembly: Assembly) -> None:
    hdf5_data['time'] = []
    hdf5_data['increment'] = []
    hdf5_data['FeildOutputs'] = {}
    hdf5_data['FeildOutputs']['Displacement'] = []
    for dof_name in assembly.props.dof.names:
        hdf5_data[dof_name] = []
    for field_name, field_values in assembly.field_variables.items():
        hdf5_data['FeildOutputs'][field_name] = []


def list_to_array(hdf5_data):
    for key in hdf5_data:
        hdf5_data[key] = array(hdf5_data[key])
    return hdf5_data


def create_hdf5(hdf5_data, assembly: Assembly) -> None:  # 现在的save是将所有帧一整个save，如果过大会占用很大内存；改成每一帧打开这个hdf文件，往里存一帧的数据。
    props = assembly.props
    timer = assembly.timer

    job_name = props.input_file.stem

    output_file = props.work_path.joinpath(f'{job_name}.hdf5')

    file = h5py.File(output_file, 'w')
    frame = file.create_group(f'Frame-{timer.increment}')
    FeildOutputs_group = frame.create_group('FeildOutputs')
    time_group = frame.create_group('time')
    time_dataset = time_group.create_dataset('time', data=timer.time0)
    increment_group = frame.create_group('increment')
    increment_dataset = increment_group.create_dataset('increment', data=timer.increment)
    element_information = file.create_group('element_information')
    elements_connectivity = element_information.create_group('elements_connectivity')
    elements_connectivity_dataset = elements_connectivity.create_dataset('elements_connectivity', data=props.mesh_data.elements)
    node_coords = element_information.create_group('node_coords')
    node_coords_dataset = node_coords.create_dataset('node_coords', data=props.mesh_data.nodes)
    # print(hdf5_data['FeildOutputs'])
    for key, value in hdf5_data['FeildOutputs'].items():
        variable = FeildOutputs_group.create_group(key)
        dataset = variable.create_dataset(key, data=value)
    file.close()


def add_hdf5(hdf5_data, assembly: Assembly) -> None:
    props = assembly.props
    timer = assembly.timer

    job_name = props.input_file.stem
    output_file = props.work_path.joinpath(f'{job_name}.hdf5')
    file = h5py.File(output_file, 'a')

    frame = file.create_group(f'Frame-{timer.increment}')
    FeildOutputs_group = frame.create_group('FeildOutputs')
    time_group = frame.create_group('time')
    time_dataset = time_group.create_dataset('time', data=timer.time0)
    increment_group = frame.create_group('increment')
    increment_dataset = increment_group.create_dataset('increment', data=timer.increment)

    # print(increment)
    for key, value in hdf5_data['FeildOutputs'].items():
        variable = FeildOutputs_group.create_group(key)
        #     # print(variable)
        dataset = variable.create_dataset(key, data=value)
    #     print(dataset)
    file.close()


if __name__ == "__main__":
    pass

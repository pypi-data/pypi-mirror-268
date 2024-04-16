try:
    from sage_lib.DFTSingleRun import DFTSingleRun
except ImportError as e:
    import sys
    sys.stderr.write(f"An error occurred while importing DFTSingleRun: {str(e)}\n")
    del sys

try:
    from sage_lib.FileManager import FileManager
except ImportError as e:
    import sys
    sys.stderr.write(f"An error occurred while importing FileManager: {str(e)}\n")
    del sys

try:
    from sage_lib.CrystalDefectGenerator import CrystalDefectGenerator
except ImportError as e:
    import sys
    sys.stderr.write(f"An error occurred while importing CrystalDefectGenerator: {str(e)}\n")
    del sys

try:
    from sage_lib.BandPathGenerator import BandPathGenerator
except ImportError as e:
    import sys
    sys.stderr.write(f"An error occurred while importing BandPathGenerator: {str(e)}\n")
    del sys

try:
    from sage_lib.AtomPositionManager import AtomPositionManager
except ImportError as e:
    import sys
    sys.stderr.write(f"An error occurred while importing AtomPositionManager: {str(e)}\n")
    del sys

try:
    from sage_lib.PeriodicSystem import PeriodicSystem
except ImportError as e:
    import sys
    sys.stderr.write(f"An error occurred while importing PeriodicSystem: {str(e)}\n")
    del sys

try:
    import numpy as np
except ImportError as e:
    import sys
    sys.stderr.write(f"An error occurred while importing numpy: {str(e)}\n")
    del sys

try:
    import os 
except ImportError as e:
    import sys
    sys.stderr.write(f"An error occurred while importing os: {str(e)}\n")
    del sys

try:
    import copy
except ImportError as e:
    import sys
    sys.stderr.write(f"An error occurred while importing copy: {str(e)}\n")
    del sys

try:
    import re
except ImportError as e:
    import sys
    sys.stderr.write(f"An error occurred while importing re: {str(e)}\n")
    del sys

class DFTPartition(FileManager): # el nombre no deberia incluir la palabra DFT tieneu qe ser ma general
    """
    A class for partitioning and managing data files for simulations.

    This class extends FileManager and provides functionalities for handling 
    different types of simulation data, applying operations to it, and organizing the results.

    Attributes:
        file_location (str): The file path where the data files are located.
        containers (list): A list of containers to hold various data structures.
    """
    def __init__(self, file_location:str=None, name:str=None, **kwargs):
        """
        Initialize the DataPartition instance.

        Parameters:
            file_location (str, optional): Location of the files to be managed.
            name (str, optional): Name of the partition.
            **kwargs: Additional keyword arguments.
        """
        super().__init__(name=name, file_location=file_location)
        self._containers = []

    def add_container(self, container: object):
        """
        Add a new container to the list of containers.

        Parameters:
            container (object): The container object to be added.
        """
        self.containers.append(container)

    def remove_container(self, container: object):
        """
        Remove a container from the list of containers.

        Parameters:
            container (object): The container object to be removed.
        """
        self.containers.remove(container)

    def empty_container(self):
        """
        Empty the list of containers.
        """
        self.containers = []

    def filter_conteiners(self, filter_class:str, value:float) -> bool:
        mask = np.ones_like(containers)
        for container_index, container in enumerate(self.containers):
            if filter_class.lower() == 'fmax':
                if np.any(container.AtomPositionManager.atomPositions > value):
                    mask[container_index] = 0

        self.containers = self.containers[mask]
        return True 

    def readConfigSetup(self, file_location:str=None, source='VASP', v=False):
        file_location = file_location if type(file_location) == str else self.file_location
        
        DFT_SR = self.readVASPFolder(file_location=file_location, add_container=False, v=v)
        DFT_SR.InputFileManager.set_LDAU( DFT_SR.AtomPositionManager.uniqueAtomLabels )

        for c_i, container in enumerate(self.containers):
            container.InputFileManager = DFT_SR.InputFileManager
            container.KPointsManager = DFT_SR.KPointsManager
            container.PotentialManager = DFT_SR.PotentialManager
            container.BashScriptManager = DFT_SR.BashScriptManager
            container.vdw_kernel_Handler = DFT_SR.vdw_kernel_Handler
            container.WaveFileManager = DFT_SR.WaveFileManager
            container.ChargeFileManager = DFT_SR.ChargeFileManager

    def readVASPSubFolder(self, file_location:str=None, v=False):
        file_location = file_location if type(file_location) == str else self.file_location
                
        for root, dirs, files in os.walk(file_location):
            DFT_SR = self.readVASPFolder(file_location=root, add_container=True, v=v)
            if v: print(root, dirs, files)

    def readVASPFolder(self, file_location:str=None, add_container:bool=True, v=False):
        file_location = file_location if type(file_location) == str else self.file_location

        DFT_SR = DFTSingleRun(file_location)
        DFT_SR.readVASPDirectory()        
        if add_container and DFT_SR.AtomPositionManager is not None: 
            self.add_container(container=DFT_SR)

        return DFT_SR

    def NonPeriodic_2_Periodic(self, latticeVectors:np.array):
        for container in self.containers:
            container.NonPeriodic_2_Periodic(latticeVectors)

    def exportVaspPartition(self, file_location:str=None, label:str='fixed'): 
        for c_i, container in enumerate(self.containers):

            if label == 'enumerate':
                container.exportVASP(file_location=file_location+f'/{c_i:03d}')
            if label == 'fixed':
                container.exportVASP(file_location=file_location)

    def read_configXYZ(self, file_location:str=None, verbose:bool=False):
        file_location = file_location if type(file_location) == str else self.file_location

        lines =list(self.read_file(file_location,strip=False))
        container = []

        for i, line in enumerate(lines):
            print(i, line)
            if line.strip().isdigit():
                num_atoms = int(line.strip())
                if num_atoms > 0:
                    DFT_SR = DFTSingleRun(file_location)
                    DFT_SR.AtomPositionManager = PeriodicSystem()
                    DFT_SR.AtomPositionManager.read_configXYZ(lines=lines[i:i+num_atoms+2])

                    container.append(DFT_SR)

        self._containers += container
        return container

    def export_configXYZ(self, file_location:str=None, verbose:bool=False):
        file_location  = file_location if file_location else self.file_location+'_config.xyz'
        with open(file_location, 'w'):pass # Create an empty file
        for container_index, container in enumerate(self.containers):
            if container.OutFileManager is not None:    
                container.OutFileManager.export_configXYZ(file_location=file_location, save_to_file='a', verbose=False)

        if verbose:
            print(f"XYZ content has been saved to {file_location}")

        return True

    def summary(self, ) -> str:
        text_str = ''
        text_str += f'{self.file_location}\n'
        text_str += f'> Conteiners : { len(self.containers) }\n'
        return text_str
    
    def generateDFTVariants(self, parameter: str, values:np.array=None, file_location: str = None) -> bool:
        containers = []
        directories = ['' for _ in self.containers]
        parameter = parameter.upper().strip()
        for container_index, container in enumerate(self.containers):
            if parameter.upper() == 'KPOINTS':
                containers += self.handleKPoints(container, values, container_index,  file_location) 
                directories[container_index] = 'KPOINTConvergence'

            elif container.InputFileManager and parameter.upper() in container.InputFileManager.parameters_data:
                containers += self.handleInputFile(container, values, parameter,  container_index, file_location)
                directories[container_index] = f'{parameter}_analysis'

            elif parameter.upper() == 'VACANCY':
                containers += self.handleVacancy(container, values, container_index, file_location)
                directories[container_index] = 'Vacancy'

            elif parameter.upper() == 'BAND_STRUCTURE':
                containers += self.handleBandStruture(container, values, container_index, file_location)
                directories[container_index] = 'band_structure'

            elif parameter.upper() == 'RATTLE':
                containers += self.handleRattle(container, values, container_index, file_location)
                directories[container_index] = 'rattle'

        self.containers = containers
        self.generate_master_script_for_all_containers(directories, file_location if not file_location is None else container.file_location )

    def handleBandStruture(self, container, values, container_index, file_location=None):
        sub_directories, containers = [], []

        for v in values:
            points, special_points = v.get('points', 20), v.get('special_points', None)
            container_copy = self.copy_and_update_container(container, f'/band_structure/{special_points}_{points}', file_location)

            if special_points==None:
                PG = BandPathGenerator(Periodic_Object=container_copy.AtomPositionManager)
                special_points = PG.high_symmetry_points_path

            container_copy.KPointsManager.set_band_path(special_points, points)
            container_copy.InputFileManager.parameters['ISMEAR'] = -5     # ISMEAR = -5 (Método de ensanchamiento de Fermi para cálculos de bandas)
            container_copy.InputFileManager.parameters['SIGMA'] =  0.05   # SIGMA = 0.05 (Valor más pequeño debido al método de ensanchamiento)
            container_copy.InputFileManager.parameters['IBRION'] = -1     # IBRION = -1 (No relajación de iones, cálculos estáticos)
            container_copy.InputFileManager.parameters['NSW'] =  0        # NSW = 0 (Sin optimización de geometría)
            container_copy.InputFileManager.parameters['LORBIT'] =  11    # LORBIT = 11 (Si se desea calcular y escribir los caracteres de las bandas)
            container_copy.InputFileManager.parameters['ICHARG'] =  11    # ICHARG = 11 (Usa la densidad de carga de un cálculo previo y no actualiza la densidad de carga durante el cálculo)
            container_copy.InputFileManager.parameters['ISIF'] =  2       # ISIF = 2 (Mantiene fija la celda durante el cálculo)
            sub_directories.append(f'/{special_points}_{points}')
            containers.append(container_copy)

        self.generate_execution_script_for_each_container(sub_directories, container.file_location + '/band_structure')
        return containers

    def handleKPoints(self, container, values, container_index,  file_location=None):
        sub_directories, containers = [], []

        for v in values:
            container_copy = self.copy_and_update_container(container, f'/KPOINTConvergence/{v[0]}_{v[1]}_{v[2]}', file_location)
            container_copy.KPointsManager.subdivisions = [v[0], v[1], v[2]]
            sub_directories.append(f'{v[0]}_{v[1]}_{v[2]}')
            containers.append(container_copy)

        self.generate_execution_script_for_each_container(sub_directories, container.file_location + '/KPOINTConvergence')
        return containers

    def handleInputFile(self, container, parameter, values, container_index, file_location=None):
        sub_directories, containers = [], []

        for v in values:
            container_copy = self.copy_and_update_container(container, f'/{parameter}_analysis/{v}', file_location)
            container_copy.InputFileManager.parameters[parameter.upper()] = ' '.join(v) if v is list else v 
            sub_directories.append('_'.join(map(str, v)) if isinstance(v, list) else str(v))
            containers.append(container_copy)

        self.generate_execution_script_for_each_container(sub_directories, container.file_location + f'/{parameter}_analysis')
        return containers

    def handleVacancy(self, container, values, container_index, file_location=None):
        sub_directories, containers = [], []

        container_copy = self.copy_and_update_container(container, '/Vacancy', file_location)
        container_copy.AtomPositionManager = CrystalDefectGenerator(Periodic_Object=container_copy.AtomPositionManager)
        all_vacancy_configs, all_vacancy_label = container_copy.AtomPositionManager.generate_all_vacancies()

        for cv_i, (vacancy_configs, vacancy_label) in enumerate(zip(all_vacancy_configs, all_vacancy_label)):
            container_copy2 = copy.deepcopy(container_copy)
            container_copy2.AtomPositionManager = vacancy_configs
            container_copy2.file_location = f'{container_copy.file_location}/{cv_i}_{vacancy_label}'
            sub_directories.append(f'{cv_i}_{vacancy_label}')
            containers.append(container_copy2)
        
        self.generate_execution_script_for_each_container(sub_directories, container.file_location + '/Vacancy')
        return containers

    def handleRattle(self, container, values, container_index, file_location=None):
        sub_directories, containers = [], []

        for v in values: 
            for n in range(v['N']):
                for std in v['std']:
                    container_copy = self.copy_and_update_container(container, f'/rattle/{std}/{n}', file_location)
                    container_copy.AtomPositionManager.rattle(stdev=std, seed=n)
                    
                    sub_directories.append(f'{std}/{n}')
                    containers.append(container_copy)
        
        self.generate_execution_script_for_each_container(sub_directories, container.file_location + '/rattle')
        return containers

    def copy_and_update_container(self, container, sub_directory: str, file_location=None):
        copy.deepcopy(container._atomic_mass)
        container_copy = copy.deepcopy(container)
        container_copy.file_location = f'{container.file_location}{sub_directory}' if file_location is None else file_location
        return container_copy

    def generate_execution_script_for_each_container(self, directories: list = None, file_location: str = None):
        self.create_directories_for_path(file_location)
        script_content = self.generate_script_content('RUNscript.sh', directories)
        self.write_script_to_file(script_content, f"{file_location}/execution_script_for_each_container.py")


    def generate_master_script_for_all_containers(self, directories: list = None, file_location: str = None):
        self.create_directories_for_path(file_location)
        script_content = self.generate_script_content('execution_script_for_each_container.py', directories)
        self.write_script_to_file(script_content, f"{file_location}/master_script_for_all_containers.py")


    def generate_script_content(self, script_name: str, directories: list = None) -> str:
        directories_str = "\n".join([f"    '{directory}'," for directory in directories])
        return f'''#!/usr/bin/env python3
import os
import subprocess

original_directory = os.getcwd()

directories = [
{directories_str}
]

for directory in directories:
    os.chdir(directory)
    subprocess.run(['chmod', '+x', '{script_name}'])
    subprocess.run(['sbatch', '{script_name}'])
    os.chdir(original_directory)
'''

    def write_script_to_file(self, script_content: str, file_path: str):
        with open(file_path, "w") as f:
            f.write(script_content)



'''
path = '/home/akaris/Documents/code/Physics/VASP/v6.1/files/dataset/CoFeNiOOH_jingzhu/bulk_NiFe/rattle'
DP = DFTPartition(path)
DP.readVASPFolder(v=False)
DP.generateDFTVariants('rattle', [ {'N':20, 'std':[0.1, 0.2]} ] )
DP.exportVaspPartition()

print(DP.containers[0].AtomPositionManager.pbc)
DP.generateDFTVariants('band_structure', values=[{'points':20, 'special_points':'GMLCXG'}])
DP.exportVaspPartition()


path = '/home/akaris/Documents/code/Physics/VASP/v6.1/files/POSCAR/Cristals/test/files'
DP = DFTPartition(path)
DP.readVASPSubFolder(v=False)
DP.readConfigSetup('/home/akaris/Documents/code/Physics/VASP/v6.1/files/POSCAR/Cristals/test/config')
DP.generate_execution_script_for_each_container([ f'{n:03d}'for n, c in enumerate(DP.containers) ], '/home/akaris/Documents/code/Physics/VASP/v6.1/files/POSCAR/Cristals/test/calcs')

#DP.read_configXYZ()

'''




'''
DP.export_configXYZ()

path = '/home/akaris/Documents/code/Physics/VASP/v6.1/files/dataset/CoFeNiOOH_jingzhu/surf_CoFe_4H_4OH/MAG'

DP = DFTPartition(path)

DP.readVASPFolder(v=True)

DP.generateDFTVariants('Vacancy', [1], is_surface=True)
#DP.generateDFTVariants('KPOINTS', [[n,n,1] for n in range(1, 15)] ) 


path = '/home/akaris/Documents/code/Physics/VASP/v6.1/files/dataset/CoFeNiOOH_jingzhu/surf_CoFe_4H_4OH/MAG'
DP = DFTPartition(path)
DP.readVASPFolder(v=True)
DP.generateDFTVariants('NUPDOWN', [n for n in range(0, 10, 1)] )
DP.writePartition()

path = '/home/akaris/DocumeEENnts/code/Physics/VASP/v6.1/files/POSCAR/Cristals/NiOOH/*OH surface with Fe(HS)'
path = '/home/akaris/Documents/code/Physics/VASP/v6.1/files/POSCAR/Cristals/NiOOH/*OH surface for pure NiOOH'
#DP = DFTPartition('/home/akaris/Documents/code/Physics/VASP/v6.1/files/bulk_optimization/Pt/parametros/ENCUT_optimization_252525_FCC')
DP = DFTPartition(path)
#DP.readVASPSubFolder(v=True)
DP.readVASPFolder(v=True)

#DP.generateDFTVariants('Vacancy', [1], is_surface=True)
#DP.generateDFTVariants('KPOINTS', [[n,n,1] for n in range(1, 15)] )    
DP.generateDFTVariants('ENCUT', [n for n in range(200, 1100, 45)] )

DP.writePartition()

DP.generateDFTVariants('ENCUT', [ E for E in range(400,700,30)] )
print( DP.summary() )

print( DP.containers[0].AtomPositionManager.summary() )
'''


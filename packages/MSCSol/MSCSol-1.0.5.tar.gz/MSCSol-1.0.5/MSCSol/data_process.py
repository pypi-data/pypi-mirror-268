from rdkit import Chem
from rdkit import DataStructs
from rdkit.Chem import AllChem
from rdkit.Chem import Descriptors
from rdkit import Chem
from rdkit.Chem import QED, Descriptors, rdMolDescriptors, QED
from rdkit.Chem import Lipinski
import numpy as np
import pandas as pd
import pandas as pd
from rdkit.Chem import MACCSkeys
import warnings
from sklearn.decomposition import PCA
warnings.filterwarnings('ignore')
from rdkit.Chem import Draw
import math,re,os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import cv2 as cv
import os
import pandas as pd
import os
current_path = os.path.dirname(os.path.abspath(__file__))

#number of points per atom
number_points=1000
#vdw radii
radiiDict={'H': 1.2, 'He': 1.4, 'Li': 2.2, 'Be': 1.9, 'B': 2, 'C': 1.7, 'N': 1.55, 'O': 1.52, 'F': 1.47, 'Ne': 1.5,
  'Na': 2.4, 'Mg': 2.2, 'Al': 2.1, 'Si': 2.1, 'P': 1.8, 'S': 1.8, 'Cl': 1.75, 'Ar': 1.9, 'K': 2.8, 'Ca': 2.4,
    'Se': 1.9, 'Ti': 2.15, 'V': 2.05, 'Cr': 2.05, 'Mn': 2.05, 'Fe': 2.05, 'Co': 2.0, 'Ni': 2.0, 'Cu': 2.0, 'Zn': 2.1,
      'Ga': 2.1, 'Ge': 2.1, 'As': 2.05, 'Br': 1.85, 'Kr': 2.0, 'Rb': 2.9, 'Sr': 2.55, 'Y': 2.4, 'Zr': 2.3, 'Nb': 2.15,
        'Mo': 2.1, 'Tc': 2.05, 'Ru': 2.05, 'Rh': 2.0, 'Pd': 2.05, 'Ag': 2.1, 'Cd': 2.2, 'In': 2.2, 'Sn': 2.25, 'Sb': 2.2,
          'Te': 2.1, 'I': 1.98, 'Xe': 2.2, 'Cs': 3.0, 'Ba': 2.7, 'La': 2.5, 'Ce': 2.54, 'Pr': 2.56, 'Nd': 2.51, 'Pm': 2.54,
            'Sm': 2.5, 'Eu': 2.64, 'Gd': 2.54, 'Tb': 2.46, 'Dy': 2.49, 'Ho': 2.42, 'Er': 2.51, 'Tm': 2.47, 'Yb': 2.6,
              'Lu': 2.43, 'Hf': 2.3, 'Ta': 2.27, 'W': 2.2, 'Re': 2.2, 'Os': 2.17, 'Ir': 2.13, 'Pt': 2.07, 'Au': 2.07,
                'Hg': 2.07, 'Tl': 2.26, 'Pb': 2.21, 'Bi': 2.31, 'Po': 2.44, 'At': 2.44, 'Rn': 2.43, 'Fr': 3.1, 'Ra': 2.85,
                  'Ac': 2.84, 'Th': 2.56, 'Pa': 2.54, 'U': 2.41, 'Np': 2.36, 'Pu': 2.54, 'Am': 2.56, 'Cm': 2.56, 'Bk': 2.56,
                    'Cf': 2.56, 'Es': 2.56, 'Fm': 2.56}

## areas && asp_ratios
def get_points(data,atom_names):
    atom_radii=[]
    atom_pos=data
    #convert coordinates to floats
    atom_pos = [[float(j) for j in i] for i in atom_pos]
    #get the corresponding radius for each atom
    for f in range(len(atom_names)):
        atom_radii.append(radiiDict[atom_names[f]])
    #define new list
    data=[]
    #for each atom
    for f in range(len(atom_names)):
        #Produce random points in a cube
        x=((2*atom_radii[f])*np.random.rand(number_points,3))-atom_radii[f]
        #Keep points inside the sphere
        keep=[]
        for point in x:
            if math.sqrt(((point[0])**2)+((point[1])**2)+((point[2])**2)) < atom_radii[f]:
                keep.append(point)
        keep=np.array(keep)
        #Project points to surface of sphere
        x1=[]
        y1=[]
        z1=[]
        for point in keep:
            d=math.sqrt(((point[0])**2)+((point[1])**2)+((point[2])**2))
            scale=(atom_radii[f]-d)/d
            point=point+(scale*point)
            x1.append(point[0])
            y1.append(point[1])
            z1.append(point[2])
        #Move atom to correct position
        for i in range(len(x1)):
            x1[i]=x1[i]+atom_pos[f][0]
        for i in range(len(y1)):
            y1[i]=y1[i]+atom_pos[f][1]
        for i in range(len(z1)):
            z1[i]=z1[i]+atom_pos[f][2]
        data.append(x1)
        data.append(y1)
        data.append(z1)
    #Discard points in shape interior
    for f in range(len(atom_names)):
        for g in range(len(atom_names)):
            if g==f:
                continue
            keep=[]
            for i in range(len(data[3*f])):
                if math.sqrt(((data[3*f][i]-atom_pos[g][0])**2)+((data[(3*f)+1][i]-atom_pos[g][1])**2)+((data[(3*f)+2][i]-atom_pos[g][2])**2)) > atom_radii[g]:
                    keep.append(i)
            x1_keep=[]
            y1_keep=[]
            z1_keep=[]
            for x in keep:
                x1_keep.append(data[3*f][x])
                y1_keep.append(data[(3*f)+1][x])
                z1_keep.append(data[(3*f)+2][x])
            data[(3*f)]=x1_keep
            data[(3*f)+1]=y1_keep
            data[(3*f)+2]=z1_keep
    x=[]
    y=[]
    z=[]
    #merge points
    for f in range(len(data)):
        if f%3 == 0:
            for g in data[f]:
                x.append(g)
        if f%3 == 1:
            for g in data[f]:
                y.append(g)
        if f%3 == 2:
            for g in data[f]:
                z.append(g)
    #return separate x, y and z point lists
    return(x,y,z)

#plot and save graphs
def graph(x,y,z,az,el):
    fig = plt.figure(figsize=(20,20)) #large canvas size for resolution and to fit larger molecules
    #use 3d plotting
    ax = fig.add_subplot(111,projection='3d')
    #colour black with big point size so image opaque
    ax.scatter(x,y,z,color="black",s=100)
    ax.set_xlim(-20,20)
    ax.set_ylim(-20,20)
    ax.set_zlim(-20,20)
    #no axes!
    plt.axis('off')
    #axim and alev are the angles to define the view, change to get projection down each axis
    ax.view_init(azim=az, elev=el)

def shadow_info(image):
    #initiate list for results
    results=[]
    #load image
    img = cv.imread(image,0)
    #fit shape
    ret,thresh = cv.threshold(img,127,255,0)
    #get shape by increasing area
    contours,hierarchy=cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
    #get second last (last is full frame)
    cnt=contours[-2]
    #get area
    area=cv.contourArea(cnt)
    results.append(area)
    #fit minimum area rectangle
    rect = cv.minAreaRect(cnt)
    #width,height,area and aspect ratio
    width = float(rect[1][0])
    length = float(rect[1][1])
    rect_area=width*length
    aspect_ratio = width/length
    #do not know whether width or height is larger
    if aspect_ratio>1:
        aspect_ratio = length/width
    results.append(aspect_ratio)
    return(results)

# 计算分子的MW
def calculate_mw(smiles):
    mol = Chem.MolFromSmiles(smiles)
    return Descriptors.MolWt(mol)

# 计算分子的LogP
def calculate_logp(smiles):
    mol = Chem.MolFromSmiles(smiles)
    return Descriptors.MolLogP(mol)

def calculate_tpsa(smiles):
    mol = Chem.MolFromSmiles(smiles)
    return Descriptors.TPSA(mol)

def calculate_hba(smiles):
    mol = Chem.MolFromSmiles(smiles)
    return Lipinski.NumHAcceptors(mol)

def calculate_hbd(smiles):
    mol = Chem.MolFromSmiles(smiles)
    return Lipinski.NumHDonors(mol)

def calculate_rob(smiles):
    mol = Chem.MolFromSmiles(smiles)
    return Lipinski.NumRotatableBonds(mol)

def calculate_aliRings(smiles):
    mol = Chem.MolFromSmiles(smiles)
    return Lipinski.NumAliphaticRings(mol)

def calculate_aroRings(smiles):
    mol = Chem.MolFromSmiles(smiles)
    return Lipinski.NumAromaticRings(mol)

def calculate_sp3(smiles):
    mol = Chem.MolFromSmiles(smiles)
    return Lipinski.FractionCSP3(mol)

def calculate_LASA(smiles):
    mol = Chem.MolFromSmiles(smiles)
    return rdMolDescriptors.CalcLabuteASA(mol)

def calculate_chiral_center(smiles):
    mol = Chem.MolFromSmiles(smiles)
    return len(Chem.FindMolChiralCenters(mol))

def calculate_qed(smiles):
    mol = Chem.MolFromSmiles(smiles)
    return QED.qed(mol)

def calculate_MACCS(smiles):
    mol = Chem.MolFromSmiles(smiles)
    return list(MACCSkeys.GenMACCSKeys(mol))

def calculate_ECFP6_1(smiles):
    mol = Chem.MolFromSmiles(smiles)
    arr = np.empty((0,2048), int).astype(int)
    fp = AllChem.GetMorganFingerprintAsBitVect(mol, radius = 1)
    array = np.zeros((1,))
    DataStructs.ConvertToNumpyArray(fp, array)
    return np.vstack((arr, array)).tolist()[0]

def calculate_ECFP6_2(smiles):
    mol = Chem.MolFromSmiles(smiles)
    arr = np.empty((0,2048), int).astype(int)
    fp = AllChem.GetMorganFingerprintAsBitVect(mol, radius = 2)
    array = np.zeros((1,))
    DataStructs.ConvertToNumpyArray(fp, array)
    return np.vstack((arr, array)).tolist()[0]

def calculate_ECFP6_3(smiles):
    mol = Chem.MolFromSmiles(smiles)
    arr = np.empty((0,2048), int).astype(int)
    fp = AllChem.GetMorganFingerprintAsBitVect(mol, radius = 3)
    array = np.zeros((1,))
    DataStructs.ConvertToNumpyArray(fp, array)
    return np.vstack((arr, array)).tolist()[0]

import pandas as pd
from rdkit.Chem import AllChem
from rdkit import Chem
import numpy as np
import sys

class Compound3DKit(object):
    """the 3Dkit of Compound"""
    @staticmethod
    def get_atom_poses(mol, conf):
        """tbd"""
        atom_poses = []
        for i, atom in enumerate(mol.GetAtoms()):
            if atom.GetAtomicNum() == 0:
                return [[0.0, 0.0, 0.0]] * len(mol.GetAtoms())
            pos = conf.GetAtomPosition(i)
            atom_poses.append([pos.x, pos.y, pos.z])
        return atom_poses

    @staticmethod
    def get_MMFF_atom_poses(mol, numConfs=None, return_energy=False):
        """the atoms of mol will be changed in some cases."""
        try:
            new_mol = Chem.AddHs(mol)
            res = AllChem.EmbedMultipleConfs(new_mol, numConfs=numConfs)
            ### MMFF generates multiple conformations
            res = AllChem.MMFFOptimizeMoleculeConfs(new_mol)
            # new_mol = Chem.RemoveHs(new_mol)
            index = np.argmin([x[1] for x in res])
            energy = res[index][1]
            conf = new_mol.GetConformer(id=int(index))
        except:
            new_mol = Chem.AddHs(mol)
            AllChem.Compute2DCoords(new_mol)
            energy = 0
            conf = new_mol.GetConformer()

        atom_poses = Compound3DKit.get_atom_poses(new_mol, conf)
        if return_energy:
            return new_mol, atom_poses, energy
        else:
            return new_mol, atom_poses

    @staticmethod
    def get_2d_atom_poses(mol):
        """get 2d atom poses"""
        AllChem.Compute2DCoords(mol)
        conf = mol.GetConformer()
        atom_poses = Compound3DKit.get_atom_poses(mol, conf)
        return atom_poses

    @staticmethod
    def get_bond_lengths(edges, atom_poses):
        """get bond lengths"""
        bond_lengths = []
        for src_node_i, tar_node_j in edges:
            bond_lengths.append(np.linalg.norm(atom_poses[tar_node_j] - atom_poses[src_node_i]))
        bond_lengths = np.array(bond_lengths, 'float32')
        return bond_lengths

    @staticmethod
    def get_superedge_angles(edges, atom_poses, dir_type='HT'):
        """get superedge angles"""
        def _get_vec(atom_poses, edge):
            return atom_poses[edge[1]] - atom_poses[edge[0]]
        def _get_angle(vec1, vec2):
            norm1 = np.linalg.norm(vec1)
            norm2 = np.linalg.norm(vec2)
            if norm1 == 0 or norm2 == 0:
                return 0
            vec1 = vec1 / (norm1 + 1e-5)    # 1e-5: prevent numerical errors
            vec2 = vec2 / (norm2 + 1e-5)
            angle = np.arccos(np.dot(vec1, vec2))
            return angle

        E = len(edges)
        edge_indices = np.arange(E)
        super_edges = []
        bond_angles = []
        bond_angle_dirs = []
        for tar_edge_i in range(E):
            tar_edge = edges[tar_edge_i]
            if dir_type == 'HT':
                src_edge_indices = edge_indices[edges[:, 1] == tar_edge[0]]
            elif dir_type == 'HH':
                src_edge_indices = edge_indices[edges[:, 1] == tar_edge[1]]
            else:
                raise ValueError(dir_type)
            for src_edge_i in src_edge_indices:
                if src_edge_i == tar_edge_i:
                    continue
                src_edge = edges[src_edge_i]
                src_vec = _get_vec(atom_poses, src_edge)
                tar_vec = _get_vec(atom_poses, tar_edge)
                super_edges.append([src_edge_i, tar_edge_i])
                angle = _get_angle(src_vec, tar_vec)
                bond_angles.append(angle)
                bond_angle_dirs.append(src_edge[1] == tar_edge[0])  # H -> H or H -> T

        if len(super_edges) == 0:
            super_edges = np.zeros([0, 2], 'int64')
            bond_angles = np.zeros([0,], 'float32')
        else:
            super_edges = np.array(super_edges, 'int64')
            bond_angles = np.array(bond_angles, 'float32')
        return super_edges, bond_angles, bond_angle_dirs

def getget_atom(smile):
    mol = Chem.MolFromSmiles(smile)
    mol = Chem.AddHs(mol)
    atoms = []
    for atom in mol.GetAtoms(): 
        atoms.append(atom.GetSymbol())   
    return atoms

def smiletoXYZ(smiles):
    mol = AllChem.MolFromSmiles(smiles)
    mol, atom_poses = Compound3DKit.get_MMFF_atom_poses(mol, numConfs=10)
    data = {}
    data['atom_pos'] = atom_poses
    data['smiles'] = smiles
    atomlist = getget_atom(smiles)
    data['atom_list'] = atomlist
    return data

def generate_xyz_file(atom_list, coords_list, smiles):
    num_atoms = len(atom_list)
    xyz_content = f"{num_atoms}\n{smiles}\n"
    
    for atom, coords in zip(atom_list, coords_list):
        x, y, z = coords
        xyz_content += f"{atom:2} {x:15.8f} {y:15.8f} {z:15.8f}\n"
    return xyz_content
import csv
def read_attributes_from_csv(filename):
    MACCS = []
    ECFP1 = []
    ECFP2 = []
    ECFP3 = []
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # 跳过表头
        for row in reader:
            MACCS.append(row[0])
            ECFP1.append(row[1])
            ECFP2.append(row[2])
            ECFP3.append(row[3])
    return MACCS, ECFP1, ECFP2, ECFP3

def get_properties(test_smiles):
    df = {}
    df['MW'] = calculate_mw(test_smiles)
    df['logP'] = calculate_logp(test_smiles)
    df['TPSA'] = calculate_tpsa(test_smiles)
    df['hba'] = calculate_hba(test_smiles)
    df['hbd'] = calculate_hbd(test_smiles)
    df['rob'] = calculate_rob(test_smiles)
    df['aliRings'] = calculate_aliRings(test_smiles)
    df['aroRings'] = calculate_aroRings(test_smiles)
    df['sp3'] = calculate_sp3(test_smiles)
    df['LASA'] = calculate_LASA(test_smiles)
    df['chiral_center'] = calculate_chiral_center(test_smiles)
    df['qed'] = calculate_qed(test_smiles)
    df['MACCS'] = calculate_MACCS(test_smiles)
    df['ECFP1'] = calculate_ECFP6_1(test_smiles)
    df['ECFP2'] = calculate_ECFP6_2(test_smiles)
    df['ECFP3'] = calculate_ECFP6_3(test_smiles)

    data = smiletoXYZ(test_smiles)
    atom_list = data['atom_list']
    coords_list = data['atom_pos']
    df['atom_seq'] = atom_list
    df['xyz_1'] = coords_list


    x,y,z = get_points(coords_list,atom_list)
    graph(x,y,z,0,0)
    plt.savefig("./shadow_MSCSol_1.png") #first angle
    plt.close()
    graph(x,y,z,90,0)
    plt.savefig("./shadow_MSCSol_2.png") #perpendicular
    plt.close()
    graph(x,y,z,90,90)
    plt.savefig("./shadow_MSCSol_3.png") #perpendicular again
    plt.close()

    #get for every molecule
    results1=shadow_info("./shadow_MSCSol_1.png")
    results2=shadow_info("./shadow_MSCSol_2.png")
    results3=shadow_info("./shadow_MSCSol_3.png")
    areas=sorted([results1[0],results2[0],results3[0]]) #get ascending areas
    asp_ratios=sorted([results1[1],results2[1],results3[1]]) #get ascending aspect ratios

    df["Area1"]=areas[0]
    df["Area2"]=areas[1]
    df["Area3"]=areas[2]
    df["Asp1"]=asp_ratios[0]
    df["Asp2"]=asp_ratios[1]
    df["Asp3"]=asp_ratios[2]


    mean = [241.17086943668875, 1.8495421750855718, 57.23876983715382, 3.192822321335961, 1.0750959444041075, 3.492065138471113, 0.4624001659578882, 1.0159734467378903, 0.43275660628058293, 98.8221895824682, 0.2150191888808215, 0.5593321579806038, 21068.645939217924, 29727.898039622447, 35152.00938699305, 0.5662082157333886, 0.6540388373095738, 0.8562607957700965]
    std = [100.12021291377042, 2.5501091746376243, 41.44511506165519, 2.1820605320680286, 1.2542896227994564, 3.4786775189266868, 0.9345681898608666, 1.043078952322485, 0.34126142183154234, 41.43150031769363, 1.0194287914458557, 0.1690662120917528, 7196.364366980063, 11027.22521817576, 12355.807381697678, 0.13877489949918362, 0.13939582337952788, 0.10669031229217894]
    columns_to_standardize = ['MW','logP','TPSA','hba','hbd','rob','aliRings','aroRings','sp3','LASA','chiral_center','qed',"Area1","Area2","Area3","Asp1","Asp2","Asp3"]
    ff = []
    num = 0
    for k in columns_to_standardize:
        ff.append(((df[k] - mean[num]) / std[num]))
        num += 1

    df2 = pd.read_csv("./fingerprint.csv", quotechar='"')
    pca = PCA(n_components=101)
    concatenated_MACCS = pd.concat([df2['MACCS'],pd.DataFrame([str(df['MACCS'])])])
    MACCS_pca = pca.fit_transform([eval(i[0]) for i in np.array(concatenated_MACCS)])
    pca = PCA(n_components=300)
    concatenated_ECFP1 = pd.concat([df2['ECFP1'],pd.DataFrame([str(df['ECFP1'])])])
    ECFP6_1_pca = pca.fit_transform([eval(i[0]) for i in np.array(concatenated_ECFP1)])
    pca = PCA(n_components=300)
    concatenated_ECFP2 = pd.concat([df2['ECFP2'],pd.DataFrame([str(df['ECFP3'])])])
    ECFP6_2_pca = pca.fit_transform([eval(i[0]) for i in np.array(concatenated_ECFP2)])
    pca = PCA(n_components=300)
    concatenated_ECFP3 = pd.concat([df2['ECFP2'],pd.DataFrame([str(df['ECFP3'])])])
    ECFP6_3_pca = pca.fit_transform([eval(i[0]) for i in np.array(concatenated_ECFP3)])

    df['features'] = [ff+ MACCS_pca[-1].tolist()+ECFP6_1_pca[-1].tolist()+ECFP6_2_pca[-1].tolist()+ECFP6_3_pca[-1].tolist()]

    mol = Chem.MolFromSmiles(test_smiles)
    Draw.MolToFile(mol,f'./img_MSCSol.png',size=(224, 224))

    return df


import numpy as np
import os

# 定义读取xyz格式的函数，返回迭代器
def read_xyz(file):
    with open(file) as f:
        while True:
            try:
                n_atoms = int(f.readline())
            except ValueError:
                break
            if not n_atoms:
                break
            f.readline()
            
            # 将坐标保存为narray
            coords = []
            for i in range(n_atoms):
                line = f.readline().split()
                coords.append([float(x) for x in line[1:]])
            yield coords

def read_xyz_full(file):
    """Read xyz file and get all the conf in same file, so return N_frames*n_atoms*3 np array"""
    with open(file) as f:
        lines = f.readlines()
        N_frames = int(len(lines)/(int(lines[0])+2))
        N_atoms = int(lines[0])
        print(N_frames, N_atoms)
        coords = np.zeros((N_frames, N_atoms, 3))
        for i in range(N_frames):
            lines = lines[2:]
            for j in range(N_atoms):
                line = lines[j].split()
                coords[i,j,0] = float(line[1])
                coords[i,j,1] = float(line[2])
                coords[i,j,2] = float(line[3])
            lines = lines[N_atoms:]

    return coords


def read_xyz_single(filename):
    with open(filename,'r') as f:
        N=int(f.readline())
        f.readline()
        data=np.zeros((N,3))
        for i in range(N):
            line=f.readline().split()
            data[i,0]=float(line[1])
            data[i,1]=float(line[2])
            data[i,2]=float(line[3])
    return data

# def read_xyz_single(filename):
#     """Read xyz file and return a list of atoms. return numpy array"""
#     with open(filename, 'r') as f:
#         lines = f.readlines()
#         lines = lines[2:]
#         atoms = []
#         for line in lines:
#             line = line.split()
#             atom = [ float(line[1]), float(line[2]), float(line[3])]
#             atoms.append(atom)
#     return np.array(atoms)

def save_xyz_single(file, X:np.ndarray, title:str, dir=None, append=False):
    # 如果dir不存在则创建
    if dir and not os.path.exists(dir):
        os.makedirs(dir)
    
    if(append):
        with open(dir+'/'+file, 'a') as f:
            f.write(str(X.shape[0]) + '\n')
            f.write(title + '\n')
            for x in X:
                f.write('1\t{:f} {:f} {:f}'.format(x[0], x[1], x[2]) + '\n')
    else:
        with open(dir+'/'+file, 'w') as f:
            f.write(str(X.shape[0]) + '\n')
            f.write(title + '\n')
            for x in X:
                f.write('1\t{:f} {:f} {:f}'.format(x[0], x[1], x[2]) + '\n')

def save_xyz_full(file,X:np.ndarray, title:str, dir=None, append=False):
    # 如果dir不存在则创建
    if dir and not os.path.exists(dir):
        os.makedirs(dir)
    
    N_frames, N_atoms, _ = X.shape

    if(append):
        with open(dir+'/'+file, 'a') as f:
            for i in range(N_frames):
                f.write(str(N_atoms) + '\n')
                f.write(title + '\n')
                for j in range(N_atoms):
                    f.write('1\t{:f} {:f} {:f}'.format(X[i,j,0], X[i,j,1], X[i,j,2]) + '\n')
    else:
        with open(dir+'/'+file, 'w') as f:
            for i in range(N_frames):
                f.write(str(N_atoms) + '\n')
                f.write(title + '\n')
                for j in range(N_atoms):
                    f.write('1\t{:f} {:f} {:f}'.format(X[i,j,0], X[i,j,1], X[i,j,2]) + '\n')


def to_lammps_ReadDataFile(data:np.ndarray,filename,type="open",Lx=200,Ly=200,Lz=200):
    N=data.shape[0]
    with open(filename,'w') as f:
        f.write("#LAMMPS input file\n")
        f.write('{} atoms\n'.format(N))
        # 写入bond数目
        if (type=="open"):
            f.write('{} bonds\n'.format(N-1))
        elif(type=="close"):
            f.write('{} bonds\n'.format(N))
        # 写入angle数目
        if (type=="open"):
            f.write('{} angles\n'.format(N-2))
        elif(type=="close"):
            f.write('{} angles\n'.format(N))

        # 写入原子类型数目
        f.write('\n1 atom types\n')
        # 写入bond类型数目
        f.write('1 bond types\n')
        # 写入angle类型数目
        f.write('1 angle types\n')

        # 写入box的大小
        min_x=np.min(data[:,0])
        data[:,0] = data[:,0] - min_x
        min_y=np.min(data[:,1])
        data[:,1] = data[:,1] - min_y
        min_z=np.min(data[:,2])
        data[:,2] = data[:,2] - min_z
        f.write('\n0.0 {} xlo xhi\n'.format(max(Lx,np.max(data[:,0]))))
        f.write('0.0 {} ylo yhi\n'.format(max(Ly,np.max(data[:,1]))))
        f.write('0.0 {} zlo zhi\n'.format(max(Lz,np.max(data[:,2]))))

        # 写入质量
        f.write('\nMasses\n\n1 1.0\n')

        # 写入原子坐标
        f.write('\nAtoms\n\n')
        for i in range(N):
            f.write('{}\t{}\t{}\t{}\t{}\t{}\n'.format(i+1,1,1,data[i,0],data[i,1],data[i,2]))
        # 写入bond信息
        f.write('\nBonds\n\n')
        if (type=="open"):
            for i in range(N-1):
                f.write('{}\t{}\t{}\t{}\n'.format(i+1,1,i+1,i+2))
        elif(type=="close"):
            for i in range(N-1):
                f.write('{}\t{}\t{}\t{}\n'.format(i+1,1,i+1,i+2))
            f.write('{}\t{}\t{}\t{}\n'.format(N,1,N,1))
        # 写入angle信息
        f.write('\nAngles\n\n')
        if (type=="open"):
            for i in range(N-2):
                f.write('{}\t{}\t{}\t{}\t{}\n'.format(i+1,1,i+1,i+2,i+3))
        elif(type=="close"):
            for i in range(N-2):
                f.write('{}\t{}\t{}\t{}\t{}\n'.format(i+1,1,i+1,i+2,i+3))
            f.write('{}\t{}\t{}\t{}\t{}\n'.format(N-1,1,N-1,N,1))
            f.write('{}\t{}\t{}\t{}\t{}\n'.format(N,1,N,1,2))
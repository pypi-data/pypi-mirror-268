import numpy as np
import os

# 定义读取lammps dump格式的函数，返回迭代器
def read_lammps_dump(file):
    """ Read lammps dump file and return a iterator"""
    with open(file) as f:
        while True:
            try:
                # 跳过前三行，第四行是原子数
                for i in range(3):
                    f.readline()
                n_atoms = int(f.readline())
                # 再跳过五行
            except ValueError:
                break
            if not n_atoms:
                break
            for i in range(5):
                f.readline()
            
            # 将坐标保存为narray
            coords = []
            for i in range(n_atoms):
                line = f.readline().split()
                coords.append([float(x) for x in line[2:5]])
            yield coords

def read_lammps_dump_full(file):
    """ read lammps dump file and return a np array"""
    with open(file) as f:
        lines = f.readlines()
        N_frames = int(len(lines)/(int(lines[3])+9))
        N_atoms = int(lines[3])
        print(N_frames, N_atoms)
        coords = np.zeros((N_frames, N_atoms, 3))
        for i in range(N_frames):
            lines = lines[9:]
            for j in range(N_atoms):
                line = lines[j].split()
                try:
                    coords[i,j,0] = float(line[1])
                    coords[i,j,1] = float(line[2])
                    coords[i,j,2] = float(line[3])
                except IndexError:
                    print(i,j)
            lines = lines[N_atoms:]

    return coords
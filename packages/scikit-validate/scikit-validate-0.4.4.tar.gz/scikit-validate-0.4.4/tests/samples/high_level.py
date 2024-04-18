from array import array
import sys

import numpy as np
import uproot
import ROOT


def analyze(input_file):
    f = uproot.open(input_file)
    tree = f['test']
    x = tree['x'].array()
    y = tree['y'].array()
    d_xy = np.sqrt(x**2 + y**2)
    return d_xy


def write(results, output_file):
    f = ROOT.TFile.Open(output_file, 'recreate')
    tree = ROOT.TTree('test', 'high-level observables')
    d_xy = array('f', [0.])
    tree.Branch('d_xy', d_xy, 'd_xy/F')

    for r in results:
        d_xy[0] = r
        tree.Fill()
    tree.Write()
    f.Close()


if __name__ == '__main__':
    args = sys.argv[1:]
    input_file = args[0]
    output_file = args[1]

    results = analyze(input_file)
    write(results, output_file)

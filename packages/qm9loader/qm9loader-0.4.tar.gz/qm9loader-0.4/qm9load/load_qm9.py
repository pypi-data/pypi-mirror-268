import pickle
import sys
sys.path.append('../..')
from Tools.read_xyz import FileReader
from Tools.prepare_morgan_vector import morgan_featurizer
from Tools.featurize_the_SMILES import rdkit_descriptors
from Tools.map4_featurizer import maccs_featurizer
import pandas as pd



def load(output=None):
    reader = FileReader()
    print('Found read_xyz!')

    smiles = reader.smile_reader("qm9load/qm9load")
    smiles_frame = pd.DataFrame(smiles, columns=['SMILES String'])

    features = reader.feature_reader("qm9load/qm9load")
    feature_titles = ['Identifier', 'Rotational Constant (A)', 'Rotational Constant (B)', 'Rotational Constant (C)',
                      'Dipole moment', 'Isotropic Polarizability', 'HOMO', 'LUMO', 'Band Gap',
                      'Electronic Spatial Extent', 'Vibrational Energy', 'Internal Energy @0K',
                      'Internal Energy @RT', 'Enthalpy @RT', 'Gibbs @RT', 'Heat Capacity']
    features_frame = pd.DataFrame(features, columns=feature_titles)
    morgan_fingerprint = morgan_featurizer(smiles)
    maccs_fingerprint = maccs_featurizer(smiles)
    rdkit_fingerprint = rdkit_descriptors(smiles)
    fingerprint_frame = pd.DataFrame({
        "Morgan Fingerprint": morgan_fingerprint,
        "MACCS Fingerprint": maccs_fingerprint,
        "RDKit Fingerprint": rdkit_fingerprint
    })
    df = pd.concat([smiles_frame, fingerprint_frame, features_frame], axis=1)

    if output is not None:
        with open(output, 'wb') as f:
            pickle.dump(df, f)

    return df

if __name__ == '__main__':
    data = load()

from log_store import log_store 
from particle  import Particle  as part
from tqdm      import tqdm

import os
import re
import vector
import pprint
import pandas as pnd

log = log_store.add_logger('misid_check')
#---------------------------------
class misid_check:
    def __init__(self, df, d_lep=None, d_had=None):
        self._df     = df
        self._d_lep  = d_lep
        self._d_had  = d_had
        self._plt_dir= None
    
        self._initialized=False
    #---------------------------------
    def _initialize(self):
        if self._initialized:
            return
    
        self._check_particle(self._d_lep)
        self._check_particle(self._d_had)

        if self._plt_dir is not None:
            os.makedirs(self._plt_dir, exist_ok=True)

        tqdm.pandas(ascii=' -')

        self._initialized=True
    #---------------------------------
    @property
    def plt_dir(self):
        return self._plt_dir

    @plt_dir.setter
    def plt_dir(self, value):
        self._plt_dir = value
    #---------------------------------
    def _check_particle(self, d_part):
        if not isinstance(d_part, dict):
            log.error(f'Dictionary expected, found: {d_part}')
            raise
    
        for par_name, pdg_id in d_part.items():
            try:
                part.from_pdgid(pdg_id)
            except:
                log.error(f'Cannot create particle for PDGID: {pdg_id}')
                raise
    #---------------------------------
    def _build_mass(self, row, d_part):
        l_vec = []
        for name, new_id in d_part.items():
            par    = part.from_pdgid(new_id)
            ms     = par.mass 
            old_id = row[f'{name}_ID']

            px = row[f'{name}_PX']
            py = row[f'{name}_PY']
            pz = row[f'{name}_PZ']
            pe = row[f'{name}_PE']
            vec_1 = vector.obj(px=px, py=py, pz=pz, t=pe)
            log.debug(f'{name}: {vec_1.mass:0f}({old_id}) -> {ms:.0f}({new_id})')
            vec_2 = vector.obj(pt=vec_1.pt, phi=vec_1.phi, theta=vec_1.theta, mass=ms)
            l_vec.append(vec_2)

        [vec_1, vec_2] = l_vec

        vec = vec_1 + vec_2

        return vec.mass
    #---------------------------------
    def _combine(self, row, had_name, kind, new_had_id):
        old_had_id = row[f'{had_name}_ID']
        had        = part.from_pdgid(old_had_id)
        l_mass     = []
        for lep_name, new_lep_id in self._d_lep.items():
            old_lep_id = row[f'{lep_name}_ID']
            lep        = part.from_pdgid(old_lep_id)

            if lep.charge == had.charge:
                continue

            lep_id = new_lep_id if kind == 'swp' else old_lep_id
            had_id = new_had_id if kind == 'swp' else old_had_id

            mass   = self._build_mass(row, {had_name : had_id, lep_name : lep_id})

            l_mass.append(mass)

        return l_mass
    #---------------------------------
    def _get_charges(self, row, name):
        pdg_id = row[f'{name}_ID']
        partic = part.from_pdgid(pdg_id)

        return partic.charge
    #---------------------------------
    def get_df(self):
        self._initialize()

        d_comb = {}
        for had_name, new_had_id in self._d_had.items():
            for kind in ['org', 'swp']:
                log.debug(f'Adding column for {had_name}/{new_had_id}/{kind}')
                sr_mass = self._df.progress_apply(self._combine, args=(had_name, kind, new_had_id), axis=1)
                sr_mass = sr_mass.explode().dropna(ignore_index=True)

                d_comb[f'{had_name}_{kind}'] = sr_mass
    
        df = pnd.DataFrame(d_comb) 

        return df
    #---------------------------------
    @staticmethod
    def rdf_to_df(rdf, regex):
        v_col_name = rdf.GetColumnNames()
        l_col_name = [ col_name.c_str() for col_name in v_col_name ]
        l_col_need = [ col_name         for col_name in l_col_name if re.match(regex, col_name) ]

        if len(l_col_need) == 0:
            log.error(f'No colum matches: {regex}')
            raise

        d_data     = rdf.AsNumpy(l_col_need)
        df         = pnd.DataFrame(d_data)

        return df
#---------------------------------


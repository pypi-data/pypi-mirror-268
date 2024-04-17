from tqdm.auto import tqdm

from matmodel.base.Trajectory import Trajectory
#from movelets.classes.Subtrajectory import Subtrajectory
#from movelets.classes.Movelet import Movelet

# ------------------------------------------------------------------------------------------------------------
# TRAJECTORY 
# ------------------------------------------------------------------------------------------------------------
def df2trajectory(df, attributes_desc=None, tid_col='tid', label_col='label'):
    
    # Translate atributes:
    if attributes_desc:
        attributes_desc = readDescriptor(readDescriptor)
    else:
        attributes_desc = makeDescriptor(df, tid_col, label_col)
    
    features = [x['text'] for x in attributes_desc['attributes']]
    
    ls_trajs = []
    def processT(df, tid):
        df_aux = df[df[tid_col] == tid]
        label = df_aux[label_col].unique()[0]
        
        points = list( df_aux[features].itertuples(index=False, name=None) )
        return Trajectory(tid, label, points, attributes_desc)
    
    tids = list(df[tid_col].unique())
    #tids = tids[from_traj: to_traj if len(tids) > to_traj else len(tids)] # TODO
    ls_trajs = list(map(lambda tid: processT(df, tid), tqdm(tids, desc='Reading Trajectories')))
        
    return ls_trajs

def readDescriptor(file_path):
    import ast
    file = open(file_path)
    desc = ast.literal_eval(file.read())
    file.close()
    return desc

def makeDescriptor(df, tid_col='tid', label_col='label'):
    columns = list(df.columns)
    desc = {
        'idFeature': {'order': columns.index(tid_col)+1, 'type': 'numeric', 'text': tid_col}, 
        'labelFeature': {'order': columns.index(label_col)+1, 'type': 'nominal', 'text': label_col},
        'attributes': []
    }
    
    for i in range(len(columns)):
        
        if columns[i] == tid_col or columns[i] == label_col:
            continue
        
        if columns[i] == 'lat_lon' or columns[i] == 'space':
            dtype = 'space2d'
            comparator = 'euclidean'
        elif columns[i] == 'xyz':
            dtype = 'space3d'
            comparator = 'euclidean'
        elif df.dtypes[i] == int or df.dtypes[i] == float:
            dtype = 'numeric'
            comparator = 'difference'
        elif df.dtypes[i] == bool:
            dtype = 'boolean'
            comparator = 'equals'
        elif df.dtypes[i] == 'datetime64[ns]' or df.dtypes[i] == '<M8[ns]':
            dtype = 'datetime'
            comparator = 'difference'
        else:
            dtype = 'nominal'
            comparator = 'equals'
        
        desc['attributes'].append({
            'order': i+1,
            'type': dtype,
            'text': columns[i],
            'comparator': {'distance': comparator}
        })
    
    return desc


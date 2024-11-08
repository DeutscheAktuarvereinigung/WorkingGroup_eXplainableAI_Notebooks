import numpy as np
import pandas as pd
pd.options.mode.copy_on_write = True

def load_gltd_data(datadir, pct=0.05):

    # name of the prepared feather file
    fn_in = "gltd09_13work.feather"

    sq = np.random.SeedSequence()
    seed_store = sq.entropy
    seed = "{}".format(seed_store)
    rng = np.random.default_rng(seed=sq)
    
    gltd = pd.read_feather(datadir + fn_in)
    gltd = gltd.reset_index(drop=True)

    # pct selection of total size of dataset as a percentage of all available Study_Ids
    if pct < 1:
        id_uq = gltd["Study_ID"].unique()

        nidsel = np.floor(pct * id_uq.size).astype(int)
        id_sel = rng.choice(id_uq, nidsel, replace=False)
        flg_sel = gltd["Study_ID"].isin(id_sel)
        tmptbl = gltd[flg_sel]
    else:
        tmptbl = gltd

    X = tmptbl.drop(["Actual_Recoveries", "Study_ID"], axis=1)
    Y = tmptbl["Actual_Recoveries"]
    ID = tmptbl["Study_ID"]

    nm_cat = tmptbl.select_dtypes("category").columns.tolist()
    nm_num = list(set(tmptbl.select_dtypes("number").columns.tolist()) 
              - {"Study_ID", "Actual_Recoveries"})

    # fresh rng instance because we used the old one above
    rng = np.random.default_rng(seed=sq)
    return(
        (X, Y, ID,
        nm_cat, nm_num,
        seed, rng)
    )
# -*- coding: utf-8 -*-

import tarfile 
import pandas as pd

with tarfile.open('gdrive/My Drive/yelp_dataset.tar', 'r:gz') as tar:
  csv_path = tar.getnames()[1]
  df = pd.read_json(tar.extractfile(csv_path), encoding = "utf-8", lines=True)
  df.to_csv(csv_path.rstrip(".json") + ".csv", index=False)

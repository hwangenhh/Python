import numpy as np
import pandas as pd
from sklearn.datasets import load_wine

# Tải tập dữ liệu
wine = load_wine()

# Dữ liệu dưới dạng ndarray
ndarray_data = np.array(wine.data)

# Dữ liệu dưới dạng DataFrame
df_data = pd.DataFrame(wine.data, columns=wine.feature_names)

# Thêm cột phân loại (target)
df_data["target"] = wine.target

# Hiển thị 5 dòng đầu tiên của DataFrame
print(df_data.head())

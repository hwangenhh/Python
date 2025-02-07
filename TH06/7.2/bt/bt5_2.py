from sklearn.datasets import load_iris
import pandas as pd

# Tải dữ liệu
iris = load_iris()

# Chuyển thành DataFrame
df_iris = pd.DataFrame(iris.data, columns=iris.feature_names)
df_iris["target"] = iris.target

# Hiển thị 5 dòng đầu tiên
print(df_iris.head())

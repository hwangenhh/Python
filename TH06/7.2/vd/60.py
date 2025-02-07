# Load module datasets trong thư viện sklearn
import sklearn.datasets as datask

# Tạo dữ liệu mẫu cho bài toán phân lớp
# Với 200 mẫu, đầu vào 5 thuộc tính, phân thành 2 lớp
X_features, y_target = datask.make_classification(n_samples=200,
                                                  n_features=5,
                                                  n_classes=2)

print(X_features[:10, :])  # Hiển thị 10 mẫu đầu tiên của dữ liệu đầu vào
print(y_target[:10])       # Hiển thị 10 mẫu đầu tiên của nhãn phân loại

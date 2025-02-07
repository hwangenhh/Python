# Load module datasets trong thư viện sklearn
import sklearn.datasets as datask

# Tạo dữ liệu mẫu cho bài toán PHÂN CỤM
X_features, y_target = datask.make_blobs(n_samples=1000,
                                         centers=4,
                                         n_features=2,
                                         random_state=0)

print(X_features[:10, :])  # Hiển thị 10 mẫu đầu tiên của dữ liệu đầu vào
print(y_target[:10])       # Hiển thị 10 mẫu đầu tiên của nhãn cụm

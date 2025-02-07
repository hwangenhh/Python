# Load module datasets trong thư viện sklearn
import sklearn.datasets as datask

# Tạo dữ liệu mẫu cho bài toán HỒI QUY
X_features, y_target, coeff = datask.make_regression(n_samples=200,
                                                     n_features=5,
                                                     n_informative=3,
                                                     n_targets=3,
                                                     noise=0.0,
                                                     coef=True,
                                                     random_state=1)

print(X_features[:10, :])  # Hiển thị 10 mẫu đầu tiên của dữ liệu đầu vào
print(y_target[:10])       # Hiển thị 10 mẫu đầu tiên của giá trị mục tiêu

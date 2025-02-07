# Import thư viện cần thiết
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Bước 1: Tạo dataset mẫu với 1000 samples, 8 features và 2 classes
X, y = make_classification(n_samples=1000, n_features=8, n_informative=6, n_classes=2, random_state=42)

# Xem kích thước của X và y
print("Shape of X:", X.shape)  # (1000, 8)
print("Shape of y:", y.shape)  # (1000,)

# Bước 2: Chia dataset thành tập huấn luyện (train) và tập kiểm tra (test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Bước 3: Xây dựng mô hình Decision Tree
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Bước 4: Dự đoán trên tập kiểm tra
y_pred = model.predict(X_test)

# Bước 5: Đánh giá mô hình bằng độ chính xác (accuracy)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy of the Decision Tree model: {accuracy * 100:.2f}%")

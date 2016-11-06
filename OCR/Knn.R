train <- read.csv("~/Desktop/Kaggle/OCR/train.csv")
test <- read.csv("~/Desktop/Kaggle/OCR/test.csv")
library(caret)

train$label <- as.factor(train$label)
fit <- knn3(label ~ ., data = train, k=10)
output <- predict(fit, test, type = "class")
outputVector <- as.vector(output)
l <- ""
Map(function (i) {l <<- paste(l,i,",",outputVector[i],'\n');i}, 1:length(outputVector))
write("ImageId,Label\n", file = "~/Desktop/Kaggle/OCR/KNN.csv")
write(l, file = "~/Desktop/Kaggle/OCR/KNN.csv",append = TRUE)
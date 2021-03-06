train <- read.csv("~/Desktop/Kaggle/OCR/train.csv")
test <- read.csv("~/Desktop/Kaggle/OCR/test.csv")
library(randomForest)
train$label <- as.factor(train$label)
fit <- rpart(label ~ ., data = train)
output <- predict(fit, test, type = "class")
outputVector <- as.vector(output)
l <- ""
Map(function (i) {l <<- paste(l,i,",",outputVector[i],'\n');i}, 1:length(outputVector))
write("ImageId,Label \n", file = "Hello.csv")
write(l, file = "Hello.csv",append = TRUE)

profvis({
train <- read.csv("~/Desktop/Kaggle/OCR/train.csv")
test <- read.csv("~/Desktop/Kaggle/OCR/test.csv")
library(randomForest)
train$label <- as.factor(train$label)
fit <- randomForest(label ~ ., data = train, ntree=5)
output <- predict(fit, test, type = "class")
outputVector <- as.vector(output)
l <- ""
#Map(function (i) {l <<- paste(l,i,",",outputVector[i],'\n');i}, 1:length(outputVector))
i <- 0
sapply(outputVector, function(x) { i <<- i+ 1; l <<- paste(l,i,",",x,'\n')})
write("ImageId,Label\n", file = "~/Desktop/Kaggle/OCR/RandomForestSubmission.csv")
write(l, file = "~/Desktop/Kaggle/OCR/RandomForestSubmission.csv",append = TRUE)
})
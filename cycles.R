data<-read.csv('./data/data.csv', header=FALSE);

names(data)[1:4]<-c("frequency", "num_cycles", "variation", "symbol");

plot(log(data$frequency), log(data$variation), 
     cex=log(data$num_cycles), col=log(data$num_cycles), 
     main="Continuous Positive Cycles Variations",
     pch=19, xlab="Log Frequency", ylab="Log Variation");

# stock<-data[which(log(data$variation)>4 & data$num_cycles>3),];
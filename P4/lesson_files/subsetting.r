getwd()
setwd('/Users/mchana/GitHub/udacity/P4/lesson_files/')

statesInfo <- read.csv('statedata.csv')

head(statesInfo)

# two ways to subset data
# subset(statesInfo, state.region==1)

# and

statesInfo[statesInfo$state.region == 1, ]

library(ggplot2)

reddit <- read.csv('reddit.csv')

table(reddit$employment.status)

str(reddit)

levels(reddit$age.range)

qplot(data=reddit, x=age.range)

# order the variables
reddit$age.range <- ordered(reddit$age.range, levels = c('Under 18','18-24','25-34','35-44','45-54','55-64','65 or Above'))

# or, order like this:
reddit$age.range <- factor(reddit$age.range, levels = c('Under 18','18-24','25-34','35-44','45-54','55-64','65 or Above'), ordered=T)


# This script codes the interactive game Rock-Paper-Scissors between a user and the computer 
# Author: Paula Spinola
# Date: 20th Jan 2021
rm(list=ls())

# installing packages
#install.packages("azuremlsdk")
library(azuremlsdk)

# option to choose from
options <- c("Rock","Paper","Scissors")

# function that gets user input
user_question <- function() {
  user_play <- readline(prompt="Enter play option: ")
  while(!user_play %in% options){
    user_play <-readline(prompt = "Please choose between Rock, Paper and Scissors: ")
  }
  return(user_play)
}

# function that simulates the game
game_simulation <- function(p1,p2) {
  if(p1== "Rock") { 
    if(p2 == "Scissors") {
      p1_output <- "Rock crushes scissors. You won :)"
    }
    if(p2 == "Paper") {
      p1_output <- "Paper covers rock. You lost :("
    }
    else{
      p1_output <- "Tie. No one wins :|"
    }
  } 
  if(p1== "Paper") { 
    if(p2 == "Rock") {
      p1_output <- "Paper covers rock. You won :)"
    }
    if(p2 == "Scissors") {
      p1_output <- "Scissors cut paper. You lost :("
    }
    else{
      p1_output <- "Tie. No one wins :|"
    }
  } 
  if(p1== "Scissors") { 
    if(p2 == "Paper") {
      p1_output <- "Scissors cut paper. You won :)"
    }
    if(p2 == "Rock") {
      p1_output <- "Rock crushes scissors. You lost :("
    }
    else{
      p1_output <- "Tie. No one wins :|"
    }
  } 
  return(p1_output)
}


# generate computer play option
computer_play <- options[sample(1:3, 1)] # did not manage to use randint()

# ask user play option
user_play <- user_question() # why R sometimes transforms first character as lower case?

# running game
game_decision <- game_simulation(p1=user_play,p2=computer_play)
print(game_decision) # there is an issue with the code, sometimes it is outputing Tie when it should not 

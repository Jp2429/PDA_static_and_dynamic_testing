### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    # Should be card.value==1 as just equal sign would set the car.value to 1 instead of checking if it is 1
    if card.value = 1:
      return True
    #should be a : after else
    else
      return False
   
  #Should be def not dif and there should be a comma after card1
  dif highest_card(self, card1 card2):
  #if and else statements not indented
  if card1.value > card2.value:
    #Is returning a variable that doesnt exist(card),should be changed to card1
    return card
  else:
    return card2
  

#Whole method not indented
def cards_total(self, cards):
  #total variable should equal 0 but i dont think it will break the tests
  total
  for card in cards:
    total += card.value
    # Having the return inside of the for loop will cause the function to return total after only one iteration of the for loop which will not return the total
    #will need to convert total to a string variable
    return "You have a total of" + total
  
```

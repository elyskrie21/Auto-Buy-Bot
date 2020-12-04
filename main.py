from config import keys
from NeweggBot import NeweggOrder
from BestBuyBot import BestBuyOrder

def main():
  print('Welcome to the Auto Buy Bot!\nTo get started, enter the product url')
  NeweggOrder(keys)
  
if __name__ == '__main__':
    main()

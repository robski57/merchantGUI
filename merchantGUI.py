from tkinter import *
import sqlite3

import math

class MerchantApp(Frame):

    def __init__(self):
        Frame.__init__(self)
        self.master.title("MerchantApp")
        self.grid()

        #Label and field of Item Name
        self._itemLabel = Label(self, text = "Item")
        self._itemLabel.grid(row = 0, column = 0)
        self._itemStr = StringVar()
        self._itemEntry = Entry(self,
                                textvariable = self._itemStr)
        self._itemEntry.grid(row = 0, column = 1)

        self._locationLabel = Label(self, text = "Location")
        self._locationLabel.grid(row = 1, column = 0)
        self._locationStr = StringVar()
        self._locationEntry = Entry(self,
                                textvariable = self._locationStr)
        self._locationEntry.grid(row = 1, column = 1)

        #Label and field of Price
        self._priceLabel = Label(self, text = "Price")
        self._priceLabel.grid(row = 2, column = 0)
        self._priceVar = DoubleVar()
        self._priceEntry = Entry(self,
                                 textvariable = self._priceVar)
        self._priceEntry.grid(row = 2, column = 1)

        #Label and field of amount you will buy
        self._amountLabel = Label(self, text = "amount")
        self._amountLabel.grid(row = 3, column = 0)
        self._amountVar = DoubleVar()
        self._amountEntry = Entry(self, textvariable = self._amountVar)
        self._amountEntry.grid(row = 3, column = 1)
        

        #Label and field of total
        self._totalLabel = Label(self, text = "total")
        self._totalLabel.grid(row = 4, column = 0)
        self._totalVar = DoubleVar()
        self._totalEntry = Entry(self, textvariable = self._totalVar)
        self._totalEntry.grid(row = 4, column = 1)


        #The command button to total up your items
    
        self._button = Button(self, text = "Compute", command = self._total)
        self._button.grid(row = 5, column = 0, columnspan = 2)

        self._button = Button(self, text = "Save", command = self._save)
        self._button.grid(row = 6, column = 0, columnspan = 2)


        self._purchese = [ ('self._itemStr.get'), ('self._locationStr.get'), ('self._priceVar.get'), ('self._amountVar.get'), ('self._totalVar.get') ]
 

        
        

        
    def _total(self):
         
        item = self._itemStr.get()
        loc = self._locationStr.get()
        #pulls price from self._Label
        Price = self._priceVar.get()
        #pulls amount from self._Label
        amount = self._amountVar.get()
        #multpy
        amount = Price * amount
        self._totalVar.set(amount)
        #print(item)
        #print(loc)
        print("Todays total from the great city of",loc,"$",amount,"for a",item)

    def _save(self):
        
        conn = sqlite3.connect("info.db")
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS inve( ItemN text, Location text, Price real, Amount real, Total real, Qyt real, RestockItm text, StateSells real, GameState text, ClothingNam text, ClothingP real, FoodN text, FoodP real, Programs real, Buttons  text, ButtonSold real, Staff text)")
        
        c.executemany("INSERT INTO inve( ItemN, Location, Price, Amount, Total, Qyt, RestockItm, StateSells, GameState, ClothingNam, ClothingP, FoodN, FoodP, Programs, Buttons, ButtonSold, Staff ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )", (self._purchese))
        
        for row in c.execute("SELECT ItemN, Location, Price, Amount, Total from self._purchese"):
            print(row)
        conn.commit()


    
 #       conn = sqlite3.connect("info.db")
 #   def _database(self):
#        c = conn.cursor()
#        c.execute("CREATE TABLE IF NOT EXISTS inven( ItemN text, Location text, Price real, Amount real, Total real)")
#        c.execute("INSERT INTO inven VALUES(" +self._itemStr.get()+ ','  +self._locationStr.get+  ','  +self._PriceVar.get()+  ','  +self._amountVar.get()+  ','  +self._total+  ")")
#        conn.commit()
#        for row in c.execute("SELECT * FROM inven ORDER BY ItemN"):
#            print(row)
#            conn.close
       
         



def main():
    MerchantApp().mainloop()
main()    

        

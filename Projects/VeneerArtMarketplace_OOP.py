class Art:
  def __init__(self, artist, title, medium, year, owner):
    self.artist = artist
    self.title = title
    self.medium = medium
    self.year = year
    self.owner = owner

  def __repr__(self):
    return f"{self.artist}. \"{self.title}\". {self.year}, {self.medium}. {self.owner.name}, {self.owner.location}. "

#marketplace class
class Marketplace:
  def __init__(self):
    self.listings = []

  #add listing
  def add_listing(self, new_listing):
    self.listings.append(new_listing)
  
  #remove listing
  def remove_listing(self, expired_listing):
    self.listings.remove(expired_listing)

  #show listings
  def show_listings(self):
    for listing in self.listings:
      print(listing)

#clients class
class Client:
  def __init__(self, name, location, is_museum, wallet):
    self.name = name
    self.wallet = wallet
    self.is_museum = is_museum
    if is_museum:
      self.location = location
    else:
      self.location = "Private Collector"

  #sell artwork method
  def sell_artwork(self, artwork, price):
    if artwork.owner == self:
      new_listing = Listing(artwork, price, self)
      veneer.add_listing(new_listing)

    #buy artwork method
  def buy_artwork(self, artwork):
    if artwork.owner != self:
      art_listing = None
      for listing in veneer.listings:
        if listing.art == artwork:
          art_listing = listing.art
          artwork.owner.wallet += listing.price
          break
      if art_listing != None:
        art_listing.owner = self
        veneer.remove_listing(listing)
        self.wallet -= listing.price


#listing class
class Listing:
  def __init__(self, art, price, seller):
    self.art = art
    self.price = price
    self.seller = seller

  #string rep
  def __repr__(self):
    return f"{self.art.title}: {self.price}"


veneer = Marketplace()

#first client
edytta = Client("Edytta Halpirt", None, False, 2000000)

#to check the client object attributes
#print(edytta.is_museum)

girl_with_mandolin = Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)","oil on canvas", 1910, edytta)

#print(girl_with_mandolin)

#second client
moma = Client("The MOMA", "New York", True, 50000000)

#add listing for girl_with_mandolin
edytta.sell_artwork(girl_with_mandolin, 6000000)

print(girl_with_mandolin)

veneer.show_listings()

moma.buy_artwork(girl_with_mandolin)

print(girl_with_mandolin)

print(moma.wallet)
print(edytta.wallet)

if (veneer.show_listings() == None):
  print("No listings")
else:
  veneer.show_listings()

#moma.sell_artwork(girl_with_mandolin, "$6m (USD)")

#veneer.show_listings()




#things to add:
#Add a wallet instance variable to clients, update the buying and selling of artworks to also exchange dollar amounts.
#Create a wishlist for your clients, things that are listed but they’re not sure if they should purchase just yet.
#Create expiration dates for listings! Have out of date listings automatically removed from the marketplace.
#also for wallet make sure to have logic in place for buying things if you do not have enough money.